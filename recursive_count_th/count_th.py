'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

#go through the whole word using recursion and no loops
def count_th(word):
        #set base case where length of word is less than or equal to 1 (it's ok if the word has one letter since we know you can't get 'th' from one letter)
      if len(word) <= 1:
        return 0
        #function will use recursion and go through the word until it reaches the last letter.  It will return 0 for this last letter and then complete function on last two letters.
        #check to see if the first letter of the word is "t" and the second letter of the word is "h"
      elif word[0]=="t" and word[1] == "h":
        #if so add 1 to what you are returning and complete already started function at previous letter
            return 1+count_th(word[1:])
      else:
        #if not add nothing and complete already started function at previous letter
            return count_th(word[1:])

