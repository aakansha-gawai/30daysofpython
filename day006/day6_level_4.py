#''''''''
#please choose an option 
#1.say hello 
#2.Do nothing
#3.quit
#''''''''

#pass=sskipping-no code will run 
choice=None
while choice!='3':
      print("\n 1.say hello \n 2. do nothing \n 3. quit")
      choice=input("choice 1-3 ")
      if   choice=='1':
            print("say hello")
      elif choice=='2': 
           print ("Do nothing")
      elif choice =='3':
            print("quit")
            break
      else :
            print("Invalid option")

print("End")
