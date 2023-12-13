i=0
while i<8:
      print(i)
      i=i+1


print("End")      

print("start")

while True:
      user_input=input("Enter a number,0 to 10, if you match my number i will exit")
      print("You have written this number"+user_input)
      user_input=int(user_input)
      if user_input== 5: 
       print("You found the lucky number")
      break

print("End")