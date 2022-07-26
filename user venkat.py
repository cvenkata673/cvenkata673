import Admin as kd

class User:
    username = " "
    password = " "
    login_info = {"Username":username,"password":password}

    def __init__(self,name,phoneno,email,address,password):
        self.name = name
        self.phoneno = phoneno
        self.email = email
        self.address = address
        self.password = password
        User.login_info["username"] = name
        User.login_info["password"] = password
        self.profile={"name":name}
        self.order_history = {}
    @classmethod
    def login(kls,name,password):
        if kls.login_info["username"] == name and kls.login_info["password"]==password:
            print("logged in successfully")  
            return True
        else:
            print("Invalid credentials")
            return False

    def place_order(self):
        print("what would you like to order in the menu")
        print(kd.show_menu())
        user_choices = int(input("If you would like to order select 1. yes 2. No"))
        if user_choices==1:
            o=int(input("what would you like to order from the list"))
            x=0
            for i in range(0):
                dishname=("Enter the Dish name:")
                dishid=int(input("Enter Dish Id:"))
                quant=int(input("Enter the quantity of the dish:"))
                quantity=int(kd.menu[dishid]["dishquantity"])
                price=kd.price_cal(dishid)
                print(price)
                if quant>quantity:
                    o=o+((price*quant)/quantity)
                    print(o)
                else:
                    print("minimum value has already order")
                if o>1500:
                    o=o-((o*10)/100)
                confirm_order=int(input("confirm the order by selecing 1.Yes 2.No"))
                if confirm_order == "Yes":
                        print(f'''your dishname is {kd.menu[dishid]["dishname"]}''')
                        print(f'''your dishname is {kd.menu[dishid]["price"]}''')
                        print(f"the quantity{quant}")
                        print(f"the cost{o}INR in Total")
                        print("you can now order the dish")
                        self.order_history[dishname] ={
                            "dishname":kd.menu[dishid]["dishname"],
                            "price":kd.menu[dishid]["price"],
                            "quantity": quant
                        }
                        final_quantity=kd.menu[dishid]["dishname"],
                        kd.menu[dishid]["stock"] = final_quantity
                        print("your order is successfully Placed ")

                elif confirm_order =="No":
                        print("This order is not Placd")
                else:
                        print("Invaid choice")
        elif confirm_order == 2:
            print("You seleted the option 2.No  so the order is not Placed")
        else:
            print("Enter the invalid choice")
    
    def display(self):
        print("name:",self.name)
        print("phoneno:",self.phoneno)
        print("email:",self.email)
        print("address:",self.address)
        print("password:",self.password)
        print("login_info:",User.login_info)


    
def account_register():
    cs = User(input("name: "),int(input("Enter Phoneno: ")),input("Email_id: "),input("Enter_Address: "),input("Enter_Password: "))
    return cs.display()

def account_update():
    cs = User(input("name: "),int(input("Enter Phoneno: ")),input("Email_id: "),input("Enter_Address: "),input("Enter_Password: "))
    return cs.display()










    


