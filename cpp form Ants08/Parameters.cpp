// ASCII art from http://www.kammerl.de/ascii/AsciiSignature.php
//////////////////////////////////////////////////////
//////////////////////////////////////////////////////
// _______       ___   .___________.    ___         //
//|       \     /   \  |           |   /   \        //
//|  .--.  |   /  ^  \ `---|  |----`  /  ^  \       //
//|  |  |  |  /  /_\  \    |  |      /  /_\  \      //
//|  '--'  | /  _____  \   |  |     /  _____  \     //
//|_______/ /__/     \__\  |__|    /__/     \__\    //
//////////////////////////////////////////////////////
//////////////////////////////////////////////////////

static string Method;

static string BorderBehavior = "periodic";   //"periodic";         // "respawn" or "periodic"

static double const numxx = 100.;
static double const numyy = 100.;

static int const NumberOfAnts = 25;

static int const MaxActiveDropletsPerAnt = 500;    // 10000

static double const IgnoreDropletsFartherThan = 5.; // 7

static int const TestWithGivenTrail = 0;    // 1=true, 0=false

static string GivenTrailType;

///////////////////////////////////////////
// Parameters for given pheromone trail  //
///////////////////////////////////////////
static double const PheroNarrow = .8*1.;
static double const PheroHigh = 5.;
///////////////////////////////////////////
// End Parameters for given pheromone trail
///////////////////////////////////////////


//static double const Pi = 3.14159;
static double const Pi =  3.1415926535;
static double const Ln2 = 0.6931471806;

// obtain a seed from the system clock:
//unsigned seed1 = std::chrono::system_clock::now().time_since_epoch().count();
unsigned seed1 = 3536835118;                   // To use same seed as another simulation. 3536131122

default_random_engine generator(seed1);
normal_distribution<double> Normal(0.,1.);          // Normal(0.,1.)
normal_distribution<double> SmallNormal(0.,.05);      // (0.,.05)
uniform_real_distribution<double> UniformAngle(0.,2.*Pi);      // Uniformly distributed angle
uniform_real_distribution<double> Uniform(0.,1.);      // Uniformly distributed in [0,1]
uniform_int_distribution<int> UniformInteger(0,10);      // Uniformly distributed integer   20
//http://www.cplusplus.com/reference/random/normal_distribution/
// Normal(mean,stddev)
// Usage:
// double number = Normal(generator);
static double const Turn_off_random = 3.*1.;    //*0.02;
//  ^^^ 0. = No Random!

//	Parameter for Regularizing Function
static double const RegularizingEpsilon = 0.01;


//////////////////////////////////////////////////////
// Ant parameters                                   //
//////////////////////////////////////////////////////

//  Time scale t_hat em segundos
static double const t_hat_in_seconds = 1.;

//  Space scale X_hat em centimetros
static double const X_hat_in_cm = 1.;                  // 1.73;

//  Relaxation time tau em segundos:
static double const tau = .1;         //    0.5

//  Nondimensional relaxation TAU = (t_hat / tau)^(-1).
//  Deve ser o relaxation time nas unidades t_hat.
//  Na equação deve aparecer 1/TAU.
static double const TAU = tau / t_hat_in_seconds;         //

//  Sensing area radius em centimetros
static double const SensingAreaRadius = .8;         //  .4

//  Sensing area radius em X_hat
static double const SENSING_AREA_RADIUS = SensingAreaRadius / X_hat_in_cm;         //

//////////////////////////////////////
//  Sensing Area Half Angle         //
//  .-. . . .-. .   .-.             //
//  |-| |\| |.. |   |-              //
//  ` ' ' ` `-' `-' `-'             //
//////////////////////////////////////
static double const SensingAreaHalfAngle = 1.*Pi/4.;         //

//  Natural Ant velocity in cm/s
static double const NaturalVelocityIncmsec = 2.;         // 2.

//  Natural Ant velocity in new units
static double const NaturalVelocity = NaturalVelocityIncmsec * t_hat_in_seconds / X_hat_in_cm;         //

// tempo final
//static double const TFINAL = 0.1;
static double const delta_t = 0.1;   //     0.05

//  Pheromone Diffusion:
static double const Diffusion = 0.002;      // .0002

//  Pheromone Evaporation:
static double const Evaporation = 0.01;        //0.01

//  Droplet amounts
static double const DropletAmountPerUnitTime = 0.*1.;        //0.00001
static double const DropletAmount = DropletAmountPerUnitTime * delta_t;        //0.00001

//  This is pheromone detection threshold
static double const Threshold = 0.7; //

//	With Deltas, Lambda =
static double const LambdaDeltas = NaturalVelocity/(SENSING_AREA_RADIUS*cos(SensingAreaHalfAngle));         //
//  With Nonlocal, L =
static double const LambdaNonlocal = (3./2.)*NaturalVelocity*SensingAreaHalfAngle/(SENSING_AREA_RADIUS*sin(SensingAreaHalfAngle));         //
//  Deprecated, for linear method
static double const Lambda = 1.;

//////////////////////////////////////////////////////
// End Ant parameters                               //
//////////////////////////////////////////////////////



string SensitivityMethod;

////////////////////////////
//  Domain definition
////////////////////////////
/////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////
// _______   ______   .___  ___.      ___       __  .__   __.  //
//|       \ /  __  \  |   \/   |     /   \     |  | |  \ |  |  //
//|  .--.  |  |  |  | |  \  /  |    /  ^  \    |  | |   \|  |  //
//|  |  |  |  |  |  | |  |\/|  |   /  /_\  \   |  | |  . `  |  //
//|  '--'  |  `--'  | |  |  |  |  /  _____  \  |  | |  |\   |  //
//|_______/ \______/  |__|  |__| /__/     \__\ |__| |__| \__|  //
/////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////
// extremo inferior do intervalo em x (cm)
static double const x_1_cm = -30.;      //-25

// extremo superior do intervalo em x (cm)
static double const x_2_cm = 30.;       //25

// extremo inferior do intervalo em y (cm)
static double const y_1_cm =  -30.;     //-25

// extremo superior do intervalo em y (cm)
static double const y_2_cm = 30.;       //25

// extremo inferior do intervalo em x
static double const x_1 = x_1_cm / X_hat_in_cm;

// extremo superior do intervalo em x
static double const x_2 = x_2_cm / X_hat_in_cm;

// extremo inferior do intervalo em y
static double const y_1 = y_1_cm / X_hat_in_cm;

// extremo superior do intervalo em y
static double const y_2 = y_2_cm / X_hat_in_cm;

////////////////////////////
// End Domain definition
////////////////////////////

static double const delta_x = (x_2-x_1)/numxx;;
static double const delta_y = (y_2-y_1)/numyy;;


//////////////////////////////////////////////////////////
// Nonlocal Sector Discretization parameters            //
//////////////////////////////////////////////////////////
static int const RNumber = 5;
static int const ThetaNumber = 5;
static double const DRSector = SENSING_AREA_RADIUS / (RNumber);
static double const DThetaSector = 2.* SensingAreaHalfAngle / (ThetaNumber);
//////////////////////////////////////////////////////////
// End Nonlocal Sector Discretization parameters        //
//////////////////////////////////////////////////////////


///////////////////////////////////////////////
//  Parametro Só para os plots não ficarem
//  com um risco do lado ao outro
//  quando muda de lado por periodicidade
///////////////////////////////////////////////
static int ChangedSide = 0;

