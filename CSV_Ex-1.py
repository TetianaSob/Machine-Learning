myAge = 32
    print(myAge)
#32
myAge = 32
    print(myAge)
#32
myAge = 33
    print(myAge)
#33
    print(myAge/3)
11.0
myAge = myAge + 1
    print(myAge)
#34
restaurantBill = 36.17
serviceCharge = 0.125
    print(restaurantBill * serviceCharge)
#4.52125
type(33)
#int
type(33.6)
#float
type("Philipp")
#str
type(myAge)
#int
type(restaurantBill)
#float

# the lists
​
firstPrime = 1
secondPrime = 2
thirdPrime = 3
​
primeNumbers = [3, 7, 61, 29, 199]
type(primeNumbers)
#list
coolPeople = ['Jay Z', 'Ghandi', 'me']
type(coolPeople)
#list
type(primeAndPeople)
primeAndPeople = ['King Arthur', 17, 11, 'me']
type(primeAndPeople)
#list
primeNumbers[2]
#61
bestPrimeEver = primeNumbers[4]
    print(bestPrimeEver)
bestPrimeEver = primeNumbers[4]
    print(bestPrimeEver)
#199

import pandas as pd
data = pd.read_csv('lsd_math_score_data.csv')
    print(data)

​'''
   Time_Delay_in_Minutes  LSD_ppm  Avg_Math_Test_Score
0                      5     1.17                78.93
1                     15     2.97                58.20
2                     30     3.26                67.47
3                     60     4.69                37.47
4                    120     5.83                45.65
5                    240     6.00                32.92
6                    480     6.41                29.97
'''

type(data)
#pandas.core.frame.DataFrame

onlyMathScores = data['Avg_Math_Test_Score']
    print(onlyMathScores)
'''
0    78.93
1    58.20
2    67.47
3    37.47
4    45.65
5    32.92
6    29.97
'''
#Name: Avg_Math_Test_Score, dtype: float64
    print(data)
data['Test_Subject'] = 'Jennifer Lopez'
    print(data)
    '''
   Time_Delay_in_Minutes  LSD_ppm  Avg_Math_Test_Score    Test_Subject
0                      5     1.17                78.93  Jennifer Lopez
1                     15     2.97                58.20  Jennifer Lopez
2                     30     3.26                67.47  Jennifer Lopez
3                     60     4.69                37.47  Jennifer Lopez
4                    120     5.83                45.65  Jennifer Lopez
5                    240     6.00                32.92  Jennifer Lopez
6                    480     6.41                29.97  Jennifer Lopez
'''
    print(data)
data['High_Score'] = 100
    print(data)
'''
   Time_Delay_in_Minutes  LSD_ppm  Avg_Math_Test_Score    Test_Subject  \
0                      5     1.17                78.93  Jennifer Lopez   
1                     15     2.97                58.20  Jennifer Lopez   
2                     30     3.26                67.47  Jennifer Lopez   
3                     60     4.69                37.47  Jennifer Lopez   
4                    120     5.83                45.65  Jennifer Lopez   
5                    240     6.00                32.92  Jennifer Lopez   
6                    480     6.41                29.97  Jennifer Lopez   

   High_Score  
0         100  
1         100  
2         100  
3         100  
4         100  
5         100  
6         100  
'''
    print(data)
data['High_Score'] = data['High_Score'] + data['Avg_Math_Test_Score']
print(data)
'''
   Time_Delay_in_Minutes  LSD_ppm  Avg_Math_Test_Score    Test_Subject  \
0                      5     1.17                78.93  Jennifer Lopez   
1                     15     2.97                58.20  Jennifer Lopez   
2                     30     3.26                67.47  Jennifer Lopez   
3                     60     4.69                37.47  Jennifer Lopez   
4                    120     5.83                45.65  Jennifer Lopez   
5                    240     6.00                32.92  Jennifer Lopez   
6                    480     6.41                29.97  Jennifer Lopez   

   High_Score  
0      257.86  
1      216.40  
2      234.94  
3      174.94  
4      191.30  
5      165.84  
6      159.94  
'''
    print(data)
data['High_Score'] = data['High_Score'] * data['High_Score']
    print(data)
    '''
   Time_Delay_in_Minutes  LSD_ppm  Avg_Math_Test_Score    Test_Subject  \
0                      5     1.17                78.93  Jennifer Lopez   
1                     15     2.97                58.20  Jennifer Lopez   
2                     30     3.26                67.47  Jennifer Lopez   
3                     60     4.69                37.47  Jennifer Lopez   
4                    120     5.83                45.65  Jennifer Lopez   
5                    240     6.00                32.92  Jennifer Lopez   
6                    480     6.41                29.97  Jennifer Lopez   

   High_Score  
0  66491.7796  
1  46828.9600  
2  55196.8036  
3  30604.0036  
4  36595.6900  
5  27502.9056  
6  25580.8036  
'''
print(data)
data['High_Score'] = data['High_Score'] ** 2
print(data)

'''
   Time_Delay_in_Minutes  LSD_ppm  Avg_Math_Test_Score    Test_Subject  \
0                      5     1.17                78.93  Jennifer Lopez   
1                     15     2.97                58.20  Jennifer Lopez   
2                     30     3.26                67.47  Jennifer Lopez   
3                     60     4.69                37.47  Jennifer Lopez   
4                    120     5.83                45.65  Jennifer Lopez   
5                    240     6.00                32.92  Jennifer Lopez   
6                    480     6.41                29.97  Jennifer Lopez   

     High_Score  
0  4.421157e+09  
1  2.192951e+09  
2  3.046687e+09  
3  9.366050e+08  
4  1.339245e+09  
5  7.564098e+08  
6  6.543775e+08  
'''
type(onlyMathScores)
pandas.core.series.Series
'LSD_ppm'
#nested list
cleanData = data[['LSD_ppm', 'Avg_Math_Test_Score']]
    print(cleanData)
'''
   LSD_ppm  Avg_Math_Test_Score
0     1.17                78.93
1     2.97                58.20
2     3.26                67.47
3     4.69                37.47
4     5.83                45.65
5     6.00                32.92
6     6.41                29.97
'''
type(cleanData)
pandas.core.frame.DataFrame
y = data[['Avg_Math_Test_Score']]
print(y)

'''
   Avg_Math_Test_Score
0                78.93
1                58.20
2                67.47
3                37.47
4                45.65
5                32.92
6                29.97
'''
type(y)
pandas.core.frame.DataFrame
 X = data[['LSD_ppm']]
 print(X)
type(X)

'''
   LSD_ppm
0     1.17
1     2.97
2     3.26
3     4.69
4     5.83
5     6.00
6     6.41
'''
pandas.core.frame.DataFrame
del data['Test_Subject']
    print(data)
'''
   Time_Delay_in_Minutes  LSD_ppm  Avg_Math_Test_Score    High_Score
0                      5     1.17                78.93  4.421157e+09
1                     15     2.97                58.20  2.192951e+09
2                     30     3.26                67.47  3.046687e+09
3                     60     4.69                37.47  9.366050e+08
4                    120     5.83                45.65  1.339245e+09
5                    240     6.00                32.92  7.564098e+08
6                    480     6.41                29.97  6.543775e+08
​'''