def num_if_70(num):
      if num>70:
         print("greater than 70")
      else:
           print("less than 70")

num_if_70(86)
num_if_70(-98)

#here is another function for our chapter number 
result=lambda num:"Greater than 50" if num> 50,else "less than 50"
print(result(90))

result3=lambda num:"Greater that -98"if num<-98,else "Less than -98"
print(result(-98))