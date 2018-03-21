#  _________________________________________________________________________
#
#  Pyomo: Python Optimization Modeling Objects
#  Copyright (c) 2014 Sandia Corporation.
#  Under the terms of Contract DE-AC04-94AL85000 with Sandia Corporation,
#  the U.S. Government retains certain rights in this software.
#  This software is distributed under the BSD License.
#  _________________________________________________________________________
#
# ad: Annotated with location of stochastic rhs entries
#       for use with pysp2smps conversion tool.

import itertools
import random

from pyomo.core import *
from pyomo.pysp.annotations import (PySP_ConstraintStageAnnotation,
                                    PySP_StochasticRHSAnnotation)

#
# Define the probability table for the stochastic parameters
#
i=0
d1_rhs_table=\
[1.4422,-2.0235,-3.0869,0.80184,-0.52591,-5.3496,-0.022841,0.93255,0.87201,-2.1873,1.3542,-0.010788,-1.501,0.68292,0.43656,1.5105,-0.49481,1.0584,1.2054,0.29818,-0.2617,-2.4717,-1.0798,-1.2271,1.3764,-3.8464,-0.094332,-1.3314,-0.64519,1.1697,-0.3883,0.37236,1.7198,-1.6083,1.707,-4.4316,1.95,-0.96798,0.06061,0.95686,0.06164,-0.31286,-1.0099,-1.2808,-0.5299,-0.41879,1.5171,1.4115,-1.6741,1.3311,-1.4794,1.1817,1.8523,1.1736,-0.29557,2.337,-3.1556,0.27254,1.8545,0.15995,2.1316,1.2093,-1.2737,0.69376,0.96108,1.2767,0.37917,1.1958,-0.1961,1.1289,0.38932,1.5853,-1.652,0.87001,-0.46165,-3.2681,2.1974,0.28009,-3.5999,1.1162,0.23367,-2.5977,0.9625,-0.87689,0.84589,-0.19384,0.29096,0.30157,1.009,-0.28285,0.99263,2.5654,0.10248,0.82776,0.85057,0.44676,-1.1522,0.0080294,1.1807,0.17561
]



num_scenarios = len(d1_rhs_table)
scenario_data = dict(('Scenario'+str(i), (d1val))
                      for i, (d1val) in
                     enumerate(d1_rhs_table, 1))

#
# Define the reference model
#

model = ConcreteModel()

# these annotations are required for using this
# model with the SMPS conversion tool
model.constraint_stage = PySP_ConstraintStageAnnotation()
model.stoch_rhs = PySP_StochasticRHSAnnotation()

# use mutable parameters so that the constraint
# right-hand-sides can be updated for each scenario
model.d1_rhs = Param(mutable=True, initialize=0.0)

# first-stage variables
model.x1 = Var(bounds=(0.7,296.4))
model.x2 = Var(bounds=(0,49.6))

# second-stage variables
model.y1 = Var(within=NonNegativeReals)
model.y2 = Var(within=NonNegativeReals)


# stage-cost expressions
model.FirstStageCost = \
    Expression(initialize=(0.1*model.x1+0.5*model.x2))
model.SecondStageCost = \
    Expression(initialize=(-3*model.y1-5*model.y2))

#
# this model has two first-stage constraints
#

model.s1 = Constraint(expr= model.x1 - 0.5*model.x2 >= 0)
model.constraint_stage.declare(model.s1, 1)

model.s2 = Constraint(expr= model.x1 + model.x2 <= 200)
model.constraint_stage.declare(model.s2, 1)

#
# this model has four second-stage constraints
#



model.s4 = Constraint(expr= model.y1 <= 8)
model.constraint_stage.declare(model.s4, 2)

model.s5 = Constraint(expr= 2*model.y2 <=24)
model.constraint_stage.declare(model.s5, 2)

model.s6 = Constraint(expr= 3*model.y1 + 2*model.y2 <= 36)
model.constraint_stage.declare(model.s6, 2)

#
# these one constraints have stochastic right-hand-sides
#
model.d1 = Constraint(expr = 3.1470 + 0.046*model.x1\
                      + 0.184*model.x2 - model.y1 - model.y2 >=model.d1_rhs)
model.constraint_stage.declare(model.d1, 2)
model.stoch_rhs.declare(model.d1)

# always define the objective as the sum of the stage costs
model.obj = Objective(expr=model.FirstStageCost + model.SecondStageCost)

def pysp_scenario_tree_model_callback():
    from pyomo.pysp.scenariotree.tree_structure_model import \
        CreateConcreteTwoStageScenarioTreeModel

    st_model = CreateConcreteTwoStageScenarioTreeModel(num_scenarios)

    first_stage = st_model.Stages.first()
    second_stage = st_model.Stages.last()

    # First Stage
    st_model.StageCost[first_stage] = 'FirstStageCost'
    st_model.StageVariables[first_stage].add('x1')
    st_model.StageVariables[first_stage].add('x2')

    # Second Stage
    st_model.StageCost[second_stage] = 'SecondStageCost'
    st_model.StageVariables[second_stage].add('y1')
    st_model.StageVariables[second_stage].add('y2')

    return st_model

def pysp_instance_creation_callback(scenario_name, node_names):

    #
    # Clone a new instance and update the stochastic
    # parameters from the sampled scenario
    #

    instance = model.clone()

    d1_rhs_val = scenario_data[scenario_name]
    instance.d1_rhs.value = d1_rhs_val

    return instance
