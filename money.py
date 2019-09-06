https://thispointer.com/python-how-to-find-keys-by-value-in-dictionary/

class money:
    import datetime as dt
    from datetime import date, time, datetime
    global dt, last_friday, this_friday, next_friday, bills

    def __init__(self, bill_sort):
        self.bill_sort = bill_sort()

    def bill_sort():
        bills = dict()
        from datetime import date, time, datetime
        this_friday = datetime.now()

        if this_friday.strftime('%a') == 'Fri':
            last_friday = this_friday - dt.timedelta(days=7)
            next_friday = this_friday + dt.timedelta(days=7)
            two_weeks_ago = this_friday - dt.timedelta(days=14)

        else:
            while this_friday.strftime('%a') != 'Fri':
                this_friday += dt.timedelta(days=1)
            last_friday = this_friday - dt.timedelta(days=7)
            next_friday = this_friday + dt.timedelta(days=7)
            two_weeks_ago = this_friday - dt.timedelta(days=14)

        bills = {
        'power': 8,
        'water': 3,
        'car': 15,
        'home': 1,
        'ccard_1': 18,
        'ccard_2': 24,
        'phone': 12,
        'gas': 5,
        'insurance': 1,
        }

        if (this_friday.day)%2 is 0:
            for value in bills.values():
            # 0 means even week, pay day week, this only works for biweeky pay. swap the 1 and 0 if yours is opposite
                if value < (this_friday.day):
                    print('\nThe following bills should have been paid {}:'.format((two_weeks_ago.strftime("%d %B, %Y"))))
                    for value in bills.values():
                        if value < (this_friday.day):
                        print(bills.keys())
                elif value < (next_friday.day):
                    print('\nThe following bills should have been paid {}:'.format((last_friday.strftime("%d %B, %Y"))))
                    print(bills.keys())
                elif value >= (this_friday.day):
                    print('\nThe following bills should be paid this friday ({}):'.format((this_friday.strftime("%d %B, %Y"))))
                    print(bills.keys())

        elif (this_friday.day)%2 is 1:
            for value in bills.values():
                if value < (next_friday.day):
                    print('\nThe following bills should have been paid {}:'.format((last_friday.strftime("%d %B, %Y"))))
                    print(bills.keys())
                elif value >= (next_friday.day):
                    print('\nThe following bills should be paid {}:'.format(next_friday.strftime("%d %B, %Y")))
                    print(bills.keys())

