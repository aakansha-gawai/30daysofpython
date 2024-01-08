from ast import Num
import numbers


count=0
while True:
      count+=1
      print(f"This will print at least once.count={count}")
      if count>=8:
            break


#New number for new exercise
for num in range (2, 10):     #2,3,4,5,6,7,8,9
      if num  % 2==0:
         print("Even number->"+str(num))
      else:      #Do nothing
         print("odd number->"+ str(num))

print("end")
