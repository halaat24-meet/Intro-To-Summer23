import random


temperatures = []
even_temp_days=[]
odd_temp_days=[]


for i in range(7) :
 	temperatures.append(random.randint(26,41))
days_of_the_week=["Sunday","Monday","Tuesday", "Wednsday", "Thursday", "Friday", "Saturday"]

for r in range(7):
	print(days_of_the_week[r], ":", temperatures[r])

for x in range(7):
	if (temperatures[x]% 2) == 0: 
		even_temp_days.append(days_of_the_week[x])
		
	else:
		odd_temp_days.append(days_of_the_week[x])
print("The even temperatures of the week:")
print (even_temp_days)

good_days_count= len(even_temp_days)
print (good_days_count)

highest_temp = 0 
for i in range(7): 
	if temperatures[i]>highest_temp:
		highest_temp=temperatures[i]
		day= days_of_the_week[i]
print("the highest temperature is", highest_temp)

lowest_temp=temperatures[0]
for h in range(7):
	if temperatures[h]<lowest_temp:
		lowest_temp=temperatures[h]
		weekday=days_of_the_week[h]
print("the lowest temperature is", lowest_temp)

sum = 0 
for y in range(7):
	sum = sum +temperatures[y]
	average= sum/7
print("the average temperature was",average)
 
above_average=[]
for k in range(7):
 	if temperatures[k]> average:
 		above_average.append(temperatures[k])
 		days= days_of_the_week[k]

print("the days with above average temperatures were:", days)


