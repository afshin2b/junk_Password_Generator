# junk_Password_Generator
Short:
This is a simple python program which helps create a new random looking password from a master password.
It generates a password using a master password (you only need to remember one strong phrase as opposed to many ones) and 
the account identifier (I personally just use website name). 
______________________________________________
Example in terminal:

$ python junkPasswordGen0.py 

please enter you secret phrase>**This is the only phrase I need to know to get my passwords.**

Enter the website>**github**

This is your password for  github :

Tux9avjXsgffb1_
___________________________________________
Another example:

$  python junkPasswordGen0.py 

please enter you secret phrase>**This is the only phrase I need to know to get my passwords.**

Enter the website>**stack overflow**

This is your password for  stack overflow :

ZZ5Lq@OS2E1wjG
___________________________________________
Another example:

$python junkPasswordGen0.py

please enter you secret phrase>**This is the only phrase I need to know to get my passwords.**

Enter the website>**my_not_so_important_email_address@someDomain.com**

This is your password for  my_not_so_important_email_address@someDomain.com :

f5Glw8dRKSxDAv_

_________________________________________

Details:
I am tired of trying to come up with a good password every time I need to sign up for a website.
I used to type in a bunch of gibberish for every new website and ask the browser to remember it. 
The problem was, when I changed browsers or even worse laptops I couldnt access the website and I had to reset the password and ...

This python script creates a new "different" password for different websites based on a single master key.
The master key should be a long phrase that you easily remeber, you can include numbers and special signs in your master key.
Several examples of master keys:

This is the only phrase I need to know to get my passwords.
The wheels on the bus go round and round!
E=mc^2 is the most famous equation.


The password is created by encrypting the website with SHA256(master key) as the key using AES-128

