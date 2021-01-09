import random
# rock=0 ,paper=1, scissor=2

count_rock = 0
count_paper = 0
count_scissor = 0
player_score = 0
computer_score = 0


def update_count(user_input):
    global count_scissor, count_rock, count_paper
    if user_input == 0:
        count_rock += 1
    elif user_input == 1:
        count_paper +=1
    elif user_input == 2:
        count_scissor += 1


def prediction():
    if count_rock > count_paper and count_rock > count_scissor:
        pred = 1
    elif count_paper > count_rock and count_paper > count_scissor:
        pred = 2
    elif count_scissor > count_rock and count_scissor > count_rock:
        pred = 0
    else:
        pred = random.randint(0, 2)
    return pred


def update_scores(pred, user_input):
    global player_score, computer_score
    if user_input == 0:
        if pred == 0:
            print("You played Rock, Computer player Rock")
            print("Player Score", player_score, "Computer Score", computer_score)
        elif pred == 1:
            print("You played Rock, Computer player Paper")
            computer_score += 1
            print("Player Score", player_score, "Computer Score", computer_score)
        elif pred == 2:
            print("You played Rock, Computer player Scissor")
            player_score += 1
            print("Player Score", player_score, "Computer Score", computer_score)
    elif user_input == 1:
        if pred == 0:
            print("You played Paper, Computer player Rock")
            player_score += 1
            print("Player Score", player_score, "Computer Score", computer_score)
        elif pred == 1:
            print("You played Paper, Computer player Paper")
            print("Player Score", player_score, "Computer Score", computer_score)
        elif pred == 2:
            print("You played Paper, Computer player Scissor")
            computer_score += 1
            print("Player Score", player_score, "Computer Score", computer_score)
    elif user_input == 2:
        if pred == 0:
            print("You played Scissor, Computer player Rock")
            computer_score += 1
            print("Player Score", player_score, "Computer Score", computer_score)
        elif pred == 1:
            print("You played Scissor, Computer player Paper")
            player_score += 1
            print("Player Score", player_score, "Computer Score", computer_score)
        elif pred == 2:
            print("You played Scissor, Computer player Scissor")
            print("Player Score", player_score, "Computer Score", computer_score)


valid_entry = [0, 1, 2]
while True:
    player_move = int(input("Please Enter 0 for Rock, 1 for Paper or 2 for Scissor"))
    while player_move not in valid_entry:
        print("Invalid entry")
        player_move = int(input("Please Enter 0 for Rock, 1 for Paper or 2 for Scissor"))
    predict = prediction()
    update_scores(predict, player_move)
    update_count(player_move)
    # game ends here
    if computer_score == 5:
        print("Computer won")
        break
    elif player_score == 5:
        print("Player won")
        break
