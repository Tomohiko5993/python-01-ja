# ここにコードを書いてください
count_words = input("Please enter the message:")
count_words = count_words.lower()#count_wordsを小文字にする
vowels = [ "a", "e", "i", "o", "u" ]#母音のリストを作成する
vowel_counter = 0 #母音のカウンターを初期化する

for char in count_words:# hello world ->h,e,l,l,o ...
    if char in vowels:#aeiouのリストに合致するかを確認し、Trueなら以下の条件に従う
        vowel_counter = vowel_counter + 1#aeiouに合致したらカウントを増やす
print(f"Number of vowels:{vowel_counter} ")





