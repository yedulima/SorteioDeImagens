# Python program to explain os.path.join() method 
   
# importing os module 
import os
 
# Path
path = "/home"
 
# Join various path components 
path = os.path.join(path, "User/Desktop", "file.txt")

print(path)