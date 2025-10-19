A = [1,3,5,9]
B = [2,2,6,7]
C=A+B
for i in range(len(C)):
    for j in range(i+1, len(C)):
        if C[i]>C[j]:
            C[i],C[j]=C[j],C[i]
print(C)
