import pandas as pd
data = pd.read_csv('lsd_math_score_data.csv')
print(data)
print(data)
​
'''
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
type(data)
pandas.core.frame.DataFrame
#onlyMathScores

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
Name: Avg_Math_Test_Score, dtype: float64
​'''