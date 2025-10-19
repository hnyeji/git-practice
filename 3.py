s='apple banana apple orange banana apple'
s=s.split()

word_list=[]
count_list=[]

for i in s:
    if i not in word_list:
        word_list.append(i)
        count_list.append(1)
    else:
        count_list[word_list.index(i)]+=1

Max=max(count_list)
Max_word=word_list[count_list.index(Max)]

print(Max_word, Max)