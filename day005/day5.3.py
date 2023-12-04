#if a>b and a>c and a>d -> a
#f b>a and b>c and b>d -> b
#if c>a and c>b and c>d -> c
#d

a=int(input("Enter value of a"))
b=int(input("Enter value of b"))
c=int(input("Enter value of c"))

#result=max(a,b,c)
if a>b and a>c:
            print(a)
elif b>a and b>c:
                 print(b)
else:
     print(c)       

#loop->Repeat a task 
# print("Pramod")x 10
# Loop-> Repeat a task 
# iterate over a sequence - list, tuple
# list[10,12,13,14,16]
# #range(10)-> [0,1,2,3,4,5,6,7,8,9]

age=31
for age in reversed(range(10)):
        print("Aakansha")

age=24
for age in reversed(range(7)):  
        print("Happy raho")