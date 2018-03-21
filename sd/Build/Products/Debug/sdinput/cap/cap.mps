NAME		capacityacquisiton
ROWS
 N OBJ
 E	k1sk3
 E	k2sk3
 E	k3sk1k2
 E	x1sk1
 E	x2sk2
 E	x1x2sk3
 E	x1sd1
 E	x2sd2
COLUMNS
 K1	OBJ		-1
 K2	OBJ		-1
 K3	OBJ		-2.5
 X1	OBJ		25
 X2	OBJ		15
 K1	k1sk3		1
 K3	k1sk3		-1
 SL1	k1sk3		1
 K2	k2sk3		1
 K3	k2sk3		-1
 SL2	k2sk3		1
 K3	k3sk1k2	1
 K1	k3sk1k2	-1
 K2	k3sk1k2	-1
 SL3	k3sk1k2	1
 X1	x1sk1		1
K1	x1sk1		-1
SL4	x1sk1		1
X2	x2sk2		1
K2	x2sk2		-1
SL4	x2sk2		1
X1	x1x2sk3	1
X2	x1x2sk3	1
K3	x1x2sk3	-1
SL5	x1x2sk3	1
X1	x1sd1		1
SL6	x1sd1		1
X2	x2sd2		1
SL7	x2sd2		1
RHS
rhs	k1sk2		0
rhs	k2sk3		0
rhs	k3sk1k2	0
rhs	x1sk1		0
rhs	x2sk2		0
rhs	x1x2sk3	0
rhs	x1sd1		5000
rhs	x2sd2		2500
BOUNDS
LO BND	K1	0
LO BND	K2	0
LO BND	K3	0
LO BND	SL1	0
LO BND	SL2	0
LO BND	SL3	0
LO BND	X1	0
LO BND	X2	0
LO BND	SL4	0
LO BND	SL5	0
LO BND	SL6	0
LO BND	SL7	0
ENDATA


