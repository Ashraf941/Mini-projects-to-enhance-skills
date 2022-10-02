s=input("Enter your roman number: ")
def romantoint(s):
    s=s.replace(' ','')
    s=s.upper()
    roman_dict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    i=len(s)-1
    result=0
    while i>=0:
        if roman_dict[s[i]] > roman_dict[s[i-1]]:
            result+= roman_dict[s[i]]-roman_dict[s[i-1]]
            s=s[:i-1]
            i-=2
        else:
            result+=roman_dict[s[i]]
            s=s[:i+1]
            i-=1
    return result
print()
print(romantoint(s))