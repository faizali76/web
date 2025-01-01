# Can you change the self parameter inside a class to some thing else (say 'faiz'). Try changing self to 'slf' or 'faiz' and see the effects.



from random import randint
class train:

    def __init__(slf, trainNo):
        slf.trainNo = trainNo
        

    def book(self, fro, to):
        print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to}")


    def getstatus(self):
        print(f"Ticket no: {self.trainNo} is running on time ")

    def getfare(self, fro, to):
        print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(222, 5555)}")

t = train(1234)
t.book("rampur","delhi")
t.getstatus()
t.getfare("rampur","delhi")