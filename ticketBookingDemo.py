from threading import *
class TicketBooking:

    def __init__(self,seats):
        self.seats=seats

    def bookTicket(self,toBookSeats):
        print(f'Total available seats at present moment: {self.seats}')
        if self.seats>=toBookSeats:
            self.seats-=toBookSeats
            print('Cecking Seat Avilability')
            print('Processing Payment')
            print('Finally Booking Seat')
            print('Sending Notification')
        else:
            print('Seat Booking not possible.')

obj=TicketBooking(10)

t1 =Thread(target=obj.bookTicket,args=(2,))
t2=Thread(target=obj.bookTicket,args=(2,))
t3=Thread(target=obj.bookTicket,args=(2,))

t1.start()
t2.start()
t3.start()
