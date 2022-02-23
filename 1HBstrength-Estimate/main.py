## https://online.stat.psu.edu/stat415/lesson/1

#The idea of point esimtation is estimate or calculate something in accurate way.
##The most widely used methods are mehod of of moments and maximum likelhood. They have formulas
## for computing a paramter in accurate way.

# estimation error e = mean_sample - mean_population
# loss function e = abs(mean_sample -  mean_population)
# squared error e =  abs(mean_sample -  mean_population)^2
# As n becomes large, the error reduces the estimate approaches unbiasedness. if the estimae is biased, then unbiased estimation.

## mean is equal to proportion if the x is 0 or 1 or bernouli trails

## Maximum Likelihood Estimation - the "likelihood function" as a function of estimate, and find the value of estimate that maximizes the function
## MLE have a higher probability of being close to the quantities to be estimated and are more often unbiased.
## one has to know the distribution or type of function like exponetial, possion. to calculate the likelihood function as a function of estimate
## constructs likelihood function as a estimate - find parameters that maximum the likelihood function
## Sample Mean, Sample variance is the MLE
## As n becomes large, the difference between sample mean and original mean approches zero

## Unbiased estimation -  An estimator of a given parameter is said to be unbiased if its expected value is equal to the true value of the parameter
## bias of estimator Bias[mean_sample] = E[mean_sample] - mean_poppulation. Estimator is unbiased if the bias is equal to zero.

## Method of moments 
## In method of moments we calculate the following moments
## The important moments are
## first — expected value
## second — variance
## third — skewness
## fourth - kurtosis
## method of moments calculate the paramters for population distribution and for sample data, equate both of them
## the idea is to check sample distribution (from sample data) is close to ideal or original distribution (from original population)
## can be applied if we dont exact function like exponential, possion

from random import choice
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
import pandas as pd

##data set
population=np.array([3.0403,3.05448,2.76165,2.79708,2.81989,3.09176,2.84921,2.8436,2.53183,2.80706,2.81939,3.07237,2.77792,2.88266,2.79205,2.96821,2.70322,2.84363,2.78725,3.01077,2.64422,2.78896,2.64665,3.29653,3.00358,3.35303,2.68521,3.08144,2.73868,3.0002,2.7082,3.02873,2.96116,3.12966,2.96395,3.48085,2.7948,2.99187,2.76322,3.04576,2.8068,3.06413,2.6631,3.03669,2.80173,3.06364,2.70768,2.98243,2.69007,3.12116,2.75045,2.97503,2.66907,3.34714,2.84317,3.16779,2.82851,3.1848,2.67991,2.91231,2.76464,2.93605,2.59857,2.80042,2.52072,3.15517,3.1027,2.96961,3.05766,3.42373,2.97849,2.83558,2.84765,2.88897,3.12334,3.40859,2.7511,2.74547,2.81073,3.27247,2.62898,2.77106,2.51814,2.90661,2.90903,2.96619,2.81232,2.75036,2.88019,2.92192,2.72746,3.35946,2.75297,3.06556,2.72322,2.75989,2.78591,2.88974,3.03529,3.22216,2.78602,3.19007,2.91777,3.03368,2.82035,3.22365,2.8675,2.97715,2.79503,2.87431,2.89355,3.16977,2.73927,2.89195,2.68226,3.11725,2.52205,2.76392,2.88307,2.79198,2.67474,3.04572,2.75542,3.01546,2.71721,3.0407,2.54992,2.64718,2.73592,2.80199,2.95253,2.84357,2.76712,2.74897,2.71947,2.83676,2.99128,2.9742,2.98353,2.96095,2.78667,2.86865,2.76514,2.77174,2.79324,3.00255,2.69393,3.11377,2.68363,2.95436,2.66171,2.85268,2.6567,2.88283,2.7408,3.05527,2.74894,3.22281,2.66002,2.71156,3.28998,3.37669,2.94527,3.0588,2.85244,2.8876,2.73995,3.40312,2.67197,3.38724,2.99208,3.37559,2.6559,2.96778,2.84456,2.91432,2.89253,2.92036,2.75273,3.19634,2.85299,3.28775,3.03729,2.93434,2.70341,2.92737,2.73951,3.17049,2.79564,2.99995,2.70083,2.94009,2.63076,2.6331,2.69012,2.88739,2.87841,3.33327,2.89364,2.88625,2.78949,2.94923,3.13953,2.97103,2.87788,3.04083,2.66728,2.65132,2.71058,3.09442,2.71958,3.32207,3.02575,2.91671,2.78764,3.03352,2.74121,3.4452,2.93692,3.01914,2.90285,3.22733,2.78117,2.84195,2.72394,3.30564,2.68394,2.95327,2.78093,3.15227,2.89735,3.18515,2.696,2.67197,2.70104,2.82723,2.61222,2.92541,2.66771,3.06518,2.9782,3.03899,2.97438,2.9385,2.68581,3.04417,2.90802,3.10666,2.72347,3.04948,3.0265,3.03976,2.87708,3.09464,2.71212,2.9845,3.05211,3.04631,2.77295,2.92195,2.68973,2.65343,2.74776,2.87934,2.74774,2.95398,2.91165,3.17124,2.9194,3.11264,2.78475,3.03921,2.95254,2.71489,2.902,2.81494,2.7435,2.80912,2.90781,2.97476,2.89053,2.99712,2.75173,2.81656,2.84361,3.096,2.82263,2.8649,2.76749,2.76709,2.64331,3.2161,2.74533,3.10577,2.96189,3.05824,2.9372,3.05395,2.76065,2.80082,3.2283,3.32164,2.68488,2.93558,2.70452,3.22626,2.79055,3.12874,2.77359,2.66718,2.71533,3.23084,2.89657,3.03683,2.63417,2.93068,2.79546,2.94877,2.64943,2.71393,2.74197,2.87809,2.98525,3.48757,2.72133,2.82698,2.61624,2.95565,2.76377,2.95818,2.65706,3.10648,2.76011,2.93388,3.00311,3.0017,2.87038,3.19382,2.78437,2.90013,2.86965,2.72179,2.93907,3.21005,2.81607,2.84988,2.69349,2.84609,2.566,2.63514,2.73038,3.00701,2.60898,3.19475,2.72332,2.92891,2.87262,2.99864,2.77251,2.97009,2.90875,3.21138,2.77929,2.85297,2.78943,2.68281,3.03762,3.02386,2.73349,3.02638,2.69616,2.92854,3.07309,3.03875,3.04969,3.10075,2.7109,2.73002,2.55319,2.759,2.76197,2.86833,2.82909,2.94513,2.53679,3.05113,2.7509,3.31964,2.88508,3.3894,2.8898,2.75704,3.01343,2.97603,2.80714,3.24077,2.63491,2.81109,2.67535,3.04042,3.2843,3.09838,2.74095,3.41239,2.86078,2.78397,2.5318,2.88702,2.77625,3.11151,3.13949,3.07332,2.80904,3.34001,2.85238,2.96192,2.71602,2.8205,2.78838,2.87624,2.62943,3.13495,2.75759,2.92207,2.59026,2.92567,2.87733,3.0872,2.8822,3.17614,3.02553,3.06306,2.89049,2.92224,2.91585,3.32754,3.2602,3.18667,2.73199,2.80584,2.91426,2.82189,2.88354,3.09396,2.6249,2.73699,2.78069,2.92759,3.0787,3.08174,2.76785,2.76183,3.10757,2.86716,2.82887,2.88783,2.78496,3.0006,2.69372,2.8828,2.79323,2.82527,2.75646,2.91568,2.83185,3.02307,2.60161,3.38808,2.93564,3.08453,2.84492,2.80152,3.08679,3.2585,2.69809,2.72563,2.62053,3.23414,3.05094,3.19885,2.91709,3.33158,2.7157,2.78406,2.75924,3.03107,2.77292,3.06042,2.5836,2.64272,2.55078,2.95815,2.86701,3.11342,3.02995,3.41844,2.84688,2.90808,2.85802])
population.sort()
#plt.hist(population, bins=np.arange(population.min(), population.max(), 0.05)  )
#plt.show()

## lambda functions for mean and variance
expected_value = lambda values: sum(values) / len(values)
standard_deviation = lambda values, expected_value: np.sqrt(sum([(v - expected_value)**2 for v in values])  / len(values))

## original population
mean_population = expected_value(population)
sd_population = standard_deviation(population, mean_population)
y_population = norm.pdf(population, mean_population, sd_population)
plt.plot(population, y_population,c ="black", label='Original population'+" Mean " + str(round(mean_population, 3)) +" SD = " + str(round(sd_population, 3)))

## sample population
for n in range(25, 226, 100):
    sample = [choice(population) for _ in range(n)]
    sample.sort()    
    mean_sample = expected_value(sample)
    sd_sample  = standard_deviation(sample, mean_sample)  
    y_sample = norm.pdf(sample, mean_sample, sd_sample)   
    plt.plot(sample, y_sample, label='Sample size = '+str(n)+", Mean = " + str(round(mean_sample, 3)) +", SD = " + str(round(sd_sample, 3)) )
plt.title("Method of moments")
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.show()
