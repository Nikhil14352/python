# to remove given character from string
str=input("given string=")
char=input("given char")
remove_char=str.replace(char,"")
print(remove_char)

#print("---------------------------------------")

# To check pallindrome or not
string_poly=input("enter any character=")
check_poly=string_poly[::-1]
if string_poly==check_poly:
    print("given string is a pallindrome")
else:
    print("given string is not a pallindrome")


#print("-----------------------------------------")
 
  #to check given character is vowel or cosonent
 
char=input("enter the char:")
vowels="a,e,i,o,u,A,E,I,O,U"
if char==vowels:
    print("the vowels or consonents")
else:
    print("the not vowels or consonents")

#print("--------------------------------------------")

re_string=input("enter any str:")
char=input("enter the char:")
replace_string=re_string.replace("char"," ")
print(replace_string)

#print("--------------------------------")

#count numbers, alphabets, special character in string
string=input("enter any string")
digits=0
alphabets=0
letters=0
special_character=0
for i in string:
    if i.isdigit():
        digits+=1
    elif i.isalpha():
        alphabets+=1
    else:
        special_character+=1
print(alphabets)
print(digits)
print(special_character)

#print("----------------------------------")

# remove spaces between the characters in a string

space_string=input("enter any character:")
replace_string=space_string.replace(" ","")
print(replace_string)

#print("---------------------------------------")

#find sum of integers in a string

a=int(input("enter any number"))
b=int(input("enter any number"))
sum=a+b
print=("sum",sum)


    




