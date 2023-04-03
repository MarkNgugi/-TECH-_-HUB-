#AFTER ADDING CODE ON SELECTIONS, BELOW IS THE FINAL CODE OF SELECTION OPTION IN THE MENU_SELECTION FILE
#REPLACE THE PREVIOUS MENU_SELECTION CODE WITH THE CODE BELOW
#DECLARING DEFAULT VALUES FOR BAKERY ITEMS

import random 
import datetime

current_date = datetime.date.today()
current_time = datetime.datetime.now().time() 

TOTAL_BREAD = 0
TOTAL_COOKIES =0
TOTAL_BUNS = 0 
TOTAL_BISCUITS = 0
TOTAL_DOUGHNUTS = 0
TOTAL_CAKES = 0
TOTAL_MAANDAZIS = 0

#DECLARING DEFAULT VALUES FOR READY MEALS ITEMS
TOTAL_CHAPATI = 0
TOTAL_SCRAMBLED_EGGS = 0
TOTAL_YELLOW_BEANS = 0
TOTAL_BEEF = 0
TOTAL_RICE = 0
TOTAL_GREEN_GRAMS = 0
TOTAL_OMENA = 0 
TOTAL_UGALI = 0
TOTAL_CHICKEN = 0
TOTAL_FRIES = 0

#DECLARING DEFAULT VALUES FOR FRUITS AND VEGETABLES ITEMS
TOTAL_APPLES = 0
TOTAL_BANANAS = 0
TOTAL_ORANGES = 0
TOTAL_WATERMELONS = 0
TOTAL_STRAWBERRIES = 0
TOTAL_AVOCADO = 0
TOTAL_KALES = 0
TOTAL_CABBAGE = 0 
TOTAL_LETTUCE = 0
TOTAL_BROCCOLI = 0

#DECLARING DEFAULT VALUES FOR HOT DRINKS ITEMS
TOTAL_COFFEE = 0
TOTAL_GREEN_TEA = 0
TOTAL_HOT_CHOCHOLATE = 0
TOTAL_HOT_LEMON_WATER = 0
TOTAL_FRUIT_TEA = 0

#DECLARING DEFAULT VALUES FOR COLD DRINKS ITEMS
TOTAL_SODA = 0
TOTAL_FLAVORED_WATER = 0
TOTAL_FRUIT_JUICE = 0
TOTAL_FRUIT_WINE = 0
TOTAL_ICE_COFFEE = 0
TOTAL_ICE_TEA = 0

#DECLARING VALUES FOR THE MENU CATEGORY
AVAILABLE_COUNTIES = ["NAIROBI","KIAMBU","KISUMU","MOMBASA","SIAYA","nairobi","kiambu","kisumu","mombasa","siaya"]

NAIROBI = 0
KIAMBU = 0
KISUMU = 0
MOMBASA = 0
SIAYA = 0

nairobi = 0
kiambu = 0
kisumu = 0
mombasa = 0
siaya = 0


def NORMAL_DELIVERY():

    print("WE OFFER DELIVERY SERVICES IN THE FOLLOWING COUNTIES:\n")
    print("1. NAIROBI  ==>  Ksh.426 - Ksh.442")
    print("2. KIAMBU  ==>  Ksh.583 - Ksh.602")
    print("3. KISUMU  ==>  Ksh.1228 - Ksh.1241")
    print("4. MOMBASA  ==> Ksh.1423 - Ksh.1444")
    print("5. SIAYA  ==>  Ksh.1412 - Ksh.1436")

def SPECIAL_DELIVERY():
    print("WE OFFER SPECIAL DELIVERY SERVICES IN THE FOLLOWING COUNTIES:\n")
    print("1. NAIROBI  ==>  Ksh.426")
    print("2. KIAMBU  ==>  Ksh.582")
    print("3. KISUMU  ==>  Ksh.1220")
    print("4. MOMBASA  ==> Ksh.1422")
    print("5. SIAYA  ==>  Ksh.1413")

def order_type():
    print("1. NORMAL DELIVERY")
    print("2. SPECIAL DELIVERY\n")

def payments():
    print("\n")
    print("1. MPESA")
    print("2. PAYPAL\n")

#will be used to clear the messages after running the program again
import os
if os.path.exists("MPESA"):
  os.remove("MPESA")
else:
  pass

import os
if os.path.exists("PAYPAL"):
  os.remove("PAYPAL")
else:
  pass

import os
if os.path.exists("FULIZA"):
  os.remove("FULIZA")
else:
  pass

from MAIN_MENU import MAIN_MENU
MAIN_MENU() #calling the main menu function
MENU_CHOICE = int(input("CHOOSE ONE CATEGORY FROM THE MENU ABOVE(NUMBER):: "))

if MENU_CHOICE == 1:
    from MAIN_MENU import bakery_products #importing bakery_products function from MAIN_MENU module
    print("\n") #start a new line before the function
    bakery_products() #calling the function
    print("\n")

    while True:
        
        BAKERY_SELECTION = int(input("SELECT THE BAKERY ITEM(S) THAT YOU WANT(EXIT = 00):: "))
      
        if BAKERY_SELECTION == 1:
           #global TOTAL_BREAD
            bread = int(input("How many breads do you want? "))
            
            TOTAL_BREAD = (bread * 60)

            print(f"TOTAL AMOUNT = Ksh.{TOTAL_BREAD}\n")

        elif BAKERY_SELECTION == 2:
            #global TOTAL_COOKIES
            cookies = int(input("How many Cookies do you want? "))
            
            TOTAL_COOKIES = (cookies * 120) 
            print(f"TOTAL AMOUNT = Ksh.{TOTAL_COOKIES}\n")

        elif BAKERY_SELECTION == 3:
            #global TOTAL_BUNS
            buns = int(input("How many Buns do you want? "))
            
            TOTAL_BUNS = (buns * 70 ) 
            print(f"TOTAL AMOUNT = Ksh.{TOTAL_BUNS}\n")

        elif BAKERY_SELECTION == 4:
            #global TOTAL_BISCUITS
            biscuits = int(input("How many Biscuits do you want? "))
            
            TOTAL_BISCUITS = (biscuits * 40) 
            print(f"TOTAL AMOUNT = Ksh.{TOTAL_BISCUITS}\n")

        elif BAKERY_SELECTION == 5:
            #global TOTAL_DOUGHNUTS
            Doughnuts = int(input("How many Doughnuts do you want? "))
            
            TOTAL_DOUGHNUTS = (Doughnuts * 65) 
            print(f"TOTAL AMOUNT = Ksh.{TOTAL_DOUGHNUTS}\n")

        elif BAKERY_SELECTION == 6:
            #global TOTAL_CAKES
            Cake = int(input("How many Cakes do you want? "))
            
            TOTAL_CAKES = (Cake * 120)
            print(f"TOTAL AMOUNT = Ksh.{TOTAL_CAKES}\n")

        elif BAKERY_SELECTION == 7:
            #global TOTAL_MAANDAZIS
            MAANDAZI = int(input("How many Maandazis do you want? "))
            
            TOTAL_MAANDAZIS = (MAANDAZI * 20) 
            print(f"TOTAL AMOUNT = Ksh.{TOTAL_MAANDAZIS}\n")

    
        elif BAKERY_SELECTION == 00:
            TOTAL_BILL = TOTAL_BREAD + TOTAL_COOKIES + TOTAL_BUNS + TOTAL_BISCUITS + TOTAL_DOUGHNUTS + TOTAL_CAKES + TOTAL_MAANDAZIS
            print(f"\nYOUR TOTAL BILL IS Ksh.{TOTAL_BILL}\n")
            break

################################################

    DELIVERY_Q = input("\tDO YOU WANT YOUR GOODS TO BE DELIVERED? (YES or NO):: ")
    if DELIVERY_Q == "YES":

        print("\n\tTHANKYOU FOR CHOOSING OUR DELIVERY SERVICES!!!\n")
        order_type()

        DELIVERY = int(input("SELECT YOUR DELIVERY TYPE(INT):: "))

        if DELIVERY == 1:
            print("\n")
            NORMAL_DELIVERY()

            while True:
                CHOICE = int(input("\nSelect county choice number to deliver to:(exit='00')  => "))


                if CHOICE == 1:
                        nairobi = random.randrange(423,442)
                        print(f"DELIVERY PRICE TO NAIROBI IS Ksh.{nairobi}")

                elif CHOICE == 2:
                        kiambu = random.randrange(583,602)
                        print(f"DELIVERY PRICE TO KIAMBU IS Ksh.{kiambu}")

                elif CHOICE == 3:
                        kisumu = random.randrange(1228,1241)
                        print(f"DELIVERY PRICE TO KISUMU IS Ksh.{kisumu}") 

                elif CHOICE == 4:
                        mombasa = random.randrange(1423,1444)
                        print(f"DELIVERY PRICE TO MOMBASA IS Ksh.{mombasa}") 

                elif CHOICE == 5:
                        siaya = random.randrange(1413,1436)
                        print(f"DELIVERY PRICE TO SIAYA IS Ksh.{siaya}") 

                elif CHOICE == 00:
                        DELIVERY_TOTAL = nairobi + kisumu +siaya + mombasa + kiambu
                        print(f"\nTOTAL NORMAL DELIVERY PRICE ON SELECTED COUNTIE(S) IS Ksh.{DELIVERY_TOTAL}\n")
                        break
                    

            #PAYMENT MODULE
            print("\nBELOW IS A PAYMENT METHOD LIST:: ")
            payments()
            payment_method = int(input("SELECT ONE PAYMENT METHOD::"))
            if payment_method == 1:
                #ENTER AMOUNT
                #ENTER PIN NUMBER THAT HAS BEEN GENERATED FOR YOU
                TOTAL_PAYMENTS = DELIVERY_TOTAL + TOTAL_BILL
                print(f"\nYOU ARE SUPPOSED TO PAY A TOTAL OF Ksh.{TOTAL_PAYMENTS}")
                ACC_BAL = float(input("HOW MUCH DO YOU HAVE IN YOUR MPESA?"))
                if ACC_BAL < TOTAL_PAYMENTS:
                    FULIZA_Q = input("YOU HAVE INSUFFICIENT FUNDS, WOULD YOU LIKE TO FULIZA?(YES OR NO)")
                    if FULIZA_Q == "YES":

                        print("\nKINDLY WAIT FOR YOUR MPESA CONFIRMATION MESSAGE.THANKYOU FOR USING OUR SERVICES")
                        MPESA_MESSAGE = open("MPESA","x")
                        MPESA_MESSAGE.write(f"Confirmed. Ksh{TOTAL_PAYMENTS} sent to GOSHEN HOTEL on {current_date} at {current_time}. \nNew M-PESA balance is Ksh.0.0")
                        MPESA_MESSAGE.close()

                        FULIZA_MESSAGE = open("FULIZA","x")
                        FULIZA_MESSAGE.write(f"CONFIRMED. FULIZA MPESA AMOUNT IS Ksh.{TOTAL_PAYMENTS - ACC_BAL}.TOTAL FULIZA MPESA OUTSTANDING BALANCE IS Ksh.{TOTAL_PAYMENTS - ACC_BAL}")

                    if FULIZA_Q =="NO":

                        print("\nTRANSACTION INCOMPLETE DUE TO INSUFFICIENT FUNDS. RECHARGE YOUR ACCOUNT AND TRY AGAIN LATER!!!")
                
                elif ACC_BAL > TOTAL_PAYMENTS:

                        print("THANKYOU FOR USING OUR SERVICES. KINDLY WAIT FOR YOUR CONFIRMATION MESSAGE")
                        MPESA_MESSAGE = open("MPESA","x")
                        MPESA_MESSAGE.write(f"Confirmed. Ksh{TOTAL_PAYMENTS} sent to GOSHEN HOTEL on {current_date} at {current_time}. \nNew M-PESA balance is Ksh.{ACC_BAL - TOTAL_PAYMENTS}")
                        MPESA_MESSAGE.close()

                                                
            elif payment_method == 2:
                #converts your account balance cash into dollars
                #enter transaction details
                # enter paypal pin number
                TOTAL_PAYMENTS = DELIVERY_TOTAL + TOTAL_BILL
                print(f"\nYOU ARE SUPPOSED TO PAY A TOTAL OF Ksh.{TOTAL_PAYMENTS}")
                ACC_BAL = float(input("HOW MUCH DO YOU HAVE IN YOUR PAYPAL ACCOUNT?"))

                if ACC_BAL < TOTAL_PAYMENTS:

                    print("\nTRANSACTION INCOMPLETE DUE TO INSUFFICIENT FUNDS. RECHARGE YOUR PAYPAL ACCOUNT AND TRY AGAIN LATER!!!")
                
                elif ACC_BAL > TOTAL_PAYMENTS:

                        print("THANKYOU FOR USING OUR SERVICES. KINDLY WAIT FOR YOUR CONFIRMATION MESSAGE")
                        MPESA_MESSAGE = open("PAYPAL","x")
                        MPESA_MESSAGE.write(f"Confirmed. Ksh{TOTAL_PAYMENTS} sent to GOSHEN HOTEL on {current_date} at {current_time}. \nNew PAYPAL ACCOUNT BALANCE IS Ksh.{ACC_BAL - TOTAL_PAYMENTS}")
                        MPESA_MESSAGE.close()




        elif DELIVERY == 2:
            print("\n")
            SPECIAL_DELIVERY()

            while True:
                choice = int(input("\nSelect county choice number to deliver to::(exit='00')  => "))

                if choice == 1:
                        NAIROBI = 1 * 426 
                        print(f"DELIVERY PRICE TO NAIROBI IS Ksh.{NAIROBI}") #more info to be sent tomorrow

                elif choice == 2:
                        KIAMBU = 1 * 582
                 
                        print(f"DELIVERY PRICE TO KIAMBU IS Ksh.{KIAMBU}") #more info to be sent tomorrow

                elif choice == 3:
                        KISUMU = 1 * 1220
                        print(f"DELIVERY PRICE TO KISUMU IS Ksh.{KISUMU}") #more info to be sent tomorrow

                elif choice == 4:
                        MOMBASA = 1 * 1422
                        print(f"DELIVERY PRICE TO MOMBASA IS Ksh.{MOMBASA}") #more info to be sent tomorrow

                elif choice == 5:
                        SIAYA = 1 * 1413
                        print(f"DELIVERY PRICE TO SIAYA IS Ksh.{SIAYA}") #more info to be sent tomorrow

                elif choice == 00:
                        DELIVERY_TOTAL = NAIROBI + KISUMU +SIAYA + MOMBASA + KIAMBU
                        print(f"\nTOTAL SPECIAL DELIVERY PRICE ON SELECTED COUNTIE(S) IS Ksh.{DELIVERY_TOTAL}\n")
                        break

                # else:
                    # ("Enter the correct option")
#######################################################
            print("\nBELOW IS A PAYMENT METHOD LIST:: ")
            payments()
            payment_method = int(input("SELECT ONE PAYMENT METHOD::"))
            if payment_method == 1:
                #ENTER AMOUNT
                #ENTER PIN NUMBER THAT HAS BEEN GENERATED FOR YOU
                TOTAL_PAYMENTS = DELIVERY_TOTAL + TOTAL_BILL
                print(f"\nYOU ARE SUPPOSED TO PAY A TOTAL OF Ksh.{TOTAL_PAYMENTS}")
                ACC_BAL = float(input("HOW MUCH DO YOU HAVE IN YOUR MPESA?"))
                if ACC_BAL < TOTAL_PAYMENTS:
                    FULIZA_Q = input("YOU HAVE INSUFFICIENT FUNDS, WOULD YOU LIKE TO FULIZA?(YES OR NO)")
                    if FULIZA_Q == "YES":

                        print("\nKINDLY WAIT FOR YOUR MPESA CONFIRMATION MESSAGE.THANKYOU FOR USING OUR SERVICES")
                        MPESA_MESSAGE = open("MPESA","x")
                        MPESA_MESSAGE.write(f"Confirmed. Ksh{TOTAL_PAYMENTS} sent to GOSHEN HOTEL on {current_date} at {current_time}. \nNew M-PESA balance is Ksh.0.0")
                        MPESA_MESSAGE.close()

                        FULIZA_MESSAGE = open("FULIZA","x")
                        FULIZA_MESSAGE.write(f"CONFIRMED. FULIZA MPESA AMOUNT IS Ksh.{TOTAL_PAYMENTS - ACC_BAL}.TOTAL FULIZA MPESA OUTSTANDING BALANCE IS Ksh.{TOTAL_PAYMENTS - ACC_BAL}")

                    if FULIZA_Q =="NO":

                        print("\nTRANSACTION INCOMPLETE DUE TO INSUFFICIENT FUNDS. RECHARGE YOUR ACCOUNT AND TRY AGAIN LATER!!!")
                
                elif ACC_BAL > TOTAL_PAYMENTS:

                        print("THANKYOU FOR USING OUR SERVICES. KINDLY WAIT FOR YOUR CONFIRMATION MESSAGE")
                        MPESA_MESSAGE = open("MPESA","x")
                        MPESA_MESSAGE.write(f"Confirmed. Ksh{TOTAL_PAYMENTS} sent to GOSHEN HOTEL on {current_date} at {current_time}. \nNew M-PESA balance is Ksh.{ACC_BAL - TOTAL_PAYMENTS}")
                        MPESA_MESSAGE.close()

            elif payment_method == 2:
            #converts your account balance cash into dollars
            #enter transaction details
            # enter paypal pin number
                TOTAL_PAYMENTS = DELIVERY_TOTAL + TOTAL_BILL
                print(f"\nYOU ARE SUPPOSED TO PAY A TOTAL OF Ksh.{TOTAL_PAYMENTS}")
                ACC_BAL = float(input("HOW MUCH DO YOU HAVE IN YOUR PAYPAL ACCOUNT?"))

                if ACC_BAL < TOTAL_PAYMENTS:

                    print("\nTRANSACTION INCOMPLETE DUE TO INSUFFICIENT FUNDS. RECHARGE YOUR PAYPAL ACCOUNT AND TRY AGAIN LATER!!!")
                
                elif ACC_BAL > TOTAL_PAYMENTS:

                        print("THANKYOU FOR USING OUR SERVICES. KINDLY WAIT FOR YOUR CONFIRMATION MESSAGE")
                        MPESA_MESSAGE = open("PAYPAL","x")
                        MPESA_MESSAGE.write(f"Confirmed. Ksh{TOTAL_PAYMENTS} sent to GOSHEN HOTEL on {current_date} at {current_time}. \nNew PAYPAL ACCOUNT BALANCE IS Ksh.{ACC_BAL - TOTAL_PAYMENTS}")
                        MPESA_MESSAGE.close()
    
    elif DELIVERY_Q == "NO":
        print("CONTINUE WITH THE NORMAL PAYMENTS")
        print("\nBELOW IS A PAYMENT METHOD LIST:: ")
        payments()
        payment_method = int(input("SELECT ONE PAYMENT METHOD::"))
        if payment_method == 1:
                #ENTER AMOUNT
                #ENTER PIN NUMBER THAT HAS BEEN GENERATED FOR YOU
                TOTAL_PAYMENTS = TOTAL_BILL
                print(f"\nYOU ARE SUPPOSED TO PAY A TOTAL OF Ksh.{TOTAL_PAYMENTS}")
                ACC_BAL = float(input("HOW MUCH DO YOU HAVE IN YOUR MPESA?"))
                if ACC_BAL < TOTAL_PAYMENTS:
                    FULIZA_Q = input("YOU HAVE INSUFFICIENT FUNDS, WOULD YOU LIKE TO FULIZA?(YES OR NO)")
                    if FULIZA_Q == "YES":

                        print("\nKINDLY WAIT FOR YOUR MPESA CONFIRMATION MESSAGE.THANKYOU FOR USING OUR SERVICES")
                        MPESA_MESSAGE = open("MPESA","x")
                        MPESA_MESSAGE.write(f"Confirmed. Ksh{TOTAL_PAYMENTS} sent to GOSHEN HOTEL on {current_date} at {current_time}. \nNew M-PESA balance is Ksh.0.0")
                        MPESA_MESSAGE.close()

                        FULIZA_MESSAGE = open("FULIZA","x")
                        FULIZA_MESSAGE.write(f"CONFIRMED. FULIZA MPESA AMOUNT IS Ksh.{TOTAL_PAYMENTS - ACC_BAL}.TOTAL FULIZA MPESA OUTSTANDING BALANCE IS Ksh.{TOTAL_PAYMENTS - ACC_BAL}")

                    if FULIZA_Q =="NO":

                        print("\nTRANSACTION INCOMPLETE DUE TO INSUFFICIENT FUNDS. RECHARGE YOUR ACCOUNT AND TRY AGAIN LATER!!!")
                
                elif ACC_BAL > TOTAL_PAYMENTS:

                        print("THANKYOU FOR USING OUR SERVICES. KINDLY WAIT FOR YOUR CONFIRMATION MESSAGE")
                        MPESA_MESSAGE = open("MPESA","x")
                        MPESA_MESSAGE.write(f"Confirmed. Ksh{TOTAL_PAYMENTS} sent to GOSHEN HOTEL on {current_date} at {current_time}. \nNew M-PESA balance is Ksh.{ACC_BAL - TOTAL_PAYMENTS}")
                        MPESA_MESSAGE.close()

        elif payment_method == 2:
                #converts your account balance cash into dollars
                #enter transaction details
                # enter paypal pin number
                TOTAL_PAYMENTS =  TOTAL_BILL
                print(f"\nYOU ARE SUPPOSED TO PAY A TOTAL OF Ksh.{TOTAL_PAYMENTS}")
                ACC_BAL = float(input("HOW MUCH DO YOU HAVE IN YOUR PAYPAL ACCOUNT?"))

                if ACC_BAL < TOTAL_PAYMENTS:

                    print("\nTRANSACTION INCOMPLETE DUE TO INSUFFICIENT FUNDS. RECHARGE YOUR PAYPAL ACCOUNT AND TRY AGAIN LATER!!!")
                
                elif ACC_BAL > TOTAL_PAYMENTS:

                        print("THANKYOU FOR USING OUR SERVICES. KINDLY WAIT FOR YOUR CONFIRMATION MESSAGE")
                        MPESA_MESSAGE = open("PAYPAL","x")
                        MPESA_MESSAGE.write(f"Confirmed. Ksh{TOTAL_PAYMENTS} sent to GOSHEN HOTEL on {current_date} at {current_time}. \nNew PAYPAL ACCOUNT BALANCE IS Ksh.{ACC_BAL - TOTAL_PAYMENTS}")
                        MPESA_MESSAGE.close()
    
################################################################################################################################################################

elif MENU_CHOICE == 2:
    from MAIN_MENU import ready_meals
    print("\n") #start a new line before the function
    ready_meals() #calling the function
    print("\n")

    while True:
        
        READY_MEALS_SELECTION = int(input("SELECT THE MEALS(S) THAT YOU WANT(EXIT = 00):: "))
    

        if READY_MEALS_SELECTION == 1:
           # global TOTAL_CHAPATIS
            chapati = int(input("How many Chapatis do you want? "))
            
            TOTAL_CHAPATIS = (chapati * 25)
            print(f"TOTAL AMOUNT = Ksh.{TOTAL_CHAPATIS}\n")

        elif READY_MEALS_SELECTION == 2:
            #global TOTAL_SCRAMBLED_EGGS
            scrambled_eggs = int(input("How many Scrambled_eggs do you want? "))
            
            TOTAL_SCRAMBLED_EGGS = (scrambled_eggs * 30) 
            print(f"TOTAL AMOUNT = Ksh.{TOTAL_SCRAMBLED_EGGS}\n")

        elif READY_MEALS_SELECTION == 3:
            #global TOTAL_YELLOW_BEANS
            yellow_beans = int(input("How many plates of Yellow_beans do you want? "))
            
            TOTAL_YELLOW_BEANS = (yellow_beans * 30) 
            print(f"TOTAL AMOUNT = Ksh.{TOTAL_YELLOW_BEANS}\n")

        elif READY_MEALS_SELECTION == 4:
            #global TOTAL_BEEF
            beef = int(input("How many pieces of Beef do you want? "))
            
            TOTAL_BEEF = (beef * 200) 
            print(f"TOTAL AMOUNT = Ksh.{TOTAL_BEEF}\n")

        elif READY_MEALS_SELECTION == 5:
            #global TOTAL_RICE
            rice = int(input("How many plates of Rice do you want? "))
            
            TOTAL_RICE = (rice * 50) 
            print(f"TOTAL AMOUNT = Ksh.{TOTAL_RICE}\n")

        elif READY_MEALS_SELECTION == 6:
            #global TOTAL_GREEN_GRAMS
            green_grams = int(input("How many plates of Green_grams  do you want? "))
            
            TOTAL_GREEN_GRAMS = (green_grams * 40)
            print(f"TOTAL AMOUNT = Ksh.{TOTAL_GREEN_GRAMS}\n")

        elif READY_MEALS_SELECTION == 7:
            #global TOTAL_OMENA
            omena = int(input("How many plates of Omena do you want? "))
           
            TOTAL_OMENA = (omena * 45) 
            print(f"TOTAL AMOUNT = Ksh.{TOTAL_OMENA}\n")

        elif READY_MEALS_SELECTION == 8:
            #global TOTAL_UGALI
            ugali = int(input("How many pieces of Ugali do you want? "))
            
            TOTAL_UGALI = (ugali * 40) 
            print(f"TOTAL AMOUNT = Ksh.{TOTAL_UGALI}\n")
        
        elif READY_MEALS_SELECTION == 9:
            #global TOTAL_CHICKEN
            chicken = int(input("How many Chickens do you want? "))
            
            TOTAL_CHICKEN = (chicken * 350) 
            print(f"TOTAL AMOUNT = Ksh.{TOTAL_CHICKEN}\n")

        elif READY_MEALS_SELECTION == 10:
            #global TOTAL_FRIES
            fries = int(input("How many packets of Fries do you want? "))
            
            TOTAL_FRIES = (fries * 150) 
            print(f"TOTAL AMOUNT = Ksh.{TOTAL_FRIES}\n")

        elif READY_MEALS_SELECTION == 00:
            TOTAL_BILL = TOTAL_CHAPATI + TOTAL_SCRAMBLED_EGGS + TOTAL_YELLOW_BEANS + TOTAL_BEEF + TOTAL_RICE + TOTAL_GREEN_GRAMS + TOTAL_OMENA + TOTAL_UGALI + TOTAL_CHICKEN + TOTAL_FRIES
            print(f"\nYOUR TOTAL BILL IS Ksh.{TOTAL_BILL}\n")
            break

    DELIVERY_Q = input("\tDO YOU WANT YOUR GOODS TO BE DELIVERED? (YES or NO):: ")

    if DELIVERY_Q == "YES":

        print("\n\tTHANKYOU FOR CHOOSING OUR DELIVERY SERVICES!!!\n")
        order_type()

        DELIVERY = int(input("SELECT YOUR DELIVERY TYPE(INT):: "))

        if DELIVERY == 1:
            print("\n")
            NORMAL_DELIVERY()

            while not DELIVERY in AVAILABLE_COUNTIES:
                CHOICE = int(input("\nSelect county choice number to deliver to:(exit='00')  => "))

                if CHOICE == 1:
                    nairobi = random.randrange(423,442)
                    print(f"DELIVERY PRICE TO NAIROBI IS Ksh.{nairobi}")

                elif CHOICE == 2:
                    kiambu = random.randrange(583,602)
                    print(f"DELIVERY PRICE TO KIAMBU IS Ksh.{kiambu}")

                elif CHOICE == 3:
                    kisumu = random.randrange(1228,1241)
                    print(f"DELIVERY PRICE TO KISUMU IS Ksh.{kisumu}") 

                elif CHOICE == 4:
                    mombasa = random.randrange(1423,1444)
                    print(f"DELIVERY PRICE TO MOMBASA IS Ksh.{mombasa}") 

                elif CHOICE == 5:
                    siaya = random.randrange(1413,1436)
                    print(f"DELIVERY PRICE TO SIAYA IS Ksh.{siaya}") 

                elif CHOICE == 00:
                    DELIVERY_TOTAL = nairobi + kisumu +siaya + mombasa + kiambu
                    print(f"\nTOTAL NORMAL DELIVERY PRICE ON SELECTED COUNTIE(S) IS Ksh.{DELIVERY_TOTAL}\n")
                    break

                # else:
                    # ("Enter the correct option")
            #PAYMENT MODULE


            print("\nBELOW IS A PAYMENT METHOD LIST:: ")
            payments()
            payment_method = int(input("SELECT ONE PAYMENT METHOD::"))
            if payment_method == 1:
                #ENTER AMOUNT
                #ENTER PIN NUMBER THAT HAS BEEN GENERATED FOR YOU
                TOTAL_PAYMENTS = DELIVERY_TOTAL + TOTAL_BILL
                print(f"\nYOU ARE SUPPOSED TO PAY A TOTAL OF Ksh.{TOTAL_PAYMENTS}")
                ACC_BAL = float(input("HOW MUCH DO YOU HAVE IN YOUR MPESA?"))
                if ACC_BAL < TOTAL_PAYMENTS:
                    FULIZA_Q = input("YOU HAVE INSUFFICIENT FUNDS, WOULD YOU LIKE TO FULIZA?(YES OR NO)")
                    if FULIZA_Q == "YES":

                        print("\nKINDLY WAIT FOR YOUR MPESA CONFIRMATION MESSAGE.THANKYOU FOR USING OUR SERVICES")
                        MPESA_MESSAGE = open("MPESA","x")
                        MPESA_MESSAGE.write(f"Confirmed. Ksh{TOTAL_PAYMENTS} sent to GOSHEN HOTEL on {current_date} at {current_time}. \nNew M-PESA balance is Ksh.0.0")
                        MPESA_MESSAGE.close()

                        FULIZA_MESSAGE = open("FULIZA","x")
                        FULIZA_MESSAGE.write(f"CONFIRMED. FULIZA MPESA AMOUNT IS Ksh.{TOTAL_PAYMENTS - ACC_BAL}.TOTAL FULIZA MPESA OUTSTANDING BALANCE IS Ksh.{TOTAL_PAYMENTS - ACC_BAL}")

                    if FULIZA_Q =="NO":

                        print("\nTRANSACTION INCOMPLETE DUE TO INSUFFICIENT FUNDS. RECHARGE YOUR ACCOUNT AND TRY AGAIN LATER!!!")
                
                elif ACC_BAL > TOTAL_PAYMENTS:

                        print("THANKYOU FOR USING OUR SERVICES. KINDLY WAIT FOR YOUR CONFIRMATION MESSAGE")
                        MPESA_MESSAGE = open("MPESA","x")
                        MPESA_MESSAGE.write(f"Confirmed. Ksh{TOTAL_PAYMENTS} sent to GOSHEN HOTEL on {current_date} at {current_time}. \nNew M-PESA balance is Ksh.{ACC_BAL - TOTAL_PAYMENTS}")
                        MPESA_MESSAGE.close()

            elif payment_method == 2:
                #converts your account balance cash into dollars
                #enter transaction details
                #enter paypal pin number
                TOTAL_PAYMENTS = DELIVERY_TOTAL + TOTAL_BILL
                print(f"\nYOU ARE SUPPOSED TO PAY A TOTAL OF Ksh.{TOTAL_PAYMENTS}")
                ACC_BAL = float(input("HOW MUCH DO YOU HAVE IN YOUR PAYPAL ACCOUNT?"))

                if ACC_BAL < TOTAL_PAYMENTS:

                    print("\nTRANSACTION INCOMPLETE DUE TO INSUFFICIENT FUNDS. RECHARGE YOUR PAYPAL ACCOUNT AND TRY AGAIN LATER!!!")
                
                elif ACC_BAL > TOTAL_PAYMENTS:

                        print("THANKYOU FOR USING OUR SERVICES. KINDLY WAIT FOR YOUR CONFIRMATION MESSAGE")
                        MPESA_MESSAGE = open("PAYPAL","x")
                        MPESA_MESSAGE.write(f"Confirmed. Ksh{TOTAL_PAYMENTS} sent to GOSHEN HOTEL on {current_date} at {current_time}. \nNew PAYPAL ACCOUNT BALANCE IS Ksh.{ACC_BAL - TOTAL_PAYMENTS}")
                        MPESA_MESSAGE.close()




        elif DELIVERY == 2:
            print("\n")
            SPECIAL_DELIVERY()

            while not DELIVERY in AVAILABLE_COUNTIES:
                choice = int(input("\nSelect county choice number to deliver to::(exit='00')  => "))

                if choice == 1:
                    NAIROBI = 1 * 426 
                    print(f"DELIVERY PRICE TO NAIROBI IS Ksh.{NAIROBI}") #more info to be sent tomorrow

                elif choice == 2:
                    KIAMBU = 1 * 582
                 
                    print(f"DELIVERY PRICE TO KIAMBU IS Ksh.{KIAMBU}") #more info to be sent tomorrow

                elif choice == 3:
                    KISUMU = 1 * 1220
                    print(f"DELIVERY PRICE TO KISUMU IS Ksh.{KISUMU}") #more info to be sent tomorrow

                elif choice == 4:
                    MOMBASA = 1 * 1422
                    print(f"DELIVERY PRICE TO MOMBASA IS Ksh.{MOMBASA}") #more info to be sent tomorrow

                elif choice == 5:
                    SIAYA = 1 * 1412
                    print(f"DELIVERY PRICE TO SIAYA IS Ksh.{SIAYA}") #more info to be sent tomorrow

                elif choice == 00:
                    DELIVERY_TOTAL = NAIROBI + KISUMU +SIAYA + MOMBASA + KIAMBU
                    print(f"\nTOTAL SPECIAL DELIVERY PRICE ON SELECTED COUNTIE(S) IS Ksh.{DELIVERY_TOTAL}\n")
                    break

                # else:
                    # ("Enter the correct option")
#######################################################
            #PAYMENT MODULE


            print("\nBELOW IS A PAYMENT METHOD LIST:: ")
            payments()
            payment_method = int(input("SELECT ONE PAYMENT METHOD::"))
            if payment_method == 1:
                #ENTER AMOUNT
                #ENTER PIN NUMBER THAT HAS BEEN GENERATED FOR YOU
                TOTAL_PAYMENTS = DELIVERY_TOTAL + TOTAL_BILL
                print(f"\nYOU ARE SUPPOSED TO PAY A TOTAL OF Ksh.{TOTAL_PAYMENTS}")
                ACC_BAL = float(input("HOW MUCH DO YOU HAVE IN YOUR MPESA?"))
                if ACC_BAL < TOTAL_PAYMENTS:
                    FULIZA_Q = input("YOU HAVE INSUFFICIENT FUNDS, WOULD YOU LIKE TO FULIZA?(YES OR NO)")
                    if FULIZA_Q == "YES":

                        print("\nKINDLY WAIT FOR YOUR MPESA CONFIRMATION MESSAGE.THANKYOU FOR USING OUR SERVICES")
                        MPESA_MESSAGE = open("MPESA","x")
                        MPESA_MESSAGE.write(f"Confirmed. Ksh{TOTAL_PAYMENTS} sent to GOSHEN HOTEL on {current_date} at {current_time}. \nNew M-PESA balance is Ksh.0.0")
                        MPESA_MESSAGE.close()

                        FULIZA_MESSAGE = open("FULIZA","x")
                        FULIZA_MESSAGE.write(f"CONFIRMED. FULIZA MPESA AMOUNT IS Ksh.{TOTAL_PAYMENTS - ACC_BAL}.TOTAL FULIZA MPESA OUTSTANDING BALANCE IS Ksh.{TOTAL_PAYMENTS - ACC_BAL}")

                    if FULIZA_Q =="NO":

                        print("\nTRANSACTION INCOMPLETE DUE TO INSUFFICIENT FUNDS. RECHARGE YOUR ACCOUNT AND TRY AGAIN LATER!!!")
                
                elif ACC_BAL > TOTAL_PAYMENTS:

                        print("THANKYOU FOR USING OUR SERVICES. KINDLY WAIT FOR YOUR CONFIRMATION MESSAGE")
                        MPESA_MESSAGE = open("MPESA","x")
                        MPESA_MESSAGE.write(f"Confirmed. Ksh{TOTAL_PAYMENTS} sent to GOSHEN HOTEL on {current_date} at {current_time}. \nNew M-PESA balance is Ksh.{ACC_BAL - TOTAL_PAYMENTS}")
                        MPESA_MESSAGE.close()

            elif payment_method == 2:
                #converts your account balance cash into dollars
                #enter transaction details
                # enter paypal pin number
                TOTAL_PAYMENTS = DELIVERY_TOTAL + TOTAL_BILL
                print(f"\nYOU ARE SUPPOSED TO PAY A TOTAL OF Ksh.{TOTAL_PAYMENTS}")
                ACC_BAL = float(input("HOW MUCH DO YOU HAVE IN YOUR PAYPAL ACCOUNT?"))

                if ACC_BAL < TOTAL_PAYMENTS:

                    print("\nTRANSACTION INCOMPLETE DUE TO INSUFFICIENT FUNDS. RECHARGE YOUR PAYPAL ACCOUNT AND TRY AGAIN LATER!!!")
                
                elif ACC_BAL > TOTAL_PAYMENTS:

                        print("THANKYOU FOR USING OUR SERVICES. KINDLY WAIT FOR YOUR CONFIRMATION MESSAGE")
                        MPESA_MESSAGE = open("PAYPAL","x")
                        MPESA_MESSAGE.write(f"Confirmed. Ksh{TOTAL_PAYMENTS} sent to GOSHEN HOTEL on {current_date} at {current_time}. \nNew PAYPAL ACCOUNT BALANCE IS Ksh.{ACC_BAL - TOTAL_PAYMENTS}")
                        MPESA_MESSAGE.close()
 

    elif DELIVERY_Q == "NO":
        print("CONTINUE WITH THE NORMAL PAYMENTS")
        print("\nBELOW IS A PAYMENT METHOD LIST:: ")
        payments()
        payment_method = int(input("SELECT ONE PAYMENT METHOD::"))
        if payment_method == 1:
                #ENTER AMOUNT
                #ENTER PIN NUMBER THAT HAS BEEN GENERATED FOR YOU
                TOTAL_PAYMENTS = TOTAL_BILL
                print(f"\nYOU ARE SUPPOSED TO PAY A TOTAL OF Ksh.{TOTAL_PAYMENTS}")
                ACC_BAL = float(input("HOW MUCH DO YOU HAVE IN YOUR MPESA?"))
                if ACC_BAL < TOTAL_PAYMENTS:
                    FULIZA_Q = input("YOU HAVE INSUFFICIENT FUNDS, WOULD YOU LIKE TO FULIZA?(YES OR NO)")
                    if FULIZA_Q == "YES":

                        print("\nKINDLY WAIT FOR YOUR MPESA CONFIRMATION MESSAGE.THANKYOU FOR USING OUR SERVICES")
                        MPESA_MESSAGE = open("MPESA","x")
                        MPESA_MESSAGE.write(f"Confirmed. Ksh{TOTAL_PAYMENTS} sent to GOSHEN HOTEL on {current_date} at {current_time}. \nNew M-PESA balance is Ksh.0.0")
                        MPESA_MESSAGE.close()

                        FULIZA_MESSAGE = open("FULIZA","x")
                        FULIZA_MESSAGE.write(f"CONFIRMED. FULIZA MPESA AMOUNT IS Ksh.{TOTAL_PAYMENTS - ACC_BAL}.TOTAL FULIZA MPESA OUTSTANDING BALANCE IS Ksh.{TOTAL_PAYMENTS - ACC_BAL}")

                    if FULIZA_Q =="NO":

                        print("\nTRANSACTION INCOMPLETE DUE TO INSUFFICIENT FUNDS. RECHARGE YOUR ACCOUNT AND TRY AGAIN LATER!!!")
                
                elif ACC_BAL > TOTAL_PAYMENTS:

                        print("THANKYOU FOR USING OUR SERVICES. KINDLY WAIT FOR YOUR CONFIRMATION MESSAGE")
                        MPESA_MESSAGE = open("MPESA","x")
                        MPESA_MESSAGE.write(f"Confirmed. Ksh{TOTAL_PAYMENTS} sent to GOSHEN HOTEL on {current_date} at {current_time}. \nNew M-PESA balance is Ksh.{ACC_BAL - TOTAL_PAYMENTS}")
                        MPESA_MESSAGE.close()

        elif payment_method == 2:
                #converts your account balance cash into dollars
                #enter transaction details
                # enter paypal pin number
                TOTAL_PAYMENTS = TOTAL_BILL
                print(f"\nYOU ARE SUPPOSED TO PAY A TOTAL OF Ksh.{TOTAL_PAYMENTS}")
                ACC_BAL = float(input("HOW MUCH DO YOU HAVE IN YOUR PAYPAL ACCOUNT?"))

                if ACC_BAL < TOTAL_PAYMENTS:

                    print("\nTRANSACTION INCOMPLETE DUE TO INSUFFICIENT FUNDS. RECHARGE YOUR PAYPAL ACCOUNT AND TRY AGAIN LATER!!!")
                
                elif ACC_BAL > TOTAL_PAYMENTS:

                        print("THANKYOU FOR USING OUR SERVICES. KINDLY WAIT FOR YOUR CONFIRMATION MESSAGE")
                        MPESA_MESSAGE = open("PAYPAL","x")
                        MPESA_MESSAGE.write(f"Confirmed. Ksh{TOTAL_PAYMENTS} sent to GOSHEN HOTEL on {current_date} at {current_time}. \nNew PAYPAL ACCOUNT BALANCE IS Ksh.{ACC_BAL - TOTAL_PAYMENTS}")
                        MPESA_MESSAGE.close()
 

#########################################################################################################################################################################

elif MENU_CHOICE == 3:
    from MAIN_MENU import fruits_and_vegetables
    print("\n") #start a new line before the function
    fruits_and_vegetables() #calling the function
    print("\n")

    while True:
        
        FRUITS_AND_VEGETABLES_SELECTION = int(input("SELECT THE FRUIT(S) THAT YOU WANT(EXIT = 00):: "))
        

        if FRUITS_AND_VEGETABLES_SELECTION == 1:
           # global TOTAL_APPLES
            apple = int(input("How many Apples do you want? "))
            
            TOTAL_APPLES = (apple * 35)

            print(f"TOTAL AMOUNT = Ksh.{TOTAL_APPLES}\n")

        elif FRUITS_AND_VEGETABLES_SELECTION == 2:
            #global TOTAL_BANANAS
            banana = int(input("How many Bananas do you want? "))
            
            TOTAL_BANANAS = (banana * 15) 
            print(f"TOTAL AMOUNT = Ksh.{TOTAL_BANANAS}\n")

        elif FRUITS_AND_VEGETABLES_SELECTION == 3:
            #global TOTAL_ORANGES
            orange = int(input("How many Oranges do you want? "))
            
            TOTAL_ORANGES = (orange * 25) 
            print(f"TOTAL AMOUNT = Ksh.{TOTAL_ORANGES}\n")

        elif FRUITS_AND_VEGETABLES_SELECTION == 4:
            #global TOTAL_WATERMELONS
            watermelon = int(input("How many Watermelons do you want? "))
            
            TOTAL_WATERMELONS = (watermelon * 55) 
            print(f"TOTAL AMOUNT = Ksh.{TOTAL_WATERMELONS}\n")

        elif FRUITS_AND_VEGETABLES_SELECTION == 5:
            #global TOTAL_STRAWBERRIES
            strawberries = int(input("How many Strawberries do you want? "))
            
            TOTAL_STRAWBERRIES = (strawberries * 60) 
            print(f"TOTAL AMOUNT = Ksh.{TOTAL_STRAWBERRIES}\n")

        elif FRUITS_AND_VEGETABLES_SELECTION == 6:
            #global TOTAL_AVOCADO
            avocado = int(input("How many Avocados  do you want? "))
            
            TOTAL_AVOCADO = (avocado * 30)
            print(f"TOTAL AMOUNT = Ksh.{TOTAL_AVOCADO}\n")

        elif FRUITS_AND_VEGETABLES_SELECTION == 7:
            #global TOTAL_KALES
            kales = int(input("How many Kales do you want? "))
            
            TOTAL_KALES= (kales * 20) 
            print(f"TOTAL AMOUNT = Ksh.{TOTAL_KALES}\n")

        elif FRUITS_AND_VEGETABLES_SELECTION == 8:
            #global TOTAL_CABBAGE
            cabbage = int(input("How many Cabbages do you want? "))
            
            TOTAL_CABBAGE = (cabbage * 25) 
            print(f"TOTAL AMOUNT = Ksh.{TOTAL_CABBAGE}\n")
        
        elif FRUITS_AND_VEGETABLES_SELECTION == 9:
            #global TOTAL_LETTUCE
            lettuce = int(input("How many Lettuces do you want? "))
            
            TOTAL_LETTUCE = (lettuce * 55) 
            print(f"TOTAL AMOUNT = Ksh.{TOTAL_LETTUCE}\n")

        elif FRUITS_AND_VEGETABLES_SELECTION == 10:
            #global TOTAL_BROCCOLI
            broccoli = int(input("How many Broccolis do you want? "))
            
            TOTAL_BROCCOLI = (broccoli * 75) 
            print(f"TOTAL AMOUNT = Ksh.{TOTAL_BROCCOLI}\n")

        elif FRUITS_AND_VEGETABLES_SELECTION == 00:
            TOTAL_BILL = TOTAL_APPLES + TOTAL_BANANAS + TOTAL_ORANGES + TOTAL_WATERMELONS + TOTAL_STRAWBERRIES + TOTAL_AVOCADO + TOTAL_KALES + TOTAL_CABBAGE + TOTAL_LETTUCE + TOTAL_BROCCOLI
            print(f"\nYOUR TOTAL BILL IS Ksh.{TOTAL_BILL}\n")
            break
        
    DELIVERY_Q = input("\tDO YOU WANT YOUR GOODS TO BE DELIVERED? (YES or NO):: ")
    if DELIVERY_Q == "YES":
          
        print("\n\tTHANKYOU FOR CHOOSING OUR DELIVERY SERVICES!!!\n")
        order_type()

        DELIVERY = int(input("SELECT YOUR DELIVERY TYPE(INT):: "))

        if DELIVERY == 1:
            print("\n")
            NORMAL_DELIVERY()

            while not DELIVERY in AVAILABLE_COUNTIES:
                CHOICE = int(input("\nSelect county choice number to deliver to:(exit='00')  => "))

                if CHOICE == 1:
                    nairobi = random.randrange(423,442)
                    print(f"DELIVERY PRICE TO NAIROBI IS Ksh.{nairobi}")

                elif CHOICE == 2:
                    kiambu = random.randrange(583,602)
                    print(f"DELIVERY PRICE TO KIAMBU IS Ksh.{kiambu}")

                elif CHOICE == 3:
                    kisumu = random.randrange(1228,1241)
                    print(f"DELIVERY PRICE TO KISUMU IS Ksh.{kisumu}") 

                elif CHOICE == 4:
                    mombasa = random.randrange(1423,1444)
                    print(f"DELIVERY PRICE TO MOMBASA IS Ksh.{mombasa}") 

                elif CHOICE == 5:
                    siaya = random.randrange(1413,1436)
                    print(f"DELIVERY PRICE TO SIAYA IS Ksh.{siaya}") 

                elif CHOICE == 00:
                    DELIVERY_TOTAL = nairobi + kisumu +siaya + mombasa + kiambu
                    print(f"\nTOTAL NORMAL DELIVERY PRICE ON SELECTED COUNTIE(S) IS Ksh.{DELIVERY_TOTAL}\n")
                    break

                # else:
                    # ("Enter the correct option")
#PAYMENT MODULE

            print("\nBELOW IS A PAYMENT METHOD LIST:: ")
            payments()
            payment_method = int(input("SELECT ONE PAYMENT METHOD::"))
            if payment_method == 1:
                #ENTER AMOUNT
                #ENTER PIN NUMBER THAT HAS BEEN GENERATED FOR YOU
                TOTAL_PAYMENTS = DELIVERY_TOTAL + TOTAL_BILL
                print(f"\nYOU ARE SUPPOSED TO PAY A TOTAL OF Ksh.{TOTAL_PAYMENTS}")
                ACC_BAL = float(input("HOW MUCH DO YOU HAVE IN YOUR MPESA?"))
                if ACC_BAL < TOTAL_PAYMENTS:
                    FULIZA_Q = input("YOU HAVE INSUFFICIENT FUNDS, WOULD YOU LIKE TO FULIZA?(YES OR NO)")
                    if FULIZA_Q == "YES":

                        print("\nKINDLY WAIT FOR YOUR MPESA CONFIRMATION MESSAGE.THANKYOU FOR USING OUR SERVICES")
                        MPESA_MESSAGE = open("MPESA","x")
                        MPESA_MESSAGE.write(f"Confirmed. Ksh{TOTAL_PAYMENTS} sent to GOSHEN HOTEL on {current_date} at {current_time}. \nNew M-PESA balance is Ksh.0.0")
                        MPESA_MESSAGE.close()

                        FULIZA_MESSAGE = open("FULIZA","x")
                        FULIZA_MESSAGE.write(f"CONFIRMED. FULIZA MPESA AMOUNT IS Ksh.{TOTAL_PAYMENTS - ACC_BAL}.TOTAL FULIZA MPESA OUTSTANDING BALANCE IS Ksh.{TOTAL_PAYMENTS - ACC_BAL}")

                    if FULIZA_Q =="NO":

                        print("\nTRANSACTION INCOMPLETE DUE TO INSUFFICIENT FUNDS. RECHARGE YOUR ACCOUNT AND TRY AGAIN LATER!!!")
                
                elif ACC_BAL > TOTAL_PAYMENTS:

                        print("THANKYOU FOR USING OUR SERVICES. KINDLY WAIT FOR YOUR CONFIRMATION MESSAGE")
                        MPESA_MESSAGE = open("MPESA","x")
                        MPESA_MESSAGE.write(f"Confirmed. Ksh{TOTAL_PAYMENTS} sent to GOSHEN HOTEL on {current_date} at {current_time}. \nNew M-PESA balance is Ksh.{ACC_BAL - TOTAL_PAYMENTS}")
                        MPESA_MESSAGE.close()

            elif payment_method == 2:
                #converts your account balance cash into dollars
                #enter transaction details
                # enter paypal pin number
                TOTAL_PAYMENTS = DELIVERY_TOTAL + TOTAL_BILL
                print(f"\nYOU ARE SUPPOSED TO PAY A TOTAL OF Ksh.{TOTAL_PAYMENTS}")
                ACC_BAL = float(input("HOW MUCH DO YOU HAVE IN YOUR PAYPAL ACCOUNT?"))

                if ACC_BAL < TOTAL_PAYMENTS:

                    print("\nTRANSACTION INCOMPLETE DUE TO INSUFFICIENT FUNDS. RECHARGE YOUR PAYPAL ACCOUNT AND TRY AGAIN LATER!!!")
                
                elif ACC_BAL > TOTAL_PAYMENTS:

                        print("THANKYOU FOR USING OUR SERVICES. KINDLY WAIT FOR YOUR CONFIRMATION MESSAGE")
                        MPESA_MESSAGE = open("PAYPAL","x")
                        MPESA_MESSAGE.write(f"Confirmed. Ksh{TOTAL_PAYMENTS} sent to GOSHEN HOTEL on {current_date} at {current_time}. \nNew PAYPAL ACCOUNT BALANCE IS Ksh.{ACC_BAL - TOTAL_PAYMENTS}")
                        MPESA_MESSAGE.close() 


        elif DELIVERY == 2:
            print("\n")
            SPECIAL_DELIVERY()


            while not DELIVERY in AVAILABLE_COUNTIES:
                choice = int(input("\nSelect county choice number to deliver to::(exit='00')  => "))


                if choice == 1:
                    NAIROBI = 1 * 426 
                    print(f"DELIVERY PRICE TO NAIROBI IS Ksh.{NAIROBI}") #more info to be sent tomorrow

                elif choice == 2:
                    KIAMBU = 1 * 582
                 
                    print(f"DELIVERY PRICE TO KIAMBU IS Ksh.{KIAMBU}") #more info to be sent tomorrow

                elif choice == 3:
                    KISUMU = 1 * 1220
                    print(f"DELIVERY PRICE TO KISUMU IS Ksh.{KISUMU}") #more info to be sent tomorrow

                elif choice == 4:
                    MOMBASA = 1 * 1422
                    print(f"DELIVERY PRICE TO MOMBASA IS Ksh.{MOMBASA}") #more info to be sent tomorrow

                elif choice == 5:
                    SIAYA = 1 * 1412
                    print(f"DELIVERY PRICE TO SIAYA IS Ksh.{SIAYA}") #more info to be sent tomorrow

                elif choice == 00:
                    DELIVERY_TOTAL = NAIROBI + KISUMU +SIAYA + MOMBASA + KIAMBU
                    print(f"\nTOTAL SPECIAL DELIVERY PRICE ON SELECTED COUNTIE(S) IS Ksh.{DELIVERY_TOTAL}\n")
                    break

                # else:
                    # ("Enter the correct option")
#######################################################
    #PAYMENT MODULE

            print("\nBELOW IS A PAYMENT METHOD LIST:: ")
            payments()
            payment_method = int(input("SELECT ONE PAYMENT METHOD::"))
            if payment_method == 1:
                #ENTER AMOUNT
                #ENTER PIN NUMBER THAT HAS BEEN GENERATED FOR YOU
                TOTAL_PAYMENTS = DELIVERY_TOTAL + TOTAL_BILL
                print(f"\nYOU ARE SUPPOSED TO PAY A TOTAL OF Ksh.{TOTAL_PAYMENTS}")
                ACC_BAL = float(input("HOW MUCH DO YOU HAVE IN YOUR MPESA?"))
                if ACC_BAL < TOTAL_PAYMENTS:
                    FULIZA_Q = input("YOU HAVE INSUFFICIENT FUNDS, WOULD YOU LIKE TO FULIZA?(YES OR NO)")
                    if FULIZA_Q == "YES":

                        print("\nKINDLY WAIT FOR YOUR MPESA CONFIRMATION MESSAGE.THANKYOU FOR USING OUR SERVICES")
                        MPESA_MESSAGE = open("MPESA","x")
                        MPESA_MESSAGE.write(f"Confirmed. Ksh{TOTAL_PAYMENTS} sent to GOSHEN HOTEL on {current_date} at {current_time}. \nNew M-PESA balance is Ksh.0.0")
                        MPESA_MESSAGE.close()

                        FULIZA_MESSAGE = open("FULIZA","x")
                        FULIZA_MESSAGE.write(f"CONFIRMED. FULIZA MPESA AMOUNT IS Ksh.{TOTAL_PAYMENTS - ACC_BAL}.TOTAL FULIZA MPESA OUTSTANDING BALANCE IS Ksh.{TOTAL_PAYMENTS - ACC_BAL}")

                    if FULIZA_Q =="NO":

                        print("\nTRANSACTION INCOMPLETE DUE TO INSUFFICIENT FUNDS. RECHARGE YOUR ACCOUNT AND TRY AGAIN LATER!!!")
                
                elif ACC_BAL > TOTAL_PAYMENTS:

                        print("THANKYOU FOR USING OUR SERVICES. KINDLY WAIT FOR YOUR CONFIRMATION MESSAGE")
                        MPESA_MESSAGE = open("MPESA","x")
                        MPESA_MESSAGE.write(f"Confirmed. Ksh{TOTAL_PAYMENTS} sent to GOSHEN HOTEL on {current_date} at {current_time}. \nNew M-PESA balance is Ksh.{ACC_BAL - TOTAL_PAYMENTS}")
                        MPESA_MESSAGE.close()

            elif payment_method == 2:
                #converts your account balance cash into dollars
                #enter transaction details
                # enter paypal pin number
                TOTAL_PAYMENTS = DELIVERY_TOTAL + TOTAL_BILL
                print(f"\nYOU ARE SUPPOSED TO PAY A TOTAL OF Ksh.{TOTAL_PAYMENTS}")
                ACC_BAL = float(input("HOW MUCH DO YOU HAVE IN YOUR PAYPAL ACCOUNT?"))

                if ACC_BAL < TOTAL_PAYMENTS:

                    print("\nTRANSACTION INCOMPLETE DUE TO INSUFFICIENT FUNDS. RECHARGE YOUR PAYPAL ACCOUNT AND TRY AGAIN LATER!!!")
                
                elif ACC_BAL > TOTAL_PAYMENTS:

                        print("THANKYOU FOR USING OUR SERVICES. KINDLY WAIT FOR YOUR CONFIRMATION MESSAGE")
                        MPESA_MESSAGE = open("PAYPAL","x")
                        MPESA_MESSAGE.write(f"Confirmed. Ksh{TOTAL_PAYMENTS} sent to GOSHEN HOTEL on {current_date} at {current_time}. \nNew PAYPAL ACCOUNT BALANCE IS Ksh.{ACC_BAL - TOTAL_PAYMENTS}")
                        MPESA_MESSAGE.close() 

    elif DELIVERY_Q == "NO":
        print("CONTINUE WITH THE NORMAL PAYMENTS")
        print("\nBELOW IS A PAYMENT METHOD LIST:: ")
        payments()
        payment_method = int(input("SELECT ONE PAYMENT METHOD::"))
        if payment_method == 1:
            #ENTER AMOUNT
            #ENTER PIN NUMBER THAT HAS BEEN GENERATED FOR YOU
                TOTAL_PAYMENTS = TOTAL_BILL
                print(f"\nYOU ARE SUPPOSED TO PAY A TOTAL OF Ksh.{TOTAL_PAYMENTS}")
                ACC_BAL = float(input("HOW MUCH DO YOU HAVE IN YOUR MPESA?"))
                if ACC_BAL < TOTAL_PAYMENTS:
                    FULIZA_Q = input("YOU HAVE INSUFFICIENT FUNDS, WOULD YOU LIKE TO FULIZA?(YES OR NO)")
                    if FULIZA_Q == "YES":

                        print("\nKINDLY WAIT FOR YOUR MPESA CONFIRMATION MESSAGE.THANKYOU FOR USING OUR SERVICES")
                        MPESA_MESSAGE = open("MPESA","x")
                        MPESA_MESSAGE.write(f"Confirmed. Ksh{TOTAL_PAYMENTS} sent to GOSHEN HOTEL on {current_date} at {current_time}. \nNew M-PESA balance is Ksh.0.0")
                        MPESA_MESSAGE.close()

                        FULIZA_MESSAGE = open("FULIZA","x")
                        FULIZA_MESSAGE.write(f"CONFIRMED. FULIZA MPESA AMOUNT IS Ksh.{TOTAL_PAYMENTS - ACC_BAL}.TOTAL FULIZA MPESA OUTSTANDING BALANCE IS Ksh.{TOTAL_PAYMENTS - ACC_BAL}")

                    if FULIZA_Q =="NO":

                        print("\nTRANSACTION INCOMPLETE DUE TO INSUFFICIENT FUNDS. RECHARGE YOUR ACCOUNT AND TRY AGAIN LATER!!!")
                
                elif ACC_BAL > TOTAL_PAYMENTS:

                        print("THANKYOU FOR USING OUR SERVICES. KINDLY WAIT FOR YOUR CONFIRMATION MESSAGE")
                        MPESA_MESSAGE = open("MPESA","x")
                        MPESA_MESSAGE.write(f"Confirmed. Ksh{TOTAL_PAYMENTS} sent to GOSHEN HOTEL on {current_date} at {current_time}. \nNew M-PESA balance is Ksh.{ACC_BAL - TOTAL_PAYMENTS}")
                        MPESA_MESSAGE.close()

        elif payment_method == 2:
            #converts your account balance cash into dollars
            #enter transaction details
            # enter paypal pin number
                TOTAL_PAYMENTS =  TOTAL_BILL
                print(f"\nYOU ARE SUPPOSED TO PAY A TOTAL OF Ksh.{TOTAL_PAYMENTS}")
                ACC_BAL = float(input("HOW MUCH DO YOU HAVE IN YOUR PAYPAL ACCOUNT?"))

                if ACC_BAL < TOTAL_PAYMENTS:

                    print("\nTRANSACTION INCOMPLETE DUE TO INSUFFICIENT FUNDS. RECHARGE YOUR PAYPAL ACCOUNT AND TRY AGAIN LATER!!!")
                
                elif ACC_BAL > TOTAL_PAYMENTS:

                        print("THANKYOU FOR USING OUR SERVICES. KINDLY WAIT FOR YOUR CONFIRMATION MESSAGE")
                        MPESA_MESSAGE = open("PAYPAL","x")
                        MPESA_MESSAGE.write(f"Confirmed. Ksh{TOTAL_PAYMENTS} sent to GOSHEN HOTEL on {current_date} at {current_time}. \nNew PAYPAL ACCOUNT BALANCE IS Ksh.{ACC_BAL - TOTAL_PAYMENTS}")
                        MPESA_MESSAGE.close() 

#######################################################################################################################################################################        

elif MENU_CHOICE == 4:
    from MAIN_MENU import drinks
    print("\n") #start a new line before the function
    drinks() #calling the function
    print("\n")

    DRINKS_SELECTION = int(input("SELECT THE DRINK CATEGORY THAT YOU WANT:: "))

    if DRINKS_SELECTION == 1:
        from MAIN_MENU import drinks_hotdrinks
        print("\n")
        drinks_hotdrinks()
        print("\n")

        while True:
        
            HOT_DRINKS_SELECTION = int(input("SELECT THE HOT DRINK(S) THAT YOU WANT.(EXIT = 00) :: "))


            if HOT_DRINKS_SELECTION == 1:
                #global TOTAL_COFFEE
                coffee = int(input("How many cups of Coffee do you want? "))
            
                TOTAL_COFFEE = (coffee * 20) 
                print(f"TOTAL AMOUNT = Ksh.{TOTAL_COFFEE}\n")

            elif HOT_DRINKS_SELECTION == 2:
                #global TOTAL_GREEN_TEA
                green_tea = int(input("How many cups of Green_tea do you want? "))
                
                TOTAL_GREEN_TEA = (green_tea * 50) 
                print(f"TOTAL AMOUNT = Ksh.{TOTAL_GREEN_TEA}\n")

            elif HOT_DRINKS_SELECTION == 3:
                #global TOTAL_HOT_CHOCHOLATE
                hot_chocholate = int(input("How many cups of Hot_chocholate do you want? "))
                
                TOTAL_HOT_CHOCHOLATE = (hot_chocholate * 65) 
                print(f"TOTAL AMOUNT = Ksh.{TOTAL_HOT_CHOCHOLATE}\n")

            elif HOT_DRINKS_SELECTION == 4:
                #global TOTAL_HOT_LEMON_WATER
                hot_lemon_water = int(input("How many cups of Hot_lemon_water do you want? "))
                
                TOTAL_HOT_LEMON_WATER = (hot_lemon_water * 35) 
                print(f"TOTAL AMOUNT = Ksh.{TOTAL_HOT_LEMON_WATER}\n")

            elif HOT_DRINKS_SELECTION == 5:
                #global TOTAL_FRUIT_TEA
                fruit_tea = int(input("How many glasses of Fruit_tea do you want? "))
                
                TOTAL_FRUIT_TEA = (fruit_tea * 58) 
                print(f"TOTAL AMOUNT = Ksh.{TOTAL_FRUIT_TEA}\n")
                

            elif HOT_DRINKS_SELECTION == 00:
                TOTAL_BILL = TOTAL_COFFEE + TOTAL_GREEN_TEA + TOTAL_HOT_CHOCHOLATE + TOTAL_HOT_LEMON_WATER + TOTAL_FRUIT_TEA
                print(f"\nYOUR TOTAL BILL IS Ksh.{TOTAL_BILL}\n")
                break
                
        DELIVERY_Q = input("\tDO YOU WANT YOUR GOODS TO BE DELIVERED? (YES or NO):: ")
        if DELIVERY_Q == "YES":
          
            print("\n\tTHANKYOU FOR CHOOSING OUR DELIVERY SERVICES!!!\n")
            order_type()

            DELIVERY = int(input("SELECT YOUR DELIVERY TYPE(INT):: "))

            if DELIVERY == 1:
                print("\n")
                NORMAL_DELIVERY()

                while True:
                    CHOICE = int(input("\nSelect county choice number to deliver to:(exit='00')  => "))

                    if CHOICE == 1:
                        nairobi = random.randrange(423,442)
                        print(f"DELIVERY PRICE TO NAIROBI IS Ksh.{nairobi}")

                    elif CHOICE == 2:
                        kiambu = random.randrange(583,602)
                        print(f"DELIVERY PRICE TO KIAMBU IS Ksh.{kiambu}")

                    elif CHOICE == 3:
                        kisumu = random.randrange(1228,1241)
                        print(f"DELIVERY PRICE TO KISUMU IS Ksh.{kisumu}") 

                    elif CHOICE == 4:
                        mombasa = random.randrange(1423,1444)
                        print(f"DELIVERY PRICE TO MOMBASA IS Ksh.{mombasa}") 

                    elif CHOICE == 5:
                        siaya = random.randrange(1413,1436)
                        print(f"DELIVERY PRICE TO SIAYA IS Ksh.{siaya}") 

                    elif CHOICE == 00:
                        DELIVERY_TOTAL = nairobi + kisumu +siaya + mombasa + kiambu
                        print(f"\nTOTAL NORMAL DELIVERY PRICE ON SELECTED COUNTIE(S) IS Ksh.{DELIVERY_TOTAL}\n")
                        break

                    # else:
                        # ("Enter the correct option")
#PAYMENT MODULE

                print("\nBELOW IS A PAYMENT METHOD LIST:: ")
                payments()
                payment_method = int(input("SELECT ONE PAYMENT METHOD::"))
                if payment_method == 1:
                    #ENTER AMOUNT
                    #ENTER PIN NUMBER THAT HAS BEEN GENERATED FOR YOU
                    TOTAL_PAYMENTS = DELIVERY_TOTAL + TOTAL_BILL
                    print(f"\nYOU ARE SUPPOSED TO PAY A TOTAL OF Ksh.{TOTAL_PAYMENTS}")
                    ACC_BAL = float(input("HOW MUCH DO YOU HAVE IN YOUR MPESA?"))
                    if ACC_BAL < TOTAL_PAYMENTS:
                        FULIZA_Q = input("YOU HAVE INSUFFICIENT FUNDS, WOULD YOU LIKE TO FULIZA?(YES OR NO)")
                        if FULIZA_Q == "YES":

                            print("\nKINDLY WAIT FOR YOUR MPESA CONFIRMATION MESSAGE.THANKYOU FOR USING OUR SERVICES")
                            MPESA_MESSAGE = open("MPESA","x")
                            MPESA_MESSAGE.write(f"Confirmed. Ksh{TOTAL_PAYMENTS} sent to GOSHEN HOTEL on {current_date} at {current_time}. \nNew M-PESA balance is Ksh.0.0")
                            MPESA_MESSAGE.close()

                            FULIZA_MESSAGE = open("FULIZA","x")
                            FULIZA_MESSAGE.write(f"CONFIRMED. FULIZA MPESA AMOUNT IS Ksh.{TOTAL_PAYMENTS - ACC_BAL}.TOTAL FULIZA MPESA OUTSTANDING BALANCE IS Ksh.{TOTAL_PAYMENTS - ACC_BAL}")

                        if FULIZA_Q =="NO":

                            print("\nTRANSACTION INCOMPLETE DUE TO INSUFFICIENT FUNDS. RECHARGE YOUR ACCOUNT AND TRY AGAIN LATER!!!")
                
                    elif ACC_BAL > TOTAL_PAYMENTS:

                        print("THANKYOU FOR USING OUR SERVICES. KINDLY WAIT FOR YOUR CONFIRMATION MESSAGE")
                        MPESA_MESSAGE = open("MPESA","x")
                        MPESA_MESSAGE.write(f"Confirmed. Ksh{TOTAL_PAYMENTS} sent to GOSHEN HOTEL on {current_date} at {current_time}. \nNew M-PESA balance is Ksh.{ACC_BAL - TOTAL_PAYMENTS}")
                        MPESA_MESSAGE.close()


                elif payment_method == 2:
                    #converts your account balance cash into dollars
                    #enter transaction details
                    # enter paypal pin number
                    TOTAL_PAYMENTS = DELIVERY_TOTAL + TOTAL_BILL
                    print(f"\nYOU ARE SUPPOSED TO PAY A TOTAL OF Ksh.{TOTAL_PAYMENTS}")
                    ACC_BAL = float(input("HOW MUCH DO YOU HAVE IN YOUR PAYPAL ACCOUNT?"))

                    if ACC_BAL < TOTAL_PAYMENTS:

                        print("\nTRANSACTION INCOMPLETE DUE TO INSUFFICIENT FUNDS. RECHARGE YOUR PAYPAL ACCOUNT AND TRY AGAIN LATER!!!")
                
                    elif ACC_BAL > TOTAL_PAYMENTS:

                        print("THANKYOU FOR USING OUR SERVICES. KINDLY WAIT FOR YOUR CONFIRMATION MESSAGE")
                        MPESA_MESSAGE = open("PAYPAL","x")
                        MPESA_MESSAGE.write(f"Confirmed. Ksh{TOTAL_PAYMENTS} sent to GOSHEN HOTEL on {current_date} at {current_time}. \nNew PAYPAL ACCOUNT BALANCE IS Ksh.{ACC_BAL - TOTAL_PAYMENTS}")
                        MPESA_MESSAGE.close() 


            elif DELIVERY == 2:
                print("\n")
                SPECIAL_DELIVERY()


                while True:
                    choice = int(input("\nSelect county choice number to deliver to::(exit='00')  => "))

                    if choice == 1:
                        NAIROBI = 1 * 426 
                        print(f"DELIVERY PRICE TO NAIROBI IS Ksh.{NAIROBI}") #more info to be sent tomorrow

                    elif choice == 2:
                        KIAMBU = 1 * 582
                 
                        print(f"DELIVERY PRICE TO KIAMBU IS Ksh.{KIAMBU}") #more info to be sent tomorrow

                    elif choice == 3:
                        KISUMU = 1 * 1220
                        print(f"DELIVERY PRICE TO KISUMU IS Ksh.{KISUMU}") #more info to be sent tomorrow

                    elif choice == 4:
                        MOMBASA = 1 * 1422
                        print(f"DELIVERY PRICE TO MOMBASA IS Ksh.{MOMBASA}") #more info to be sent tomorrow

                    elif choice == 5:
                        SIAYA = 1 * 1412
                        print(f"DELIVERY PRICE TO SIAYA IS Ksh.{SIAYA}") #more info to be sent tomorrow

                    elif choice == 00:
                        DELIVERY_TOTAL = NAIROBI + KISUMU +SIAYA + MOMBASA + KIAMBU
                        print(f"\nTOTAL SPECIAL DELIVERY PRICE ON SELECTED COUNTIE(S) IS Ksh.{DELIVERY_TOTAL}\n")
                        break
#PAYMENT MODULE

                print("\nBELOW IS A PAYMENT METHOD LIST:: ")
                payments()
                payment_method = int(input("SELECT ONE PAYMENT METHOD::"))
                if payment_method == 1:
                    #ENTER AMOUNT
                    #ENTER PIN NUMBER THAT HAS BEEN GENERATED FOR YOU
                    TOTAL_PAYMENTS = DELIVERY_TOTAL + TOTAL_BILL
                    print(f"\nYOU ARE SUPPOSED TO PAY A TOTAL OF Ksh.{TOTAL_PAYMENTS}")
                    ACC_BAL = float(input("HOW MUCH DO YOU HAVE IN YOUR MPESA?"))
                    if ACC_BAL < TOTAL_PAYMENTS:
                        FULIZA_Q = input("YOU HAVE INSUFFICIENT FUNDS, WOULD YOU LIKE TO FULIZA?(YES OR NO)")
                        if FULIZA_Q == "YES":

                            print("\nKINDLY WAIT FOR YOUR MPESA CONFIRMATION MESSAGE.THANKYOU FOR USING OUR SERVICES")
                            MPESA_MESSAGE = open("MPESA","x")
                            MPESA_MESSAGE.write(f"Confirmed. Ksh{TOTAL_PAYMENTS} sent to GOSHEN HOTEL on {current_date} at {current_time}. \nNew M-PESA balance is Ksh.0.0")
                            MPESA_MESSAGE.close()

                            FULIZA_MESSAGE = open("FULIZA","x")
                            FULIZA_MESSAGE.write(f"CONFIRMED. FULIZA MPESA AMOUNT IS Ksh.{TOTAL_PAYMENTS - ACC_BAL}.TOTAL FULIZA MPESA OUTSTANDING BALANCE IS Ksh.{TOTAL_PAYMENTS - ACC_BAL}")

                        if FULIZA_Q =="NO":

                            print("\nTRANSACTION INCOMPLETE DUE TO INSUFFICIENT FUNDS. RECHARGE YOUR ACCOUNT AND TRY AGAIN LATER!!!")
                
                    elif ACC_BAL > TOTAL_PAYMENTS:

                        print("THANKYOU FOR USING OUR SERVICES. KINDLY WAIT FOR YOUR CONFIRMATION MESSAGE")
                        MPESA_MESSAGE = open("MPESA","x")
                        MPESA_MESSAGE.write(f"Confirmed. Ksh{TOTAL_PAYMENTS} sent to GOSHEN HOTEL on {current_date} at {current_time}. \nNew M-PESA balance is Ksh.{ACC_BAL - TOTAL_PAYMENTS}")
                        MPESA_MESSAGE.close()


                elif payment_method == 2:
                    #converts your account balance cash into dollars
                    #enter transaction details
                    # enter paypal pin number
                    TOTAL_PAYMENTS = DELIVERY_TOTAL + TOTAL_BILL
                    print(f"\nYOU ARE SUPPOSED TO PAY A TOTAL OF Ksh.{TOTAL_PAYMENTS}")
                    ACC_BAL = float(input("HOW MUCH DO YOU HAVE IN YOUR PAYPAL ACCOUNT?"))

                    if ACC_BAL < TOTAL_PAYMENTS:

                        print("\nTRANSACTION INCOMPLETE DUE TO INSUFFICIENT FUNDS. RECHARGE YOUR PAYPAL ACCOUNT AND TRY AGAIN LATER!!!")
                
                    elif ACC_BAL > TOTAL_PAYMENTS:

                        print("THANKYOU FOR USING OUR SERVICES. KINDLY WAIT FOR YOUR CONFIRMATION MESSAGE")
                        MPESA_MESSAGE = open("PAYPAL","x")
                        MPESA_MESSAGE.write(f"Confirmed. Ksh{TOTAL_PAYMENTS} sent to GOSHEN HOTEL on {current_date} at {current_time}. \nNew PAYPAL ACCOUNT BALANCE IS Ksh.{ACC_BAL - TOTAL_PAYMENTS}")
                        MPESA_MESSAGE.close() 

                    # else:
                        # ("Enter the correct option")

        elif DELIVERY_Q == "NO":
            print("CONTINUE WITH THE NORMAL PAYMENTS")
            print("\nBELOW IS A PAYMENT METHOD LIST:: ")
            payments()
            payment_method = int(input("SELECT ONE PAYMENT METHOD::"))
            if payment_method == 1:
                #ENTER AMOUNT
                #ENTER PIN NUMBER THAT HAS BEEN GENERATED FOR YOU
                TOTAL_PAYMENTS = TOTAL_BILL
                print(f"\nYOU ARE SUPPOSED TO PAY A TOTAL OF Ksh.{TOTAL_PAYMENTS}")
                ACC_BAL = float(input("HOW MUCH DO YOU HAVE IN YOUR MPESA?"))
                if ACC_BAL < TOTAL_PAYMENTS:
                    FULIZA_Q = input("YOU HAVE INSUFFICIENT FUNDS, WOULD YOU LIKE TO FULIZA?(YES OR NO)")
                    if FULIZA_Q == "YES":

                        print("\nKINDLY WAIT FOR YOUR MPESA CONFIRMATION MESSAGE.THANKYOU FOR USING OUR SERVICES")
                        MPESA_MESSAGE = open("MPESA","x")
                        MPESA_MESSAGE.write(f"Confirmed. Ksh{TOTAL_PAYMENTS} sent to GOSHEN HOTEL on {current_date} at {current_time}. \nNew M-PESA balance is Ksh.0.0")
                        MPESA_MESSAGE.close()

                        FULIZA_MESSAGE = open("FULIZA","x")
                        FULIZA_MESSAGE.write(f"CONFIRMED. FULIZA MPESA AMOUNT IS Ksh.{TOTAL_PAYMENTS - ACC_BAL}.TOTAL FULIZA MPESA OUTSTANDING BALANCE IS Ksh.{TOTAL_PAYMENTS - ACC_BAL}")

                    if FULIZA_Q =="NO":

                        print("\nTRANSACTION INCOMPLETE DUE TO INSUFFICIENT FUNDS. RECHARGE YOUR ACCOUNT AND TRY AGAIN LATER!!!")
                
                elif ACC_BAL > TOTAL_PAYMENTS:

                        print("THANKYOU FOR USING OUR SERVICES. KINDLY WAIT FOR YOUR CONFIRMATION MESSAGE")
                        MPESA_MESSAGE = open("MPESA","x")
                        MPESA_MESSAGE.write(f"Confirmed. Ksh{TOTAL_PAYMENTS} sent to GOSHEN HOTEL on {current_date} at {current_time}. \nNew M-PESA balance is Ksh.{ACC_BAL - TOTAL_PAYMENTS}")
                        MPESA_MESSAGE.close()


            elif payment_method == 2:
                #converts your account balance cash into dollars
                #enter transaction details
                # enter paypal pin number
                TOTAL_PAYMENTS = TOTAL_BILL
                print(f"\nYOU ARE SUPPOSED TO PAY A TOTAL OF Ksh.{TOTAL_PAYMENTS}")
                ACC_BAL = float(input("HOW MUCH DO YOU HAVE IN YOUR PAYPAL ACCOUNT?"))

                if ACC_BAL < TOTAL_PAYMENTS:

                    print("\nTRANSACTION INCOMPLETE DUE TO INSUFFICIENT FUNDS. RECHARGE YOUR PAYPAL ACCOUNT AND TRY AGAIN LATER!!!")
                
                elif ACC_BAL > TOTAL_PAYMENTS:

                        print("THANKYOU FOR USING OUR SERVICES. KINDLY WAIT FOR YOUR CONFIRMATION MESSAGE")
                        MPESA_MESSAGE = open("PAYPAL","x")
                        MPESA_MESSAGE.write(f"Confirmed. Ksh{TOTAL_PAYMENTS} sent to GOSHEN HOTEL on {current_date} at {current_time}. \nNew PAYPAL ACCOUNT BALANCE IS Ksh.{ACC_BAL - TOTAL_PAYMENTS}")
                        MPESA_MESSAGE.close() 
#######################################################

    elif DRINKS_SELECTION == 2:
        

        from MAIN_MENU import drinks_colddrinks
        print("\n")
        drinks_colddrinks()
        print("\n")

        while True:

        
            COLD_DRINKS_SELECTION = int(input("SELECT THE COLD DRINK(S) THAT YOU WANT?(EXIT = 00):: "))

            if COLD_DRINKS_SELECTION == 1:
            #global TOTAL_SODA
                soda = int(input("How many bottles of Soda do you want? "))
            
                TOTAL_SODA = (soda * 40) 
                print(f"TOTAL AMOUNT = Ksh.{TOTAL_SODA}\n")

            elif COLD_DRINKS_SELECTION == 2:
            #global TOTAL_FLAVORED_WATER
                flavored_water = int(input("How many bottles of Flavored_water do you want? "))
            
                TOTAL_FLAVORED_WATER = (flavored_water * 65) 
                print(f"TOTAL AMOUNT = Ksh.{TOTAL_FLAVORED_WATER}\n")


            elif COLD_DRINKS_SELECTION == 3:
            #global TOTAL_FRUIT_JUICE
                fruit_juice = int(input("How many glasses of Fruit_juice do you want? "))
            
                TOTAL_FRUIT_JUICE = (fruit_juice * 75) 
                print(f"TOTAL AMOUNT = Ksh.{TOTAL_FRUIT_JUICE}\n")

            elif COLD_DRINKS_SELECTION == 4:
            #global TOTAL_FRUIT_WINE
                fruit_wine = int(input("How many bottles of Fruit_wine do you want? "))
            
                TOTAL_FRUIT_WINE = (fruit_wine * 250) 
                print(f"TOTAL AMOUNT = Ksh.{TOTAL_FRUIT_WINE}\n")

            elif COLD_DRINKS_SELECTION == 5:
            #global TOTAL_ICE_COFFEE
                ice_coffee = int(input("How many cups of Ice_coffee do you want? "))
            
                TOTAL_ICE_COFFEE = (ice_coffee * 120) 
                print(f"TOTAL AMOUNT = Ksh.{TOTAL_ICE_COFFEE}\n")

            elif COLD_DRINKS_SELECTION == 6:
            #global TOTAL_ICE_TEA
                ice_tea = int(input("How many cups of Ice_tea do you want? "))
            
                TOTAL_ICE_TEA = (ice_tea * 80)
                print(f"TOTAL AMOUNT = Ksh.{TOTAL_ICE_TEA}\n")

            elif COLD_DRINKS_SELECTION == 00:
                TOTAL_BILL = TOTAL_SODA + TOTAL_FLAVORED_WATER + TOTAL_FRUIT_JUICE + TOTAL_FRUIT_WINE + TOTAL_ICE_COFFEE + TOTAL_ICE_TEA
                print(f"\nYOUR TOTAL BILL IS Ksh.{TOTAL_BILL}\n")
                break

        DELIVERY_Q = input("\tDO YOU WANT YOUR GOODS TO BE DELIVERED? (YES or NO):: ")
        if DELIVERY_Q == "YES":
          
            print("\n\tTHANKYOU FOR CHOOSING OUR DELIVERY SERVICES!!!\n")
            order_type()

            DELIVERY = int(input("SELECT YOUR DELIVERY TYPE(INT):: "))

            if DELIVERY == 1:
                print("\n")
                NORMAL_DELIVERY()

                while True:
                    CHOICE = int(input("\nSelect county choice number to deliver to:(exit='00')  => "))

                    if CHOICE == 1:
                        nairobi = random.randrange(423,442)
                        print(f"DELIVERY PRICE TO NAIROBI IS Ksh.{nairobi}")

                    elif CHOICE == 2:
                        kiambu = random.randrange(583,602)
                        print(f"DELIVERY PRICE TO KIAMBU IS Ksh.{kiambu}")

                    elif CHOICE == 3:
                        kisumu = random.randrange(1228,1241)
                        print(f"DELIVERY PRICE TO KISUMU IS Ksh.{kisumu}") 

                    elif CHOICE == 4:
                        mombasa = random.randrange(1423,1444)
                        print(f"DELIVERY PRICE TO MOMBASA IS Ksh.{mombasa}") 

                    elif CHOICE == 5:
                        siaya = random.randrange(1413,1436)
                        print(f"DELIVERY PRICE TO SIAYA IS Ksh.{siaya}") 

                    elif CHOICE == 00:
                        DELIVERY_TOTAL = nairobi + kisumu +siaya + mombasa + kiambu
                        print(f"\nTOTAL NORMAL DELIVERY PRICE ON SELECTED COUNTIE(S) IS Ksh.{DELIVERY_TOTAL}\n")
                        break

                    # else:
                        # ("Enter the correct option")
#PAYMENT MODULE

            print("\nBELOW IS A PAYMENT METHOD LIST:: ")
            payments()
            payment_method = int(input("SELECT ONE PAYMENT METHOD::"))
            if payment_method == 1:
                #ENTER AMOUNT
                #ENTER PIN NUMBER THAT HAS BEEN GENERATED FOR YOU
                TOTAL_PAYMENTS = DELIVERY_TOTAL + TOTAL_BILL
                print(f"\nYOU ARE SUPPOSED TO PAY A TOTAL OF Ksh.{TOTAL_PAYMENTS}")
                ACC_BAL = float(input("HOW MUCH DO YOU HAVE IN YOUR MPESA?"))
                if ACC_BAL < TOTAL_PAYMENTS:
                    FULIZA_Q = input("YOU HAVE INSUFFICIENT FUNDS, WOULD YOU LIKE TO FULIZA?(YES OR NO)")
                    if FULIZA_Q == "YES":

                        print("\nKINDLY WAIT FOR YOUR MPESA CONFIRMATION MESSAGE.THANKYOU FOR USING OUR SERVICES")
                        MPESA_MESSAGE = open("MPESA","x")
                        MPESA_MESSAGE.write(f"Confirmed. Ksh{TOTAL_PAYMENTS} sent to GOSHEN HOTEL on {current_date} at {current_time}. \nNew M-PESA balance is Ksh.0.0")
                        MPESA_MESSAGE.close()

                        FULIZA_MESSAGE = open("FULIZA","x")
                        FULIZA_MESSAGE.write(f"CONFIRMED. FULIZA MPESA AMOUNT IS Ksh.{TOTAL_PAYMENTS - ACC_BAL}.TOTAL FULIZA MPESA OUTSTANDING BALANCE IS Ksh.{TOTAL_PAYMENTS - ACC_BAL}")

                    if FULIZA_Q =="NO":

                        print("\nTRANSACTION INCOMPLETE DUE TO INSUFFICIENT FUNDS. RECHARGE YOUR ACCOUNT AND TRY AGAIN LATER!!!")
                
                elif ACC_BAL > TOTAL_PAYMENTS:

                        print("THANKYOU FOR USING OUR SERVICES. KINDLY WAIT FOR YOUR CONFIRMATION MESSAGE")
                        MPESA_MESSAGE = open("MPESA","x")
                        MPESA_MESSAGE.write(f"Confirmed. Ksh{TOTAL_PAYMENTS} sent to GOSHEN HOTEL on {current_date} at {current_time}. \nNew M-PESA balance is Ksh.{ACC_BAL - TOTAL_PAYMENTS}")
                        MPESA_MESSAGE.close()


            elif payment_method == 2:
                #converts your account balance cash into dollars
                #enter transaction details
                # enter paypal pin number
                TOTAL_PAYMENTS = DELIVERY_TOTAL + TOTAL_BILL
                print(f"\nYOU ARE SUPPOSED TO PAY A TOTAL OF Ksh.{TOTAL_PAYMENTS}")
                ACC_BAL = float(input("HOW MUCH DO YOU HAVE IN YOUR PAYPAL ACCOUNT?"))

                if ACC_BAL < TOTAL_PAYMENTS:

                    print("\nTRANSACTION INCOMPLETE DUE TO INSUFFICIENT FUNDS. RECHARGE YOUR PAYPAL ACCOUNT AND TRY AGAIN LATER!!!")
                
                elif ACC_BAL > TOTAL_PAYMENTS:

                        print("THANKYOU FOR USING OUR SERVICES. KINDLY WAIT FOR YOUR CONFIRMATION MESSAGE")
                        MPESA_MESSAGE = open("PAYPAL","x")
                        MPESA_MESSAGE.write(f"Confirmed. Ksh{TOTAL_PAYMENTS} sent to GOSHEN HOTEL on {current_date} at {current_time}. \nNew PAYPAL ACCOUNT BALANCE IS Ksh.{ACC_BAL - TOTAL_PAYMENTS}")
                        MPESA_MESSAGE.close() 


            elif DELIVERY == 2:
                print("\n")
                SPECIAL_DELIVERY()


                while not DELIVERY in AVAILABLE_COUNTIES:
                    choice = int(input("\nSelect county choice number to deliver to::(exit='00')  => "))

                    if choice == 1:
                        NAIROBI = 1 * 426 
                        print(f"DELIVERY PRICE TO NAIROBI IS Ksh.{NAIROBI}") #more info to be sent tomorrow

                    elif choice == 2:
                        KIAMBU = 1 * 582
                 
                        print(f"DELIVERY PRICE TO KIAMBU IS Ksh.{KIAMBU}") #more info to be sent tomorrow

                    elif choice == 3:
                        KISUMU = 1 * 1220
                        print(f"DELIVERY PRICE TO KISUMU IS Ksh.{KISUMU}") #more info to be sent tomorrow

                    elif choice == 4:
                        MOMBASA = 1 * 1422
                        print(f"DELIVERY PRICE TO MOMBASA IS Ksh.{MOMBASA}") #more info to be sent tomorrow

                    elif choice == 5:
                        SIAYA = 1 * 1412
                        print(f"DELIVERY PRICE TO SIAYA IS Ksh.{SIAYA}") #more info to be sent tomorrow

                    elif choice == 00:
                        DELIVERY_TOTAL = NAIROBI + KISUMU +SIAYA + MOMBASA + KIAMBU
                        print(f"\nTOTAL SPECIAL DELIVERY PRICE ON SELECTED COUNTIE(S) IS Ksh.{DELIVERY_TOTAL}\n")
                        break

                    # else:
                        # ("Enter the correct option")
#######################################################
    #PAYMENT MODULE

                print("\nBELOW IS A PAYMENT METHOD LIST:: ")
                payments()
                payment_method = int(input("SELECT ONE PAYMENT METHOD::"))
                if payment_method == 1:
                    #ENTER AMOUNT
                    #ENTER PIN NUMBER THAT HAS BEEN GENERATED FOR YOU
                    TOTAL_PAYMENTS = DELIVERY_TOTAL + TOTAL_BILL
                    print(f"\nYOU ARE SUPPOSED TO PAY A TOTAL OF Ksh.{TOTAL_PAYMENTS}")
                    ACC_BAL = float(input("HOW MUCH DO YOU HAVE IN YOUR MPESA?"))
                    if ACC_BAL < TOTAL_PAYMENTS:
                        FULIZA_Q = input("YOU HAVE INSUFFICIENT FUNDS, WOULD YOU LIKE TO FULIZA?(YES OR NO)")
                        if FULIZA_Q == "YES":

                            print("\nKINDLY WAIT FOR YOUR MPESA CONFIRMATION MESSAGE.THANKYOU FOR USING OUR SERVICES")
                            MPESA_MESSAGE = open("MPESA","x")
                            MPESA_MESSAGE.write(f"Confirmed. Ksh{TOTAL_PAYMENTS} sent to GOSHEN HOTEL on {current_date} at {current_time}. \nNew M-PESA balance is Ksh.0.0")
                            MPESA_MESSAGE.close()

                            FULIZA_MESSAGE = open("FULIZA","x")
                            FULIZA_MESSAGE.write(f"CONFIRMED. FULIZA MPESA AMOUNT IS Ksh.{TOTAL_PAYMENTS - ACC_BAL}.TOTAL FULIZA MPESA OUTSTANDING BALANCE IS Ksh.{TOTAL_PAYMENTS - ACC_BAL}")

                        if FULIZA_Q =="NO":

                            print("\nTRANSACTION INCOMPLETE DUE TO INSUFFICIENT FUNDS. RECHARGE YOUR ACCOUNT AND TRY AGAIN LATER!!!")
                
                    elif ACC_BAL > TOTAL_PAYMENTS:

                        print("THANKYOU FOR USING OUR SERVICES. KINDLY WAIT FOR YOUR CONFIRMATION MESSAGE")
                        MPESA_MESSAGE = open("MPESA","x")
                        MPESA_MESSAGE.write(f"Confirmed. Ksh{TOTAL_PAYMENTS} sent to GOSHEN HOTEL on {current_date} at {current_time}. \nNew M-PESA balance is Ksh.{ACC_BAL - TOTAL_PAYMENTS}")
                        MPESA_MESSAGE.close()


                elif payment_method == 2:
                    #converts your account balance cash into dollars
                    #enter transaction details
                    # enter paypal pin number
                    TOTAL_PAYMENTS = DELIVERY_TOTAL + TOTAL_BILL
                    print(f"\nYOU ARE SUPPOSED TO PAY A TOTAL OF Ksh.{TOTAL_PAYMENTS}")
                    ACC_BAL = float(input("HOW MUCH DO YOU HAVE IN YOUR PAYPAL ACCOUNT?"))

                    if ACC_BAL < TOTAL_PAYMENTS:

                        print("\nTRANSACTION INCOMPLETE DUE TO INSUFFICIENT FUNDS. RECHARGE YOUR PAYPAL ACCOUNT AND TRY AGAIN LATER!!!")
                
                    elif ACC_BAL > TOTAL_PAYMENTS:

                        print("THANKYOU FOR USING OUR SERVICES. KINDLY WAIT FOR YOUR CONFIRMATION MESSAGE")
                        MPESA_MESSAGE = open("PAYPAL","x")
                        MPESA_MESSAGE.write(f"Confirmed. Ksh{TOTAL_PAYMENTS} sent to GOSHEN HOTEL on {current_date} at {current_time}. \nNew PAYPAL ACCOUNT BALANCE IS Ksh.{ACC_BAL - TOTAL_PAYMENTS}")
                        MPESA_MESSAGE.close() 

        elif DELIVERY_Q == "NO":
            print("CONTINUE WITH THE NORMAL PAYMENTS")
            print("\nBELOW IS A PAYMENT METHOD LIST:: ")
            payments()
            payment_method = int(input("SELECT ONE PAYMENT METHOD::"))
            if payment_method == 1:
                #ENTER AMOUNT
                #ENTER PIN NUMBER THAT HAS BEEN GENERATED FOR YOU
                TOTAL_PAYMENTS = TOTAL_BILL
                print(f"\nYOU ARE SUPPOSED TO PAY A TOTAL OF Ksh.{TOTAL_PAYMENTS}")
                ACC_BAL = float(input("HOW MUCH DO YOU HAVE IN YOUR MPESA?"))
                if ACC_BAL < TOTAL_PAYMENTS:
                    FULIZA_Q = input("YOU HAVE INSUFFICIENT FUNDS, WOULD YOU LIKE TO FULIZA?(YES OR NO)")
                    if FULIZA_Q == "YES":

                        print("\nKINDLY WAIT FOR YOUR MPESA CONFIRMATION MESSAGE.THANKYOU FOR USING OUR SERVICES")
                        MPESA_MESSAGE = open("MPESA","x")
                        MPESA_MESSAGE.write(f"Confirmed. Ksh{TOTAL_PAYMENTS} sent to GOSHEN HOTEL on {current_date} at {current_time}. \nNew M-PESA balance is Ksh.0.0")
                        MPESA_MESSAGE.close()

                        FULIZA_MESSAGE = open("FULIZA","x")
                        FULIZA_MESSAGE.write(f"CONFIRMED. FULIZA MPESA AMOUNT IS Ksh.{TOTAL_PAYMENTS - ACC_BAL}.TOTAL FULIZA MPESA OUTSTANDING BALANCE IS Ksh.{TOTAL_PAYMENTS - ACC_BAL}")

                    if FULIZA_Q =="NO":

                        print("\nTRANSACTION INCOMPLETE DUE TO INSUFFICIENT FUNDS. RECHARGE YOUR ACCOUNT AND TRY AGAIN LATER!!!")
                
                elif ACC_BAL > TOTAL_PAYMENTS:

                        print("THANKYOU FOR USING OUR SERVICES. KINDLY WAIT FOR YOUR CONFIRMATION MESSAGE")
                        MPESA_MESSAGE = open("MPESA","x")
                        MPESA_MESSAGE.write(f"Confirmed. Ksh{TOTAL_PAYMENTS} sent to GOSHEN HOTEL on {current_date} at {current_time}. \nNew M-PESA balance is Ksh.{ACC_BAL - TOTAL_PAYMENTS}")
                        MPESA_MESSAGE.close()


            elif payment_method == 2:
                #converts your account balance cash into dollars
                #enter transaction details
                # enter paypal pin number
                TOTAL_PAYMENTS = TOTAL_BILL
                print(f"\nYOU ARE SUPPOSED TO PAY A TOTAL OF Ksh.{TOTAL_PAYMENTS}")
                ACC_BAL = float(input("HOW MUCH DO YOU HAVE IN YOUR PAYPAL ACCOUNT?"))

                if ACC_BAL < TOTAL_PAYMENTS:

                    print("\nTRANSACTION INCOMPLETE DUE TO INSUFFICIENT FUNDS. RECHARGE YOUR PAYPAL ACCOUNT AND TRY AGAIN LATER!!!")
                
                elif ACC_BAL > TOTAL_PAYMENTS:

                        print("THANKYOU FOR USING OUR SERVICES. KINDLY WAIT FOR YOUR CONFIRMATION MESSAGE")
                        MPESA_MESSAGE = open("PAYPAL","x")
                        MPESA_MESSAGE.write(f"Confirmed. Ksh{TOTAL_PAYMENTS} sent to GOSHEN HOTEL on {current_date} at {current_time}. \nNew PAYPAL ACCOUNT BALANCE IS Ksh.{ACC_BAL - TOTAL_PAYMENTS}")
                        MPESA_MESSAGE.close()
    
else:
    print("ENTER THE CORRECT OPTION NUMBER!!!")
