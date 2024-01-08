#Using built in function
my_list=[90,86,98,98.25]
max_result=max(my_list)
print(max_result)

#sort and list element
sort_result=sorted(my_list)
print(sort_result[len(sort_result)-1])

#comparing with each element
def find_large_element(number):
      large_element=number[0]
      for number in number:
            if number > large_element:
                  large_element=number
            return large_element
      
result= find_large_element(my_list)
print("Large number is",result)



