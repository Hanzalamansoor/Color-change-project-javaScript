# Can you change the self-parameter inside a class to something else (say
# “harry”). Try changing self to “slf” or “harry” and see the effects.

from random import randint
class train :


    def __init__(slf,train_no) : # Nothing happend you can write harry, slf or whatever you want but it is not a good practice
         slf.train_no = train_no
            

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
