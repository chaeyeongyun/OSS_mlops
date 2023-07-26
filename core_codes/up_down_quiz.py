import random

rnd_val = random.randint(0, 100)


def updown(val):
    global rnd_val
    if rnd_val > val:
        print("Up")
        return False
    elif rnd_val < val:
        print("Down")
        return False
    elif rnd_val == val:
        print("정답")
        return True


if __name__ == "__main__":
    print("숫자를 맞춰보세요 (0이상 100이하)")
    for _ in range(3):
        val = int(input())
        res = updown(val)
        if res:
            break
    if not res:
        print("실패! 정답은 ", rnd_val)
