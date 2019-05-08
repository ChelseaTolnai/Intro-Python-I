import random

CODE = {'A': '.-',     'B': '-...',   'C': '-.-.',
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',

        '1': '.----',  '2': '..---',  '3': '...--',
        '4': '....-',  '5': '.....',  '6': '-....',
        '7': '--...',  '8': '---..',  '9': '----.',
        '0': '-----',

        ',': '--..--', '.': '.-.-.-', '!': '-·-·--',
        '?': '..--..', '(': '-.--.',  ')': '-.--.-',
        '/': '-..-.',  '-': '-....-',
        }


def morse(text):
    morse = ''
    for char in text:
        if char != ' ':
            morse += CODE[char.upper()] + ' '
        else:
            morse += ' '
    return morse


def cmd_func(cmd, text):
    results = text
    if cmd == 'u':
        results = text.upper()
    if cmd == 'l':
        results = text.lower()
    if cmd == 'b':
        results = ' '.join(format(ord(x), 'b') for x in text)
    if cmd == 'm':
        results = morse(text)
    print("\n", results)

try:
    text = input("\nEnter text: ")
    choices = ['u', 'l', 'b', 'm']
    while text:
        print("\nOptions - "
              "[u]:uppercase / "
              "[l]:lowercase / "
              "[b]:binary / "
              "[m]:morse / "
              "[r]:random / "
              "[q]:quit"
              )
        cmd = input("Enter convert type: ")
        if cmd == 'q':
            print("\nCome back soon!\n")
            break
        elif cmd == 'r':
            cmd_rand = random.choice(choices)
            cmd_func(cmd_rand, text)
        else:
            cmd_func(cmd, text)
except:
    print("Invalid input or command")
