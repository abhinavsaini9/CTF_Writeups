flag=list("Once upon a time the original flag was here...")
base=1
sum=1
l=len(flag)
for i in range(0,l+1,2):
    for j in range(i):
        flag[j]=chr(ord(flag[j])^1337)
    base<<=1
    sum^=base
for i in range(1,l+1,2):
    for j in range(i):
        flag[j]=chr(ord(flag[j])^42)
    base<<=1
    sum^=base

for i in range(l):
    flag[i]=chr(ord(flag[i])<<1)

enc_flag="".join(flag)

print(enc_flag) # present in 'encrypted_flag.txt'
