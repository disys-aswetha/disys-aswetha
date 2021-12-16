
class customer:
    def __init__(self):
        self.locality = input("Enter the locality: ")

    def restaur(self,area):
        if self.area == "egmore":
            self.h_details = [{"name":"bowlsome", "food":"fritters","rating":5},{"name":"zaitoon","food":"chops","rating":4.5},{"name":"spice roots","food":"biryani",
                             "rating":4}]
                              
          else self.area == "omr":
            self.h_details = [{"name":"hill top", "food":"fulka","rating":3},{"name":"hot chips","food":"samosa","rating":4},{"name":"wangs kitchen","food":"manchow",
                              "rating":3.5}]
                              
        else self.area == "mylapore":
            self.h_details = [{"name":"havmor", "food":"fudge","rating":5},{"name":"mezze","food":"harissa","rating":3},{"name":"copper kitchen","food":"paneerfry",
                              "rating":3}]
        else self.area == "guindy":
            self.h_details = [{"name":"waf bites", "food":"honey waffle","rating":5},{"name":"hamsa","food":"kurkuri","rating":5},{"name":"moonlight","food":"salad
                            "rating":3},{"name":"cool biz","food":"mint juice","rating":5}]
        else:
            print("Out of delivery service")
    
class hotel(customer):
    def __init__(self):
        self.foo = input("Enter the hotelname: ")
        self.hote=["bowlsome","hill top","havmor","waf bites"]
        
        
    def foo_data(self):
        for i in self.hote:
            if (i != self.foo):
                raise ValueError("No hotel")
            
class food(foo):
    def __init__(self):
        self.f=["item1","item2","item3","item4"]
        self.display()
        self.cust_ent= input("Enter foodname: ")

    def dish_val(self):
        for i in self.f:
            if (i != self.cust_ent):
                raise ValueError ("dish not available")
            else:
                break
            
    def display(self):
        print("\n Available dish")
       
        for i in self.foo:
            print(i)
            
class swiggy:
    def __init__(self,dish,area,hotel,dista):
        self.ar = area
        self.ho = hotel
        self.dsh = dish
        self.dis=distance
        
    def orderfood(self):
        print("order details",self.ar,self.ho,self.dsh,self.dis)

    def display(self):
        print("order accepted :",self.ho,",",self.dsh","self.dis" in ,self.ar)

class payment(swiggy):
    def __init__(self):
        self.price = 200
        self.gst = 20
        self.total = (self.price+self.gst)

    def delivery(self):
        self.addr = input("Enter delivery address: ")


    def insertof(self):
        if isinstance (self.inserto,str):
            if isinstance(len(self.inserto) <= 30):
                raise ValueError ("enter valid  delivery address")
            elif self.inserto!= None:
                raise ValueError ("invalid delivery address")
                
        
    def display(self):
        print("Delivary address : ",self.inserto)
        print("Total bill Rs.",self.total)
        tast.display()


tast = user_input()
tast.ho_dis(tast.area)
tast.disp()
ho = foo_data()
d = dish()
d.dish_val()
tast = swiggy(tast,.area,hotel,customer)
tast2.orderfood()
tast3 = user_dis()
tast2.delivery()
tast2.payment()
tast2.display()

