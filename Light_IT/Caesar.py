def alphabet_position(character):
    alph = 'abcdefghijklmnopqrstuvwxyz'
    lower = character.lower()
    return alph.index(lower)

def rotate_string(text):

    rotated = ''
    alph = 'abcdefghijklmnopqrstuvwxyz'

    for char in text:
        rotated_idx = (alphabet_position(char) + 13) % 26
        if char.isupper():
            rotated = rotated + alph[rotated_idx].upper()
        else:
            rotated = rotated + alph[rotated_idx]

    return rotated

def rotate_character(char, rot):
    alph = 'abcdefghijklmnopqrstuvwxyz'
    rotated_idx = (alphabet_position(char) + rot) % 26

    if char.isupper():
        return alph[rotated_idx].upper()
    else:
        return alph[rotated_idx]

def rotate(text, rot):

    rotated = ''

    for char in text:
        if (char.isalpha()):
            rotated = rotated + rotate_character(char, rot)
        else:
            rotated = rotated + char

    return rotated
