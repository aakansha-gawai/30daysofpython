#creating a set
string=('h','f','k','c','j','q','p')
Fset1=frozenset(string)
print("The frozeen set is: ")
print(Fset1)

set1={1,2,3}
set2={5,6,7}
my_set=set1.union(set2)
print(my_set)

set1={1,2,3,4,5}
set2={6,7,8,9,10,4,2,3,1,7,9}
my_set=set1.intersection(set2)
print(my_set)

set1={1,2,3,4,5,6}
set2={7,9,1,2,3,4}
my_set=set1.difference(set2)
print(my_set)

set1={1,2,3,4,5}
set2={2,3,4}
subset=set2.issubset(set1)
print(subset)
superset=set1.issuperset(set2)
print(superset)


