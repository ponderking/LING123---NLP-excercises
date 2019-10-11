import codecs
from collections import defaultdict

# Code responsible for reading a locally stored text-file. The text in this file is then stored as a variable (text)
# ready to be proccesed.
file_in = codecs.open("ttr_input.txt","r","utf-8")
text = file_in.read()
file_in.close()

# split the list entire text into a list of all words by separating the text by empty space.
tokens = text.split(" ")
# The amount of tokens is equal the length of this list.
token_amount = len(tokens)
# The amount of types can be found by converting the list of words into a set. This works because a set only contains
# unique values and will hence remove duplicate words.
type_amount = len(set(tokens))



# alternative solution with defaultdict. This code goes through all tokens and increments
# type_amount only on new tokens we have not encountered so far in the loop.

# type_amount = 0
# freq = defaultdict(int)
# for token in tokens:
#     if freq[token] != True:
#         type_amount += 1
#         freq[token] = True


# formula for calculating TTR.
type_token_ratio = (type_amount / token_amount) * 100
# in the following line I use the round function the restrict the output to only two decimal places.
print("TTR is: ", round(type_token_ratio, 2),"percent")