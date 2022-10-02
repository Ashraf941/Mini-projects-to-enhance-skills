first_name=input("Enter the first name: ")
second_name=input("Enter the second name: ")

def flames(f,s):
    name1=f.title()
    name2=s.title()
    s,f=s.replace(" ",""),f.replace(" ","")
    s,f=s.lower(),f.lower()
    if len(f)>len(s):
        for letter in f:
            if letter in s:
                f=f.replace(letter,"",1)
                s=s.replace(letter,"",1)
    else:
        for letter in s:
            if letter in f:
                s=s.replace(letter,"",1)
                f=f.replace(letter,"",1)
    length=len(s)+len(f)
    if length==0:
        print("It's the same name, weird...")
    else:
        l=["Friends","Lovers","Affectionates","Married","Enemies","Siblings"]
        def recursion(length,l):
            if len(l)==1:
                 status=str(l[0])
                 return status
            else:
                right=[]
                left=[]
                i=(length%len(l))-1
                if i+1>0:
                    right=l[i+1:]
                    left=l[:i]
                    l=right+left
                else:
                    left=l[:i]
                    l=left
                return recursion(length,l)
        print(f"{name1} and {name2} are {recursion(length,l)}")
        



flames(first_name,second_name)
