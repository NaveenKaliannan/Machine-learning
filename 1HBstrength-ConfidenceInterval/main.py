## confidence interval - gives upper and lower bound for
## population mean with a certain level of confidence.

## sd decreases, confidence interval length decreases
## sample size increases, confidence interval length decreases
## confidence level decreases, confidence interval length decreases

## use the below formula only if the distribution is normal. otherwise use more
## data to make it normally distributed
## for non normal distribution, use nonparametric confidence interval for the median


import numpy as np
import scipy.stats as st
import math


### Formula for confidence intercal
confidence_interval = lambda mean, z_value, std, n: (mean  - z_value * (std/math.sqrt(n)), mean  + z_value * (std/math.sqrt(n)) )


np.random.seed(0)
population = np.random.randint(10, 30, 50)
mean_population = np.mean(population)
std_population = np.std(population)
sem_population = st.sem(population)

## z-score
#    90%      Two-Sided Z-Score: 1.64        One-Sided Z-Score: 1.28
#    95%      Two-Sided Z-Score: 1.96        One-Sided Z-Score: 1.65
#    99%      Two-Sided Z-Score: 2.58        One-Sided Z-Score: 2.33

#create 95% confidence interval for population mean weight
con_int_population = st.norm.interval(alpha=0.95, loc=mean_population, scale=sem_population)

alpha=str(0.95)
zvalue = {"0.90":1.64,"0.95":1.96,"0.99":2.58}
print("(Lower bound, upper bound) ", con_int_population, confidence_interval(mean_population, zvalue[alpha], std_population, len(population) ))
print("Length of the bound or confidence interval or margin of error ", con_int_population[1] - con_int_population[0]  )


