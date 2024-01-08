#can we have way to iterate over the each element and run a function
#map()-> built
#def double_me(a)-> a*2
#2,4,6,8,10,12

def double_me(a):
  return a*2
a=76
print(a)

my_list=[1,2,3,4,6,8,9]
#map=(print,tuplr or string,list)-> map -> list
result=list(map(double_me,my_list))
print(result)

