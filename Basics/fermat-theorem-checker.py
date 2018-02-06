def check_fermat(a,b,c,n):
    l=a**n + b**n
    r=c**n
    if l==r and n>2:
        print("Fermat was wrong")
    else:
        print("No,that doesn't work")  
check_fermat(9,80,56,2)
