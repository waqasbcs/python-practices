student_scores = [70,80,50,30,10,100,120,40,5,1,0,150,110,]
#highest_score
highest_score = 0

for score in student_scores:
    if score > highest_score:
        highest_score = score
print(f"the highest score for student is {highest_score}")

#lowest_score

lowest_score = highest_score
for score in student_scores:
    if score < lowest_score:
        lowest_score = score
print(f"the lowest score for student is {lowest_score}")

#range fuction

for number in range(1,11):
    print(f"{number}")
    
total = 0
for number in range(1, 101):
    total += number
print(total)

#even numbers
total = 0
for number in range(2, 101 , 2):
    total += number
print(total)

#or in this way but will gave us a same results

totalW = 0
for number in range(1, 101):
    if number % 2 == 0:
        totalW += number
print(totalW)

     

