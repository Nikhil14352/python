#1add a key to dictionary
dict1={}
print(dict1)
dict1[0]=10
print(dict1)
dict1[1]=20
dict1[2]=30
print(dict1) 

#2check wheather a given key is already exits in dict

myDict = {'a': 'apple', 'b': 'Banana' , 'o': 'Orange', 'm': 'Mango'}
print("Dictionary : ", myDict)

key = input("Please enter the Key you want to search for: ")

if key in myDict:
    print("\nKey Exists in this Dictionary")
    print("Key = ", key, " and Value = ", myDict[key])
else:
    print("\nKey Does not Exists in this Dictionary")


#3a Python program to iterate over dictionaries using for loops

d = {'x': 10, 'y': 20, 'z': 30} 
for dict_key, dict_value in d.items():
    print(dict_key,'->',dict_value)

#4 a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.

dic={}
for i in range(1,16):
    dic[i]=1**3
print(dic)

#5 converting string to dictionary

string="marolix technology"
letter_count={}
for char in string:
    if char in letter_count:
        letter_count[char]+=1
    else:
        letter_count[char]=1
print(letter_count)      

#6 a Python program to sum all the items in a dictionary.
dict={'orange':20,'banana':30,'apple':40}
print(sum(dict.values()))

#7 a Python program to combine two dictionary by adding values for common keys.

dict1 = {'a': 100, 'b': 200, 'c':300}
dict2 = {'a': 300, 'b': 200, 'd':400}
for key in dict2:
    if key in dict1:
        dict2[key]=dict2[key]+ dict1[key]
print(dict2)

#8 a Python program to access dictionary key's element by index.

dict={'cricket':50,'volleyball':20,'basketball':30}
print(dict.keys())
for i in dict:
    print(i)

#9 a Python program to remove a key from a dictionary.

dict={'cricket':50,'volleyball':20,'basketball':30}
print(dict.popitem())
print(len(dict))
print(dict.pop('volleyball'))
print(dict)

#10  a Python script to merge two Python dictionaries.d

dict={'cricket':50,'volleyball':25,'basketball':35}
dict1={'orange':20,'banana':30,'apple':20}
dict2=dict1.copy()
dict2.update(dict)
print(dict2)
