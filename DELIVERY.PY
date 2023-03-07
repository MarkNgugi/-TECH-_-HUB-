import random    
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

        else:
            ("Enter the correct option")

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

        else:
            ("Enter the correct option")





