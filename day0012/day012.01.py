#1. How to check if a list is empty in python

my_list=[]
non_list=[2,3,4,5,6,7]

def check_list(temp_list):
     if len(temp_list)==0:
        print("List is empty")
     else:
        print("List is non_empty")


check_list(my_list)
check_list(non_list)
