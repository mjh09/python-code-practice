sent = "This is an example of *correct* sentence."

def isSentenceCorrect(sentence):
    # ^ starts with -- [^]* no occur inbetween -- [!.?]$ endswith
    pattern = '^[A-Z][^?!.]*[?.!]$'
    return re.match(pattern, sentence) is not None

isSentenceCorrect(sent)

sent = "CodeFight On"

def swapAdjacentWords(s):
    # forst pat - word -no word- word, 3 sequence flip
    return re.sub(r'(\w+)(\W+)(\w+)', r'\3\2\1', s)
    
swapAdjacentWords(sent)