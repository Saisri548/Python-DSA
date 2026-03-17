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

print("Maximum of three numbers")  
a1=int(input("Enter number1"))  
b1=int(input("Enter number2"))
c1=int(input("Enter number3"))

if(a1>b1 and a1>c1):
    print(a1)
elif (b1>c1):
    print(b1)
else:
    print(c1)        
s1=int(input("Enter side1"))  
s2=int(input("Enter side2"))  
s3=int(input("Enter side3"))
if(s1+s2>s and s1+s3>s2 and s2+s3>s1):
    if s1==s2 and s2==s3 and s3==s1:
        print("Equilateral Triangle")
    elif s1!=s2 and s2!=s3 and s3!=s1:
        print("Scalene triangle")
    else:
        print("Isocesless triangle")    
