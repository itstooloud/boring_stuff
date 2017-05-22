
import random

def get_answer(answer_number):
    if answer_number == 1:
        return 'It is certain'

    if answer_number == 2:
        return 'who the hell knows'

    if answer_number == 3:
        return 'I have no idea'

    if answer_number == 4:
        return 'I am drunk'
        
    if answer_number == 5:
        return 'You are drunk'

    if answer_number == 6:
        return 'I have leukemia'

    if answer_number == 7:
        return 'I have no herpes'

    if answer_number == 8:
        return 'Everyone I know is drunk'

fortune = random.randint(1,9)
r = get_answer(fortune)
print(r)
