import numpy as np

#median- middle number if n is odd, then middle observation is (n+1)/2 . if n is even, then middle observation is average between n/2 and (n+1)/2
#mean  - average value

a = [57,61,57,57,58,57,61,54,68,51,49,64,50,48,65,52,56,46,54,49,51,47,55,55,54,42,51,56,55,51,54,51,60,61,43,55,56,61,52,69,64,46,54,47,70]

print("N = ", len(a) )
print("Mean = ", np.mean(a) )
#a.sort()
print("sorted = ", a )
print("median = ", np.median(a), )


## truncated or trimmer mean will eliminate the extreme outliers, trimmed p means it cuts p percenet on the right side and p percenet on the left of the distribution. then arithemetic mean is taken for the trimmer data set. 10 percent trimmed means we have only 80 percent data for calculating mean. 
## mean is sensitive to the outliers, while the median is not. Median is considered as resistance measure, while mean is not.

## Measuring spread - Box plot (min, first quartile, median, third quartile, max). Interquartile = third quartile - first quartile
##                              if value is is greater than third quartile + 3/2 Interquartile or less than the first quartile - 3/2 Interquartile then it is called outliers.
##                              3/2 is the standard value it can be changed

print(min(a), np.quantile(a, 0.25), np.quantile(a,0.5), np.quantile(a,0.75),  max(a))
outliers=[]
for i in a:
    if(i > np.quantile(a,0.75) + 1.5 * (np.quantile(a,0.75) - np.quantile(a,0.25))  ):
        outliers.append(i)
print("outliers = ,", outliers)

## sample variance is the  square of standard deviation  and square of diffences from mean
## coefficient of varitation - dispersion of data points = ratio between standard deviation / mean . Higher value means strongle dispersed.

## mean , variance for aggregated data (number of observation, mean, variance for two measurements)
## combined mean = (noofobservation1*mean1+noofobservation2*mean2)/(noofobservation1 + noofobservation2)
## combined variance = write it?????

## z-score or standard score = x - mean / standard deviation  has mean zero and deviation 1, z-value gives the number of sd below or above the mean

print((a-np.mean(a)) / np.std(a))


