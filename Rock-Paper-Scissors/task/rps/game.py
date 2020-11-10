# Write your code here
import random

name = input("Enter your name: ").strip()

print("Hello,", name)

game_options = input("Please enter your options").strip().split(',')
chose = game_options if len(game_options) > 0 and game_options[0] != '' else ['rock', 'paper', 'scissors']

print("Okay, let's start")
file = open("rating.txt", 'r')

rating = 0
for line in file:
    player_in_file = line.split()
    if player_in_file[0] == name:
        rating = int(player_in_file[1])

word = input().strip()

computer = chose[random.randint(0, len(chose) - 1)]


def play(play_word, computer_word):
    word_index = chose.index(play_word)
    play_list = []
    if word_index == len(chose) - 1:
        play_list = chose[:word_index]
    else:
        play_list = chose[word_index + 1:] + chose[: word_index]

    if play_list.index(computer_word) >= len(play_list) / 2:
        print("Well done. The computer chose", computer_word, "and failed")
        return 100
    else:
        print("Sorry, but the computer chose", computer_word)
        return 0


while word != '!exit':
    if word == computer:
        print("There is a draw (", computer, ")")
        rating += 50

    elif word == '!rating':
        print("Your rating is: ", rating)

    elif word not in chose:
        print('Invalid input')

    else:
        rating += play(word, computer)

    word = input().strip()
    computer = chose[random.randint(0, len(chose) - 1)]

print('Bye!')
