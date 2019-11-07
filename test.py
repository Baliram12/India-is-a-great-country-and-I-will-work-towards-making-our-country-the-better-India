from collections import Counter
s="India is a great country and I will work towards making our country  the better India"
s=s.split(' ')
word=[item for items, c in Counter(s).most_common() for item in [items] * c]
word_un=[]
for i in range (len(word))P:
    if word[i] not in word_un:
       word_un.append(word[i])
count=sorted(word_un,key=len,reverse=True)
print"Input Sentence: ",s
print"\nOutput:",count
