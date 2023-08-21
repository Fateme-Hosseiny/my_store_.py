from pyfiglet import Figlet
def showmenu():
    print("1-add product")
    print("2-edit product")
    print("3-delete product ")
    print("4-search product ")
    print("5-show list")
    print("6-buy")
    print("7-exit")
myfile=open("datashopp.txt","r")
data= myfile.read()
f= Figlet(font="standard")
print(f.renderText("Tameshk store"))
product_list= data.split("\n")
Pr_list=[]
for i in range(len(product_list)):
    product_info= product_list[i].split(",")
    mydict= {}
    mydict["code"]=product_info[0]
    mydict["name"]=product_info[1]
    mydict["price"]=product_info[2]
    mydict["count"]=product_info[3]
    Pr_list.append(mydict)
print(Pr_list)
showmenu()
choice= int (input("choice a number 1,7: "))
def Add():
   add= int(input("etelat chand mahsool ro mikhay add kony? :"))
   for i in range(add):
    
    code= int(input("enter code product:"))
    name=input("enter name product:")
    price= int(input("enter price product:"))
    count= int(input("enter count product:"))
    dict_add= {}
    dict_add["code"]= code
    dict_add["name"]=name
    dict_add["price"]=price
    dict_add["count"]=count
    Pr_list.append(dict_add)
def Edit(PRODUCTS,e_code):
    for product in PRODUCTS:
        if product["code"]== e_code:
            
            edited=input("taghir bede : ")
            Pr_list[product["code"]][Choice_e] = edited
            return product
        
       
            
def Delete(Products,d_name):
    for product in Products:
        if product["name"]==d_name:
            Pr_list.remove(product)
def Search(products,pr_name):
    for product in products:
        if product ["name"]==pr_name:
            return product
        else:
             print("nothing")
def Show():
   print(Pr_list)
if choice ==1:
    Add()
    print(Pr_list) 

elif choice ==2:
   choice_e= int(input("enter code from that product you want edit it : "))
   Choice_e= str(input("kdoom mored ro mikhay edit kony? : "))
   PRODUCTS= Pr_list
   edit= Edit(PRODUCTS,choice_e)
   if Choice_e=="name":
     print(f"Name:{edit['name']}")
   elif Choice_e=="price":
      print(f"Price: {edit['price']}")  
elif choice ==3:
    pr_del= str(input("enter name from that product you want delete it : "))
    Products=Pr_list
    delete=Delete(Products,pr_del)
    print(Pr_list)
elif choice ==4:
    
    name= str(input("enter a product name : "))
    products= Pr_list
    search=Search(products,name)
    
    print(f"code : {search['code']}")
    print(f"name : {search['name']}")
    print(f"price : {search['price']}")
    print(f"count : {search['count']}")
          
elif choice ==5:
  Show()
elif choice ==6:
    pass
elif choice ==7:
    pass


