s=input('Enter your string: ')
i,j,ans,d=0,0,0,{}


while i < len(s):
    
    if s[i] not in d or j>d[s[i]]:
        d[s[i]]=i
        ans=max(ans,i-j+1)

    else:
        j=d[s[i]]+1
        ans=max(ans,i-j+1)
        i-=1

    i+=1

print(ans)