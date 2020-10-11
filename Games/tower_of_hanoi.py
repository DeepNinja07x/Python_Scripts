def toh(n,s,t,d):
    if n==1:
        print(s,'-->',d)
        return
    toh(n-1,s,d,t)
    print(s,'-->',d)
    toh(n-1,t,s,d)

if __name__=="__main__":
    while 1:

        n = int(input('''Enter number of disks:'''))

        if n<0:
            print("Try Again with a valid input")
            continue
        elif n==0:
            break
        toh(n,'Source','Temporary','Destination')

        print('ENTER 0 TO EXIT')

