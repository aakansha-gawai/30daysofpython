def do_something (a) :
      return(2,a)   #2^3-> ?

numbers=[2,3,4]
result=list(map(do_something,numbers))
print(numbers)

#for i in result:
#    print(i)
r=[]
for i in numbers:
      temp=do_something(i)
      r.append(temp)

print(r)
#map-100-> 100 True 