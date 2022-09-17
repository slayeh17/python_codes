sen=input("Enter a string: ")
n=int(input("Enter the number of words to be replaced: "))
rep={}
for i in range(n):
    or_word=input("Enter the word to be replaced: ")
    re_word=input("Enter the new word: ")
    rep[or_word]=re_word
words=sen.split(" ")
s=""
for w in words:
    if w in rep.keys():
        s+=rep[w]+" "
    else:
        s+=w+" "
print(s)