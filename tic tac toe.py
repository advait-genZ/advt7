l=['','','','','','','','','']
for i in range(len(l)):
    n=int(input("Enter the place no. between 0 & 8"))
    if n>8 or n<0:
        print("The no. should be between 0 and 8")
    else:
        if l[n]=='':
            l[n]='X'
            
        else:
            print("that place already has a value")
    if n==0 or n==3 or n==6:
        if l[n]==l[n+1]=='X':
            l[n+2]='O'
        elif l[n+2]==l[n]=='X':
            l[n+1]='O'
    if n==1 or n==4 or n==7:
        if l[n]==l[n+1]=='X':
            l[n-1]='O'
        elif l[n]==l[n-1]=='X':
            l[n+1]='O'
    if n==2 or n==5 or n==8:
        if l[n]==l[n-1]=='X':
            l[n-2]='O'
        elif l[n]==l[n-2]=='X':
            l[n-1]='O'
    if n<3:
        if l[n]==l[n+3]=='X':
            l[n+6]='O'
        if l[n+6]==l[n]=='X':
            l[n+3]='O'
    if n>2 and n<6:
        if l[n]==l[n+3]=='X':
            l[n-3]='O'
        if l[n-3]==l[n]=='X':
            l[n+3]='O'
    if n>5 and n<9:
        if l[n]==l[n-3]=='X':
            l[n-6]='O'
        if l[n]==l[n-6]=='X':
            l[n-3]='O'
    l1=[[0,4,8],[2,4,6]]
    for j in l1:
        if n in j:
            j.remove(n)
            if l[j[0]]=='X':
        
                l[j[1]]='O'
            if l[j[1]]=='X':
                l[j[0]]=='O'
    print(l) 
    if l[0]==l[1]==l[2]=='X' or l[3]==l[4]==l[5]=='X' or l[6]==l[7]==l[8]=='X':
        print("you won")
        break
    if l[0]==l[4]==l[8]=='X' or l[2]==l[4]==l[6]=='X':
        print("you won")
        break
    if l[0]==l[3]==l[6]=='X' or l[1]==l[4]==l[7]=='X' or l[2]==l[5]==l[8]=='X':
        print("you won")
        break
for k in range(len(l)):
    if l[k]!='':
        print("this match is a tie")
        break
