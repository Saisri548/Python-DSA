# # #22 Patterns from Striver sheet 
# # #Pattern printing
# n1=int(input("Enter n1:"))
# for i in range(0,n1):
#     print("*"*n1)
# n2=int(input("Enter n2:"))    
# for i in range(1,n2+1):
#     print("*"*i)
# n3=int(input("Enter n3:"))
# for i in range(1,n3+1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print("")  
# n4=int(input("Enter n4:"))
# for i in range(1,n4+1):
#     for j in range(1,i+1):
#         print(i,end="")
#     print("")    
# n5=int(input("Enter n5"))
# for i in range(n5,0,-1):
#     for j in range(i,0,-1):
#         print("*",end=" ")
#     print("")    
# n6=int(input("Enter n5"))
# for i in range(n6,0,-1):
#     for j in range(i,0,-1):
#         print(j,end=" ")
#     print("")      
# n7=int(input("Enter n6:"))    
# for i in range(1,n7+1):
#     for j in range(n7-i,0,-1):
#         print(" ",end=" ")
#     for k in range(1,2*i):
#         print("*",end=" ")  
#     print("")     
# n8=int(input("Enter n8:"))
# for i in range(n8,0,-1):
#     for j in range(n8-i):
#         print(" ",end="")
#     for k in range(2*i-1):
#         print("*",end="")  
#     print(" ")  
# n9=int(input("enter n9:"))        
# for i in range(1,n9+1):
#     for j in range(n9-i,0,-1):
#         print(" ",end=" ")
#     for k in range(1,2*i):
#         print("*",end=" ")  
#     print(" ")     

# for i in range(n9,0,-1):
#     for j in range(n9-i):
#         print(" ",end=" ")
#     for k in range(2*i-1):
#         print("*",end=" ")  
#     print(" ") 
# n10=int(input("Enter n10:"))
# for i in range(1,n10+1,1):
#     print("*"*i)
# for i in range(n10,0,-1):
#     print("*"*i)       
# n11=int(input("Enter n11:"))
# for i in range(1,n11+1,1):
#     for j in range(1,i+1,1):
#         if (i+j)%2==0:
#             print(1,end=" ")  
#         else:
#             print(0,end=" ")
#     print()       
# n12=int(input("Enter n12:"))
# for i in range(1,n12+1,1):
#     for j in range(1,i+1):
#         print(j,end="")   
#     for k in range((2*n12-i*2)):
#         print("",end=" ") 
#     for l in range(i,0,-1):
#         print(l,end="")
#     print("")  
n13=int(input("Enter n13"))   
count=0 
for i in range(1,n13+1):
    for j in range(1,i+1):
        count=count+1
        print(count,end=" ")  
    print()  
n14=int(input("Enter n14:"))      
for i in range(65,65+n14+1):
    for j in range(65,i):
        print(chr(j),end=" ")
    print()   
n15=int(input("Enter n14:"))      
for i in range(n15+1,0,-1):
    for j in range(65,65+i):
        print(chr(j),end=" ")
    print()       
n16=int(input("Enter n16:"))
for i in range(1,n16+1):
    for j in range(i):
        print(chr(65+(i-1)),end="")
    print()     
n17=int(input("Enter n17:"))
for i in range(1,n17+1):
    for j in range(1,n17-i+1,1):
        print(" ",end=" ") 
    for k in range(1,i+1):
        print(chr(65+k-1),end=" ")
    for l in range(i-1,0,-1):
        print(chr(65+l-1),end=" ")    
    print()    
n18=int(input("Enter input:"))
for i in range(1,n18+1):
    for j in range(i):
        print(chr(65+n18-i+j),end=" ")
    print()    
n=int(input("Enter size"))
size=2*n-1
for i in range(size):
    for j in range(size):
        val=n-min(i,j,size-1-i,size-1-j)
        print(val,end=" ")
    print(" ")    