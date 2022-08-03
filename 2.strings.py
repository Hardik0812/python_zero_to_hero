course = "Python programming"  # string

print(len(course))  # print length of the string
print(course[0])  # print first character of the string
print(course[-1])  # print last character of the string
print(course[0:3])  # print first 3 characters of the string

course = "Python \"programming" # string with double quotes
print(course) # print the string with double quotes

course = 'Python \n programming' # string with new line
print(course) # print the string with new line

first = "John"
last = "Doe"
full = "{} {}".format(first, last) # string with format
print(full) # print John Doe

# string with methods
course = "Python programming"
print(course.upper()) # print the string in upper case
print(course.lower()) # print the string in lower case
print(course.title()) # print the string in title case
print(course.count("o")) # print the number of times the character occurs in the string
print(course.find("o")) # print the index of the first occurrence of the character
print(course.find("x")) # print -1 if the character is not found
print(course.replace("Python", "Java")) # replace the string
print(course.strip()) # remove the leading and trailing spaces
print(course.lstrip()) # remove the leading spaces
print(course.rstrip()) # remove the trailing spaces
print(course.startswith("P")) # check if the string starts with the character
print(course.endswith("g")) # check if the string ends with the character
print(course.isalpha()) # check if the string contains only alphabets
print(course.isalnum()) # check if the string contains only alphanumeric characters
print(course.isnumeric()) # check if the string contains only numeric characters
print(course.isspace()) # check if the string contains only spaces
print("Python" in course) # check if the string contains the substring
print("Python" not in course) # check if the string does not contain the substring
