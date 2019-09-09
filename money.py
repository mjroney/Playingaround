class money:
    import datetime as dt
    from datetime import date, time, datetime
    global dt, last_friday, this_friday, next_friday, bills
    
    bills = dict()
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

    def __init__(self, bill_sort):
        self.bill_sort = bill_sort()

    def bill_sort():
        from datetime import date, time, datetime
        this_friday = datetime.now()

        if this_friday.strftime('%a') == 'Fri':
            last_friday = this_friday - dt.timedelta(days=7)
            next_friday = this_friday + dt.timedelta(days=7)
            two_weeks_ago = this_friday - dt.timedelta(days=14)
            pass

        else:
            while this_friday.strftime('%a') != 'Fri':
                this_friday += dt.timedelta(days=1)
            last_friday = this_friday - dt.timedelta(days=7)
            next_friday = this_friday + dt.timedelta(days=7)
            two_weeks_ago = this_friday - dt.timedelta(days=14)
 
        week_num = this_friday.strftime("%W")
        div_week = int(week_num)%2
        two_weeks_later = this_friday + dt.timedelta(days=14)
        three_weeks_later = this_friday + dt.timedelta(days=21)
        four_weeks_later = this_friday + dt.timedelta(days=28)
    
        if div_week is 1:
            print('\nThe following bills should have been paid {}:'.format((last_friday.strftime("%d %B, %Y"))))
            for items in bills.items():
                one_week = [key for (key, value) in bills.items() if value < (this_friday.day)]
                early_bird = [key for (key, value) in bills.items() if value >= (next_friday.day)]
                one_more = [key for (key, value) in bills.items() if (three_weeks_later.day) < value >= (next_friday.day)]
            print(one_week)                
            print('\nThe following bills should be paid {}:'.format(next_friday.strftime("%d %B, %Y")))
            print(early_bird)
            print('\nThe following will be due {}:'.format(three_weeks_later.strftime("%d %B, %Y")))
            print(one_more)
            pass
        
        else:
            print('\nThe following bills should have been paid on {}:'.format((two_weeks_ago.strftime("%d %B, %Y"))))
            for items in bills.items():
                two_weeks_late = [key for (key, value) in bills.items() if value < (this_friday.day)]
                on_time = [key for (key, value) in bills.items() if two_weeks_later.day > value >= (this_friday.day)]
                in_two = [key for (key, value) in bills.items() if four_weeks_later.day < value > (two_weeks_later.day)]
                in_four = [key for (key, value) in bills.items() if value >= (four_weeks_later.day)]
            print(two_weeks_late)
            print('\nThe following bills should be paid this friday ({}):'.format((this_friday.strftime("%d %B, %Y"))))
            print(on_time)
            print('\nThe following bills should be paid {}:'.format(two_weeks_later.strftime("%d %B, %Y")))
            print(in_two)
            print('\nThe following will be due {}:'.format(four_weeks_later.strftime("%d %B, %Y")))
            print(in_four)
