import Admin as kd
import User as Us
from User import User

ra= User(str,str,str,str,str)

venkat = int(input("where you want to login select 1.Admin and 2.User and 3.Exit"))
if venkat == 1:
    username = input("Admi Username:")
    password = input("Admin password:")
    if kd.admin_keys[username] == password:
        print("Logged in successfully.....")
        admin_crawler = True
        while admin_crawler:
            admin_choice = int(input("choose he admin panel 1.Add new dish, 2.Edit dish, 3.View dish, 4.Remove dish, 5.Exit"))
            if admin_choice == 1:
                kd.add_new_dish()
            elif admin_choice == 2:
                kd.edit_from_dish()
            elif admin_choice == 3:
                kd.show_menu()
            elif admin_choice == 4:
                kd.remove_dish()
            elif admin_choice == 5:
                print(f"You are exit t admin panel{username}")
                admin_crawler = False
            else:
                print("Entered option is wrong please select properly")
        else:
            print("Enter credentials wre wrong,,,sorry....")

elif venkat == 2:
    print("Welcom to th user dashboard, register userself")
    Us.account_register()
    username = input("Admi Username:")
    password = input("Admin password:")
    if User.login(username, password):
        print("logged in successfully")
    user_crawler = True
    while user_crawler:
        prsn_choice = int(input(f"{username},Enter the option 1.place order 2.order history 3.exit"))
        if prsn_choice ==1:
            ra.place_order()
        elif prsn_choice ==2:
            print(f"hee is your order history, repeat order{username}")
            print(ra.order_history)
        elif prsn_choice ==3:
            user_crawler = False
            print("logged out")
        else:
            print("You have choosen the Invalid option")
    else:
        print("wrong credentials")
else:
     exit()

