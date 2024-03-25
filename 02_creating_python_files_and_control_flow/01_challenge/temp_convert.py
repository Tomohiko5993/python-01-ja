
def convert(temp, deg):
    # ここにコードを書いてください
    # temp変数を編集し、ユーザー入力として温度を受け取ります。整数に変換することを忘れないでください
    if (deg == "f"):
        celsius = (temp - 32 ) * 5 / 9
        return celsius

    elif (deg == "c"):
        fahrenheit = (temp * 9 / 5) + 32
        return fahrenheit


def main():
    temp = float(input("Enter the temperature: "))
    deg = input("Enter the unit (c for Celsius, f for Fahrenheit): ")

    converted_temp = convert(temp, deg)

    if isinstance(converted_temp, float):
        if deg == "f":
            print(f"{temp} degrees Fahrenheit is {converted_temp} degrees Celsius.")
        elif deg == "c":
            print(f"{temp} degrees Celsius is {converted_temp} degrees Fahrenheit.")
    else:
        print(converted_temp)
main()
