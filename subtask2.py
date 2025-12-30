def naturalNB():
    n=0 #counter
    s=0 #sum
    m=None #minimum
    while True:
        nb=int(input("Enter a natural number (-1 to stop):"))
        if nb==-1:
            break
        n+=1
        s+=nb
        if m is None or nb<m:
            m=nb
if n==0:
       m=-1
       a=-1
else:
       a=s/n
print("n= ",n)
print("s= ",s)
print("m= ",m)
print("a= ",a)

naturalNb()
# it looks like I learned how to use git today
