# your code goes here!

    
class Anagram:
    def __init__(self,word):
        self.word = word.lower()
        self.sorted_word = sorted(self.word)

    def match(self,list):
        return [
            wrd for wrd in list
            if sorted(wrd.lower()) == self.sorted_word and wrd.lower() != self.word
        ]

        
    
