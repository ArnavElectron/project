import hashlib 
import getpass
class login:
    def __init__(self,username,password):
        self.username=username 
        self.password=password
        print("username",username,"Password",password)


c1=login("demon","pass")
