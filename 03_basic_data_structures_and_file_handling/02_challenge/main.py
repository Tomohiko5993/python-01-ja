import math
import random

# ここにコードを書いてください
#ユーザーからグー (rock):0、チョキ (scissors):1、パー (paper):2を選択してもらう。
print("じゃんけんマシーンとじゃんけん対決をします")
print("グー (rock):0、チョキ (scissors):1、パー (paper):2を数字で入力してください。")

#0~2以外の数字が入力された場合、再入力をしてもらうためのループを作る
#ユーザーの選択を取得するための関数
def get_user_choice():
    while True:
        user_choice = input( "あなたの選択:" )
        if user_choice in ['0', '1', '2' ]:
            return int(user_choice)
        else:
            print( "無効な入力です。入力し直してください。")

#ユーザーの選択を取得
user_choice = get_user_choice()

#コンピューターの選択を決定する
#乱数で値を取得する
def random_0_1_2():
    r = random.random()
    if r < 1/3:
        return 0
    elif r < 2/3:
        return 1
    else:
        return 2
computer_choice = random_0_1_2()

#じゃんけんの結果を表示する
choices = ['グー (rock)' , 'チョキ (scissors)' , 'パー (paper)']
#for _ in range(10):
#    print(random_0_1_2()) # 乱数が呼び出されているか確認

choices = ['グー', 'チョキ', 'パー']
print(f"あなたの選択: {choices[user_choice]}")
print(f"コンピュータの選択: {choices[computer_choice]}")

# 勝敗を判定
if user_choice == computer_choice:
    print("引き分けです！")
elif (user_choice - computer_choice) % 3 == 1:
    print("コンピュータの勝ちです！")
else:
    print("あなたの勝ちです！")