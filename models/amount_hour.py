class AmountHour:
    def __init__(self, hour, amount, name_day):
        self.hour = hour
        self.amount = amount
        self.day_name = name_day

    def __str__(self):
        return str(self.hour) + self.day_name
