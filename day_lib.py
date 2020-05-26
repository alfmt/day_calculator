class Day_lib:

    def input_data(self):
        year = int(input("년도를 입력하세요: "))
        month = int(input("월을 입력하세요: "))
        day = int(input("일을 입력하세요: "))
        return year, month, day

    def is_leap(self, year):
        if year % 400 == 0:
            return True
        elif year % 100 == 0:
            return False
        elif year % 4 == 0:
            return True
        else:
            return False

    

