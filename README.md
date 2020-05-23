# MyPyspm
Deterministic password generator. Meant to be an alternative to password managers. Associate a website with a three digit number such as "214", run this file in terminal to retrive password as needed.

**I strongly recommend opening file in a text editor and making changes to items in list**. You can do this by opening file in a text editor of your choice. Do not change after you have used it to create a password for a site unless you have password recovery/reset options from that site. Default template generates a 15 character password from input of three numbers. 

When prompted for input use only numbers 0-9. Any other input will result in errors. 

Created By Rodney Maynard. No licnese or copyright. Meant to be free software that can be used, distributed, shared, or modified as you please. 

The rest of the readme is the actual code. You could just copy from here and paste in a text editor then save as a .py file. Once again I have to urge to modify values in list for your security. Hope everyone enjoys my attempt at creating my ideal password manager. 

Thanks,
Rodney

-------------------------Actual Code. It's mostly comments but this is my first project be gentle----------------
Blank template


items = ("", "", "", "", "", "", "", "", "", "",)

a = input("What numbers do you want to use?")

b = input("Second number?")

c = input("Third number?")


print (items[int(a)] + items[int(b)] + items[int(c)])


Ready to run template. Please make minor changes for your security.


items = ("x3#1c", "b7^X4", "jM88k", "c2^vB", "l!19d", "hB7&n", "v4$Ka",
 "mIkL7", "i8N4a", "vVb8&",)

a = input("First number you want to use?")

b = input("Second number?")

c = input("Third number?")

print (items[int(a)] + items[int(b)] + items[int(c)])

