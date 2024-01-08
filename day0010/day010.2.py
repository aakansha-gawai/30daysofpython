bool_val=int(False)
print(bool_val)
#int(False)=0,int(True)=1

bool_val=int(True)
print(bool_val)

string_num=int("101")
print(string_num)
print(type(string_num))

binary=int("1010",2)
print(binary)

octal=int("12",8)
print(octal)

hex_de=int("A",34)
print(hex_de)

ran_val=int("@!123")  #invalid literalfor int() with base 10:@123!
print(ran_val)