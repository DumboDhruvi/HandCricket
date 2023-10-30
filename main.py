import random


def chooices() -> tuple:
    choices = [0, 1, 2, 3, 4, 5, 6]
    choice_human = int(input("Enter choice in range 0 - 6: "))
    if choice_human not in choices:
        print("Wrong input")
        return chooices()
    choice_comp = random.choice(choices)

    return choice_comp, choice_human


def human_play():
    choice = int(input("1: batting, 2: bowling: "))
    play(choice)


def play(choice):
    if choice == 1:
        print("You are batting 1st")
        runs = 0
        for i in range(6):
            if runs:
                print(f"Score: {runs}")
            ball = batting()
            if ball == -1:
                print("OUT!")
                break
            else:
                runs += ball
        print(f"target is {runs + 1} runs")
        chase = 0
        for i in range(6):
            if chase:
                print(f"Score: {chase}, {runs - chase + 1} runs remaining")
            ball = bowling()
            if ball == -1:
                print("OUT!")
                break
            else:
                print(f"computer scored {ball} in this ball")
                chase += ball
            if chase > runs:
                print("game won! by Computer")
                break

        if chase == runs:
            print("Draw")
        elif chase < runs:
            print("print player won!")

    else:
        print("you are bowling 1st")
        chase = 0
        for i in range(6):
            if chase:
                print(f"Score: {chase}")
            ball = bowling()
            if ball == -1:
                print("OUT")
                break
            else:
                print(f"computer scored {ball} runs in this ball")
                chase += ball
        print(f"target is {chase + 1} runs")
        runs = 0
        for i in range(6):
            if runs:
                print(f"Score: {runs}, {chase - runs + 1} runs remaining")
            ball = batting()
            if ball == -1:
                break
            else:
                runs += ball
            if runs > chase:
                print("player won")
                break

        if runs == chase:
            print("draw")
        elif runs < chase:
            print("Computer won")


def batting():
    comp, human = chooices()
    if comp == human:
        return -1
    else:
        return human


def bowling():
    comp, human = chooices()
    if comp == human:
        return -1
    else:
        return comp


def game():
    print("Toss!")
    toss = random.choice([0, 1])
    player = {0: "Computer", 1: "Human"}
    print(f"{player[toss]} won the toss!")
    if toss == 1:
        human_play()
    else:
        h = random.choice([0, 1])
        if h == 1:
            play(0)
        else:
            play(1)


if __name__ == "__main__":
    game()
