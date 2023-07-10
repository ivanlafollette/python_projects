"""
Exam Grade Calculator: This will calculate a grade based on a test score. 
"""
studentName = input("What is your first and last name? ")
examName = input("What class is this exam for? ")
print()
examScore = int(input("What grade did you get on the score? "))
print()

# This is the various grades possible.
if examScore >= 90:
  score_rounded = round(examScore, 2)
  score_formatted = f"{score_rounded:.2f}"
  print("You did very well on the", examName, f"exam. You received a {score_formatted}, which is an A+. Good job,", studentName)

elif examScore >= 80:
  score_rounded = round(examScore, 2)
  score_formatted = f"{score_rounded:.2f}"
  print("You did great on the", examName, f"exam. You received a {score_formatted}, which is an A-. Nice,", studentName)

elif examScore >= 70:
  score_rounded = round(examScore, 2)
  score_formatted = f"{score_rounded:.2f}"
  print("You did okay on the", examName, f"exam. You received a {score_formatted}, which is an B. Not bad,", studentName)
  
elif examScore >= 60:
  score_rounded = round(examScore, 2)
  score_formatted = f"{score_rounded:.2f}"
  print("You did decently on the", examName, f"exam. You received a {score_formatted}, which is a C. At least you passed,", studentName)
  
elif examScore >= 50:
  score_rounded = round(examScore, 2)
  score_formatted = f"{score_rounded:.2f}"
  print("You did so-so on the", examName, f"exam. You received a {score_formatted}, which is a D. You could do better,", studentName)

elif examScore >= 40:
  score_rounded = round(examScore, 2)
  score_formatted = f"{score_rounded:.2f}"
  print("You did poorly on the", examName, f"exam. You received a {score_formatted}, which is a U. Just awful,", studentName)
  
else:
  score_rounded = round(examScore, 2)
  score_formatted = f"{score_rounded:.2f}"
  print("You failed the", examName, f"exam. You received a {score_formatted}, which is an F. We need to talk after class,", studentName)
  

