def convert():
    # ここにコードを書いてください
    # temp変数を編集し、ユーザー入力として温度を受け取ります。整数に変換することを忘れないでください
    print("Please enter the temperature")
    temp = input()
    print("Please enter the f or c")
    degree = input()

    if ( degree == "f" ) :
        temp = (int(temp) -32) * 5 / 9
        print(temp)
    else :
        temp = (int(temp) * 9 / 5) -32
        print(temp)

    return temp


convert()