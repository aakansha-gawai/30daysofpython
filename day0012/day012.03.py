#check if two lists are identical 
#if all lists are presents in the list
#len and sort -values are same 

lis1=[1,2,3,4]   #first list
lis2=(1,2,3,4) #second list

if len(lis1)==len(lis2):
      lis1=sorted(lis1)
      lis2=sorted(lis2)
      if lis1==lis2:
            print("identical")
      else:
            print("Non identical")

else:
      print("Non identical")


      
