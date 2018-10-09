static string Method;

static string BorderBehavior = "periodic";   //"periodic";         // "respawn" or "periodic"

static double const numxx = 100.;
static double const numyy = 100.;

static int const NumberOfAnts = 25;

static int const MaxActiveDropletsPerAnt = 500;    // 10000

static double const IgnoreDropletsFartherThan = 5.; // 7

static int const TestWithGivenTrail = 0;    // 1=true, 0=false

static string GivenTrailType;

static double const PheroNarrow = .8*1.;
static double const PheroHigh = 5.;
static double const Pi =  3.1415926535;
static double const Ln2 = 0.6931471806;

unsigned seed1 = 3536835118;                   // To use same seed as another simulation. 3536131122

//default_random_engine generator(seed1);
//normal_distribution<double> Normal(0.,1.);          // Normal(0.,1.)
//normal_distribution<double> SmallNormal(0.,.05);      // (0.,.05)
//uniform_real_distribution<double> UniformAngle(0.,2.*Pi);      // Uniformly distributed angle
//uniform_real_distribution<double> Uniform(0.,1.);      // Uniformly distributed in [0,1]
//uniform_int_distribution<int> UniformInteger(0,10);      // Uniformly distributed integer   20


static double const Turn_off_random = 3.*1.;    //*0.02;
static double const RegularizingEpsilon = 0.01;
static double const t_hat_in_seconds = 1.;

static double const X_hat_in_cm = 1.;                  // 1.73;

static double const tau = .1;         //    0.5
static double const TAU = tau / t_hat_in_seconds;         //

static double const SensingAreaRadius = .8;         //  .4
static double const SENSING_AREA_RADIUS = SensingAreaRadius / X_hat_in_cm;         //

static double const SensingAreaHalfAngle = 1.*Pi/4.;         //


static double const NaturalVelocityIncmsec = 2.;         // 2.
static double const NaturalVelocity = NaturalVelocityIncmsec * t_hat_in_seconds / X_hat_in_cm;         //

static double const delta_t = 0.1;   //     0.05


static double const Diffusion = 0.002;      // .0002


static double const Evaporation = 0.01;        //0.01

static double const DropletAmountPerUnitTime = 0.*1.;        //0.00001
static double const DropletAmount = DropletAmountPerUnitTime * delta_t;        //0.00001


static double const Threshold = 0.7; //


static double const LambdaDeltas = NaturalVelocity/(SENSING_AREA_RADIUS*cos(SensingAreaHalfAngle));         //

static double const LambdaNonlocal = (3./2.)*NaturalVelocity*SensingAreaHalfAngle/(SENSING_AREA_RADIUS*sin(SensingAreaHalfAngle));         //

static double const Lambda = 1.;


string SensitivityMethod;

static double const x_1_cm = -30.;      //-25


static double const x_2_cm = 30.;       //25


static double const y_1_cm =  -30.;     //-25


static double const y_2_cm = 30.;       //25


static double const x_1 = x_1_cm / X_hat_in_cm;


static double const x_2 = x_2_cm / X_hat_in_cm;


static double const y_1 = y_1_cm / X_hat_in_cm;


static double const y_2 = y_2_cm / X_hat_in_cm;


static double const delta_x = (x_2-x_1)/numxx;;
static double const delta_y = (y_2-y_1)/numyy;;


static int const RNumber = 5;
static int const ThetaNumber = 5;
static double const DRSector = SENSING_AREA_RADIUS / (RNumber);
static double const DThetaSector = 2.* SensingAreaHalfAngle / (ThetaNumber);
static int ChangedSide = 0;

