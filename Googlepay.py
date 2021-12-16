class googlepay:
    
    def __init__(self):
        
        self.name=input("enter name:")
        self.mail=input("enter mailid:")
        self.phnum=input("enter phone number:")
        self.otp=input("enter otp:")
        self.acct=input("enter bank account number:")
       
    def name_verif(self):
        if type(self.name) == str:
            if len(self.name) <= 15:
                print("name is verified")
            else:
                raise TypeError("only strings allowed")
       
    def mail_check(self):
        if type(self.mail)== str:
            if len(self.mail)<=30:
                print("mail id is verified")
            else:
                raise ValueError("invalid email id, please enter the correct email id")
        
    def contact(self):
        phnum=input("enter the number:")
        print("phnum is:"+phnum)
        if type(self.phnum)== int:
            if len(self.phnum) == 10:
                print("mobile number verified")
            else:
                raise ValueError("Invalid Phone Number")

    
    def validation(self):
        if type(self.otp == int):
            print("otp verified")
        else:
            raise ValueError("mismatched otp")
        
    def accountdetails(self):
        self.accnum = 4532786590766
        
        print(self.accnum)
        print("Bank details verified")
    
    def pin(self):
        self.otp = num
        if len(self.otp)<= 7:
         print("successfully created")
        else:
            raise ValueError("Invalid pin")
        
    def enterpin(self):
        if len(self.match) == 6:
            print("Pin is created")
        else:
            raise ValueError("not matching")
        
        

                      
aswetha=googlepay()
aswetha.name_verif()
aswetha.mail_check()
aswetha.contact()
aswetha.validation()
aswetha.accountdetails()
aswetha.pin()
aswetha.enterpin()
    

