import string
from ps4a import get_permutations

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


### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

# you may find these constants helpful
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'

class SubMessage(object):
    def __init__(self, text):
        self.massage_text=text
        self.vaild_words=load_words(WORDLIST_FILENAME)
    
    def get_message_text(self):
        return self.massage_text

    def get_valid_words(self):
        return self.vaild_words.copy()
                
    def build_transpose_dict(self, vowels_permutation):
        transpose_dict={}
        for i in range(5):
            transpose_dict[VOWELS_LOWER[i]]=vowels_permutation[i].lower()
            transpose_dict[VOWELS_UPPER[i]]=vowels_permutation[i].upper()
        for j in range(21):
            transpose_dict[CONSONANTS_LOWER[j]] = CONSONANTS_LOWER[j]
            transpose_dict[CONSONANTS_UPPER[j]] = CONSONANTS_UPPER[j]
        return transpose_dict.copy()


    def apply_transpose(self, transpose_dict):
        encrypt_message = ''
        for char in self.get_message_text():
            if char in transpose_dict:
                encrypt_message += transpose_dict[char]
            else:
                encrypt_message += char
        
        return encrypt_message
        
class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        SubMessage.__init__(self,text)
    def decrypt_message(self):
        result=[0,0]
        word_list=self.get_valid_words()
        vowel_perms=get_permutations("aeiou")
        for perm in vowel_perms:
            v_dict=self.build_transpose_dict(perm)
            new_phrase=self.apply_transpose(v_dict)
            new_words=new_phrase.split()
            count=0
            for word in new_words:
                if is_word(word_list,word):
                    count+=1
                if count>result[0]:
                    result=[count,new_phrase]
        return result[1]
    

if __name__ == '__main__':

    # Example test case
    message = SubMessage("Hello World!")
    permutation = "eaiuo"
    enc_dict = message.build_transpose_dict(permutation)
    print("Original message:", message.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "Hallu Wurld!")
    print("Actual encryption:", message.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print("Decrypted message:", enc_message.decrypt_message())
     
    #TODO: WRITE YOUR TEST CASES HERE
