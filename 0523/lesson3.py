import random

def number_guessing_game():
    print("🎮 歡迎來到猜數字遊戲！")
    print("我已經想好一個 1 到 100 的數字。")

    secret_number = random.randint(1, 100)
    guess_count = 0

    while True:
        try:
            guess = int(input("請輸入你的猜測："))
            guess_count += 1

            if guess < secret_number:
                print("📉 太小了！")
            elif guess > secret_number:
                print("📈 太大了！")
            else:
                print(f"🎉 恭喜你猜中了！答案是 {secret_number}")
                print(f"你總共猜了 {guess_count} 次！")
                break

        except ValueError:
            print("⚠️ 請輸入有效的整數！")

# 開始遊戲
number_guessing_game()
