coined_term = {"취존": "취향존중",
               "솔까말": "솔직히까놓고말해서",
               "케바케": "케이스바이케이스",
               "반모": "반말모드"}


def print_hello():
    print("hello")


def is_correct(answer, target):
    answer = answer.replace(" ", "")
    return answer == target


if __name__ == "__main__":
    num_quiz = len(coined_term)
    num_correct = 0
    for term in coined_term:
        print(f"{term}이 어떤 문장의 줄임말인가요?")
        answer = input()
        if is_correct(answer, coined_term[term]):
            print("정답")
            num_correct += 1
        else:
            print("오답")
    print(f"{num_quiz}개 문제 중 {num_correct}개 정답")
