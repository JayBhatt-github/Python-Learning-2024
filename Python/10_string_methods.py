# String Methods In python



# Slicing Method
s1 = 'python'
print(s1[0:3])   # can also use ex: print(s1[0:3])
# o/p: "pyt"
print(s1[1:3])   # can also use ex: print(s1[0:3])
# o/p: "yt"


# Upper Method
a = "Hello World"
print(a.upper()) # converts string to upper case


# Lower Method
a = "Hello World"
print(a.upper()) # converts string to upper case

# rstrip Method
b = "Hello!!!!"
print(b.rstrip("!"))  # removes character from string end


# Replace Method
c = "hello my name is devid and my username is devid123"
print(c.replace("devid","john")) # replace first parameter to second 


# Split Method
d = "john,devid,Jack,Arthur"
print(d.split(","))     # it separates the string into list where "," is spotted


# Capitalize Method
e = "this is paragraph"
print(e.capitalize())   # it capitalize the first letter of the string, rest of the letters remains lower case


# Center Method
s1 = "Lorem Ipsum"
print(s1.center(50)) # returns string that is padded with value or specified character
print(s1.center(50,"*")) # returns string that is padded with value or specified character


# Count Method
s2 = "my name is devid, and my facebook username is devid123"
print(s2.count("devid"))  # counts specified words from the string


# Find Method
s3 = "He's name is Dan. He is working."
print(s3.find("is"))    # finds the first occurrence of the specified value


# isAlphaNumeric Method
s4 = "Hello123"
print(s4.isalnum())    # check if all the characters in the text are alphanumeric (A-Z, a-z, 0-9), will return false if it finds special characters and white space


# isLower Method
s5 = "hello world"
print(s5.islower())   # check if all the characters in the text are lower case


# isUpper Method
s6 = "HELLO WORLD"
print(s6.isupper())   # check if all the characters in the text are upper case


# isPrintable Method
s7 = "Happy Birthday\n"    # not printable 
print(s7.isprintable())   # check if all the characters in the text are printable


# isSpace Method
s8 = "     "           # using Spacebar
print(s8.isspace())    # check if all the characters in the text are whitespaces


# Title Method
s9 = "His name is david"
print(s9.title())  # make the first letter of each word to upper case:


# isTitle Method
t1 = "Python Language" 
print(t1.istitle())  # check if each word start with an upper case letter


# StartsWith Method
t2 = "Welcome Alex" 
print(t2.startswith("Welcome"))   # check if the string starts with specified value


# EndsWith Method
t3 = "executed successfully"
print(t3.endswith("successfully"))  # check if the string ends with specified value


# SwapCase Method
t4 = "My name is david" 
print(t4.swapcase()) # converts lowercase to uppercase and uppercase to lowercase
