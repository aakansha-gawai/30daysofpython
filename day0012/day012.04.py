my_list=[2,3,4,5,6,7]
print(my_list)
my_list[0]= 42
print(my_list)

#list mutable=IT can be changed
#Tuple()=immutable
car=("i10","uhvyt","98mup")
print(car)
print(car[0])
print(car[2])
print(car[1])

print(car[0:2])
print(car[1:2])

#creating tuple with
list1=[1,2,3,4,5]
print("n\Tuple with the use of function")
print(tuple(list1))

Tuple1=("Aakansha")
print("n\  tuple with the use of function")
print(tuple(Tuple1))

#unpack
tuple1=(2,3,4)
a,b,c=tuple1
print(a)
print(c)
print(b)

#duplicate is allowed ?
dup=[33,44,33,77,77]
t_dup=tuple(dup)
print(t_dup)

del t_dup
#print(t_dup)





