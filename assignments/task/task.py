def sum(num):
    return num+1
numbers=[1,2,3,4,5,6,7,8,9]
new_list=list(map(sum,numbers))
print(new_list)

def mul(num):
    return num**3

numbers=[2,3,4,5,6]
new_list=list(map(mul,numbers))
print(new_list)

def even(num):
    return num%2==0

numbers=[1,2,3,4,5,6,7,8]
new_list=list(map(even,numbers))  #OP in boolean value
print(new_list)

# Nested Functions

def power_generator(num):

    
    def power_n(power):
        return num ** power

    return power_n

power_two = power_generator(8)
power_three = power_generator(36)
print(power_two(26))
print(power_three(4))

def function1():
    def function2():
        print('hello'+name)
    return function2
func=function1(nikhil)
func()

def outer_function(x):
    # Hidden from the outer code
    def inner_increment(x):
        return x + 2
    y = inner_increment(x)
    print(x, y)

#inner_increment(5)
outer_function(5)

#Reduced Function


s=reduce(lambda a,b: a*b)
print(s(3,4))

