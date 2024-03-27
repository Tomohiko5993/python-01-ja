def compute_factorial():
    # ここにコードを書いてください
    # number変数を編集し、ユーザー入力として正の整数を受け取ります。整数に変換することを忘れないでください
    number = int(input( "Enter a number: ")) #"5"
    if number == 0:
        return 1
    else :
        result = 1
        count = number
    while (count > 1):
        result = result * count
        count = count - 1
    # result変数を編集し、最終的な計算結果を保存します
    return result

result = compute_factorial()
print( result )
