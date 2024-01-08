#set
#set is an unordered collection of data types 
#{}
lis=[1,2,3,4,5,6,7]
my_set=print(lis)
print(my_set)

empty_set=set()
print(empty_set)

non_empty_set=set("Aakansha")
print(non_empty_set)

#creating a set with the use of tuple 
t=("the testing academy","lucky","the testing academy")
print("\n set with the use of table")
print(set(t))

set1=("the testing academy","123","happyme")
set2=("happyme","123","hi every one")
set3=set1+set2
print(set3)
print("\n initial set")


for i in set3:
      print(i,end=" *")

for i in set1:
      print(i,end="")

for i in set2:
      print(i,end="")

#creating a set
set1=(1,2,3,4,5,6,7,8,9,10,11,12)
print("\n initial set")
print(set1)

