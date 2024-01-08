#List-[]
#store the elemments 
#different data types 
#List items are changable

#create a list
my_marks=[]
print(my_marks)
my_marks2=list()
print(type(my_marks2))

my_marks.insert(0,91)   #91
print(my_marks)
my_marks.insert(1,91)
my_marks.insert(33,91)
my_marks.insert(98,9)
print(my_marks)

#my_marks_clear()
#print(my_marks)
my_marks.append(89)
print(my_marks)
print(len(my_marks))

nested_list=[[1,2,3],[4,5,6],[7,8,9]]
print(nested_list[2])
print(nested_list[1])
print(nested_list[0])

nested_list[0]=["abc","vrt","ui"]
print(nested_list)

dup_list=[1,1,1,1,1,1,1,1,1]
print(dup_list)

mix_list=["abc",123,True]
print(mix_list)
