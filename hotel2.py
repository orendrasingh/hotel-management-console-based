global amt # total bill
global rec
amt=100
rec=[]  #for printing bill
def detail():
    print()
def _():
        a = [77, 97, 100, 101, 32, 98, 121, 32, 58, 45, 45, 79, 36, 45, 45]
        print("-" * 20, end="")
        for x in range(len(a)):
            print(chr(a[x]), end="")
        print("-" * 20)

def slp():
    import time
    import sys
    s = '.'
    print("\n","\n","\n","\n",)
    sys.stdout.write( '              \033[1;33mPlease wait While \033[1;37;40m loading       ' )
    for i in range(3):
            sys.stdout.write( s )
            sys.stdout.flush()
            time.sleep(0.4)
    print("\r")
def room(a): # for room type
    global amt
    global rec
    print("We have different types of rooms as per there services..")
    print("-" * 60)
    print("1. Room  with AC cost = 1500")
    print('\r')
    print("2. Non - AC Room cost = 800")
    print("-" * 60)
    b = int(input("Enter the choice = "))
    print("_" * 60)
    if (b == 1):
        print(" You have selected Ac room ")
        print("You have assigned room no = 48")
        print("=" * 60)
        amt = amt + 1500
        rec.append(" Room  with AC cost = 1500")
        b = input("Would you like to order something to eat.(Y/N)")
        if (b == 'yes' or b == 'Yes' or b == 'Y' or b == 'y'):
            c = catg()
            if (c == 1):
                veg()
            elif (c == 2):
                nonv()
            elif (c == 3):
                bread()
        else:
                bill()
                quit()

    elif (b == 2):
        print("You have selected Non-Ac Room")
        print("You have assigned room no = 47")
        print("=" * 60)
        amt = amt + 800
        rec.append(" Non - AC Room cost = 800")
        b = input("Would you like to order something to eat.(Y/N)")
        if (b == 'yes' or b == 'Yes' or b == 'Y' or b == 'y'):
            c = catg()
            if (c == 1):
                veg()
            elif (c == 2):
                nonv()
            elif (c == 3):
                bread()
        else:
                bill()
                quit()
    else:
        print("Wrong input")
        room(a)
def bill():  #definition of bill
    global rec
    global amt
    print('\r')
    print('\r')
    print("=" * 60)
    print("*"*27,"BILL","*"*27)
    print("-"*60)
    print("******* You have added following items in your bill *********")
    print("-"*60)
    print('\r')
    print(*rec, sep='\n')
    print(" Services charge - 100")
    print("\r")

    print("-"*60)
    print(" Total bill amount is = ",amt)
    print("-" * 60)
    print("*"*5,"| Thankyou kindly, visit again |","*"*5)
    print("-" * 60)
    _()
    print("=" * 60)
    print("\r")
    print('\r')
    print("How would you like to pay select from the following options:")
    print("-"*60)
    print("1. Paytm")
    print("2. Internet Banking")
    print("-"*60)
    c=int(input("Select the options shown above"))
    if (c==1):
        print("*"*60)
        print("Enter you paytm number")
        p=int(input(""))
        print("-"*60)
        o=int(input("Enter Otp"))
        print("You have successfully Paid = Rs.",amt)
    elif(c==2):
        print("*"*60)
        user=input("Enter your username.")
        pas=input("Enter your password")
        print('-'*60)
        print("You have successfully debited = Rs.",amt)

def chs(list,list2,list3): #funtion for adding more items in your bill
    global rec
    global amt
    while True:
        k = input("Do you want to add more items?..")
        print("-"*60)
        if (k == 'yes' or k == 'y' or k == 'Y'):
            a = int(input("Enter the Choice"))
            print("-"*60)
            print("You have added ", list[a])
            print("\r")
            amt = list2[a] + amt
            rec.append(list3[a])
        elif (k == 'no' or k == 'no' or k == 'n'):
            ch = input("Do you want to add more items from anoter category??..")
            if (ch == 'yes' or ch == 'y' or ch == 'Yes'):
                j = catg()
                if (j == 1):
                    veg()
                elif (j == 2):
                    nonv()
                elif (j == 3):
                    bread()
            else:
                bill()
                quit()
        else:
            bill()
            quit()

def catg():  # for showing categories
    print("Select Type of food.")
    print("_"*60)
    print("1. Veg Food.")
    print('\r')
    print("2. Non-Veg Food.")
    print('\r')
    print("3. Indian Bread.")
    print('\r')
    a=int(input("Select your choice.."))
    return a
def home(): # for showing menu content

    print('\033[1;34m')
    print("-"*60)
    print('             Welcome to the Skylines Hotel')
    print("-"*60)
    print('\r','\033[1;0m')
    print('Select the services you would like to have!..')
    print('\r','\033[1;31m')
    print("1. Room service")
    print('\r')
    print("2. Have something to eat?.. ")
    print('\r','\033[1;0m')
    print("-"*60)
    a=int(input("Enter your choice = "))
    return a
def nonv(): # for non veg list
    global amt
    global rec
    print("Select Items from Non-Veg. Category")
    print("_" * 60)
    list=["  |---Non Veg---|","1. Chicken Fry - 150rs. per plate.","2. Squid Fry - 180rs. per plate.","3. Chicken Biryani  - 140rs. per plate.","4. Hyderabadi Chicken Biryani - 130rs. per plate.",
          "5. Chicken-Tikka - 170rs. per plate.","6. Butter-Chicken - 190rs. per plate."]
    list3 = ["  |---Non Veg---|", " Chicken Fry - 150rs. per plate.", " Squid Fry - 180rs. per plate.",
            " Chicken Biryani  - 140rs. per plate.", " Hyderabadi Chicken Biryani - 130rs. per plate.",
            " Chicken-Tikka - 170rs. per plate.", " Butter-Chicken - 190rs. per plate."]
    print(*list, sep='\n')
    print("_" * 60)
    list2 = [" ", 150, 180, 140, 130,
           170, 190]
    a = int(input("Enter the Choice"))
    print("-"*60)
    print("You have added ", list[a])
    print("-")
    amt = list2[a] + amt
    rec.append(list3[a])
    chs(list,list2,list3)
def veg(): # for veg content
    global rec
    global amt
    print("Select Items from Veg. Category")
    print("_"*60)
    list = ["  |---Veg---| ","1. Dal Fry - 70rs. per plate.", "2. Paneer Tikka - 80rs. per plate.", "3. Sahi Paneer - 90rs. per plate.", "4. Chole Bhature - 45rs. per plate.", "5. Spcl Mix - 60rs. per plate.",
            "6. Kadi Chawal - 120rs. per plate."]
    list3 = ["  |---Veg---| ", " Dal Fry - 70rs. per plate.", " Paneer Tikka - 80rs. per plate.", " Sahi Paneer - 90rs. per plate.", " Chole Bhature - 45rs. per plate.", " Spcl Mix - 60rs. per plate.",
            " Kadi Chawal - 120rs. per plate."]
    print(*list, sep='\n')
    print("_" * 60)
    list2 = [0,70,80,90,45,60,120]
    a=int(input("Enter the Choice"))
    print("-"*60)
    print("You have added ",list[a])
    print("-")
    amt=list2[a]+amt
    rec.append(list3[a])
    chs(list,list2,list3)
def bread(): # for bread types content
    global rec
    global amt
    print("Select Bread & Rice Types.")
    print("_"*60)
    list = ["  |---Indian Bread---|","1. Lachaa parantha - 8rs. per pc.", "2. Bhature - 7rs. per pc.", "3. Roti 5rs. per pc.", "4. Rumali roti 25rs per pc.", "5. Rice 45rs. per 200gm ",
            "6. Fried Rice 80rs. per 200gm"]
    list3 = ["  |---Indian Bread---|", " Lachaa parantha - 8rs. per pc.", " Bhature - 7rs. per pc.",
            " Roti 5rs. per pc.", " Rumali roti 25rs per pc.", " Rice 45rs. per 200gm ",
            " Fried Rice 80rs. per 200gm"]
    print(*list, sep='\n')
    list2 = [" ", 8, 7,5, 25, 45,
            80]
    print("_" * 60)
    a = int(input("Enter the Choice"))
    print("-"*60)
    print("You have added ", list[a])
    print("-")
    amt = list2[a] + amt
    rec.append(list3[a])
    chs(list,list2,list3)

# Starting of execution
while True:
    slp()
    a=home()
    if (a == 1):
        room(a)
    elif(a==2):
        c=catg()
        if(c==1):
            veg()
        elif(c==2):
            nonv()
        elif(c==3):
            bread()
    else:
        print(" !!!!!wrong input!!!!!")


