# Strings are immutable
a = "Arafat !!!!!! Arafat"
b = "!!Arafat!!!"
print(a)
print(len(a))
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(b.rstrip("!")) # A point
print(a.replace("Arafat","Alvee"))
print(a.split("  ")) # It will make list

Comment = "my name is Arafat"
print(Comment.capitalize())

str1 = "Welcome to the Console !!!"
print(len(str1))
print(len(str1.center(50)))

print(a.count("Arafat"))

print(str1.endswith("!!!"))

print(str1.endswith("to", 4, 10))

str2 = "He`s name is Dan. He is an honest man."
print(str2.find("is"))
print(str2.find("ishh"))
str3 = "WelcomeToTheConsole"
print(str3.isalnum())
str4 = "hello world\n"
print(str4.isalpha())
print(str4.islower())
print(str4.isalnum())
print(str4.isprintable())

str5 = "        " #using space bar
print(str5.isspace())
str6 = "        " #using tab
print(str6.isspace())
str7 = "World Health Organization"
print(str7.istitle())

str8 = "To kill a moking bard"
print(str8.istitle())