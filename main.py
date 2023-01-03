import login
import tasks as ts
ch=0
while True:
    print("enter 1 to create new user \n enter 2 to login")
    ch=int(input("enter choice"))
    if ch==1:
        login.new_user()
    elif ch==2:
        x=login.userlogin()
        li=["enter 1 to see inventory table","enter 2 to show user logs","enter 3 to show table of your choice","enter 4 to add inventory","enter 5 to change quantity","enter 6 to visualize data"]
        while x=="Admin":
            for i in li:
                print(i)
            ch=int(input("enter choice: "))
            if ch==1:
                ts.show_inventory_tabel()
            elif ch==2:
                ts.show_user_table()
            elif ch==3:
               ts.show_table()
            elif ch==4:
                ts.add_inventory()
            elif ch==5:
                ts.update_qty()
            elif ch==6:
                ts.graph_parts_quantity_price()
        while x=="Genral_Manager":
            for i in range(0,6):
                if i in [0,1,5]:
                    print(li[i])
            if ch==1:
                ts.show_inventory_tabel()
            elif ch==2:
                ts.show_user_table()
            elif ch==5:
                ts.update_qty()
            