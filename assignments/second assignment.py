# to remove given character from string
str=input("given string=")
char=input("given char")
remove_char=str.replace(char,"")
print(remove_char)

print("---------------------------------------")

# To check pallindrome or not
string_poly=input("enter any character=")
check_poly=string_poly[::-1]
if string_poly==check_poly:
    print("given string is a pallindrome")
else:
    print("given string is not a pallindrome")


print("-----------------------------------------")
 
  #to check given character is vowel or cosonent
 
char=input("enter the char:")
vowel="a,e,i,o,u,A,E,I,O,U"
if char==vowel:
    print("the vowels or consonents")
else:
    print("the not vowels or consonents")

print("--------------------------------------------")

re_string=input("enter any str:")
char=input("enter the char:")
replace_string=re_string.replace("char"," ")
print(replace_string)

print("--------------------------------")




