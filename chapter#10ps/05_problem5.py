#Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats)
# and get fare information of train running under Indian Railways.
from random import randint
class train :


    def __init__(self,train_no) :
         self.train_no = train_no
            

    def book(self,fro,to):
        print(f"The ticket is booked in train no {self.train_no} from {fro} to {to}")

    def status(self,):
                print(f"train no :{self.train_no} is running ")


    def fare_info(self,fro,to):
                 print(f"The ticket fare of  train no {self.train_no} from {fro} to {to} is {randint(2222,5555)}")


t = train(1595)
t.book("Dehli","Mumbai")
t.status()
t.fare_info("Dehli","Mumbai")