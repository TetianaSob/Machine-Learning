# Machine_learning_Graph.py

data
​
time = data['Time_Delay_in_Minutes']
LSD = data['LSD_ppm']
score = data['Avg_Math_Test_Score']

print(time)
print(LSD)
print(score)

plt.plot(time, LSD, color='g')
plt.plot(time, score, color='red')
plt.plot(LSD, color='blue')
plt.show()

​