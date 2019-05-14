import pymysql
db=pymysql.connect("localhost","root","","data_science")
cursor=db.cursor()

print("Hi! Welcome in My Bank Transation System ")
print("We Provide Following Services : ")
while(1):
    print("****************************************************************************")
    print(1," Create An Account Table ")
    print(2," Insert User Detail Into Account")
    print(3," Show All The User Detail ")
    print(4," Show User Detail As Per Account Number ")
    print(5," Deposit Amount In User Account")
    print(6," Witdraw Amount From User Account")
    print(7," Update the Record of User As Per Id ")
    print(8," Delete the Record of User As Per Id ")
    print(9," Transfer The fund From one user account to another user account ")
    print(10," Exit ")
    print("****************************************************************************")
    n=int(input("Enter Your Choice  :"))
    if(n==1):
        sql="show tables"
        cursor.execute(sql);
        x=cursor.fetchall()
        l=[]
        for i in x:
            l=l+[i[0]]
        if "bank" in l:
            print("Table Already Exist in Database ")
        else:
            sql="create table bank(acno int primary key, achname varchar(50), actype varchar(50),balance double);"
            cursor.execute(sql)
            print("DataBase Bank Table Schema Formed")
        input("Press Enter To Continue :")

        
    if(n==2):
        number=int(input("Enter Account Number :"))
        name=input("Enter User Name :")
        actype=input("Enter Account Type :")
        balance=float(input("Enter Amount :"))
        if(balance<1000):
            print("Amount Must Greater Then 1000")
            print("User Not Registered ")
        else:
            sql="show tables"
            cursor.execute(sql);
            x=cursor.fetchall()
            l=[]
            for i in x:
                l=l+[i[0]]
            if "bank" in l:                        
                sql="insert into bank values('%i','%s','%s','%d')"%(number,name,actype,balance)
                r=cursor.execute(sql);
                db.commit()
                if(r>0):
                    print("User Registration Sucess-Fully ")
                else:
                    print("User Not Registered ")
            else:
                print("Please Create Database Schema")
        input("Press Enter To Continue :")

        
    if(n==3):
        sql="show tables"
        cursor.execute(sql);
        x=cursor.fetchall()
        l=[]
        for i in x:
            l=l+[i[0]]
        if "bank" in l:
            sql="select * from bank"
            cursor.execute(sql)
            x=cursor.fetchall()
            if(x):
                print("User Detail : ")
                for i in x:
                    for j in i:
                        print(j,end=" ")
                    print()
            else:
                print("You Have No User Please Create Some User")
        else:
            print("Please Database Schema Create")
        input("Press Enter To Continue :")

        
    if(n==4):
        sql="show tables"
        cursor.execute(sql);
        x=cursor.fetchall()
        l=[]
        for i in x:
            l=l+[i[0]]
        if "bank" in l:
            ac=int(input("Enter Account Number :"))
            sql="select * from bank where acno = "+str(ac)
            cursor.execute(sql)
            x=cursor.fetchall()
            if(x):
                for i in x:
                    for j in i:
                        print(j,end=" ")
                    print()
            else:
                print("Account Does Not Exist")
        else:
            print("Please DataBase Schema Create ")
        input("Press Enter To Continue : ")

        
    if(n==5):
        sql="show tables"
        cursor.execute(sql);
        x=cursor.fetchall()
        l=[]
        for i in x:
            l=l+[i[0]]
        if "bank" in l:
            acno=int(input("Enter Account Number :"))
            balance=float(input("Enter Balance To Deposit: "))
            sql="select * from bank where acno = "+str(acno)
            cursor.execute(sql)
            x=cursor.fetchall()
            if(x):        
                sql="update bank set balance=balance+('%d') where acno=('%i')"%(balance,acno)
                r=cursor.execute(sql)
                db.commit()
                if(r>0):
                    print("Updation SucessFully")
                    print("User Detail :")
                    sql="select * from bank where acno = "+str(acno)
                    cursor.execute(sql)
                    x=cursor.fetchall()
                    if(x):
                        for i in x:
                            for j in i:
                                print(j,end=" ")
                            print()
                else:
                    print("Updation Failed")
            else:
                print("Account Does Not Exist")
        else:
            print("Please Database Schema Create ")
        input("Press Enter To Continue : ")

        
    if(n==6):
        sql="show tables"
        cursor.execute(sql);
        x=cursor.fetchall()
        l=[]
        for i in x:
            l=l+[i[0]]
        if "bank" in l:
            acno=int(input("Enter Account Number :"))
            balance=float(input("Enter Balance To Withdarw : "))
            sql="select * from bank where acno = "+str(acno)
            cursor.execute(sql)
            x=cursor.fetchall()
            if(x):
                sql="select * from bank where acno = "+str(acno)
                cursor.execute(sql)
                x=cursor.fetchall()
                l=[]
                for i in x:
                    for j in i:
                        l=l+[j]
                d=l[3]
                if(d-balance>1000):
                    sql="update bank set balance=balance-('%d') where acno=('%i')"%(balance,acno)
                    r=cursor.execute(sql)
                    db.commit()
                    if(r>0):
                        print("Updation SucessFully")
                        print("User Detail :")
                        sql="select * from bank where acno = "+str(acno)
                        cursor.execute(sql)
                        x=cursor.fetchall()
                        if(x):
                            for i in x:
                                for j in i:
                                    print(j,end=" ")
                                print()
                    else:
                        print("Updation Failed")
                else:
                    print("Amount Is Less Then Minimum Balance So Maintain Balance ")
            else:
                print("Account Does Not Exist")
        else:
            print("Please Database Schema Create ")
        input("Press Enter To Continue : ")

        
    if(n==7):
        sql="show tables"
        cursor.execute(sql);
        x=cursor.fetchall()
        l=[]
        for i in x:
            l=l+[i[0]]
        if "bank" in l:
            acno=int(input("Enter Account Number :"))
            name=input("Enter User Name :")
            actype=input("Enter Account Type :")
            balance=float(input("Enter Amount To Updated:"))
            if(balance>=1000):
                    sql="select * from bank where acno = "+str(acno)
                    cursor.execute(sql)
                    x=cursor.fetchall()
                    if(x):
                        sql="update bank Set achname=('%s'),actype=('%s'),balance=('%f') where acno = ('%i')"%(name,actype,balance,acno)
                        r=cursor.execute(sql)
                        db.commit()
                        if(r>0):
                            print("Updation SucessFully")
                            print("User Detail :")
                            sql="select * from bank where acno = "+str(acno)
                            cursor.execute(sql)
                            x=cursor.fetchall()
                            if(x):
                                for i in x:
                                    for j in i:
                                        print(j,end=" ")
                                    print()
                        else:
                            print("Updation Failed")
                    else:
                        print("Account Does Not Exist")
            else:
                print("Minimum Amount Will Be 1000 \n Try Again.........")
        else:
            print("Please DataBase Schema Create")
        input("Press Enter To Continue : ")

        
    if(n==8):
        sql="show tables"
        cursor.execute(sql);
        x=cursor.fetchall()
        l=[]
        for i in x:
            l=l+[i[0]]
        if "bank" in l:
            acno=int(input("Enter Account Number : "))
            sql="select * from bank where acno = "+str(acno)
            cursor.execute(sql)
            x=cursor.fetchall()
            if(x):
                sql="delete from bank where acno ="+str(acno)
                cursor.execute(sql)
                y=cursor.fetchall()
                if(y):
                    print("Deletion Failed ")
                else:
                    print("Deletion SucessFul")
            else:
                print("Account Does Not Exist")
        else:
            print("Please DataBase Schema Create ")
        input("Press Enter To Continue : ")

    if(n==9):
        sql="show tables"
        cursor.execute(sql);
        x=cursor.fetchall()
        l=[]
        for i in x:
            l=l+[i[0]]
        if "bank" in l:
            acno1=int(input("Enter Sendet Account Number : "))
            acno2=int(input("Enter Sendet Account Number : "))
            balance=float(input("Enter Amount To Transfer : "))
            sql="select * from bank where acno = "+str(acno1)
            cursor.execute(sql)
            x=cursor.fetchall()
            sql="select * from bank where acno = "+str(acno2)
            cursor.execute(sql)
            y=cursor.fetchall()
            if(x):
                if(y):
                    sql="select * from bank where acno = "+str(acno1)
                    cursor.execute(sql)
                    x=cursor.fetchall()
                    l=[]
                    for i in x:
                        for j in i:
                            l=l+[j]
                    d=l[3]
                    if(d-balance<1000):
                        print("Please Maintain Your Balance ")
                    else:
                        sql="update bank set balance=balance+('%d') where acno=('%i')"%(balance,acno2)
                        r=cursor.execute(sql)
                        db.commit()
                        sql="update bank set balance=balance-('%d') where acno=('%i')"%(balance,acno1)
                        r=cursor.execute(sql)
                        db.commit()
                        if(r>0):
                            print("Updation SucessFully")
                            sql="select balance from bank where acno = "+str(acno1)
                            cursor.execute(sql)
                            x=cursor.fetchall()
                            sql="select balance from bank where acno = "+str(acno2)
                            cursor.execute(sql)
                            y=cursor.fetchall()
                            print("Sender Balance : ",x[0])
                            print("Recevier Balance : ",y[0])
                        else:
                            print("Updation Failed")  
                else:
                    print("Recevier Account Does Not Exist ")

            else:
                print("Sender Account Number Does Not Exist ")
        else:
            print("Please DataBase Create ")
        input("Press Enter To Continue : ")
    
    if(n==10):
        break
    if(n<1 or n>10):
        print("You Enterd Wrong Number")
        print("Please Enter Right Choice")
        input("Press Enter To Continue : ")
    
print("Thank You For Using My BankSystem")
print("See You Again ")
