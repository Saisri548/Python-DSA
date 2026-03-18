#list intro and imp methods and imp problems 
arr=[10,20,30,40,50]
empty=[]
mixed=["hi","Priya",10,30]
print(arr[0])
print(arr[1])
print(mixed[2])
arr1=[1,2,3,4,5,6]
arr1.append(2)
arr1.append(10)
arr1.insert(1,10)
print(arr1,arr,mixed)
slice=[13,4,6,8,9,10]
print(slice[1])
print(slice[::-1])
print(slice[2:])
#slicing
#indexing
#methods
arr2=[1,2,3,4]
#appending the element
arr2.append(4)
print(arr2)
arr2.insert(2,3)
print(arr2)
arr3=[4,5,6,7,8]
arr4=[4,6,3,7,8]
arr3.extend(arr4)
print(arr3)
arr3.pop()
arr3.pop(2)
print(arr3)
arr3.remove(4)
print(arr3)
arr3.sort()
print(arr3)
arr3.reverse()
print(arr3)
print(max(arr3))
print(min(arr3))
print(sum(arr3))
print(len(arr3))
print(arr3.index(6))
#basic-problems
#1.second largest element 
def second_largest_element(arr):
    a=max(arr)
    s=0
    for i in arr:
        if a>i and s<i:
            s=i
    return s
print(second_largest_element([1,4,6,72,10,50]))   
arrS=[1,3,4,6,7,8]
flag=1
for i in range(1,len(arrS)):
    if arrS[i] < arrS[i-1]:
        flag = 0
        break 
      
if(flag==1):
    print("sorted")
else:
    print("not sorted")                

arrR=[1,2,3,4,5,6,7,8,9,10]
k=4
n=len(arrR)
for i in range(0,n,k):
    arrR[i:i+k]=arrR[i:i+k][::-1]
print(arrR)    
arr01=[0, 1, 0, 1, 1, 1, 1]
count=1
maxCount=0
for i in range(1,len(arr01)):
    if arr01[i]==arr01[i-1]:
        count+=1
    else:
        maxCount=max(count,maxCount) 
        count=1  
print(count)        
def pushZerostoend(arr):
    arr1=[]
    arr2=[]
    for i in arr:
        if i!=0:
            arr1.append(i)
        else:
            arr2.append(i) 
    arr1.extend(arr2)
    return arr1
print(pushZerostoend([1,2,0,4,3,0,5,0]))           
def arrMaxP(arr):
    n=len(arr)
    arr.sort()
    return max(arr[0]*arr[1]*arr[n-1],arr[n-1]*arr[n-2]*arr[n-3])
print(arrMaxP([1,3,7,0,-6,-4]))
arrW=[1,2,3,4,5]
for i in range(0,len(arrW)-1,2):
    arrW[i],arrW[i+1]=arrW[i+1],arrW[i]
print(arrW)   
n=[1,9,9] 
m="" 
for i in range(len(n)): 
    m+=str(n[i]) 
print(int(m)+1) 