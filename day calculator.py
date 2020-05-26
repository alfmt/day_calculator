import day_lib
import day_oop

def main():
    day_calculator = day_oop.Day_calculator()
    year, month, day = day_lib.Day_lib.input_data(0)
    day_name = day_calculator.calculate_day_name(year, month, day)

    print(f"{year}년 {month}월 {day}일은 {day_name}입니다")

if __name__ == "__main__":
    main()