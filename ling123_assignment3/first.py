import codecs
import re

file_in = codecs.open("testing.txt","r","utf-8")
text = file_in.read()
file_in.close()

# matches = re.findall(r"\b([0-9]|[1-9][0-9]|100)\b", "0, 1, 2, 55, 100, 101")

# matches = re.findall(r"\b(-?[0-9]|[1-9][0-9]|[1-9][0-9][0-9]|10[0-3][0-9]|104[0-5])\b", "0, 1, ,-1 2, 55, 100, 1045")

# matches = re.findall(r"[24]?A[0-9]\+?", "A0, A6, A13 ,A3+, 2A0, 3A0, asdasda")

# matches = re.findall(r"\b(A[0-9]|A1[0-3])\b", "A0, A6, A13 ,A3+, 2A0, 3A0, asdasda")
#
#
#

# matches = re.findall(r"([24]A0|A[013]\+?|A[4-9]|A1[0-3])", "A0, A6, A13 , A3+, 2A0, 4A0, asdasda")

matches = re.findall(r"[A-Za-zæøåÆØÅ0-9]{3}", "aaa, aaaa, æøå, u123, a")

# matches = re.findall(r"\d{3}-\d\d-\d{5}-\d{2}-\d", "978-92-95055-02-5, 000-92-95055-02-5")

# matches = re.findall(r"511[5-9]|5121", "5115, 5116, 5117, 5118, 5119, 5121 ")

print(matches)