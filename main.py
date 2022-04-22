import pandas as pd
import random as rand
import os


def clrscr():
    os.system("cls||clear")


def prompt_continue():
    print("Do you want to continue? [Y/N]")
    pInput = input().capitalize()
    if not pInput in ["Y", "N"]:
        pInput = "N"
    if pInput == "Y":
        clrscr()
        os.execv()
    else:
        exit()


clrscr()


class bcolors:
    GREEN = "\u001b[42;1m"
    YELLOW = "\u001b[43;1m"
    BLACK = "\u001b[40;1m"
    RESET = "\u001b[0m"


df = pd.read_csv("words.csv")
words = df.columns.array

chosen = rand.choice(words).capitalize()


def check_correct_word(str, attempt):
    if str == chosen:
        print("Congratulation! You have guessed the right word!")
        prompt_continue()
    else:
        hint = ""
        for i in range(len(str)):
            if str[i] in chosen and chosen[i] == str[i]:
                hint += f'{bcolors.GREEN}{str[i]}'
            else:
                if str[i] in chosen and chosen[i] != str[i]:
                    hint += f'{bcolors.YELLOW}{str[i]}'
                else:
                    hint += f'{bcolors.BLACK}{str[i]}'
        hint += bcolors.RESET
        print(hint)
    if attempt == 4 and str != chosen:
        print(
            f'Incorrect words after 5 attempts. The correct word is {chosen}')
        prompt_continue()


print(f'You have 5 attemps to guess the correct {len(chosen)}-character word')
print(
    "For each word, if the answer is incorrect, your hint will appear in a form of word like below"
)
print(
    f'{bcolors.BLACK}C{bcolors.YELLOW}R{bcolors.GREEN}A{bcolors.BLACK}NE{bcolors.RESET}'
)
print(f'{bcolors.BLACK} {bcolors.RESET}: The character is not in the answer')
print(
    f'{bcolors.YELLOW} {bcolors.RESET}: The character is in the answer but not that position'
)
print(
    f'{bcolors.GREEN} {bcolors.RESET}: The character is in the answer and have the exact position'
)
print("Happy Playing!")
for i in range(5):
    wInput = input()
    while len(wInput) != len(chosen):
        print(f'Please only enter a word with {len(chosen)} characters')
        wInput = input()
    check_correct_word(wInput.capitalize(), i)
