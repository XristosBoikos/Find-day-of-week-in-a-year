import re


def is_year_leap(year):
    if year >= 1582:
        if year % 4 != 0:
            return False
        elif year % 100 != 0:
            return True
        elif year % 400 != 0:
            return False
        else:
            return True
    elif year % 4 == 0:
        return True
    else:
        return False


def days_in_month(year, month):
    if month >= 1 and month <= 12:
        if is_year_leap(year) and month == 2:
            return 29
        elif not is_year_leap(year) and month == 2:
            return 28
        elif month in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        else:
            return 30
    else:
        return "Month is False"


def day_of_year(year, month, day):
    if days_in_month(year, month) in [28, 29, 30, 31]:
        if day >= 1 and day <= days_in_month(year, month):

            # Year Code
            year_code = year % 100
            if month == 1 or month == 2:
                year_code -= 1

            # Month Code
            month_codes = [11, 12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            month_code = month_codes[month - 1]

            # Century Code
            # if Gregorian Date
            century_code = year // 100

        else:
            return "Day number is false"

        if is_year_leap:
            day_code = (day + int(2.6 * month_code - 0.2) - 2 * century_code + year_code + (year_code // 4) + (
                        century_code // 4)) % 7

            day_codes = ["SUNDAY", "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY"]

            return day_codes[int(day_code)]
        else:
            day_code = (day + (2.6 * month_code - 0.2) - 2 * century_code + year_code + (year_code // 4) + (
                        century_code // 4) - 1) % 7

            day_codes = ["SUNDAY", "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY"]

            return day_codes[int(day_code)]

    else:
        return "Month number is False"

if __name__ == "__main__":
    try:
        user_input_year, user_input_month, user_input_day = re.split(' |/|-', input("Enter the year month day (space - or /):\n"))
        print(day_of_year(int(user_input_year), int(user_input_month), int(user_input_day)))
    except:
        print("Something went wrong \nGoodbye!")
