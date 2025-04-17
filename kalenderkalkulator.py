class calendar:
    # As the object gets initiated, it will make a dictionary with every month being a key, and the number of days in that month being a list and value to the corresponding key.
    # It will also check whether the year number in the parameter is a leapyear or not, and give febuary the correct number of days.
    def __init__(self, year: int):
        self.year = {}

        # Checks whether the year is a leapyear using the inputed year to accurately determine the number of days in febuary. Then it creates a list of all the dates in febuary.
        if year%4 == 0 and ((year%100 != 0) or (year%400 == 0)):
            self.leapYear = True
            febuary = [i for i in range(1,30)]
        else:
            self.leapYear = False
            febuary = [i for i in range(1,29)]

        # Creates a list of the keys (months) and 2 variations in month day number (aside from febuary) with lists of all the dates.
        keyList = ["January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        days31 = [i for i in range(1,32)]
        days30 = [i for i in range(1,31)]

        # Here it creates 13 months of alternating between 31 and 30 days, before removing the 7th, as both july and august have 31 days, and setting the 2nd month to the number of months in febuary.
        valueList = []
        for i in range(13):
            if i%2 == 0:
                valueList.append(days31)
            else:
                valueList.append(days30)
        valueList.pop(7)
        valueList[1] = febuary

        # Finally, there's a for-loop that fills the year dictionary with the keys from keyList (the months) and their corresponding items from valueList (lists of the month's dates).
        for i in range(len(keyList)):
            self.year[keyList[i]] = valueList[i]

    # This function converts the day of the year to the date of the year, and uses a parameter of whether 1st of january is the 1st or 0th day of the year in its calculations.
    def dayToDate(self, day: float | int, startIndex: int) -> tuple:
        # Converts from whatever iterative system was in the input to one that starts with 0.
        day = int(day)-startIndex

        # The while loop calculates the given day number (tweaked for iterability) minus the amount of days in each month of the year until its value is less than or equal to the last day of a month. Basically, day 32 , where january 1st is 1 becomes the (32 - 1) - 31 = 31 - 31 = 0th iteration of month 2, AKA 1st of Febuary.
        month = 0
        run = True
        while run:
            for monthItem in self.year.values():
                if day < len(monthItem):
                    run = False
                else:
                    day -= len(monthItem)
                    month += 1
        
        # Converts the month number and day iteration to month name and day number, and returns them as a tuple.
        monthName = list(self.year.keys())[month]
        dayName = self.year[monthName][day]
        return (dayName, monthName)

year2024 = calendar(2024)
print(year2024.dayToDate(135.01, 1))