"""
Creating Variables
Python has no command for declaring a variable.

A variable is created the moment you first assign a value to it.
"""

x = 5
y = 10

print(x)
print(y)

"""
Variables do not need to be declared with any particular
 type, and can even change type after they have been set.
"""

x = 4
x = "sally"

print(x)

# casting

"""
Casting
If you want to specify the data type of a variable, 
this can be done with casting.
"""
x = str(3)
y = int(3)
z = float(3)

"""You can get the data type of a variable with the type() function."""

x = 5
y = "john"

print(type(x))
print(type(y))

#Many Values to Multiple Variables

x,y,z = "orange","banana","cherry"
print(x)
print(y)
print(z)

print('hello','world')

a = 'hello'
b = 'world'
print(a + b)