Magic Eight Ball using lists

import random

messages = ['you are gay',
            'you are stupid',
            'i think you have herpes',
            'you definitely have herpes',
            'kill yourself right now',
            'who cares',
            'you suck']

position = random.randint(0, len(messages)-1)
print(messages[position])

