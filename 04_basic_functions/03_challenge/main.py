def unique_substrings(input_string):
    # 「pass」を削除して、ここにコードを書いてください
    #pass
    #部分もじを格納するためのセットを使用
    substrings = set()

    #すべての開始位置を考慮
    for start in range(len(input_string)):
        #すべての終了位置を考慮
        for end in range(start + 1, len(input_string) + 1):
            #部分文字をセットに追加
            substrings.add(input_string[start:end])

    #セットをリストに変換して返す
    return sorted(substrings)

input_string = "banana"
print(unique_substrings(input_string))
