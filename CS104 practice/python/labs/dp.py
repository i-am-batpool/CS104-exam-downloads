'''
    Let's go to casino
    Author: Saksham Rathi
'''
import sys
# Please write your code in this file.
n=int(sys.argv[1])
ls =[0]*(n+1)
ls[0]=1
for i in range((n+1)):
    for j in range(1,7):
        if ((i+j)<=n):
            ls[i+j]=(ls[i+j]+(ls[i]%1000000007))%1000000007
            
print(ls[n])