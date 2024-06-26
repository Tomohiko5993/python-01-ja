def counter():
    occurrences = {}
    fruits = [
        "apple",
        "banana",
        "orange",
        "grape",
        "apple",
        "kiwi",
        "banana",
        "melon",
        "orange",
        "strawberry",
    ]

    # ここにコードを書いてください
    #`fruits` リストの要素の数をカウントするプログラムを書きます。
    #各要素をキーとして `occurrences` 辞書に保存します。各キーの値はこの単語の出現回数です。
    ##for, in の組み込み関数を書く
    for fruit in fruits:
        if fruit in occurrences:
            occurrences[fruit] += 1
        else:
            occurrences[fruit] = 1
    #print(occurrences)
    #{'apple': 2, 'banana': 2, 'orange': 2, 'grape': 1, 'kiwi': 1, 'melon': 1, 'strawberry': 1}
    #完了したら、辞書をループ処理して各キーと値を次のように出力します。
    #for in を使って、キーと値を出力する
    for item, value in occurrences.items():
        print(f"{item}: {value}")

    return occurrences

print(counter())
