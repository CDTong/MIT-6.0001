import string

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    def __init__(self, text):
        self.message_text=text
        self.vaild_words=load_words(WORDLIST_FILENAME)

    def get_message_text(self):
        return self.message_text

    def get_valid_words(self):
        return self.vaild_words

    def build_shift_dict(self, shift):
        map_letter={}
        string_low=string.ascii_lowercase
        string_upp=string.ascii_uppercase
        for i in range(26):
            if shift+i<26:
                map_letter[string_low[i]]=string_low[shift+i]
                map_letter[string_low[i]]=string_low[shift+i]
            else:
                map_letter[string_low[i]]=string_low[shift+i-26]
                map_letter[string_low[i]]=string_low[shift+i-26]
        return map_letter

    def apply_shift(self, shift):
        dict=self.build_shift_dict(shift)
        shifted_message=[]
        for let in self.message_text:
            shifted_message.append(dict[let])
        return ''.join(shifted_message)

class PlaintextMessage(Message):
    def __init__(self, text, shift):
        Message.__init__(self,text)
        self.get_encryption_dict=self.build_shift_dict(shift)
        self.message_text_encrypted=self.apply_shift(shift)
        self.shift=shift

    def get_shift(self):
        return self.shift

    def get_encryption_dict(self):
        return self.get_encryption_dict

    def get_message_text_encrypted(self):
        return self.message_text_encrypted

    def change_shift(self, shift):
        self.get_encryption_dict=self.build_shift_dict(shift)
        self.message_text_encrypted=self.apply_shift(shift)
        self.shift=shift
        return

class CiphertextMessage(Message):
    def __init__(self, text):
        Message.__init__(self,text)

    def decrypt_message(self):
        max_shift_value = 0
        max_word_num = 0

        for shift in range(26):
            word_num = 0
            temp_text = self.apply_shift(shift)
            temp_text_list = temp_text.split()
            for word in temp_text_list:
                if is_word(self.get_valid_words(), word):
                    word_num +=1
                if word_num > max_word_num:
                    max_shift_value = shift
                    max_word_num = word_num

        return (max_shift_value, self.apply_shift(max_shift_value))

if __name__ == '__main__':

   #Example test case (PlaintextMessage)
   plaintext = PlaintextMessage('hello', 2)
   print('Expected Output: jgnnq')
   print('Actual Output:', plaintext.get_message_text_encrypted())

   #Example test case (CiphertextMessage)
   ciphertext = CiphertextMessage('jgnnq')
   print('Expected Output:', (24, 'hello'))
   print('Actual Output:', ciphertext.decrypt_message())

    #TODO: WRITE YOUR TEST CASES HERE


    #TODO: best shift value and unencrypted story 
