# To replace the string 
s1=input("enter any string:")
char=input("enter the char:")
remove_char=s1.replace("char","")
print(remove_char)

# the count occurance of given string

string=input("enter any string:")
char=input("enter any char:")
count=0
for i in range(len(string)):
    if (string[i] == char):
        count = count+1
print("the total number of",char,"is :",count)

string=input("enter any string:")
char=input("enter any char:")
index,count=0,0
while(index < len(string)):
    if(string[index] == char):
        count=count+1
    index=index+1
print("the total number of occurances",char,"is:",count)

#Anagrams
string1=input("enter any string")
string2=input("enter any string")
if len(string1)!= (string2):
    print("this is anagrams")
else:
    if sorted(string1) == sorted(string2):
       print("this is anagrams")
    else:
        print("this is not anagrams")

# count occrence of given string 

string = input("enter str1")
char = input("enter str2")
char_count=string.count(char)
print(char_count)

# converting lower string to upper string

string = input("enter any string:")
result=''
for i in string:
    if i.islower():
        i = i.upper()
    result+= i
print("the string after converting lower to upper:",result)

# converting vowels to upper

string = input("enter any string:")
vowels="aeiou"
for char in string:
    if char in vowels:
        upper_char=char.upper()
        string=string.replace(char,upper_char)
    print("updated string", string)


string = input("enter any string:")
vowels=0
consonants=0
for i in string:
    if i in ('a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U'):
        vowels+=1
    elif i.isalpha():
        consonants+=1
print('vowels',vowels,'consonent',consonants)

# printing specialcharacters,digits,alphabets
string=input("enter any string=")
alphabets=0
digits=0
special_characters=0
for i in string:
    if i.isalpha():
        alphabets+=1
    elif i.isdigit():
        digits+=1
    else:
        special_characters+=1
print("alphabets",alphabets,"digits",digits,"special_characters")

#separate chracters in given string

str='hello worls'
for char in str:
    print(char)
    print('\n')

# concanate two strings using join method

str1=input('enter the string:')
str2=input('enter the string:')
print('the concanate the string:',"".join(str1,str2))

# Python code to find sum of integers in the string
str1=input('enter any string=')
sum=0
for i in str1:
    if i.isdigit():
        sum=sum+int(i)
print('sum',sum)

#copy the string

string=input('enter any string:')
new_string=string[:]
print('new stringafter copy :',new_string)






