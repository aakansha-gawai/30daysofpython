#We have to create a programme with will take user input and 2^num
#num**2 orpow(2,num)

user_input=input("Enter a number and i wwill do num^2\n")
user_input=int(user_input)
 
def pow_by_2(num):
     return pow(2,num)

result=pow_by_2(user_input)
print(result)

