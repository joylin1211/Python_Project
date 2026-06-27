from __future__ import annotations

import sys


def add(a: int, b: int) -> int:
    return a + b


def greet(name: str) -> str:
    return f"Hello, {name}!"


class Calculator:
    def __init__(self) -> None:
        self.history: list[tuple[str, int]] = []

    def add(self, a: int, b: int) -> int:
        result = a + b
        self.history.append((f"{a} + {b}", result))
        return result

    def multiply(self, a: int, b: int) -> int:
        result = a * b
        self.history.append((f"{a} * {b}", result))
        return result

    def show_history(self) -> list[tuple[str, int]]:
        return self.history


def run_tests() -> None:
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

    assert greet("Python") == "Hello, Python!"
    assert greet("") == "Hello, !"

    calc = Calculator()
    assert calc.add(3, 4) == 7
    assert calc.multiply(3, 4) == 12
    assert len(calc.history) == 2

    print("所有測試通過！")


def main() -> None:
    print("=== Lesson Template ===")
    print(greet("Python"))
    calc = Calculator()
    print(f"3 + 4 = {calc.add(3, 4)}")
    print(f"3 * 4 = {calc.multiply(3, 4)}")
    print(f"歷史紀錄: {calc.show_history()}")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        run_tests()
    else:
        main()
