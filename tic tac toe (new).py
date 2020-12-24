l=[[],[],[],[],[],[],[],[],[]]
for i in range(len(l)):
    n=int(input("Enter the place no. between 0 & 8"))
    if n>8 or n<0:
        print("The no. should be between 0 and 8")
    else:
        if l[n]==[]:
            l[n]='X'
            print(l)
    
    if i==0 or i==3 or i==6:
        if l[i]==l[i+1]=='X':
            l[i+2]='O'
        elif l[i+2]==l[i]=='X':
            l[i+1]='O'
    if i==1 or i==4 or i==7:
        if l[i]==l[i+1]=='X':
            l[i-1]='O'
        elif l[i]==l[i-1]=='X':
            l[i+1]='O'
    if i==2 or i==5 or i==9:
        if l[i]==l[i-1]=='X':
            l[i-2]='O'
        elif l[i]==l[i-2]=='X':
            l[i-2]='O'
    if i<3:
        if l[i]==l[i+3]=='X':
            l[i+6]='O'
    if i>2 and i<6:
        if l[i]==l[i+3]=='X':
            l[i-3]='O'
    if i==4:
        if l[i]==l[i+4]=='X':
            l[0]='O'
        if l[i]==l[i+2]=='X':
            l[2]='O'
    if l[0]==l[1]==l[2]=='X' or l[3]==l[4]==l[5]=='X' or l[6]==l[7]==l[8]=='X':
        print("you won")
        break
    if l[0]==l[4]==l[8]=='X' or l[2]==l[4]==l[6]=='X':
        print("you won")
        break
    if l[0]==l[3]==l[6]=='X' or l[1]==l[4]==l[7]=='X' or l[2]==l[5]==l[8]=='X':
        print("you won")
        break
