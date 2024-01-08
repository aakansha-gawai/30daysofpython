#writing a programme 
#If user entered +ve or -ve 

num=int(input("enter a int number"))
print("You have entered a number->",str(num))

match num:
      case 0:
            print("You have entered 0")
      case num if num >0:
            print("+ve number")
      case num if num <0:
            print("-ve num")
      case _:
            print("No idea!!")   


