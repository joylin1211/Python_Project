import random


def guess_number_game():
    """Run a simple number guessing game."""
    secret_number = random.randint(1, 100)
    attempts = 0

    print("歡迎來到猜數字遊戲！")
    print("我已經想好一個1到100的整數，請在最少次數內猜中它。")

    while True:
        guess_text = input("請輸入你的猜測：")
        attempts += 1

        if not guess_text.strip().isdigit():
            print("請輸入一個有效的整數。")
            continue

        guess = int(guess_text.strip())
        if guess < 1 or guess > 100:
            print("請輸入1到100之間的數字。")
            continue

        if guess < secret_number:
            print("太小了！再試一次。")
        elif guess > secret_number:
            print("太大了！再試一次。")
        else:
            print(f"恭喜你！答對了，答案就是 {secret_number}。")
            print(f"你總共猜了 {attempts} 次。")
            break

上傳完成
if __name__ == "__main__":
    guess_number_game()
