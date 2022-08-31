string="Ash"
#len function shows the lenght of the string
print(len(string))

#if condtion in strings to check if they are equal and greater than each other
a="Pop"
b="Push"
if (a!=b):
    print ("Not Equal")
else:
    print("Equal")

if(a>b):
    print ("a is greater than b")
else:
    print ("b is greater than a")
    
print(b[2]) #string[i] function prints the character at that index of the string

c="uncopywriteable"
print(c[3:7]) #string[i:j] prints the cracters in the string from i to j-1 position
print(c[3]) #if j is ommitted then it's the length of the string by default

print (c.upper()) #.upper() return the string in Uppercase

print (b.lower()) #.lower() return the string in Lowercase

d=" Strings in Python are fun "
print(d.lstrip()) #.lstrip() prints the string without the left space

print(d.rstrip()) #.rstrip() prints the string without the right space

e="Aesops fables"
print(e.count("s")) #counts the no. of times a substring is present in a string

print(e.isnumeric()) #will return True if the string contains numeric characters

print(e.isalpha()) #will return True if the string contains only alphabetic characters

print(e.split()) #will split the strings according to the whitespaces

print(d.replace("are","will be")) #d.replace(old,new) will print the string after replacing the old string with the new substring

