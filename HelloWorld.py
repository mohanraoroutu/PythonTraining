def main():
    print("Hello World!")


if __name__ == "__main__":
    main()
print("Mohan")


# Declare a variable and initialize it
f = 786
print(f)
# re-declaring the variable works
f = 'Mohan786'
print(f)

a = "Mohan"
b = 365
print(a+str(b))


f = 101;
print(f)
# Global vs.local variables in functions
def someFunction():
  global f
print(f)
f = "changing global variable"
someFunction()
print(f)

x = "Hello World!"
print(x[:6])
print(x[0:6] + "Mohan")

var1 = "Mohan!"
var2 = "Software Testing"
print ("var1[0]:",var1[0])
print("var2[1:5]:", var2[1:5])

oldstring = 'I like Mohan'
newstring = oldstring.replace('like', 'love')
print(newstring)

string="python at mohan"
print(string.upper())

string="python at mohan"
print(string.capitalize())

string="PYTHON AT MOHAN"
print(string.lower())

string="12345"
print(''.join(reversed(string)))

word="mohan career mohan"
print(word.split(' '))

word="mohan career mohan"
print(word.split('r'))

x = "Mohan"
x.replace("Mohan","Python")
print(x)

x = "Mohan"
x = x.replace("Mohan","Python")
print(x)

