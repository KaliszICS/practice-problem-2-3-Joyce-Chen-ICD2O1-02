'''
    Lesson: Else if
    Author: Joyce Chen
    Date Created: Oct 16, 2024
    Date Last Modified: Oct 16, 2024
'''

def q1(): 
  word = input("In: ")
  if word[-3] == "i" and word[-2] == "f" and word [-1] == "e":
    print("-ives")
  elif word[-2] == "e" and word[-1] == "y":
    print("-eys")
  elif word[-1] == "y":
    print("-ies")
  else:
    print("-s")

def q2(): 
  num = int(input("In: "))
  if num > 0:
    print(f"{num} is positive")
  elif num < 0:
    print(f"{num} is negative")

def q3():
  side1 = float(input("Input a number: "))
  side2 = float(input("Input a number: "))
  side3 = float(input("Input a number: "))
  if side1 == side2 and side1 == side3 and side2 == side3:
    print("Equilateral")
  elif side1 == side2 or side1 == side3 or side2 == side3:
    print("Isosceles")
  elif (side1 + side2) < side3:
    print("No Triangle")
  else:
    print("Scalene")

#Do not alter the following code
#Comment out the following code when running your tests

# q1()
# q2()
# q3()