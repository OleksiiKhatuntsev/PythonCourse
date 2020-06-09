# print(4*(6+5))
# print(4*6+5)
# print(4+5*6)
# print(type(3+1.5+4))
# print(3**2)

#STRINGS

s = 'hello'
print(s[1])
print(s[::-1])
print(s[4] + ' ' + s[-1])

#LISTS
mylist = [0,0,0]
my_second_list = [0]
my_second_list.append(0)
my_second_list.append(0)
print(mylist)
print(my_second_list)

list3 = [1,2,[3,4,'hello']]
list3[2][2] = 'goodbye'
print(list3)

list4 = [5,3,4,6,1]
list4.sort()
print(list4)

#DICTIONARIES

# Grab 'hello'
d = {'simple_key':'hello'}
print(d['simple_key'])

# Grab 'hello'
d = {'k1':{'k2':'hello1'}}
print(d['k1']['k2'])

# Getting a little tricker
#Grab hello
d = {'k1':[{'nest_key':['this is deep',['hello2']]}]}
print(d['k1'][0]['nest_key'][1])

# This will be hard and annoying!
d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello_hard']]}]}]}
print(d['k1'][2]['k2'][1]['tough'][2][0])

#SETS

list5 = [1,2,2,33,4,4,11,22,3,3,2]
set1 = set(list5)
print(set1)

#BOOLEAN

print(3.0 == 3)
print(4**0.5 != 2)

l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]
print(l_one[2][0] >= l_two[2]['k1'])