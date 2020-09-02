import math
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7
SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code 
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """

    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """

    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x, 0) + 1
    return freq


# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    word = word.lower()
    score_a = 0
    score_b = 0
    for i in word:
        score_a += SCRABBLE_LETTER_VALUES.get(i, 0)
    score_b = 7*len(word)-3*(n-len(word))
    if score_b < 1:
        score_b = 1

    return score_a*score_b

#
# Make sure you understand how this function works and what it does!
#


def display_hand(hand):
    for letter in hand.keys():
        for j in range(hand[letter]):
            print(letter, end=' ')      # print all on the same line
    print()                              # print an empty line


#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#
def deal_hand(n):
    hand = {}
    num_vowels = int(math.ceil(n / 3))-1

    hand['*'] = 1
    if num_vowels > 0:
        for i in range(num_vowels):
            x = random.choice(VOWELS)
            hand[x] = hand.get(x, 0) + 1

    for i in range(num_vowels+1, n):
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1

    return hand


#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    new_hand = hand.copy()
    word = word.lower()

    for i in word:
        new_hand[i] = new_hand.get(i, 0)-1
        if new_hand[i] < 0:
            del(new_hand[i])
    return new_hand


#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    test = []
    test_list = []
    word = str.lower(word)
    word_copy = word

    if '*' not in word:
        for i in range(len(word)):
            if word[i] in hand and hand[word[i]] >= word.count(word[i]) and word in word_list:
                test.append(1)
            else:
                test.append(0)
        if sum(test) == len(word):
            return True
        else:
            return False

    elif '*' in word_copy:
        for i in range(len(VOWELS)):
            if word_copy.replace('*', VOWELS[i]) in word_list:
                test_list.append(1)
                for j in range(len(word_copy)):
                    if word_copy[j] in hand and hand[word_copy[j]] >= word_copy.count(word_copy[j]):
                        test.append(1)
                    else:
                        test.append(0)
                if sum(test) == len(word_copy):
                    return True
                else:
                    return False
            else:
                test_list.append(0)
        if sum(test_list) != len(VOWELS):
            return False

#
# Problem #5: Playing a hand
#


def calculate_handlen(hand):
    len = 0
    for i in hand.values():
        len += i
    return len


def play_hand(hand, word_list):
    score = 0
    while True:
        if calculate_handlen(hand) == 0:
            print()
            print('Total score is: ', score)
            break
        print()
        print('Current hand is: ', end=''), display_hand(hand)
        user_input = str.lower(
            input('Please enter a word or use"!!"to indicate that you are finished:'))
        if user_input == '!!':
            print('Total score is: ', score)
            break
        else:
            if is_valid_word(word, hand, word_list):
                word_score = get_word_score(word, calculate_handlen(hand))
                print(f"\"{word} \" earned {word_score} points. ", end='')
                score += word_score
                print(f"total: {score} points")
            else:
                print("That is not a valid word. Choose another word instead")
    return score

#
# Problem #6: Playing a game
#


#
# procedure you will use to substitute a letter in a hand
#

def substitute_hand(hand, letter):
    copy_hand = hand.copy()
    available_letter = ''
    new_letter = ''
    for i in string.ascii_lowercase:
        if i not in copy_hand.keys():
            available_letter += i
    if letter in copy_hand.keys():
        new_letter = random.choice(available_letter)
        copy_hand[new_letter] = copy_hand[letter]
        del(copy_hand[letter])
    return copy_hand


def play_game(word_list):
    hand_number = int(input("Enter total number of hands: "))
    total_score = 0
    sub = False
    replay = False

    while hand_number > 0:
        if sub == False:
            hand = deal_hand(HAND_SIZE)
            print("Current hand: "), display_hand(hand)
            if input("Would you like to substitute a letter? yes/no") == 'yes':
                letter = str(input('Which letter to replace: '))
                hand = substitute_hand(hand, letter)
                sub = True
        score = play_hand(hand, word_list)
        if replay == False and input("Would you like to replay the hand? yes/no") == 'yes':
            replay == True
            replay_score = play_hand(hand, word_list)
            if score < replay_score:
                score = replay_score

        hand_number -= 1
        total_score += score

    print('Total score is: ', total_score)


#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
