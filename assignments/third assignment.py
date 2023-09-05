#1)python programme merge two lists

l1=list(eval(input("enter any value seprated by comma(,) in a single line:")))
l2=list(eval(input("enter any value seprated by comma(,) in a single line:")))
l3=l1+l2
print(f"merging two lists:{l3}")

#2)python program to sum of lists elements


l1=eval(input("enter any element:"))
l2=eval(input("enter any element:"))
l3=l1+l2
print(l3)

#3)to print even and odd numbers in list

a=list(range(10))
print(a)
b=list(range(0,10,2))
print(b)
c=list(range(1,10,2))

#4)to print the delete element in given index of list
l1=list(eval(input("enter the elements in separated comma(,) in a single line")))
index=eval(input("enter a index position to insert elements at that position"))
l1.pop(index)
print(l)


#5)to delete given element from list:
l=list(eval(input("enter the elements by seperated comma(,) in a single line ")))
element=eval(input("enter the removing elements:"))
l.remove(element)
print(l)

#6)to insert an element at given index position

l=list(eval(input('enter a group of elements separated by comma(,) in a single line: ')))
index=eval(input('enter a index position to insert element at that position'))
element=input('enter a element to insert in a list: ')
l.insert(index,element)
print(f'list after inserting elements at a given index position: {l}')

#7)check the sizes of the given list are same

l1=list(eval(input('enter a group of elements separated by comma(,) in a single line: ')))
l2=list(eval(input('enter a group of elements separated by comma(,) in a single line: ')))
if(len(l1)==len(l2)):
    print("size of the lists are same")
else:
    print("size of the lists are not same")

#8)a Python function that takes two lists and returns True if they have at least one common member.

def list_fun():
    l1=list(eval(input('enter a group of elements separated by comma(,) in a single line: ')))
    l2=list(eval(input('enter a group of elements separated by comma(,) in a single line: ')))
    for ch in l1:
        if ch in l2:
            return(True)
            break
    else:
        return(False)
print(list_fun())

# a Python program to remove a specified column from a given nested list.

l=[[1, 2, 3], [2, 4, 5], [1, 1, 1]]
l1=[]
for i in range(int(len(l))):
    element=l[i]
    element.pop(0)
    l1.append(element)
    print(l1)


#9)a Python program to convert a list of multiple integers into a single integer.

l=list(eval(input("enter elements by seprated comma(,) in single line")))
l1=''
for i in l:
    l1+=str(i)
    print(l1)

#10) a Python program to remove duplicates from a list.

l1=list(set(eval(input('enter a group of elements separated by comma(,) in a single line: '))))
print(f'list after removing duplicates: {l1}')

