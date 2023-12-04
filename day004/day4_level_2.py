import keyword

all_keywords="keyword:kwlist"
'for' 'keyword' in all_keywords
print(keyword)

#identity operators (is,is not)
a=5   #values are checked 
b=5
print(a is b)


password = "Aakansha"
comfirm_password= "Aakansha"
print("password is confirm_password") 
print(id(password))
print(id("confirm_password"))
