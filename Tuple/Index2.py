def palind(r):
    e = len(r) -1
    s = 0
    while(s<e):
        if(r[s]!=r[e]):
            return False
        s+=1
        e-=1
    return True
r = ("Hannah")
if(palind(r)):
    print("The tuple is a Palindrome")
else:
    print("The tuple is not Palindromic")    