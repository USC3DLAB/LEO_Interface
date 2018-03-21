* Problem:    test
* Class:      LP
* Rows:       4
* Columns:    7
* Non-zeros:  15
* Format:     Fixed MPS
*
NAME          test
ROWS
 N  ObJ
 G  C1
 G  C2
 E  C3
COLUMNS
    X1        C2                -100   C3                -215
    X2        C1                  -1   C2                  78
    X2        C3                 100
    X3        C1                  -1   C3               -59.2
    X4        C1                  -1   C3               -60.8
    Y1        C2                   1   C3                 2.2
    Y2        C2                  -1   C3                  -2
    Y3        ObJ                 -1   C3                   1
RHS
    RHS1      C1               -1000
BOUNDS
 LO BOUND     X1     0
 LO BOUND     X2     0
 LO BOUND     X3     0
 LO BOUND     X4     0
 LO BOUND     Y1     0
 LO BOUND     Y2     0
 LO BOUND     Y3     0
ENDATA
