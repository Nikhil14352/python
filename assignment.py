def check(letter):
    list_of_vowels=['a','e','i','o','u']
    if letter in list_of_vowels:
        return True
    else:
        return False
letters=['u','a','q','c','i','d','z','p','e']
filter_object=filter(check,letters)
print("the of returned object is:",type(filter_object))
filtered_list=list(filter_object)
print("the list of vowels:",filtered_list)