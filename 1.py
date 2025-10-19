s = "This is is a a Test test TEST"
s=s.lower()
s=s.split()
words=[]
for i in s:
    if i not in words:
        words.append(i)
print(words)
