import pickle
import mysql.connector as mycon
co=mycon.connect(host='localhost', user='Deeksha', passwd='Alohomora', database='hospital')    #assuming database hospital has already been created

if not co.is_connected():
    print('Error connecting to database!')

c=co.cursor()
pl=0

s="create table if not exists PATIENTS (PID char(4) not null primary key, PATIENT_NAME char(20), DOB date, GENDER char(1), MOBILE_NO integer, DATE_OF_REGISTRATION date, DID char(4) references DOCTORS(DID), FEES_PENDING int)"
c.execute(s)
co.commit()

s="create table if not exists DOCTORS (DID char(4) not null primary key, DOCTOR_NAME char(20), DATE_OF_EMPLOYMENT date, SALARY_PENDING int)"
c.execute(s)
co.commit()

s="create table if not exists APPOINTMENTS (PID char(4) references patients(pid), PATIENT_NAME char(20), DATE date, DID char(4) references doctors(did), TREATMENT char(20))"
c.execute(s)
co.commit()

na=input('DOCTOR(D)/ PATIENT(P)/ MANAGEMENT(M)....')
print()

if na=='P':    
    n=input('NEW PATIENT(N)/ EXISTING PATIENT(E)....')
    if n=='N' or n=='n':
        f=open('pat.dat', 'ab')
        print()
        u=input('Enter a username(PXXX):')
        print()
        p=input('Enter a password:')
        print()
        n=input('Enter your name:')
        print()
        d=input('Enter your date of birth(YYYY-MM-DD):')
        print()
        g=input('Enter your gender(M/F/O):')
        print()
        m=int(input("Enter your mobile number:"))
        print()
        x=input("Enter today's date(YYYY-MM-DD):")
        l=[u,p]
        pickle.dump(l, f)
        f.close()
        s="insert  into patients values('{}','{}', '{}', '{}', {}, '{}', null, null)".format(u, n, d, g, m, x)
        c.execute(s)
        co.commit()
        print()
        print('Account successfully created.')
        print()
        
        while True:
            print('1. View existing appointments')
            print()
            print('2. Fix new appointment')
            print()            
            print('3. View pending fees')
            print()
            print('4. Logout')
            print()
            print()

            q=int(input('What would you like to do?'))
            print()
            
            if q==2:
                x=input("Enter today's date(YYYY-MM-DD):")
                print()
                n=input('Enter your name:')
                print()
                r=input("Enter the doctor's ID provided by the hospital:")
                print()                            
                s="insert into appointments(PID, PATIENT_NAME, DATE, DID) values('{}', '{}', '{}', '{}')".format(u, n, x, r)               
                c.execute(s)
                co.commit()
                print('Appointment fixed.')
                print()

            elif q==1:
                s="select * from appointments where PID='{}'". format(u)
                c.execute(s)
                d=c.fetchall()
                if len(d)==0:
                    print('No existing appointments')
                    print()
                else:
                    print('ID, NAME, DATE_OF_APPOINTMENT, DID, TREATMENT')
                    print()
                    for i in d:
                        print(d)
                    print()


            elif q==3:
                s="select DID, FEES_PENDING from patients where FEES_PENDING is not null and PID='{}'".format(u)
                c.execute(s)
                d=c.fetchall()
                if len(d)==0:
                    print('No pending fees')
                    print()
                else:
                    print('DID, FEES PENDING')
                    print()
                    for i in d:
                        print(d)
                    print()


            elif q==4:
                break

            else:
                print ('Invalid input. Enter a number (1 to 4)')               
          
                  

    elif n=='e' or n=='E':
        f=open('pat.dat', 'rb')
        l=[]
        print()
        u=input('Enter your username(PXXX):')
        print()
        p=input('Enter your password:')
        print()
        try:
            while True:
                l=pickle.load(f)
                if l==[u, p]:
                    print('Welcome', u)
                    pl=1
                    print()
                    
                    while True:
                        print('1. View existing appointments')
                        print()
                        print('2. Fix new appointment')
                        print()
                        print('3. View pending fees')
                        print()
                        print('4. Logout')
                        print()
                        print()

                        q=int(input('What would you like to do?'))
                        print()

                        if q==2:
                            x=input("Enter today's date(YYYY-MM-DD):")
                            print()
                            n=input('Enter your name:')
                            print()
                            r=input("Enter the doctor's ID provided by the hospital:")
                            print()
                            s="insert into appointments(PID, PATIENT_NAME, DATE, DID) values('{}', '{}', '{}', '{}')".format(u, n, x, r)               
                            c.execute(s)
                            co.commit()
                            print('Appointment fixed.')
                            print()

                        elif q==1:
                            s="select * from appointments where PID='{}'". format(u)
                            c.execute(s)
                            d=c.fetchall()
                            if len(d)==0:
                                print('No existing appointments')
                                print()
                            else:
                                print('ID, NAME, DATE_OF_APPOINTMENT, DID, TREATMENT')
                                print()
                                for i in d:
                                    print(d)
                                print()


                        elif q==3:
                            s="select DID, FEES_PENDING from patients where FEES_PENDING is not null and PID='{}'".format(u)
                            c.execute(s)
                            d=c.fetchall()
                            if len(d)==0:
                                print('No pending fees')
                                print()
                            else:
                                print('DID, FEES PENDING')
                                print()
                                for i in d:
                                    print(d)
                                print()


                        elif q==4:
                            break

                        else:
                            print ('Invalid input. Enter a number (1 to 4)')
                    
                    
        except EOFError:
            f.close()
            if pl==0:
                print('Invalid login details!')

elif na=='D':
    f=open('doc.dat', 'rb')
    l=[]
    print()
    u=input('Enter your username(DXXX):')
    print()
    p=input('Enter your password:')
    print()
    try:
        while True:
            l=pickle.load(f)
            if l==[u, p]:
                print('Welcome', u)
                pl=1
                print()
                
                while True:
                        print("1. View todays appointments")
                        print()
                        print('2. View all upcoming appointments')
                        print()
                        print('3. View all patients')
                        print()
                        print('4. View a specific patient')
                        print()
                        print('5. Logout')
                        print()
                        print()

                        q=int(input('What would you like to do?'))
                        print()

                        if q==1:
                            w="select * from appointments where DID='{}'".format(u) 
                            c.execute(w)
                            d=c.fetchall()

                            s="select curdate() from dual"
                            c.execute(s)
                            p=c.fetchall()

                            for i in p:
                                for j in i:
                                    for k in d:                     
                                        if k[2]==j:
                                            print(k)                           
                            print()

                        elif q==2:
                            w="select * from appointments where DID='{}'".format(u) 
                            c.execute(w)
                            d=c.fetchall()

                            s="select curdate() from dual"
                            c.execute(s)
                            p=c.fetchall()

                            for i in p:
                                for j in i:
                                    for k in d:                     
                                        if k[2]>=j:
                                            print(k)                        
                            print()                         
                           

                        elif q==3:
                            s="select * from patients where DID='{}'".format(u)             
                            c.execute(s)
                            d=c.fetchall()
                            if len(d)==0:
                                print('No records')
                                print()
                            else:
                                print('ID, NAME, DOB, GENDER, MOBILE NO, REGISTRATION DATE, DOCTOR ID, PENDING FEES')
                                for i in d:                                                                   
                                    print(i)
                                print()
                          

                        elif q==4:
                            i=input("Enter the patient's ID:")
                            s="select * from patients where PID='{}'".format(i)
                            c.execute(s)
                            d=c.fetchall()
                            if len(d)==0:
                                print('Patient not found.')
                                print()
                            else:
                                print('ID, NAME, DOB, GENDER, MOBILE NO, REGISTRATION DATE, DOCTOR ID, PENDING FEES')
                                for i in d:                                                                   
                                    print(i)
                                print()                                                         
                            

                        elif q==5:
                            break

                        else:
                            print ('Invalid input. Enter a number (1 to 5)')                          
                             
            
              
    except EOFError:
        f.close()
        if pl==0:            
            print('Invalid login details!')

elif na=='M':
    f=open('mgm.dat', 'rb')
    l=[]
    print()
    u=input('Enter your username(MXXX):')
    print()
    p=input('Enter your password:')
    print()
    try:
        while True:
            l=pickle.load(f)
            if l==[u, p]:
                print('Welcome', u)
                pl=1
                print()
                while True:
                        print("1. View doctors")
                        print()
                        print('2. View patients')
                        print()
                        print('3. View pending fees of patients')
                        print()
                        print('4. View pending salaries of doctors')
                        print()
                        print('5. Add new doctor')
                        print()
                        print('6. Add new management account')
                        print()
                        print('7. Logout')
                        print()
                        print()

                        q=int(input('What would you like to do?'))
                        print()

                        if q==1:
                            s="select * from doctors"
                            c.execute(s)
                            d=c.fetchall()
                            if len(d)!=0:
                                print('ID, NAME, DATE OF EMPLOYMENT, SALARY PENDING')
                                for i in d:
                                    print(i)
                                print()
                            else:
                                print('No records.')
                                print()
                                


                        elif q==2:
                            s="select * from patients"
                            c.execute(s)
                            d=c.fetchall()
                            if len(d)!=0:
                                print('ID, NAME, DOB, GENDER, MOBILE NO, REGISTRATION DATE, DOCTOR ID, PENDING FEES')
                                for i in d:
                                    print(i)
                                print()
                            else:
                                print('No records.')
                                print()
                            
                            
                            
                        elif q==3:
                            s="select PID, FEES_PENDING from patients where FEES_PENDING is not null"
                            c.execute(s)
                            d=c.fetchall()
                            if len(d)!=0:
                                print('ID, PENDING FEES')
                                for i in d:
                                    print(i)
                                print()
                            else:
                                print('No patients with pending fees.')
                                print()
                            

                        elif q==4:
                            s="select DID, SALARY_PENDING from doctors where SALARY_PENDING is not null"
                            c.execute(s)
                            d=c.fetchall()
                            if len(d)!=0:
                                print('ID, PENDING SALARY')
                                for i in d:
                                    print(i)
                                print()
                            else:
                                print('No doctors with pending salary.')

                        elif q==5:
                            z=input('Enter the username:')
                            x=input('Enter the password:')
                            t=input("Enter the doctor's name:")
                            d=input("Enter the date of employment(YYYY-MM-DD):")
                            h=[z,x]
                            f=open("doc.dat", 'ab')
                            pickle.dump(h,f)
                            f.close()
                            s="insert into doctors(DID, DOCTOR_NAME, DATE_OF_EMPLOYMENT) values('{}', '{}', '{}')".format(z, t, d)
                            c.execute(s)
                            co.commit()
                            print("Doctor successfully added.")
                            print()
                            

                        elif q==6:
                            z=input('Enter the username:')
                            x=input('Enter the password:')
                            h=[z,x]
                            f=open("mgm.dat", 'ab')
                            pickle.dump(h,f)
                            f.close()
                            print("Management account successfully added.")
                            print()
                        
                        elif q==7:
                            break

                        else:
                            print ('Invalid input. Enter a number (1 to 7)')                          
                
                
    except EOFError:
        f.close()
        if pl==0:
            print('Invalid login details!')

else:
    print('Invalid input! Try again!')

co.close()
    
    
