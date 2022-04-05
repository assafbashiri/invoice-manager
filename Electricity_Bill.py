


class Electricity_Bill():
    def __init__(self, start_date,end_date,price,receipt_number):
        self.start_date = start_date
        self.end_date = end_date
        self.pric = price
        self.receipt_number = receipt_number
    def to_string(self):
        a = f"start date: {self.start_date}\n"
        b = f"end date: {self.end_date}\n"
        c = f"price: {self.price}\n"
        d = f"receipt number: {self.receipt_number}\n"
        to_return = a + b + c + d +";"
        return to_return
