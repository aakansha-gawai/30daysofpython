my_list=[1,2,3,4,5,6,8,10]
def is_even(x):
      return x%2==0

#even_numbers=filter(is_even,my_list)
even_number=filter(lambda x:x%2==0,my_list)
print(even_number)

even_number=list(even_number)
print(even_number)

#filter->100->x(less 100)
