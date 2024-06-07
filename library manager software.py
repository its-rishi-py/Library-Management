#WAP TO MAKE A LIBRARY MANAGEMENT SYSTEM

import mysql.connector as mys
mycon=mys.connect(host='localhost',user='root',passwd='maiyakasam',database='library_manager')
cor=mycon.cursor()
print("#",'⋯'*12,'⋙ LIBRARY MANAGEMENT SOFTWARE ⋘','⋯'*12,"#")

def menu():
    print("∵∴"*27)
    print("\t\t\t  ① CENTRAL LIBRARY")
    print("\t\t\t  ② MEMBERSHIP PORTAL")
    print("\t\t\t  ③ BOOKS ISSUED")
    print("\t\t\t  ④ BOOKS RETURNED")
    print("\t\t\t  ⑤ READING IN LIBRARY")
    print("\t\t\t  ⑥ SEARCH A BOOK")
    print("\t\t\t  ⑦ SEARCH A MEMBER")
    print("\t\t\t  ⑧ FINE CALCULATOR")
    print("\t\t\t  ⑨ EXIT")
    print("∵∴"*27)

def phone():
        A=input("Phone Number ⋙ ")
        if A.isnumeric():
            X=len(A)
            if X==10:
                A=int(A)
                return A 
            else:
                print("Invalid Phone Number")
                A=phone()
                return A

def booknum():
    A=input("Book Number ⋙ ")
    if A.isnumeric():
        A=int(A)
        return(A)
    else:
        print(" Invalid Code ")
        A=booknum()
        
def bookshelf():
     A=input("Shelf Code ⋙ ")
     if A.isalnum():
        return(A)
     else:
        print(" Invalid Code ")
        A=bookshelf()

def memberID():
    A=input("Member's ID (Numeric) ⋙ ")
    if A.isnumeric():
        A=int(A)
        return(A)
    else:
        print(" Invalid ID ")
        A=memberID()
      
def memberAge():
    A=input("Member's Age ⋙ ")
    if A.isnumeric():
        A=int(A)
        return(A)
    else:
        print(" Invalid Age ")
        A=memberAge()

menu()
Munni=int(input("ENTER THE OPTION NUMBER ⋙ "))
while Munni==0 or Munni>9:
    print("Invalid Option") 
    Munni=int(input("ENTER THE OPTION NUMBER ⋙ "))
ch='y'
while Munni!=0:  
    if Munni==1:
        print("#",'⋯'*6,'⋙ CENTRAL LIBRARY ⋘','⋯'*6,"#")
        A=input("Book Title ⋙ ")
        B=booknum()
        C=bookshelf()
        D=input("Author ⋙ ")
        E=input("Category ⋙ ")
        F=input("Date of Publishing (YYYY-MM-DD) ⋙ ")
        G=input("Date of Arrival in Library (YYYY-MM-DD) ⋙ ")
        cor.execute("insert into central_lib values({0},'{1}','{2}','{3}','{4}','{5}','{6}')".format(B,A,C,D,E,F,G))   
        mycon.commit()
        print("∵∴"*27)     
        print("{~}  Book Title                           ⋙ ",A)
        print("{~}  Book Number                      ⋙ ",B)
        print("{~}  Shelf Code                         ⋙ ",C)
        print("{~}  Author                               ⋙ ",D)
        print("{~}  Category                            ⋙ ",E)
        print("{~}  Date of Publishing              ⋙ ",F)
        print("{~}  Date of Arrival in Library  ⋙ ",G)   
        print("∵∴"*27)
        ch=input("Add more ???? (enter y key to enter more\nor input any letter to return to the main menu ) ⋙ ")
        if ch=='y':
            Munni=1
        else:
            menu()
            Munni=int(input("ENTER THE OPTION NUMBER ⋙ "))     
    elif Munni==2:
        print("#",'⋯'*6,'⋙ MEMBERSHIP PORTAL ⋘','⋯'*6,"#")
        A=input("Member Name ⋙ ")
        B=memberID()
        C=phone()
        D=memberAge()
        E=input("{M for Male}\n{F for Female}\n{O for Others}\nGender of Member ⋙ ")
        F=input("Email ID (optional) ⋙ ")
        G=input("Card Issue Date (YYYY-MM-DD) ⋙ ")
        H=input("Card Expiry Date (YYYY-MM-DD)\n{Minimum 1 month} ⋙ ")
        cor.execute("insert into members values({0},'{1}',{2},{3},'{4}','{5}','{6}','{7}')".format(B,A,C,D,E,F,G,H))   
        mycon.commit()
        print("∵∴"*27)
        print("{~}  Member Name       ⋙ ",A)
        print("{~}  Member's ID         ⋙ ",B)
        print("{~}  Phone Number       ⋙ ",C)
        print("{~}  Age                       ⋙ ",D)
        print("{~}  Gender                  ⋙ ",E)
        print("{~}  Email ID                ⋙ ",F)
        print("{~}  Card Issue Date    ⋙ ",G)
        print("{~}  Card Expiry Date   ⋙ ",H)
        print("∵∴"*27)
        ch=input("Add more ???? (enter y key to enter more\nor input any letter to return to the main menu ) ⋙ ")
        if ch=='y':
            Munni=2
        else:
            menu()
            Munni=int(input("ENTER THE OPTION NUMBER ⋙ "))
    elif Munni==3:
        print("#",'⋯'*6,'⋙ BOOKS ISSUED ⋘','⋯'*6,"#")
        A=input("Book Title ⋙ ")
        B=booknum()
        C=bookshelf()
        D=input("Author ⋙ ")
        E=input("Category ⋙ ")
        F=input("Date of Publishing (YYYY-MM-DD) ⋙ ")
        G=input("Book Issue Date (YYYY-MM-DD) ⋙ ")
        H=input("Book 'to be Returned by' Date (YYYY-MM-DD)  ⋙ ")
        ZXC="{One book can be borrowed for maximum 1 week.}"
        print(ZXC)
        I=input("Member's Name ⋙ ")
        J=memberID()
        K=phone()
        cor.execute("insert into issued_books values({0},'{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}',{9},{10})".format(B,A,C,D,E,F,G,H,I,J,K))   
        mycon.commit()
        print("∵∴"*27)
        print("{~}  Book Title                                       ⋙ ",A)
        print("{~}  Book Number                                  ⋙ ",B)
        print("{~}  Shelf Code                                      ⋙ ",C)
        print("{~}  Author                                           ⋙ ",D)
        print("{~}  Category                                         ⋙ ",E)
        print("{~}  Date of Publishing                           ⋙ ",F)
        print("{~}  Book Issue Date                             ⋙ ",G)
        print("{~}  Book 'to be Returned by' Date      ⋙ ",H,)
        print(ZXC)
        print("{~}  Member's Name                              ⋙ ",I)
        print("{~}  Member's ID                                  ⋙ ",J)
        print("{~}  Phone Number                                 ⋙ ",K)
        print("∵∴"*27)
        ch=input("Add more ???? (enter y key to enter more\nor input any letter to return to the main menu ) ⋙ ")
        if ch=='y':
            Munni=3
        else:
            menu()
            Munni=int(input("ENTER THE OPTION NUMBER ⋙ "))       
    elif Munni==4:
        print("#",'⋯'*6,'⋙ BOOKS RETURNED ⋘','⋯'*6,"#")
        A=input("Book Title ⋙ ")
        B=booknum()
        C=bookshelf()
        D=input("Author ⋙ ")
        E=input("Category ⋙ ")
        F=input("Date of Publishing (YYYY-MM-DD) ⋙ ")
        G=input("Book Issue Date (YYYY-MM-DD) ⋙ ")
        H=input("Book Returned Date (YYYY-MM-DD)  ⋙ ")
        ZXC="{One book can be borrowed for maximum 1 week.}"
        I=input("Member's Name ⋙ ")
        J=memberID()
        K=phone()
        cor.execute("insert into returned_books values({0},'{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}',{9},{10})".format(B,A,C,D,E,F,G,H,I,J,K))   
        mycon.commit()
        print("∵∴"*27)
        print("{~}  Book Title                              ⋙ ",A)
        print("{~}  Book Number                         ⋙ ",B)
        print("{~}  Shelf Code                            ⋙ ",C)
        print("{~}  Author                                  ⋙ ",D)
        print("{~}  Category                               ⋙ ",E)
        print("{~}  Date of Publishing                 ⋙ ",F)
        print("{~}  Book Issue Date                    ⋙ ",G)
        print(ZXC)
        print("{~}  Book Returned on Date         ⋙ ",H,)
        print("{~}  Member's Name                    ⋙ ",I)
        print("{~}  Member's ID                         ⋙ ",J)
        print("{~}  Phone Number                        ⋙ ",K)
        print("If the book is not returned on the scheduled date or is returned in poor condition , A fine will be charged")
        
        print("∵∴"*27)
        ch=input("Add more ???? (enter y key to enter more\nor input any letter to return to the main menu ) ⋙ ")
        if ch=='y':
            Munni=4
        else:
            menu()
            Munni=int(input("ENTER THE OPTION NUMBER ⋙ "))       
    elif Munni==5:
        print("#",'⋯'*6,'⋙ READING IN LIBRARY ⋘','⋯'*6,"#")
        A=input("Book Title ⋙ ")
        B=booknum()
        C=bookshelf()
        D=input("Author ⋙ ")
        E=input("Category ⋙ ")
        F=input("Date of Publishing (YYYY-MM-DD) ⋙ ")
        G=input("(HH:MM:SS){24 hour format}\nBook Issue Time  ⋙ ")
        H=input("Book Returned Time   ⋙ ")
        I=input("Reader's Name ⋙ ")
        J=phone()
        cor.execute("insert into read_in_library values({0},'{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}',{9})".format(B,A,C,D,E,F,G,H,I,J,))   
        mycon.commit()
        print("∵∴"*27)
        print("TIMINGS :- 10:00 a.m. - 8:00 p.m.")
        print("{~}  Book Title                                      ⋙ ",A)
        print("{~}  Book Number                                 ⋙ ",B)
        print("{~}  Shelf Code                                     ⋙ ",C)
        print("{~}  Author                                           ⋙ ",D)
        print("{~}  Category                                        ⋙ ",E)
        print("{~}  Date of Publishing                          ⋙ ",F)
        print("{~}  Book Issue Time(HH:MM:SS)         ⋙ ",G)
        print("{~}  Book Returned Time(HH:MM:SS)   ⋙ ",H)
        print("{~}  Reader's Name                               ⋙ ",I)
        print("{~}  Reader's Phone Number                 ⋙ ",J)
        print("∵∴"*27)
        ch=input("enter y key to enter more/nor to return to main menu input any letter")
        if ch=='y':
            Munni=5
        else:
            menu()
            Munni=int(input("ENTER THE OPTION NUMBER ⋙ "))
    elif Munni==6:
        print("#",'⋯'*6,'⋙ SEARCH A BOOK ⋘','⋯'*6,"#")
        B=booknum()
        cor.execute("select * from central_lib where book_no={}".format(B))
        rec=cor.fetchone()
        if rec!=None:
            print(rec)
        else:
            print("No such book present in the library....")
        input("Press enter to return to the main menu")
        menu()
        Munni=int(input("ENTER THE OPTION NUMBER ⋙ "))
    elif Munni==7:
        print("#",'⋯'*6,'⋙ SEARCH A MEMBER ⋘','⋯'*6,"#")
        B=memberID()
        cor.execute("select * from members where mem_id={}".format(B))
        rec=cor.fetchone()
        if rec!=None:
            print(rec)
        else:
            print("No such member in the library....")
        input("Press enter to return to the main menu")
        menu()
        Munni=int(input("ENTER THE OPTION NUMBER ⋙ "))    
    elif Munni==8:
            print("#",'⋯'*6,'⋙ FINE CALCULATOR ⋘','⋯'*6,"#")
            print("\t\t\t  ⑴ Book Misplaced")
            print("\t\t\t  ⑵ Book Returned In Bad Condition")
            print("\t\t\t  ⑶ Book Not Returned \n\t\t\t      Within the mentioned 'TO BE RETURNED DATE'.")
            print("∵∴"*27)
            A=input("Member Name ⋙ ")
            B=memberID()
            C=input("Book Title ⋙ ")
            D=booknum()
            M=int(input("Enter the number which best describes your reason ⋙ "))
            if M==1:
                  print("\t\t\t  Book Misplaced")
                  print("If the book is misplaced , member will be charged ₹500/-.")
                  FINE1=500
                  print("∵∴"*27)
                  print("Member's Name                    ⋙ ",A)
                  print("Member's ID                         ⋙ ",B)
                  print("Book Title                              ⋙ ",C)
                  print("Book Number                         ⋙ ",D)
                  print("Book Misplaced")
                  print("Hence, FINE ⋙ ₹",FINE1,"/-")
                  cor.execute("insert into fine values({0},'{1}',{2},{3},{4},'{5}')".format(B,A,FINE1,M,D,C))   
                  mycon.commit()
            elif M==2:
                  print("\t\t\t  Book Returned In Bad Condition")
                  print("If the book is returned in bad condition , member will be charged ₹200/-.")
                  FINE2=200
                  print("∵∴"*27)
                  print("Member's Name                    ⋙ ",A)
                  print("Member's ID                         ⋙ ",B)
                  print("Book Title                              ⋙ ",C)
                  print("Book Number                         ⋙ ",D)
                  print("Book Returned In Bad Condition")
                  print("Hence, FINE ⋙ ₹",FINE2,"/-")
                  cor.execute("insert into fine values({0},'{1}',{2},{3},{4},'{5}')".format(B,A,FINE2,M,D,C))   
                  mycon.commit()
            elif M==3:
                  print("\t\t\t  Book Not Returned within scheduled 'TO BE RETURNED DATE'.")
                  n=int(input("Number of Days Return is Delayed.\n{Calculate number of days return is delayed from 'To Be Returned Date' to Today's Date.} ⋙ "))
                  print("If the book is not returned within the mentioned 'to be returned by date'\n member will be charged ₹50/- per day delayed.")
                  FINE3=n*50
                  print("∵∴"*27)
                  print("Member's Name                    ⋙ ",A)
                  print("Member's ID                         ⋙ ",B)
                  print("Book Title                              ⋙ ",C)
                  print("Book Number                         ⋙ ",D)
                  print("Book Not Returned Within the mentioned 'TO BE RETURNED DATE'.")
                  print("Book returned ",n," days late.")
                  print("Hence, FINE ⋙ ₹",FINE3,"/-")
                  cor.execute("insert into fine values({0},'{1}',{2},{3},{4},'{5}')".format(B,A,FINE3,M,D,C))   
                  mycon.commit()
            input("Press enter to return to the main menu")
            menu()
            Munni=int(input("ENTER THE OPTION NUMBER ⋙ "))
    elif Munni==9:
        print("THANK YOU FOR USING OUR SERVICES")
        print("∵∴"*27)
        break 
