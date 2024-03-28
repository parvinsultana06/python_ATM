from cardHolder import cardHolder

def print_menu():
     #==========Print options of the user=====
    print("Please choose from one of the following options........")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Show Balance")
    print("4. Exit")
    
def deposit(cardHolder):
    try:
        deposit = float(input("How much money would you like to deposit: "))
        cardHolder.set_balance(cardHolder.get_balance()+ deposit)
        print("Thank you for your $$. Your new balance is: ", str(cardHolder.get_balance()))
    except:
        print("Invalid input")
        

def withdraw(cardHolder):
    try:
        withdraw = float(input("How much  money would you like to Withdraw: "))
        #========= Check if user has enough mouny===========
        
        if(cardHolder.get_balance() < withdraw):
            print("Insufficient balance:(")
        else:
            cardHolder.set_balance(cardHolder.get_balance() - withdraw)
            print("You're good to go! Thank you:) ")
    except:
        print("Invalid input")
        
def chack_balance(cardHolder):
    print("Your current balance is:", cardHolder.get_balance())
    
    
if __name__ == "__main__":
    Current_user = cardHolder("","","","","")
    
    
    #=============== Create a repo of cardHolders
    list_of_cardHolders = []
    list_of_cardHolders.append(cardHolder("456321789",1234,"jhon","Sekh",150.31))
    list_of_cardHolders.append(cardHolder("456321780",1235,"Riya","Das",145.11))
    list_of_cardHolders.append(cardHolder("456321781",1334,"Munib","Kumar",156.01))
    list_of_cardHolders.append(cardHolder("456321782",1235,"Frida","Roy",250.21))
    list_of_cardHolders.append(cardHolder("456321783",1244,"Nic","Jons",170.51))
    
    
    #========Promt user for debit card number==================
    debitCardNum =""
    while True:
        try:
            debitCardNum = input("Please insert your debit card:")
            #========= Check again repo
            debitMatch = [holder for holder in list_of_cardHolders if holder.cardNum == debitCardNum]
            if(len(debitMatch) > 0):
                current_user = debitMatch[0]
                break
            else:
                 print("Card number not recognized . Please try again later..")
        except:
            print("Card number not recognized . Please try again later..")  
            
    #====================== Prompt for pin========
    
    
    while True:
        try:
            userPin = int(input(" Please enter your pin:".strip()))
            if(current_user.get_pin() == userPin):
                break
            else:
                 print("Invalid PIN. Please try again...") 
        except:
            print("Invalid PIN. Please try again...")  
            
    #====== Print options===========
    
    print("Welcome", current_user.get_firstname()," :)")
    option = 0
    while (True):
        print_menu()
        try:
            option= int(input())
        except:
            print("Invalid input. Please try again.")
        
        if(option == 1):
            deposit(current_user)
        elif(option == 2):
            withdraw(current_user)
        elif(option == 3):
            chack_balance(current_user)
        elif(option == 4):
            break
        else:
            option = 0
    print("Thank you. Have a nice day. :)")    
        