import day_lib

class Day_calculator:

    def calculate_day_name(self, year, month, day):
        total_days = 0
        month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        day_names = ["일요일", "월요일", "화요일", "수요일", "목요일", "금요일", "토요일"]
        for i in range(1, year):
            if day_lib.Day_lib.is_leap(0, i):
                total_days = total_days + 366
            else:
                total_days = total_days + 365
        
        for i in range(1, month):
            total_days = total_days + month_days[i]

        if day_lib.Day_lib.is_leap(0, year) and month >= 3:
            total_days = total_days + 1

        total_days = total_days + day

        return day_names[total_days % 7]