s = 'Programming is fun'
result=''
for i in s:
    if i not in 'aeiouAEIOU':
        result+=i
print(result)
