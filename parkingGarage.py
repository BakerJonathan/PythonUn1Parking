#Jonathan Baker
#Parking garage prompt
#Make a 3 funtion 3 attribute parking garage using object oriented programming

class parkingGarage():

    def __init__(self, tickMax=20, parkMax=20):
        self.tickets=[tickMax] #Feel like for this itteration it makes more sense for these to be ints?
        self.parkingSpaces=[parkMax] #Once the specific parking space matters, parking space should be a list though
        #Since it calls for a list, I'll make it a list (though I'm using it as an int here)
        self.currentTicket={"paid":False}#For that matter I'm using this as a bool, until we care about other tickets

    def takeTicket(self):
        if self.tickets[0]>0 and self.parkingSpaces[0]>0:
            self.tickets[0]-=1
            self.parkingSpaces[0]-=1
            print('Here is your ticket')
        else: #Clause so we don't hand out what's not available
            print("There's not enough tickets or parking spots")

    def payForParking(self):
        payment=input("Enter your payment here: ")
        if payment!="":
            print("Your ticket has been paid. You have 15 minutes to leave.")
            self.currentTicket["paid"]=True
        else:
            print("Move along if you're not here to pay for your ticket.")


    def leaveGarage(self):
        #Decided I wanted a while loop, as one could keep not paying, while payment untrue
        while self.currentTicket["paid"]!=True:
            payment=input("Enter your payment here: ")
            if payment!="":
                self.currentTicket["paid"]=True    
        print("Thank you, have a nice day")#If while was skipped, or when while succesfully concluded
        self.tickets[0]+=1
        self.parkingSpaces[0]+=1
        self.currentTicket["paid"]=False #Instructions don't mention this, but it makes sense that you would then be dealing with another ticket

    def printData(self):
        print(f'There are {self.tickets[0]} tickets and {self.parkingSpaces[0]} parking spaces left')


#Some light test code
myPark=parkingGarage(1)
myPark.takeTicket()
myPark.takeTicket()
myPark.printData()
myPark.leaveGarage()
myPark.payForParking()
myPark.leaveGarage()
myPark.printData()
