class money:
    def __init__(self, find_fridays, bill_sort):
        self.find_fridays = find_fridays()
        self.bill_sort = bill_sort()

    def find_fridays():
        from datetime import date, time, datetime
        global last_friday, this_friday, next_friday
        today = date.today()
        last_friday = today
        this_friday = today
        next_friday = today
        if this_friday.strftime('%a') == 'Fri':
            last_friday = today.replace(days=(today.days - 7)
            next_friday = today.replace(days=(today.days + 7)
            print(last_friday.strftime("%U"), this_friday.strftime("%U"), next_friday.strftime("%U"))
        elif this_friday.strftime('%a') != 'Fri':
            this_friday += datetime.timedelta(1)
            last_friday = this_friday.replace(days=(this_friday.days - 7)
            next_friday = this_friday.replace(days=(this_friday.days + 7)
            return last_friday.strftime("%U"), this_friday.strftime("%U"), next_friday.strftime("%U")

    def bill_sort():
        from datetime import date, time, datetime
        today = date.today()
        money.find_fridays()
        week_num = today.strftime("%U")
        bills = {
        power: 8,
        water: 3,
        car: 15,
        home: 1,
        ccard_1: 18,
        ccard_2: 24,
        phone: 12,
        gas: 5,
        insurance: 1,
        }
        for day in bills.values():
            if day < (this_friday.day):
                if (this_friday.strftime("%U"))%2 is 0:
                    print('The following bills should have been paid {}: \n'.format((this_friday.timedelta(-14), bills.keys())))
                elif (this_friday.strftime("%U"))%2 is 1:
                    print('The following bills should have been paid {}: \n'.format((this_friday.timedelta(-7), bills.keys())))
            if day >= (this_friday.day):
                if (this_friday.strftime("%U"))%2 is 0:
                    print('The following bills should be paid this friday ({}): \n'.format((this_friday, bills.keys())))
                elif (this_friday.strftime("%U"))%2 is 1:
                    if day < (next_friday.day):
                        print('The following bills should have been paid {}: \n'.format((this_friday.timedelta(-7), bills.keys())))
                    elif day >= (next_friday.day):
                        print('The following bills should be paid {}: \n'.format(next_friday, bills.keys()))
