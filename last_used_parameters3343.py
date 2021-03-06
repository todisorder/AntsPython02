import numpy as np
NumberOfAnts = 25
MaxActiveDropletsPerAnt = 400
Cores = 2
seed1 = 1
t_hat_in_seconds = 1.0
X_hat_in_cm = 1.0
tau = 0.08
TAU = tau / t_hat_in_seconds
SensingAreaRadius = 1.0
SENSING_AREA_RADIUS = SensingAreaRadius /X_hat_in_cm
SensingAreaHalfAnglePiOver = 4.0
SensingAreaHalfAngle = np.pi/SensingAreaHalfAnglePiOver
NaturalVelocityIncmsec = 2.3
NaturalVelocity = NaturalVelocityIncmsec * t_hat_in_seconds / X_hat_in_cm
delta_t = 0.08
Diffusion = 0.005
Evaporation = 0.0001
DropletAmountPerUnitTime = 10.0
drop_every_seconds = 0.5
drop_every_t_hat = drop_every_seconds / t_hat_in_seconds
DropletAmount = DropletAmountPerUnitTime * drop_every_t_hat
Threshold = 0.4
LambdaDeltas = NaturalVelocity/(SENSING_AREA_RADIUS*np.cos(SensingAreaHalfAngle))
x_1_cm = -30
x_2_cm = 30
y_1_cm = -30
y_2_cm = 30
x_1 = x_1_cm / X_hat_in_cm
x_2 = x_2_cm / X_hat_in_cm
y_1 = y_1_cm / X_hat_in_cm
y_2 = y_2_cm / X_hat_in_cm

