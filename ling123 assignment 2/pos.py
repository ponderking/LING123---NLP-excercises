import codecs
import re
from collections import defaultdict

# Code responsible for reading a locally stored text-file. The text in this file is then stored as a variable (text)
# ready to be proccesed.
file_in = codecs.open("pos_input.txt","r","utf-8")
text = file_in.read()
file_in.close()

# split all word/tag combinations into its own list.
pos_tags = text.split(" ")
# empty lists of all data I wish to collect.
nouns = []
prons = []
propns = []
sequences = []


# a loop that goes through each token/tag combination and finds all occurances of a
# PUNCT tag being followed by a NOUN, PRON or PROPN tag.
# The loop finds these sequences and also makes lists of nouns, prons and propns.

index = 0
for tag in pos_tags:
    if tag.split("/")[1] == "PUNCT":
        if index < len(pos_tags)-1:
            # find out if next token is noun, pron or propn.
            # first we split the token/tag combination into a token and a tag.
            next_tag = pos_tags[index+1].split("/")[1]
            next_token = pos_tags[index + 1].split("/")[0]
            if next_tag == "NOUN" or next_tag == "PRON" or next_tag == "PROPN":
               sequences.append(tag+ " " + pos_tags[index+1])
            if next_tag == "NOUN":
               nouns.append(next_token)
            elif next_tag == "PRON":
               prons.append(next_token)
            elif next_tag == "PROPN":
               propns.append(next_token)
    index += 1

# # A potential regex solution
# nouns = re.findall(r"[?,.:\-]/PUNCT\s\w+/NOUN", text)
# prons = re.findall(r"[?,.:\-]/PUNCT\s\w+/PRON", text)
# propns = re.findall(r"[?,.:\-]/PUNCT\s\w+/PROPN", text)


# calculating the frequencies of all NOUNS, all PRONs and all PROPNs.
noun_freq = defaultdict(int)
pron_freq = defaultdict(int)
propn_freq = defaultdict(int)
for noun in nouns:
    noun_freq[noun] += 1
for pron in prons:
    pron_freq[pron] += 1
for propn in propns:
    propn_freq[propn] += 1

print("\nFrequencies of nouns: ")
print(noun_freq.items(), "\n\n")
print("Frequencies of prons: ")
print(pron_freq.items(), "\n\n")
print("Frequencies of propns: ")
print(propn_freq.items(), "\n\n")


# calculating the frequencies of all sequences found. Then it finds the sequence with the highest frequency.
seq_freq = defaultdict(int)
for sequence in sequences:
    seq_freq[sequence] += 1
print("Frequencies of desired sequences: ")
print(seq_freq.items(), "\n\n")

# The data is sorted in decreasing order, meaning that the highest frequency can be found at index 0.
sorted_data = sorted(seq_freq .items() , key=lambda x: x[1], reverse=True)
highest_frequency = sorted_data[0]
print("Highest sequence-frequency:", highest_frequency)

