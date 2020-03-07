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



# no idea
sent = "8one 003number 201numbers li-000233le number444"
n = 4
def nthNumber(s, n):
    pattern = "\D*(?:\d+\D+){" + str(n-1) + "}0*(\d+)"
    return re.match(pattern, s).group(1)
nthNumber(sent,n)
#233