import login
import tasks as ts
ch=0
while True:
    print("Enter 1 to create new user \nEnter 2 to login \nEnter 0 to exit")
    ch=int(input("enter choice: "))
    if ch==1:
        login.new_user()
    elif ch==2:
        x=login.userlogin()
        li=["Enter 1 to see inventory table","Enter 2 to show user logs","Enter 3 to show table of your choice","Enter 4 to add inventory","Enter 5 to change quantity","Enter 6 to visualize data","Enter 7 to get datasheet link","Enter 0 to logout"]
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
            elif ch==7:
                ts.show_datasheet()
            elif ch==0:
                break
#---------------------------------------------------------------------------------------------------------------

        while x=="Genral_Manager":
            for i in range(0,6):
                if i in [0,1,3,4,5,6,7]:
                    print(li[i])
            ch=int(input("enter choice: "))
            if ch==1:
                ts.show_inventory_tabel()
            elif ch==2:
                ts.show_user_table()
            elif ch==4:
                ts.add_inventory()
            elif ch==5:
                ts.update_qty()
            elif ch==6:
                ts.graph_parts_quantity_price()
            elif ch==7:
                ts.show_datasheet()
            elif ch==0:
                break
#---------------------------------------------------------------------------------------------------------------
        
        while x=="Floor_Manager":
            for i in range(0,6):
                if i in [0,3,4,6,7]:
                    print(li[i])
            ch=int(input("enter choice: "))
            if ch==1:
                ts.show_inventory_tabel()
            elif ch==4:
                ts.add_inventory()
            elif ch==5:
                ts.update_qty()
            elif ch==6:
                ts.graph_parts_quantity_price()
            elif ch==7:
                ts.show_datasheet()
            elif ch==0:
                break
#---------------------------------------------------------------------------------------------------------------
        
        while x=="Technician":
            for i in range(0,6):
                if i in [0,4,6,7]:
                    print(li[i])
            ch=int(input("enter choice: "))
            if ch==1:
                ts.show_inventory_tabel()
            elif ch==2:
                ts.show_user_table()
            # elif ch==3:
            #    ts.show_table()
            elif ch==5:
                ts.update_qty()
            elif ch==7:
                ts.show_datasheet()
            elif ch==0:
                break
        while x=="Guest_User":
            for i in range(0,6):
                if i in [5,7]:
                    print(li[i])
            ch=int(input("enter choice: "))
            if ch==6:
                ts.graph_parts_quantity_price()
            elif ch==0:
                break
#---------------------------------------------------------------------------------------------------------------
    elif ch==0:
        print("thank you")
        break
