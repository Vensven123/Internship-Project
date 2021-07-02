from db_class import *
from User import *


class Admin_Details(User):

    def Create_Admin_Account(self):

        found = 0
        while found == 0:
           
            obj.Check_Admin_Account()
            results = A_cursor.fetchall()
            if results:
                print("This Adminname already taken")
                print("Please enter again your Admin name")
                print('\n')
                obj.Create_Admin_Account()
                found = 1
            else:
                print("Please enter again your Admin name")
                obj.Create_Admin_Account()
                print('-' * 40)
                print("Account created,Please Go To Login Page")
                print('-' * 40)
                found = 1

    def Login_Admin_Account(self):

        found = 0
        while found == 0:
            
            obj.Check_Admin_Account()
            results = A_cursor.fetchall()
            if results:
                obj.Admin_Parking_Details_Page()
            else:
                print("Your Account Not Found")
                repeat = input("If you want to register you details again(y/n):")
                if repeat == 'n':
                   print("Thank you")
                   found = 1
#___________________________________________________________________________________________________________#

    def Update_Bike_Parking_Amount(self):

        T_Amount = int(input("Enter the two wheeler Amount :"))
        obj.Update_Two_Parking_detail(T_Amount)

    def Update_Car_Parking_Amount(self):
        C_Amount = int(input("Enter the two wheeler Amount :"))
        obj.Update_Car_Parking_detail(C_Amount)

    def Update_Bus_Parkin_Amount(self):
        B_Amount = int(input("Enter the two wheeler Amount :"))
        obj.Update_Bus_Parking_detail(B_Amount)

    def Update_Truck_Parking_Amount(self):
        Tr_Amount = int(input("Enter the two wheeler Amount :"))
        obj.Update_Truck_Parking_detail(Tr_Amount)


    def Create_Bike_Parking_Slot(self):
        
        Bike_Max_Slot = int(input("Enter space :"))
        obj.Count_Total_Bike_Space( Bike_Max_Slot)
        while Bike_Max_Slot:
            obj.Create_Vehicle_Parking_Car_Slot()
            Bike_Max_Slot -= 1
        if Bike_Max_Slot == 0:
            Admin.commit()
            print("Car Parking Slot Created")

    def Create_Car_Parking_Slot(self):
        Car_Max_Slot = int(input("Enter space :"))
        obj.Count_Total_Bike_Space( Car_Max_Slot)
        while Car_Max_Slot:
            obj.Create_Vehicle_Parking_Car_Slot()
            Car_Max_Slot -= 1
        if Car_Max_Slot == 0:
            Admin.commit()
            print("Car Parking Slot Created")

    def Create_Bus_Parking_Slot(self):
        Bus_Max_Slot = int(input("Enter slot Count :"))
        obj.Count_Total_Bike_Space(Bus_Max_Slot)
        Max = Bus_Max_Slot
        while Max:
            obj.Create_Vehicle_Parking_Bus_Slot()
            Bus_Max_Slot -= 1
        if Bus_Max_Slot == 0:
            Admin.commit()
            print("Bus Parking Slot Created")

    def Create_Truck_Parking_Slot(self):
        Truck_Max_Slot = int(input("Enter space :"))
        obj.Count_Total_Bike_Space(Truck_Max_Slot)
        while Truck_Max_Slot:
            obj.Create_Vehicle_Parking_Truck_Slot()
            Truck_Max_Slot -= 1
        if Truck_Max_Slot == 0:
            Admin.commit()
            print("Truck Parking Slot Created")

    def Remove_Parking_Slot(self):
          obj.Remove_Parking_Slot()
          print(" All Slot Deleted") 

    def DayPayment(self):
        obj.Day_Payment()
        

    def MontlyPayment(self):
        obj.Monthly_Payment()
        

    def YearPayment(self):
        obj.Year_Payment()

    def Total_Amount(self):
        obj.Total_Payment()
        result = A_cursor.fetchone()
        if result:
            print("Total Amount is   :", result[0])
        else:
            print("Not Available")                   
#________________________________________________________________________________________________________________#

    def Upadate_Parking_Slot(self):

        while True:

            print("\n 1.Bike slot       ")
            print("\n 2.Car  slot    ")
            print("\n 3.Bus  slot     ")
            print("\n 4.Truck slot     ")
            print("\n 5.Exit       ")
            print("\n")
            choice = int(input("Enter the option which one you want to Upadate :"))
            print("\n")

            if choice == 1:
                obj.Create_Total_Bike_Slot()

            if choice == 2:
                obj.Create_Total_Car_Slot()
            if choice == 3:
                obj.Create_Total_Bus_Slot()

            if choice == 4:
                obj.Create_Total_Truck_Slot()

            if choice == 5:
                obj.Admin_Parking_Details_Page()

    def Update_Parking_Amount():

        while True:
            print("\n 1.Bike Parking Amount       ")
            print("\n 2.Car  Parking Amount    ")
            print("\n 3.Bus  Parking Amount     ")
            print("\n 4.Truck Parking Amount     ")
            print("\n 5.Exit       ")
            choice = input("Enter the option which one you want to Upadate :")
            print("\n")

            if choice == 1:
                obj.Update_Bike_Parking_Amount()
            if choice == 2:
                obj.Update_Car_Parking_detail()
            if choice == 3:
                obj.Update_Bus_Parking_detail()
            if choice == 4:
                obj.Update_Truck_Parking_detail()
            if choice == 5:
                obj.Admin_Parking_Details_Page()

    def Money_Collection_Report(self):

        while True:

            print("\n1.  DAY PAYMENT")
            print("\n2.  MONTH PAYMENT")
            print("\n3.  YEAR PAYMENT")
            print("\n4.  CURRENT TOTAL MONEY")
            print("\n5.  Exit")

            print("\n")

            Choice = int(input("Enter the Option  :"))
            print("\n")

            if Choice == 1:
               obj.DayPayment()
            if Choice == 2:
               obj.MontlyPayment()
            if Choice == 3:
               obj.YearPayment()
            if Choice == 4:
               obj.Total_Amount()
            if Choice == 5:
               obj.Admin_Parking_Details_Page()

    def Admin_Parking_Details_Page(self):
        
        print('-' * 180)
        print(
            "                                                              Welcome To The Your Admin Page                                                          ")
        print('-' * 180)
        while True:
            print("\n1.  CURRENT PARKING SPACE_DETAILS")
            print("\n2.  REMOVE  ALL PARKING SLOT DETAILS")
            print("\n3.  DISPLAY PARKING SLOT DETAILS")
            print("\n4.  UPDATE PARKING SLOT DETAILS")
            print("\n5.  UPDATE PARKING AMOUNT DETAILS")
            print("\n6.  CURRENT PARKING DETAILS")
            print("\n7.  PAYMENT DETAILS")
            print("\n8.  REMOVE CUSTOMER_DETAILS ")
            print("\n9.  EXIT")

            print("\n")

            Choice = int(input("Enter the Option  :"))

            if Choice == 1:
               obj.Display_Parking_System()
               
            if Choice == 2:
               obj.Remove_Parking_Slot()

            if Choice == 3:
               obj.Display_Parking_Slot()
                
            if Choice == 4:
               obj.Upadate_Parking_Slot()
                
            if Choice == 4:
               obj.Update_Parking_Amount()

            if Choice == 5:
               obj.Update_Parking_Amount()

            if Choice == 6:
               obj.Check_Current_Parking_Details()

            if Choice == 7:
               obj.Money_Collection_Report()

            if Choice == 8:
               obj.Remove_Customer_Details_HistoryDetails()

            if Choice == 9:   
                pass
    def Admin_Home_Page(self):
         
          while True:
            print('-' * 180)
            print(
                "                                                             ***********Welcome to the Customer Page*************                                                                                                                                                                                                                                                                                                                                                       ")
            print('-' * 180)
            print("\n1.   Create Admin Account")
            print("\n2.   Log In Account")
            print('\n3.   Exit')
            print("\n")
            choice = int(input('Enter your choice ...: '))
            print("\n")
            if choice == 1:
                obj.Create_Admin_Account()
               
            if choice == 2:
                obj. Login_Admin_Account()

            if choice == 3:
                pass
                          

obj = Admin_Details()
#obj.Admin_Home_Page()

