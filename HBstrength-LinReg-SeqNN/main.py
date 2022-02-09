##plot
from mpl_toolkits import mplot3d
from matplotlib import pyplot 
import matplotlib.pyplot as plt

##linear regression
import numpy as np
import pandas as pd
from sklearn.datasets import load_boston
from sklearn.linear_model  import LinearRegression
from sklearn.model_selection import train_test_split

##tensorflow
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

##3d plot
from mpl_toolkits import mplot3d

## explanatory variables or features
x=pd.DataFrame(
  {"OOdistance":[3.0403,3.05448,2.76165,2.79708,2.81989,3.09176,2.84921,2.8436,2.53183,2.80706,2.81939,3.07237,2.77792,2.88266,2.79205,2.96821,2.70322,2.84363,2.78725,3.01077,2.64422,2.78896,2.64665,3.29653,3.00358,3.35303,2.68521,3.08144,2.73868,3.0002,2.7082,3.02873,2.96116,3.12966,2.96395,3.48085,2.7948,2.99187,2.76322,3.04576,2.8068,3.06413,2.6631,3.03669,2.80173,3.06364,2.70768,2.98243,2.69007,3.12116,2.75045,2.97503,2.66907,3.34714,2.84317,3.16779,2.82851,3.1848,2.67991,2.91231,2.76464,2.93605,2.59857,2.80042,2.52072,3.15517,3.1027,2.96961,3.05766,3.42373,2.97849,2.83558,2.84765,2.88897,3.12334,3.40859,2.7511,2.74547,2.81073,3.27247,2.62898,2.77106,2.51814,2.90661,2.90903,2.96619,2.81232,2.75036,2.88019,2.92192,2.72746,3.35946,2.75297,3.06556,2.72322,2.75989,2.78591,2.88974,3.03529,3.22216,2.78602,3.19007,2.91777,3.03368,2.82035,3.22365,2.8675,2.97715,2.79503,2.87431,2.89355,3.16977,2.73927,2.89195,2.68226,3.11725,2.52205,2.76392,2.88307,2.79198,2.67474,3.04572,2.75542,3.01546,2.71721,3.0407,2.54992,2.64718,2.73592,2.80199,2.95253,2.84357,2.76712,2.74897,2.71947,2.83676,2.99128,2.9742,2.98353,2.96095,2.78667,2.86865,2.76514,2.77174,2.79324,3.00255,2.69393,3.11377,2.68363,2.95436,2.66171,2.85268,2.6567,2.88283,2.7408,3.05527,2.74894,3.22281,2.66002,2.71156,3.28998,3.37669,2.94527,3.0588,2.85244,2.8876,2.73995,3.40312,2.67197,3.38724,2.99208,3.37559,2.6559,2.96778,2.84456,2.91432,2.89253,2.92036,2.75273,3.19634,2.85299,3.28775,3.03729,2.93434,2.70341,2.92737,2.73951,3.17049,2.79564,2.99995,2.70083,2.94009,2.63076,2.6331,2.69012,2.88739,2.87841,3.33327,2.89364,2.88625,2.78949,2.94923,3.13953,2.97103,2.87788,3.04083,2.66728,2.65132,2.71058,3.09442,2.71958,3.32207,3.02575,2.91671,2.78764,3.03352,2.74121,3.4452,2.93692,3.01914,2.90285,3.22733,2.78117,2.84195,2.72394,3.30564,2.68394,2.95327,2.78093,3.15227,2.89735,3.18515,2.696,2.67197,2.70104,2.82723,2.61222,2.92541,2.66771,3.06518,2.9782,3.03899,2.97438,2.9385,2.68581,3.04417,2.90802,3.10666,2.72347,3.04948,3.0265,3.03976,2.87708,3.09464,2.71212,2.9845,3.05211,3.04631,2.77295,2.92195,2.68973,2.65343,2.74776,2.87934,2.74774,2.95398,2.91165,3.17124,2.9194,3.11264,2.78475,3.03921,2.95254,2.71489,2.902,2.81494,2.7435,2.80912,2.90781,2.97476,2.89053,2.99712,2.75173,2.81656,2.84361,3.096,2.82263,2.8649,2.76749,2.76709,2.64331,3.2161,2.74533,3.10577,2.96189,3.05824,2.9372,3.05395,2.76065,2.80082,3.2283,3.32164,2.68488,2.93558,2.70452,3.22626,2.79055,3.12874,2.77359,2.66718,2.71533,3.23084,2.89657,3.03683,2.63417,2.93068,2.79546,2.94877,2.64943,2.71393,2.74197,2.87809,2.98525,3.48757,2.72133,2.82698,2.61624,2.95565,2.76377,2.95818,2.65706,3.10648,2.76011,2.93388,3.00311,3.0017,2.87038,3.19382,2.78437,2.90013,2.86965,2.72179,2.93907,3.21005,2.81607,2.84988,2.69349,2.84609,2.566,2.63514,2.73038,3.00701,2.60898,3.19475,2.72332,2.92891,2.87262,2.99864,2.77251,2.97009,2.90875,3.21138,2.77929,2.85297,2.78943,2.68281,3.03762,3.02386,2.73349,3.02638,2.69616,2.92854,3.07309,3.03875,3.04969,3.10075,2.7109,2.73002,2.55319,2.759,2.76197,2.86833,2.82909,2.94513,2.53679,3.05113,2.7509,3.31964,2.88508,3.3894,2.8898,2.75704,3.01343,2.97603,2.80714,3.24077,2.63491,2.81109,2.67535,3.04042,3.2843,3.09838,2.74095,3.41239,2.86078,2.78397,2.5318,2.88702,2.77625,3.11151,3.13949,3.07332,2.80904,3.34001,2.85238,2.96192,2.71602,2.8205,2.78838,2.87624,2.62943,3.13495,2.75759,2.92207,2.59026,2.92567,2.87733,3.0872,2.8822,3.17614,3.02553,3.06306,2.89049,2.92224,2.91585,3.32754,3.2602,3.18667,2.73199,2.80584,2.91426,2.82189,2.88354,3.09396,2.6249,2.73699,2.78069,2.92759,3.0787,3.08174,2.76785,2.76183,3.10757,2.86716,2.82887,2.88783,2.78496,3.0006,2.69372,2.8828,2.79323,2.82527,2.75646,2.91568,2.83185,3.02307,2.60161,3.38808,2.93564,3.08453,2.84492,2.80152,3.08679,3.2585,2.69809,2.72563,2.62053,3.23414,3.05094,3.19885,2.91709,3.33158,2.7157,2.78406,2.75924,3.03107,2.77292,3.06042,2.5836,2.64272,2.55078,2.95815,2.86701,3.11342,3.02995,3.41844,2.84688,2.90808,2.85802],
   "OH distance":[6.33056,9.60838,11.7177,19.7833,13.0955,16.86,9.50841,13.5383,16.1217,3.14063,14.7443,8.99743,22.3557,12.0173,10.8151,28.1883,16.2228,6.3074,10.2873,11.5723,10.4571,17.2618,5.46283,2.81753,3.07812,13.693,9.92387,12.003,10.3602,6.07742,4.8874,10.3475,17.5737,25.0908,18.5622,14.8525,14.2642,29.0281,2.57132,15.3484,11.526,10.7756,3.54259,17.6118,18.9567,11.7024,10.2516,20.2118,5.54235,10.6789,15.8079,18.9375,12.1145,30.3122,8.85487,11.5355,12.1872,14.726,18.9303,3.32851,4.79213,8.46081,3.41427,8.21198,2.63728,25.9403,5.60692,16.4079,15.5615,30.1025,5.1418,23.7605,9.8478,14.7334,34.5257,5.95801,8.75661,19.0901,10.5195,3.79328,13.0344,12.2961,15.8746,15.4608,4.08911,16.3578,10.1101,11.7324,18.2268,8.84901,7.07695,17.5581,7.48505,6.47474,10.6557,16.8058,8.05795,19.2199,30.1049,31.8821,12.4011,32.75,12.4121,34.0328,12.428,29.647,8.51541,23.6372,8.66141,12.7358,18.0255,5.55378,12.0669,15.5264,4.48797,32.0015,6.61368,33.0139,9.26366,19.534,15.0926,9.78917,11.1263,2.85869,18.7068,12.3517,5.99596,15.192,11.8991,11.127,12.0009,18.6629,6.29135,26.3115,3.03212,11.753,10.9396,25.7351,14.2646,18.2177,16.5128,23.4971,13.773,9.44783,1.3616,7.13156,12.5745,15.4849,13.9961,7.32461,7.315,9.49942,14.6404,4.52387,27.5949,11.8176,6.80449,25.1889,12.8034,5.52698,1.50021,20.6376,8.37167,22.6497,6.04475,5.7659,5.5272,26.9035,14.7192,15.9142,6.95611,8.71186,8.74838,18.9085,14.805,5.81029,1.45668,8.31219,23.317,16.403,9.91783,30.3321,7.83655,19.6035,15.8193,12.3219,6.60902,26.0933,16.0322,12.0779,14.8239,9.89619,8.47511,12.2265,12.0829,13.0125,16.1226,5.43136,6.07807,8.51866,17.805,15.5159,14.0532,16.7538,9.04245,21.4894,11.4893,30.1527,8.22524,12.3779,7.22256,19.3494,2.91758,10.6341,10.5337,17.9127,15.2228,5.97037,16.2937,19.2736,9.02577,34.2697,12.6829,22.3912,8.61289,21.7237,13.7772,18.1851,8.93303,6.55692,13.7153,10.2642,9.55185,11.5817,10.5794,12.3132,11.0976,20.9512,10.2124,6.77758,7.89923,25.4618,6.91462,7.84161,7.47175,19.8244,22.728,16.0625,12.0365,14.3812,20.4078,9.34817,0.897189,1.90683,3.84861,3.11904,16.9626,11.0106,16.6542,19.9516,7.0746,17.6415,14.8152,17.1761,7.8883,16.0209,4.84057,7.09553,10.6552,19.8643,13.0344,32.5376,3.38606,29.7434,13.4783,29.8651,24.0764,10.8829,10.5781,21.3576,10.6527,3.5283,8.0346,10.1294,33.2883,24.8201,2.00516,8.284,12.525,27.8276,7.94392,32.5293,5.65408,13.859,6.83276,16.4604,15.8889,16.9147,14.5204,15.1915,27.9522,22.4369,1.7427,5.16722,10.4208,31.8329,8.82378,20.5695,15.9343,17.7271,3.88698,10.5472,16.864,16.78,8.10435,6.75505,14.5843,4.65127,16.7738,15.8212,1.83585,17.7271,14.6384,28.0507,22.0818,33.3045,5.36759,5.80016,15.2109,19.1915,5.23185,9.21717,12.2459,13.4414,11.9053,16.2626,3.37535,28.9533,10.2587,24.7504,21.9239,33.5721,25.1027,6.30535,2.7648,8.16716,6.99813,5.48145,8.52863,8.67321,19.9192,13.5701,15.3261,7.69017,5.38997,10.5425,8.09043,10.0784,16.4629,5.39785,23.7511,20.6017,10.2288,3.8543,3.25189,27.6177,10.9031,8.24315,4.82663,16.6851,1.0476,17.7743,14.0807,28.7049,13.3544,34.768,2.8628,3.12269, 7.68996, 27.0842 ,20.4471,11.1124,7.59469,18.6431,14.7493,30.0064,20.3943,14.2301,24.9814,21.4956,15.2939,10.109,21.3004,31.0451,12.3823,16.3069,22.7073,6.99996,6.36825,13.9215,5.57235,27.8544,3.88033,4.04211,1.24437,11.3924,12.2571,10.5835,5.96071,19.44,22.6388,28.8518,21.4692,21.1125,2.16152,9.78669,18.0742,12.8791,6.0197,11.3616,15.1977,18.3506,13.7401,9.83726,7.82994,15.1427,21.0593,3.84704,15.9695,22.8241,14.5986,20.1114,7.60238,4.61754,6.88215,16.3099,8.58947,20.3596,13.9458,16.5146,8.27705,33.1357,7.91402,21.8031,7.61943,9.80685,13.0358,13.6119,10.1342,4.81903,7.92115,17.9564,10.7752,30.7535,10.7064,14.6595,26.4286,18.9052,2.13941,11.8577,5.75865,10.5447,14.791,13.1553,17.1884,12.2324,2.77884,16.3983,9.4455,26.5254,6.8879,21.819,27.4912,21.9554,6.95577,10.3311,6.71704,10.0456,8.19775,1.95496,18.4191,26.7724,5.29683,16.5827,12.8968,6.51598,16.8461,24.1496,5.86226,9.27521,13.2538,7.48264,11.3202,24.2187,5.71733,9.6915,7.16352,27.0342,10.3755]})
x=pd.DataFrame(
  {"OOdistance":[3.0403,3.05448,2.76165,2.79708,2.81989,3.09176,2.84921,2.8436,2.53183,2.80706,2.81939,3.07237,2.77792,2.88266,2.79205,2.96821,2.70322,2.84363,2.78725,3.01077,2.64422,2.78896,2.64665,3.29653,3.00358,3.35303,2.68521,3.08144,2.73868,3.0002,2.7082,3.02873,2.96116,3.12966,2.96395,3.48085,2.7948,2.99187,2.76322,3.04576,2.8068,3.06413,2.6631,3.03669,2.80173,3.06364,2.70768,2.98243,2.69007,3.12116,2.75045,2.97503,2.66907,3.34714,2.84317,3.16779,2.82851,3.1848,2.67991,2.91231,2.76464,2.93605,2.59857,2.80042,2.52072,3.15517,3.1027,2.96961,3.05766,3.42373,2.97849,2.83558,2.84765,2.88897,3.12334,3.40859,2.7511,2.74547,2.81073,3.27247,2.62898,2.77106,2.51814,2.90661,2.90903,2.96619,2.81232,2.75036,2.88019,2.92192,2.72746,3.35946,2.75297,3.06556,2.72322,2.75989,2.78591,2.88974,3.03529,3.22216,2.78602,3.19007,2.91777,3.03368,2.82035,3.22365,2.8675,2.97715,2.79503,2.87431,2.89355,3.16977,2.73927,2.89195,2.68226,3.11725,2.52205,2.76392,2.88307,2.79198,2.67474,3.04572,2.75542,3.01546,2.71721,3.0407,2.54992,2.64718,2.73592,2.80199,2.95253,2.84357,2.76712,2.74897,2.71947,2.83676,2.99128,2.9742,2.98353,2.96095,2.78667,2.86865,2.76514,2.77174,2.79324,3.00255,2.69393,3.11377,2.68363,2.95436,2.66171,2.85268,2.6567,2.88283,2.7408,3.05527,2.74894,3.22281,2.66002,2.71156,3.28998,3.37669,2.94527,3.0588,2.85244,2.8876,2.73995,3.40312,2.67197,3.38724,2.99208,3.37559,2.6559,2.96778,2.84456,2.91432,2.89253,2.92036,2.75273,3.19634,2.85299,3.28775,3.03729,2.93434,2.70341,2.92737,2.73951,3.17049,2.79564,2.99995,2.70083,2.94009,2.63076,2.6331,2.69012,2.88739,2.87841,3.33327,2.89364,2.88625,2.78949,2.94923,3.13953,2.97103,2.87788,3.04083,2.66728,2.65132,2.71058,3.09442,2.71958,3.32207,3.02575,2.91671,2.78764,3.03352,2.74121,3.4452,2.93692,3.01914,2.90285,3.22733,2.78117,2.84195,2.72394,3.30564,2.68394,2.95327,2.78093,3.15227,2.89735,3.18515,2.696,2.67197,2.70104,2.82723,2.61222,2.92541,2.66771,3.06518,2.9782,3.03899,2.97438,2.9385,2.68581,3.04417,2.90802,3.10666,2.72347,3.04948,3.0265,3.03976,2.87708,3.09464,2.71212,2.9845,3.05211,3.04631,2.77295,2.92195,2.68973,2.65343,2.74776,2.87934,2.74774,2.95398,2.91165,3.17124,2.9194,3.11264,2.78475,3.03921,2.95254,2.71489,2.902,2.81494,2.7435,2.80912,2.90781,2.97476,2.89053,2.99712,2.75173,2.81656,2.84361,3.096,2.82263,2.8649,2.76749,2.76709,2.64331,3.2161,2.74533,3.10577,2.96189,3.05824,2.9372,3.05395,2.76065,2.80082,3.2283,3.32164,2.68488,2.93558,2.70452,3.22626,2.79055,3.12874,2.77359,2.66718,2.71533,3.23084,2.89657,3.03683,2.63417,2.93068,2.79546,2.94877,2.64943,2.71393,2.74197,2.87809,2.98525,3.48757,2.72133,2.82698,2.61624,2.95565,2.76377,2.95818,2.65706,3.10648,2.76011,2.93388,3.00311,3.0017,2.87038,3.19382,2.78437,2.90013,2.86965,2.72179,2.93907,3.21005,2.81607,2.84988,2.69349,2.84609,2.566,2.63514,2.73038,3.00701,2.60898,3.19475,2.72332,2.92891,2.87262,2.99864,2.77251,2.97009,2.90875,3.21138,2.77929,2.85297,2.78943,2.68281,3.03762,3.02386,2.73349,3.02638,2.69616,2.92854,3.07309,3.03875,3.04969,3.10075,2.7109,2.73002,2.55319,2.759,2.76197,2.86833,2.82909,2.94513,2.53679,3.05113,2.7509,3.31964,2.88508,3.3894,2.8898,2.75704,3.01343,2.97603,2.80714,3.24077,2.63491,2.81109,2.67535,3.04042,3.2843,3.09838,2.74095,3.41239,2.86078,2.78397,2.5318,2.88702,2.77625,3.11151,3.13949,3.07332,2.80904,3.34001,2.85238,2.96192,2.71602,2.8205,2.78838,2.87624,2.62943,3.13495,2.75759,2.92207,2.59026,2.92567,2.87733,3.0872,2.8822,3.17614,3.02553,3.06306,2.89049,2.92224,2.91585,3.32754,3.2602,3.18667,2.73199,2.80584,2.91426,2.82189,2.88354,3.09396,2.6249,2.73699,2.78069,2.92759,3.0787,3.08174,2.76785,2.76183,3.10757,2.86716,2.82887,2.88783,2.78496,3.0006,2.69372,2.8828,2.79323,2.82527,2.75646,2.91568,2.83185,3.02307,2.60161,3.38808,2.93564,3.08453,2.84492,2.80152,3.08679,3.2585,2.69809,2.72563,2.62053,3.23414,3.05094,3.19885,2.91709,3.33158,2.7157,2.78406,2.75924,3.03107,2.77292,3.06042,2.5836,2.64272,2.55078,2.95815,2.86701,3.11342,3.02995,3.41844,2.84688,2.90808,2.85802]})
## response or target
y=pd.DataFrame(
  {"hydrogenbondstrength":[-8.39084,-5.15736,-30.0507,-9.47462,-15.1347,-6.47587,-13.2604,-13.1133,-36.0654,-18.6279,-16.7918,-6.37431,-16.2805,-12.2691,-17.5547,-6.80172,-18.0682,-8.73322,-19.7488,-8.29111,-22.2187,-14.4159,-25.4086,-4.62937,-7.40775,-3.91978,-21.3801,-5.28439,-21.3309,-6.28107,-24.5513,-9.51618,-8.94626,-3.65051,-8.56598,-3.84045,-13.7383,-5.01884,-16.5164,-5.47887,-15.9512,-5.66782,-29.084,-9.58285,-13.0997,-7.32638,-18.4397,-7.3914,-26.4519,-5.58973,-24.6951,-7.09107,-25.0351,-2.79633,-15.6273,-5.98747,-20.1683,-3.57893,-21.4944,-16.2541,-17.8883,-16.9023,-42.3418,-15.4328,-53.8918,-4.31075,-6.594,-5.71948,-6.5357,-0.998637,-12.4002,-11.4154,-19.5332,-14.8477,-4.32398,-3.58084,-25.0445,-13.6229,-16.3677,-6.31691,-18.4334,-17.1118,-30.5508,-9.53353,-12.8957,-8.77708,-22.1768,-21.9337,-9.18627,-8.49513,-21.5347,-3.9197,-22.4331,-5.67651,-20.5863,-12.148,-14.2253,-11.8072,-6.60859,-2.81227,-18.1411,-3.43741,-11.6831,-4.1417,-16.6815,-2.68438,-14.6982,-6.76785,-19.8563,-9.96282,-8.33802,-5.73681,-16.8845,-9.69244,-32.545,-3.91834,-34.3203,-7.72062,-15.9134,-13.1407,-27.1225,-7.14722,-19.6884,-6.8339,-19.3978,-6.60432,-45.5162,-28.6485,-22.9101,-15.4384,-12.6067,-10.7234,-22.5155,-11.5605,-27.389,-13.0018,-13.7334,-8.43953,-12.5767,-8.06014,-16.8864,-11.0529,-23.1543,-18.2751,-12.2765,-9.98001,-28.1109,-3.32853,-20.0674,-9.94875,-37.4154,-18.834,-25.4602,-11.2576,-10.6333,-8.91972,-18.1585,-3.73464,-23.6807,-21.1592,-5.10893,-3.43379,-11.6696,-4.18273,-21.2662,-13.5066,-19.5496,-1.58879,-18.4336,-2.566,-9.59472,-2.00868,-28.1849,-6.57066,-14.9737,-11.5491,-15.8559,-11.9515,-15.2629,-5.87031,-22.4554,-2.46105,-11.1628,-9.17587,-18.2602,-11.0147,-43.7388,-3.75672,-13.1502,-9.55545,-19.6684,-14.0767,-33.9255,-24.4798,-30.2101,-11.7765,-17.5276,-4.72621,-16.3418,-15.5298,-16.2919,-12.0263,-5.75224,-5.72751,-16.0525,-5.1555,-17.5759,-12.7064,-21.4762,-8.72967,-27.7339,-3.29351,-15.0237,-10.6326,-24.8696,-7.07364,-19.7029,-3.14816,-10.5405,-7.36633,-8.61024,-2.63647,-20.9241,-8.48479,-25.1681,-2.15226,-24.2338,-9.513,-19.5002,-6.8213,-8.99149,-4.96697,-25.7644,-22.0494,-20.6938,-14.9729,-38.7232,-13.6582,-24.6486,-9.25024,-10.0359,-4.14873,-9.31607,-6.25459,-17.2392,-5.92875,-8.94582,-5.03659,-16.5563,-7.01951,-8.60296,-7.60071,-15.4692,-6.13069,-28.8711,-9.92481,-11.2024,-8.80302,-16.4676,-7.86681,-25.4252,-15.7871,-18.3048,-10.0896,-17.18,-9.55027,-11.82,-4.20045,-11.7972,-5.04777,-15.3038,-5.22147,-10.6876,-8.77485,-14.0544,-8.98839,-12.9947,-12.0268,-12.6218,-6.92108,-12.3011,-8.87276,-21.9572,-19.1784,-6.71795,-5.1361,-22.5035,-14.2276,-18.1689,-10.5248,-19.6438,-1.78418,-25.2279,-6.33869,-9.84887,-6.08262,-8.06027,-8.04478,-19.6512,-13.0076,-4.83504,-4.53868,-27.0496,-15.3732,-27.4189,-2.54391,-19.54,-7.3327,-22.1012,-20.251,-21.2696,-5.43632,-10.2208,-8.83735,-33.6709,-7.01875,-15.0888,-9.82404,-20.8249,-19.2249,-32.0841,-8.98913,-9.3456,-2.16203,-14.3575,-8.1994,-22.761,-10.8924,-17.7372,-7.7233,-27.168,-4.66148,-21.0154,-10.9485,-11.1774,-7.97089,-14.9658,-1.17258,-17.9058,-7.20523,-11.1598,-11.0837,-7.4434,-7.14483,-19.3591,-14.2106,-30.1943,-14.9249,-27.0588,-24.0715,-15.5288,-6.24411,-31.5294,-5.19343,-32.8261,-15.6947,-14.539,-10.5839,-17.5498,-9.8663,-10.0532,-2.42859,-26.5508,-23.8211,-19.9775,-8.34543,-12.0565,-8.505,-28.8128,-8.82874,-22.2384,-7.54743,-10.6641,-4.59748,-5.14597,-3.34769,-26.7099,-21.4421,-51.1977,-9.65113,-17.1575,-17.0281,-12.5456,-5.97791,-42.9009,-5.03084,-14.6657,-1.95192,-5.9571,-2.07019,-15.1986,-14.8576,-6.63461,-4.30983,-14.0256,-3.42282,-19.1242,-17.9056,-20.6923,-7.61657,-5.33376,-4.86113,-20.4653,-1.66465,-15.1813,-14.9948,-27.1827,-13.0528,-22.249,-6.50459,-6.02385,-5.45643,-16.4975,-3.29075,-15.041,-10.412,-20.6289,-16.3656,-21.0245,-11.1364,-25.6212,-5.35274,-12.2349,-10.9297,-35.1818,-9.84212,-11.5666,-8.02218,-16.9133,-5.47963,-7.7506,-5.66987,-15.8354,-11.2733,-18.0739,-2.86634,-7.20591,-6.15061,-21.6134,-12.5488,-11.2917,-6.09809,-16.3138,-4.39162,-30.5077,-16.3613,-23.4895,-8.4136,-8.42614,-6.76602,-15.3634,-11.2147,-7.94225,-6.87254,-13.7593,-12.4364,-13.3191,-8.47783,-26.6144,-13.2028,-15.8432,-13.6371,-16.8656,-13.5559,-11.1343,-10.6245,-40.6644,-3.62575,-13.7107,-4.41255,-15.6165,-14.054,-5.16285,-2.57421,-24.5687,-14.8598,-24.2363,-3.77919,-9.83396,-5.5324,-10.2399,-2.89666,-30.2145,-14.287,-16.0062,-9.64953,-19.6603,-4.6336,-52.5016,-28.6831,-34.3704,-11.4247,-13.8748,-6.63521,-8.54779,-3.53438,-25.7402,-7.90821,-19.3088]})


## ---- Multiple linear regression -----##
linreg=LinearRegression()
linreg.fit(x,y)

## intercept and linear and non-linear coeffcients
beta=linreg.coef_
alpha=linreg.intercept_
print("beta ", beta,  " alpha ", alpha)

x1=np.array(x['OOdistance'])
y1=linreg.predict(x) ## equivalent to the expression alpha+beta[0][0]*x1+beta[0][1]*x2
y1=y1[:,0]
#z1=np.array(x['OH distance'])
#z1 = [xf for _,xf in sorted(zip(x1, z1))]
y1 = [xf for _,xf in sorted(zip(x1, y1))]
x1.sort()
## ---- Multiple linear regression -----##


## ---- Neural network -----##
scale_x = MinMaxScaler()
xs = scale_x.fit_transform(x)
scale_y = MinMaxScaler()
ys = scale_y.fit_transform(y)

model = Sequential()
model.add(Dense(10, input_dim=1, activation='relu', kernel_initializer='he_uniform'))
model.add(Dense(10, activation='relu', kernel_initializer='he_uniform'))
model.add(Dense(1))
model.compile(loss='mse', optimizer='adam')
model.fit(xs, ys, epochs=500, batch_size=10, verbose=0)
yhat = model.predict(xs)

x_plot = scale_x.inverse_transform(xs)
y_plot = scale_y.inverse_transform(ys)
yhat_plot = scale_y.inverse_transform(yhat)
ynn=yhat_plot

xnn=np.array(x['OOdistance'])
##znn=np.array(x['OH distance'])
##znn = [xf for _,xf in sorted(zip(xnn, znn))]
ynn = [xf for _,xf in sorted(zip(xnn, ynn))]
xnn.sort()
## ---- Neural network -----##

##2D plot
plt.scatter(x['OOdistance'], y ,c='red', label='Actual')
plt.plot(x1,y1,c='black', label='Multiple Linear regression')
plt.plot(xnn,ynn, c='green', marker='o', label='Neural network')
plt.legend(loc="upper left")
#plt.title('Input (x) versus Output (y)')
plt.xlabel('O-O distance (angstrom)')
plt.ylabel('HB strength (KJ per mol)')
plt.show()


