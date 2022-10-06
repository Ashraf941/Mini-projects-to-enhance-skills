s=input("Enter your list:")
s=s.split(',')
def longestprefix(lst):
    size = len(lst)
    if size==0:
        return ''
    if size==1:
        return lst[0]
    lst.sort()
    end= min(len(lst[0]),len(lst[size-1]))

    i=0
    while i<end and lst[0][i]==lst[size-1][i]:
        i+=1
    prfx=lst[0][0:i]
    return prfx

print(longestprefix(s))
