""" My Py Strong Password Maker.
Take a string of numbers and use it to create a strong password.
inside is a template of a tuple which you can modify.
Add tuple items such as "Cv7*x" for numbers 0-9
Choose three random number to associate with a site,
use those numbers to print items from tuple and have your strong password.
"""

"""  <<Remove these quotes and all text within up until -- marker
Assign your own values for desired password strength.
Remeber to add more items in print section.
ex: print(items[], items[])  use comma and repeat itmes[] desired
amount of times --


items = ("", "", "", "", "", "", "", "", "", "",)

a = input("What numbers do you want to use?")
b = input("Second number")
c = input("Third number")
print (items[int(a)] + items[int(b)] + items[int(c)]) 

-- Also remove these quotes to use  >>>"""

"""Example using numbers 5 9 7 to create password for site
called eggedspam.dotcom

items = ("Vb@", "1X", "A8n", "x9*", "c!k", "b99", "hbOr", "kLm", "a#4", "h2",)

a = input("First number you want to use?") = 5
b = input("Second number") = 7
c = input("Third number") = 9

print (items[int(a)] + items[int(b)] + items[int(c)]) 


Your password for eggedspam.dotcom is b99h2kLm
You can think of your password for this site as 597 and simply
run the program anytime you log in.
It's safer to enter your secret number into the program rather than writing down
the actual password or saving it to a file.
"""



items = ("x3#1c", "b7^X4", "jM88k", "c2^vB", "l!19d", "hB7&n", "v4$Ka",
 "mIkL7", "i8N4a", "vVb8&",)

a = input("First number you want to use?")
b = input("Second number")
c = input("Third number")

print (items[int(a)] + items[int(b)] + items[int(c)]) 



"""
Here is a template for creating a 15 digit password from three letters
!!Modify each item in some way for your security!!
To use this template remove triple quotes around
this template. Run the file and follow prompts.
Once a password has been created for a site using this do not
change values unless you have password recovery options.
"""
