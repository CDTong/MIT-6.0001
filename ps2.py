import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    for i in secret_word:
        if i not in letters_guessed:
            return False
    return True


def get_guessed_word(secret_word, letters_guessed):
    guessed_word = ''
    for i in secret_word:
        if i in letters_guessed:
            guessed_word += i
        else:
            guessed_word += '_'
    return guessed_word


def get_available_letters(letters_guessed):
    available_letters = ''
    for i in string.ascii_lowercase:
      if i not in letters_guessed:
        available_letters+=i
    return available_letters


def check_guess_vaild(user_guess,letters_guessed):
  if len(user_guess)>1 or (not str.isalpha(user_guess)):
    print("It is not a vaild letter.",end='')
    return False
  if user_guess in letters_guessed:
    print("You have already guessed that letter",end='')
    return False
  return True


def hangman(secret_word):
  letters_guessed=[]
  guesses_remaining=6
  warning_remaining=3

  print("Welcome to HANGMAN")
  print(f"I am think of a word {len(secret_word)} letters long")
  print(f"You have {warning_remaining} warnings left")

  while guesses_remaining>0 and (not is_word_guessed(secret_word,letters_guessed)):
    print(f"You have {guesses_remaining} guesses left")
    print("Availbale letters: ",get_available_letters(letters_guessed))
    user_guess=input("Please guess a letter: ")
    if not check_guess_vaild(user_guess,letters_guessed):
      if warning_remaining>0:
        warning_remaining-=1
        print(f"You have {warning_remaining} warnings left")
      else:
        guesses_remaining-=1
        print("You have no warning left, you lose.",end ='')
        
      print(get_guessed_word(secret_word,letters_guessed))
      continue
    letters_guessed.append(user_guess)
    if user_guess in secret_word:
      print("Yes: ",end='')
    else:
      print("NO: ",end='')
      guesses_remaining-=1
      if user_guess in 'aeiou':
        guesses_remaining-=1
    print(get_guessed_word(secret_word,letters_guessed))
  
  print("-"*10)
  if is_word_guessed(secret_word,letters_guessed):
    print("YOU WIN")
    print("Total score is: ",guesses_remaining * len(set(list(secret_word))))
  else:
    print("YOU LOSE. The word was:",secret_word)


def match_with_gaps(my_word, other_word):
  visable_letter=[]
  hidden_letter=[]
  my_word=my_word.replace("_","_")

  if len(my_word)!=len(other_word):
    return False
  for i in range(len(my_word)):
    if my_word[i]=="_":
      hidden_letter.append(other_word[i])
    else:
      if my_word[i]!=other_word[i]:
        return False
      else:
        visable_letter.append(other_word[i])

      for hidden in hidden_letter:
        if hidden in visable_letter:
          return False
  return True


def show_possible_matches(my_word):
  match_word=0
  for word in wordlist:
    if match_with_gaps(my_word,word):
      print(word,end='\n')
      match_word+=1
  if match_word==0:
    print("No match word",end='')
  print()


def hangman_with_hints(secret_word):
  letters_guessed=[]
  guesses_remaining=6
  warning_remaining=3
  my_word=''

  print("Welcome to HANGMAN")
  print(f"I am think of a word {len(secret_word)} letters long")
  print(f"You have {warning_remaining} warnings left")

  while guesses_remaining>0 and (not is_word_guessed(secret_word,letters_guessed)):
    print(f"You have {guesses_remaining} guesses left")
    print("Availbale letters: ",get_available_letters(letters_guessed))
    user_guess=input("Please guess a letter: ")

    #hints
    if user_guess=="*":
      print("Possible word matches are: ")
      show_possible_matches(my_word)
      continue

    if not check_guess_vaild(user_guess,letters_guessed):
      if warning_remaining>0:
        warning_remaining-=1
        print(f"You have {warning_remaining} warnings left")
      else:
        guesses_remaining-=1
        print("You have no warning left, you lose.",end ='')
        
      print(get_guessed_word(secret_word,letters_guessed))
      continue
    letters_guessed.append(user_guess)
    if user_guess in secret_word:
      print("Yes: ",end='')
    else:
      print("NO: ",end='')
      guesses_remaining-=1
      if user_guess in 'aeiou':
        guesses_remaining-=1
    my_word=get_guessed_word(secret_word,letters_guessed)
    print(my_word)
  
  print("-"*10)
  if is_word_guessed(secret_word,letters_guessed):
    print("YOU WIN")
    print("Total score is: ",guesses_remaining * len(set(list(secret_word))))
  else:
    print("YOU LOSE. The word was:",secret_word)


if __name__ == "__main__":
  #1
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

  #2
    # secret_word = choose_word(wordlist)
    # hangman_with_hints(secret_word)
