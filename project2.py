jazz_points = 0
judge_points = 0
stanton_points = 0

answer1 = input("do you like  A, an all round baseball player or B, a power hitter? ")
if answer1 == "A":
    jazz_points += 1
elif answer1 == "B":
    judge_points += 1
    stanton_points += 1
input()
answer2 = input("Do you care about A, style B, Likability or C, humbleness? ")
if answer2 == "A":
    jazz_points += 1
elif answer2 == "B":
    judge_points += 1
elif answer2 == "C":
    stanton_points += 1
input()
answer3 = input("Do you like people hitting home runs with A, quantity B, quality, or C, flair? ")
if answer3 == "A":
    judge_points += 1
elif answer3 == "B":
    stanton_points += 1
elif answer3 == "C":
    jazz_points += 1
input()
answer4 = input("would you like a vacation is A, the bahamas or B, California? ")
if answer4 == "A":
    jazz_points +=1
elif answer4 == "B":
    judge_points += 1
    stanton_points += 1
input()
answer5 = input("Do you think people size matters in baseball? (yes or no) ")
if answer5 == "yes" or answer5 == "Yes" or answer5 == "YES":
    judge_points += 1
    stanton_points += 1
elif answer5 == "no" or answer5 == "No" or answer5 == "NO":
    jazz_points += 1
input()
if jazz_points >= judge_points and jazz_points >= stanton_points:
    print("You like or would like Jazz Chisholm Jr (Jasrado Hermis Arrington Chisholm Jr.)!")
elif judge_points >= jazz_points and judge_points >= stanton_points:
    print("You like or would like Aaron Judge!")
elif stanton_points >= judge_points and stanton_points >= jazz_points:
    print("You like or would like Giancarlo Stanton!")