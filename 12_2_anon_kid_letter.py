# this problem is about building letters from a catalogue
# basically are all the characters of the letter included in the catalogue 
import collections

def is_possible(letter, mag):
    ispossible = False 
    letterFrequency = collections.Counter(letter) #build a dictionnary containing
    #each characters and its frequency

    # count all occurrences in letter
    # check if each occurrences exist in catalogue
    for c in mag:
        if c in letterFrequency:
            letterFrequency[c] -= 1
            if letterFrequency[c] == 0:
                del letterFrequency[c]
                if not letterFrequency:
                    # all characters have been counted
                    return True
        


    return not letterFrequency # return True if no letter left. 

print(is_possible(l,c))


