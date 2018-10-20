import numpy as np
Method = ''
BorderBehavior = 'periodic'
numxx = 100.0
numyy = 100.0
NumberOfAnts = 16
MaxActiveDropletsPerAnt = 300
IgnoreDropletsFartherThan = 5.0
TestWithGivenTrail = 0
GivenTrailType = ''
PheroNarrow = 8.0
PheroHigh = 5.0
Pi = 3.1415926535
seed1 = 3536835118
TurnOffRandom = 3.0
RegularizingEpsilon = 0.01
t_hat_in_seconds = 1.0
X_hat_in_cm = 1.0
tau = 0.1
TAU = tau / t_hat_in_seconds
SensingAreaRadius = 1.0
SENSING_AREA_RADIUS = SensingAreaRadius / X_hat_in_cm
SensingAreaHalfAngle = 0.785398163375
NaturalVelocityIncmsec = 3.5
NaturalVelocity = NaturalVelocityIncmsec * t_hat_in_seconds / X_hat_in_cm
delta_t = 0.1
Diffusion = 0.003
Evaporation = 0.0001
DropletAmountPerUnitTime = 10.0
DropletAmount = DropletAmountPerUnitTime * delta_t
Threshold = 0.2
LambdaDeltas = NaturalVelocity/(SENSING_AREA_RADIUS*np.cos(SensingAreaHalfAngle))
LambdaNonlocal = (3./2.)*NaturalVelocity*SensingAreaHalfAngle/(SENSING_AREA_RADIUS*np.sin(SensingAreaHalfAngle))
Lambda = 1.0
SensitivityMethod = ''
x_1_cm = -10
x_2_cm = 10
y_1_cm = -10
y_2_cm = 10
x_1 = x_1_cm / X_hat_in_cm
x_2 = x_2_cm / X_hat_in_cm
y_1 = y_1_cm / X_hat_in_cm
y_2 = y_2_cm / X_hat_in_cm
delta_x = (x_2-x_1)/numxx
delta_y = (y_2-y_1)/numyy
RNumber = 5
ThetaNumber = 5
DRSector = SENSING_AREA_RADIUS / (RNumber)
DThetaSector = SensingAreaHalfAngle / (ThetaNumber)
ChangedSide = 0
