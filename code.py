import csv
import datetime

###################################################################################################
                              #INTITALIZEING#
f=open('cred','a+',newline='')#centralized file #intializing cred username password
stuwriter1 = csv.writer(f) 
data1 = [ ]
header1 = ['Username','password']
data1.append(header1)
stuwriter1.writerows(data1)
f.close()

        ####creating a rating file#####

frate=open("rating_info","a+",newline="")
ratewriter=csv.writer(frate)
data24=[]
header24=["ratings"]
data24.append(header24)
ratewriter.writerow(data24)
frate.close()
        #####defining a rating function#####

def rate():
    frate=open("rating_info","a+",newline="")
    rw=int(input("Please rate us!!,from 0-5 :"))
    data25=[]
    header25=[rw]
    data25.append(header25)
    frate.close()

        #####rating value####
def ratevalue():
    global n
    n=5
    fte=open("rating_info","a+",newline="")
    reader2 = csv.reader(fte)
    rows2=[]
    for a in reader2:
     rows2.append(a)
    for i in range(len(rows2)):
        n+=i
        n=n/i
    
    print("our rating is:",n,"\n")
    

fh = open("user_info","a+",newline='') #centralized file #intializing user info 
stuwriter2 = csv.writer(fh) 
data2 = [ ]
header2 = ['Username ','NAME','PHONE_NUMBER',' ADRESS ','EMAIL']
data2.append(header2)
stuwriter2.writerows(data2)
fh.close()

f=open('booksinfo','a+',newline='')#centralized file #intializing bookinfo- bookname and book author
stuwriter1 = csv.writer(f) 
data1 = [ ]
header1 = ['Book Name', 'Author\'s name']
data1.append(header1)
stuwriter1.writerows(data1)
f.close()

f=open('bookuhavered','a',newline='')#initializing bookuhavered file
fwriter = csv.writer(f)
data=[]
header1 = ['Book ID ', 'Book details']
data.append(header1)
fwriter.writerows(data)

f.close()

global key
key='csolm2022project'
####################################################################################################
                     #PROGRAM DEFINATION#
def forcreateaccount():
    fh = open("user_info","a+",newline='') 
    stuwriter2 = csv.writer(fh) 
    data2 = [ ]
    
    name = str(input("Enter Name : "))
    phone_no =str(int(input("Enter Phone Number : ")))

    username=''
    namelist=list(name)
    for n in range (5):
        for i in namelist[n]:
            for b in  i :
                username+=b

    username+='@'
    pnolist=list(phone_no)
    for n in range (5):
         for i in pnolist[n]:
              for b in  i :
                 username+=b
                    
    adress = str(input("Enter adress : "))
    email= str(input("Enter email id : "))

    rec2 = [username,name,phone_no, adress, email ] 
    data2.append(rec2)
    stuwriter2.writerows(data2)
    print('Your username is :',username)

    f0=open(username,'w')
    f0.close()

    f=open('cred','a+',newline='')#for password
    stuwriter1 = csv.writer(f)
    psswd=str(input("Enter  password : "))
    data1=[]
    rec1 = [username,psswd]
    data1.append(rec1)
    stuwriter1.writerows(data1)
    f.close()

    fh.close()
    main()

def forcredentials():
    f=open('cred','a+',newline='')
    stuwriter1 = csv.writer(f)
    psswd=str(input("Enter  password : "))
    data1=[]
    rec1 = [username,psswd]
    data1.append(rec1)
    stuwriter1.writerows(data1)
    f.close()

def forlogin():
    f=open('cred','r',newline='')
    reader=csv.reader(f)
    rows=[]
    c=1
    for row in reader:
        rows.append(row)
    user=input('Enter your username: ')
    psswd=input('Enter your password:')

    for i in rows:
        if i[0]==str(user):
            print()
            print('Corrrect username')
            if i[1]==str(psswd):
                print()
                print('Correct pssword')
                c=c+1
                f0=open(user,'a+')
                wr=csv.writer(f0)
                a=str(datetime.datetime.now())
                d=['last login at']
                d.append(a)
                wr.writerow(d)
                f0.close()
                break
            else:
                print()
                print('Incorrect Password')
                forlogin()

    if c==1:
        print()
        print('Incorrect Username')
        forlogin()
    global usename
    usename=user
    main3()

def addbook():
    f=open('booksinfo','a+',newline='')
    stuwriter1 = csv.writer(f)
    bokname=str(input('Enter the name of the book :'))
    bokauthor=str(input('Enter the name of  Author of this book :'))
    data1=[]
    rec1 = [bokname,bokauthor]
    data1.append(rec1)
    stuwriter1.writerows(data1)
    f.close()

def readabook():
     f=open('bookuhavered','a',newline='')
     f1=open('booksinfo','r',newline='')
     reader1 = csv.reader(f1)
     rows1=[]
     for row in reader1:
         rows1.append(row)
     global bookid
     bookid=0

     print('Choose the book of your choice by typing the  serial number of the book: ')
     for i in range(len(rows1)):
         print(i,'-',rows1[i][0])
     print()
     while bookid==0:
         bokid=int(input('Enter the serial number:'))
         if bokid==0 or bokid>=len(rows1) :
              print('Please choose a correct serial number')
              continue
         else:
             bookid=bokid
     rate()
     f0=open(usename,'a',newline='')
     wr=csv.writer(f0)
     l=[]
     l.append(bookid)
     wr.writerow(l)
     f0.close()

     wr1=csv.writer(f)
     l=[]
     l.append(bookid)
     l.append(rows1[bookid][0]+' by '+rows1[bookid][1])
     wr1.writerow(l)
     f.close()
     

def bookuhaveread():
    f=open('bookuhavered','r',newline='')
    reader= csv.reader(f)
    rows=[]
    for row in reader:
        rows.append(row)
    print(rows[0][0],',',rows[0][1])
    for i in range(1,len(rows)):
        print(rows[i][0],',',rows[i][1])

    f.close()

def recomendabook():
    f=open('bookuhavered','r',newline='')
    reader= csv.reader(f)
    rows=[]
    l=[]
    for row in reader:
        rows.append(row)
    for i in range(1,len(rows)):
        l.append(rows[i][0])

    print('These are some  Books that we highly recomend')
    print()
    f1=open('booksinfo','r',newline='')
    reader1 = csv.reader(f1)
    rows1=[]
    for row in reader1:
        rows1.append(row)

    for a in l:
        if (int(a)+1)<=len(rows)and str(int(a)+1)not in l :
           print(rows1[int(a)+1][0],' by ',rows1[int(a)+1][1])
        
    print()    
    a=input('If you want to read these books press\'y ')
    if a=='y'or a=='Y':
        readabook() 

    f.close()
    f1.close()

def donate():
    doner=open("donate_info","a+",newline="")
    stuwriter3 = csv.writer(doner)
    bokn=str(input('Enter the name of the book :'))
    bokau=str(input('Enter the name of  Author of this book :'))
    data3=[]
    rec3 = [bokn,bokau]
    data3.append(rec3)
    stuwriter3.writerows(data3)
    doner.close()

def request():
    req=open("request_info","a+",newline="")
    stuwriter4 = csv.writer(req)
    bokna=str(input('Enter the name of the book :'))
    bokaut=str(input('Enter the name of  Author of this book :'))
    data4=[]
    rec4 = [bokna,bokaut]
    data4.append(rec4)
    stuwriter4.writerows(data4)
    doner.close()

def forlogout():
    f0=open(usename,'a+')
    wr=csv.writer(f0)
    a=str(datetime.datetime.now())
    d=['last logout at']
    d.append(a)
    wr.writerow(d)
    f0.close()

#######################################################################################################
                                #MAIN PROGRAM #
def main():
     ratevalue()
     
     abc=sal()
     print('Welcome ',abc,"\n")

     print('Want to create a new acoount press \'1\' ')
    
     print('Already a customer , wanna! login press \'2\' ')
     b=str(input())
     
     if b=='1':
         print('ok!!')
         forcreateaccount()
         
         
     elif b=='2':
         print('Ok!!')
         print('Want to login as a coustomer press \'1\'' )
         print('Or as a manager press \'2\'') 
         a=str(input())
         if a=='1':
             forlogin()
         elif a=='2':
             formanager()
         else:
            print('Enter the correct number')
            print()
            main()
     else:
        print('Enter the correct number')
        print()
        main()

              ################################################
                             #mangement#
def formanager():
    a=str(input('Enter the key'))
    if a=='csolm2022project':
        main2()

def main2():
        print()
        print('Welcome Sir/Mam')
        print()
        print('1.Want to add a book to the server')
        print('2.Want  to see the  number of  customers' )
        print('3. Want to see the deails of the customers' )
        print('4.Want  to see the  number of  books donated' )
        print("5.want to see books donated")
        print("6.Want to see books requested")
        print('\'More options to come as we upgrade\'')
        b=str(input('Enter the Choice'))
        if b=='1':
            addbook()
            main2()

        elif b=='2':
            f=open('user_info','r',newline='')
            reader= csv.reader(f)
            rows=[]
            
            for row in reader:
                rows.append(row)

            print(len(rows))
            f.close()
            main2()
            
        elif b=='3':
            f=open('user_info','r',newline='')
            reader= csv.reader(f)
            rows=[]
               
            for row in reader:
                rows.append(row)

            print()
            for i in range (0,len(rows)):
                print(rows[i][0],'/',rows[i][1],'/',rows[i][2],'/',rows[i][3],'/',rows[i][4])
            f.close
            main2()
            
        elif b=="4":
            fno=open('donate_info','r',newline='')
            reader= csv.reader(fno)
            rows=[]
            
            for row in reader:
                rows.append(row)

            print(len(rows))
            fno.close()
            main2()

        elif b=="5":
            fne=open('donate_info','r',newline='')
            reader= csv.reader(fne)
            rows=[]
               
            for row in reader:
                rows.append(row)

            print()
            for i in range (0,len(rows)):
                print(rows[i][0],'/',rows[i][1])
            fne.close()
            main2()

        elif b=="6":
            fnd=open('request_info','r',newline='')
            reader= csv.reader(fne)
            rows=[]
               
            for row in reader:
                rows.append(row)

            print()
            for i in range (0,len(rows)):
                print(rows[i][0],'/',rows[i][1])
            fnd.close()
            main2()
            
        else:
            print()
            print('Enter the correct number')
            print()
            main2()
        ################refrence########################
def sal():
    gender=input("Please enter your sex : male or female    :  ")
    
    if gender=="male"or"Male":
        return "sir"
    elif gender=="Female":
        return "Mam"

        ########################## Main code ##########################################
def main3():
        abc=sal()
        print('Welcome ',abc)
        print()
        print('1.Want to read a book ')
        print('2.Want  to see the books that you have read' )
        print('3. Want to get some book  recomendation from us ' )
        print("4.Want to donate a book")
        print("5.Want to request a book")
        print('6. \'Done for the day\',want to log out') 
        print('\'More options to come as we upgrade\'')
        b=str(input('Enter the Choice'))

        if b=='1' :
            print()
            readabook()
            main3()
             
        elif b=='2':
            print()
            bookuhaveread()
            main3()
            
            
        elif b=='3':
            print()
            recomendabook()
            main3()

        elif b=="4":
            print()
            donate()
            main3()

        elif b=="5":
            print()
            request()
            main3()

        elif b=='6':
            print()
            forlogout()
            
            
        else:
            print('Enter the correct number')
            print()
            main3()

###########################################################
          #Calling#
main()


