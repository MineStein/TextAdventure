import time


def compare(one, two):
    return one.lower() == two.lower()


def dialog(arr):
    for el in arr:
        print(el)
        time.sleep(1.5)


def game_over(msg):
    print(msg)
    quit()


name = input('What is your name? ')

valid_age = False

while not valid_age:
    age = input('How old are you? ')

    try:
        age = int(age)

        valid_age = True
    except ValueError:
        print('That was an invalid age!')

if age < 18:
    game_over('You are not old enough!')

dialog([
    'You stumble through some dark woods',
    'Not knowing where you are, you reach a divergence in the trees',
    'What path do you take? Left, or right?'
])

path = input()

if compare(path, 'left'):
    print('You go to the left.')
elif compare(path, 'right'):
    print('You take a right.')
else:
    game_over('You chose neither path, and were slaughtered.')
