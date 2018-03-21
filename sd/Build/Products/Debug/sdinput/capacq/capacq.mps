NAME          CAPACQ
ROWS
 L  x1sk1
 L  x2sk2
 L  x1x2sk3
 L  k1sk3
 L  k2sk3
 L  k3sk1sk2
 N  OBJ
COLUMNS
    x1     x1sk1         1
    x1     x1x2sk3       1
    x1     OBJ           -25
    x2     x2sk2         1
    x2     x1x2sk3       1
    x2     OBJ           -15
    k1     x1sk1        -1
    k1     k1sk3         1
    k1     k3sk1sk2     -1
    k1     OBJ          1
    k2     x2sk2        -1
    k2     k2sk3         1
    k2     k3sk1sk2     -1
    k2     OBJ          1
    k3     x1x2sk3      -1
    k3     k1sk3        -1
    k3     k2sk3        -1
    k3     k3sk1sk2      1
    k3     OBJ          2.5
RHS
BOUNDS
 MI BOUND     x1   
 UP BOUND     x1         5000
 MI BOUND     x2   
 UP BOUND     x2         2500
 FR BOUND     k1   
 FR BOUND     k2   
 FR BOUND     k3   
ENDATA

