\ENCODING=ISO-8859-1
\Problem name: ad_01

Minimize
 obj: 0.1 x1 + 0.5 x2 - 3 x3 - 5 x4
Subject To
 c_l_x6_:              x1 - 0.5 x2 >= 0
 c_u_x7_:              x1 + x2 <= 200
 c_l_x8_:              0.046 x1 + 0.184 x2 - x3 - x4 >= -1.7048
 c_u_x9_:              3 x3 + 2 x4 <= 36
 c_u_x10_:             x3 <= 8
 c_u_x11_:             2 x4 <= 24
 c_e_ONE_VAR_CONSTANT: ONE_VAR_CONSTANT  = 1
Bounds
 0.7 <= x1 <= 296.4
 0 <= x2 <= 49.6
End
