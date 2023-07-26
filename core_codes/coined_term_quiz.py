coined_term = {"취존": "취향존중",
               "솔까말": "솔직히까놓고말해서",
               "케바케": "케이스바이케이스"}


def print_hello():
    print("hello")


def quiz():
    global coined_term
    num_quiz = len(coined_term)
    num_correct = 0
    for term in coined_term:
        print(f"{term}이 어떤 문장의 줄임말인가요?")
        answer = input()
        answer = answer.replace(" ", "")
        if answer == coined_term[term]:
            print("정답")
            num_correct += 1
        else:
            print("오답")
    print(f"{num_quiz}개 문제 중 {num_correct}개 정답")


if __name__ == "__main__":
    quiz()
