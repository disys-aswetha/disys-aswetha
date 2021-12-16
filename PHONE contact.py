class phonebook_info:                                                           
    
    def __init__(self):
        print("Add to contacts")
        self.conno=input("enter your contact no:")
        self.name=input("enter the name:")
        self.bday = input("Add birthday:")
        self.hub = input("Add company name:")
        


   
    def phno_check(self):
        if (len(self.conno)==10):
            if type(self.conno) == "int":                                                                            
                print("contact number is verified")
        else:
            raise ValueError("invalid contact number")
        
        
    def name_check(self):
            if len(self.name) <= 15:
                 if type(self.name) == str:
                     print("name verified")
                 else:
                     raise TypeError("invalid name")
                    

    def add_birthday(self):
        if len(self.bday) <= 10:
            print("birthday added")
        else:
            raise ValueError("Invalid bday")
    def comp_name(self):
        self.hub = company
        if type(self.hub)==str:
            print("workplace added")
        else:
            print("other group")

def main():
    print("phno_check")
    print("name_check")
    print("add_birthday")
    print("contact saved")
    print("workplace given")

Aswetha=phonebook_info()
Aswetha.phno_check()
Aswetha.name_check()
Aswetha.add_birthday()
Aswetha.comp_name()

    
