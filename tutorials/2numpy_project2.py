
import numpy as np

country = ['Great Britain', 'China', 'Russia', 'United States', 'Korea', 'Japan', 'Germany']
countrycode = ['GBR','CHN','RUS','US','KOR','JPN','GER']
year=2012
gold=np.array([29,38, 24, 46, 13, 7, 11 ])
silver=np.array([17,28,25,28,8,14,11])
bronze=np.array([19,22,32,29,7,17,14])

print("Country won most golds = ", country[np.argmax(gold)]) 

for position, name in enumerate(country):
    if(gold[position] > 20):
        print("Country", name,' gold ', gold[position])

totalmedal=gold+silver+bronze
for position, name in enumerate(country):
    print(" {}, Gold medals {}, total medals {}". format(country[position], gold[position], totalmedal[position]) )

for position, name in enumerate(country):
    print(" {}, Gold medals {}". format(country[position], gold[position]) )

for position, name in enumerate(country):
    print(" {}, Total medals {}". format(country[position], totalmedal[position]) )

