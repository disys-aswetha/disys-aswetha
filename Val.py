data = [{"id":1000,"Name":"John Smith","DOB":"01/01/2000","Gender":"Male","Age":20,"Zip code":"08122-2324","Amount":"1500.20"},
        {"id":2000,"Name":"Jim McDonald","DOB":"02/02/2020","Gender":"Male","Age":25,"Zip code":"08136-2324","Amount":"1500.20"},
        {"id":20,"Name":"Jim McDonald","DOB":"01/01/1999","Gender":"Male","Age":25,"Zip code":"08124-6565","Amount":"1500.20"}]

for i in data:
    if (i["DOB"]=="01/01/2000"):
        print("John Smith is available")
    if (i["Amount"]=="1500.20"):
        print("1500.20")
    if (i["Gender"]=="Male"):
        print("Male employee")
