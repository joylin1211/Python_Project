#!/usr/bin/env python3
import random
import argparse
import sys
import time

def play_game(low=1, high=100):
    secret = random.randint(low, high)
    attempts = 0
    print(f"我已選好一個介於 {low} 到 {high} 的數字，開始猜吧！")
    while True:
        guess = input("請輸入一個整數：").strip()
        attempts += 1
        if not guess:
            print("請輸入內容。")
            continue
        if guess.lower() in ("quit", "exit"):
            print("遊戲結束。")
            return
        try:
            g = int(guess)
        except ValueError:
            print("輸入不是整數，請再試一次。")
            continue
        if g < low or g > high:
            print(f"請輸入介於 {low} 和 {high} 的數字。")
            continue
        if g < secret:
            print("太小了。")
        elif g > secret:
            print("太大了。")
        else:
            print(f"答對了！你一共猜了 {attempts} 次。")
            return

def demo(low=1, high=100):
    secret = random.randint(low, high)
    attempts = 0
    lo, hi = low, high
    print(f"[DEMO] 秘密數字：{secret}")
    while True:
        guess = (lo + hi) // 2
        attempts += 1
        print(f"[DEMO] 猜：{guess}")
        if guess < secret:
            print("[DEMO] 太小，更新區間")
            lo = guess + 1
        elif guess > secret:
            print("[DEMO] 太大，更新區間")
            hi = guess - 1
        else:
            print(f"[DEMO] 答對！共 {attempts} 次。")
            break
        time.sleep(0.05)

def main():
    parser = argparse.ArgumentParser(description="猜數字遊戲")
    parser.add_argument("--low", type=int, default=1, help="最小值，預設 1")
    parser.add_argument("--high", type=int, default=100, help="最大值，預設 100")
    parser.add_argument("--demo", action="store_true", help="執行自動示範模式（非互動）")
    args = parser.parse_args()
    if args.low >= args.high:
        print("錯誤：--low 必須小於 --high。")
        sys.exit(1)
    if args.demo:
        demo(args.low, args.high)
    else:
        play_game(args.low, args.high)

if __name__ == "__main__":
    main()