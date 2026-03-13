#Question 1. Even/Odd Check
# Input: an integer
# Print Even if divisible by 2, Odd if not
n=int(input("Enter number"))
if(n%2==0):
    print("Even")
else:
    print("Odd")   
p=int(input("Enter number"))     
if(p>0):
    print("Positive")
elif(p<0):
    print("Negative") 
else:
    print("Zero")       
Fizz_Buzz=int(input("Enter number"))   
if(Fizz_Buzz%3==0 and Fizz_Buzz%5==0):
    print("Fizz_Buzz")

elif(Fizz_Buzz%3==0):
    print("Fizz")
elif(Fizz_Buzz%5==0):
    print("Buzz")
else:
    print("Neither it can't be print in 3 and 5")    

Leap_Year=int(input("Enter Year"))
if(Leap_Year%4==0 and (not Leap_Year%100!=0) or Leap_Year%400==0):
    print("Leap Year")
else:
    print("Not leap Year")    