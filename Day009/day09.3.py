#Lambda is an expression
#a lambda is an anonyms function that returns some form of the data

def sum_of_two_numbers(a,b):
      return a+b


result =sum_of_two_numbers(5,9)
print(result)
#anonyms =have no name 

def mul_by_three(a):
      return a*3

result2=mul_by_three(9)
print(result2)

final_result=lambda num:num*6
print(final_result(8))