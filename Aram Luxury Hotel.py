import mysql.connector

mydb = mysql.connector.connect(user="root",
                               password="tanmay",
                               host="localhost",
                               database="ARAM_HOTEL")


d1={} #0-Name,1-Phone,2-Email,3-Indate,4-outdate,5-Room type,6-room number,7-Payment Pending,8-Room service Bill
d2={1:('SPACIOUS LUXURY SUITE - KING BED',5000),2:('SPACIOUS LUXURY SUITE - QUEEN BED ',4500),3:('STANDARD LUXURY SUITE - SINGLE BED',3000),4:('STANDARD AC SUITE - DOUBLE BED',2300),5:('STANDARD AC SUITE - SINGLE BED ',2000)}
d3={}
rooms=[101,102,103,104,105,106,107,108,201,202,203,204,205,206,207,208,301,302,303,304,305,306,307,308,401,402,403,404,405,406,407,408,501,502,503,504,505,506,507,508,601,602,603,604,607,608,701,702,703,704,705,706,707,708]


print("--------------------------------WELCOME TO ARAM LUXURY HOTEL--------------------------------")


def menuset():
  choice=int(input('''

Please choose from the following

1. Book new Room

2. Make changes to Current Stay

3. Room Service

4. Check Customer Details

5. Bill Payment'''))

def New_Room():
  n=input("Please enter your name")
  p=int(input("Please enter your contact number"))
  e=input("Please enter your Email Address")
  p1=input("Please enter Check-In date (DD/MM/YYYY)")
  p2=input("Please enter Check-Out date (DD/MM/YYYY)")
  i=p1.split("/")
  o=p2.split("/")
  from datetime import date
  indate=date(int(i[2]),int(i[1]),int(i[0]))
  outdate=date(int(o[2]),int(o[1]),int(o[0]))
  while outdate<=indate:
    print("Please choose a Check-out date later than Check-In date")
    p1=input("Please enter Check-In date (DD/MM/YYYY)")
    p2=input("Please enter Check-Out date (DD/MM.YYYY)")
    i=p1.split("/")
    o=p2.split("/")
    from datetime import date
    indate=date(int(i[2]),int(i[1]),int(i[0]))
    outdate=date(int(o[2]),int(o[1]),int(o[0]))
  days= outdate - indate
  days=days.days
  s=0
  R=int(input('''We have the following rooms available:

1. SPACIOUS LUXURY SUITE - KING BED --------- ₹ 5000 PER NIGHT

2. SPACIOUS LUXURY SUITE - QUEEN BED --------- ₹ 4500 PER NIGHT

3. STANDARD LUXURY SUITE - SINGLE BED --------- ₹ 3000 PER NIGHT

4. STANDARD AC SUITE - DOUBLE BED ----------- ₹ 2300 PER NIGHT

5. STANDARD AC SUITE - SINGLE BED ----------- ₹ 2000 PER NIGHT'''))
  if R==1:
    s=5000*days
    print("Total price is ₹",s)
  if R==2:
    s=4500*days
    print("Total price is ₹",s)
  if R==3:
    s=3000*days
    print("Total price is ₹",s)
  if R==4:
    s=2300*days
    print("Total price is ₹",s)
  if R==5:
    s=2000*days
    print("Total price is ₹",s)
  if R not in range(1,6):
    print('Please choose from the above options')
  else:
    import random
    cstid=random.randint(100,999)
    room=random.randint(0,54)
    room=rooms[room]
    while cstid in d1:
      cstid=random.randint(100,999)
    F=0 #Room service bill
    mycur=mydb.cursor()
    mycur.execute("INSERT INTO Customer_Details values('"+str(cstid)+"','"+str(n)+"','"+str(p)+"','"+str(e)+"','"+str(indate)+"','"+str(outdate)+"','"+str(R)+"','"+str(room)+"','"+str(s)+"','"+str(F)+"')")
    mydb.commit()
    print("Customer ID -",cstid)
    print("Room Number -",room)
    print("Enjoy your stay")
    menuset()

def info_retrieve():
    cur=mydb.cursor()
    cur.execute("select * from Customer_Details")
    d1={}
    for entry in cur:
        
        p1=str(entry[4])
        p2=str(entry[5])
        i=p1.split("-")
        o=p2.split("-")
        from datetime import date
        indate=date(int(i[0]),int(i[1]),int(i[2]))
        outdate=date(int(o[0]),int(o[1]),int(o[2]))

        d1[entry[0]]=[entry[1],int(entry[2]),entry[3],indate,outdate,int(entry[6]),entry[7],entry[8],entry[9]]

   

    
def Make_Change():
    cur=mydb.cursor()
    cur.execute("select * from Customer_Details")
    d1={}
    for entry in cur:
        
        p1=str(entry[4])
        p2=str(entry[5])
        i=p1.split("-")
        o=p2.split("-")
        from datetime import date
        indate=date(int(i[0]),int(i[1]),int(i[2]))
        outdate=date(int(o[0]),int(o[1]),int(o[2]))

        d1[entry[0]]=[entry[1],int(entry[2]),entry[3],indate,outdate,int(entry[6]),entry[7],entry[8],entry[9]]
        print(d1)


    x=int(input("Please Enter Customer ID"))
  
    if x not in d1:
      print("Please enter Valid Customer ID")
      Make_Change()
    else:
      print('Your current stay details:','''
''')
      print('Check-In Date-',d1[x][3],'''
''')
      print('Check-Out Date-',d1[x][4],'''
''')
      print('Room type-',d2[d1[x][5]][0],'''
''')
      print('Room number-',d1[x][6],'''
''')
      print('Payment pending -₹',d1[x][7],'''
''')
      u=int(input('''Please Choose from the following:
1. Change Check-Out Date

2. Change Room Type'''))
      def date_change():
        date1=d1[x][4]
        x2=input("Please enter New Check-Out date (DD/MM/YYYY)")
        o=x2.split("/")
        from datetime import date
        date2=date(int(o[2]),int(o[1]),int(o[0]))
        c=d1[x][7]
        if date2>date1:
          no_days= date2 - date1
          no_days=no_days.days
          c= c + no_days * d2[d1[x][5]][1]
          d1[x][4]=date2
          d1[x][7]=c
          mycursor=mydb.cursor()
          mycursor.execute("update Customer_Details set CheckOut_date='"+str(date2)+"' where Customer_ID='"+str(x)+"'")
          mycursor.execute("update Customer_Details set Payment_Pending='"+str(c)+"' where Customer_ID='"+str(x)+"'") 
          mydb.commit()
          print("Total Payment Pending -",c,'''
              ''')
          print('Stay increased by',no_days,'days','''
              ''')
          print("Check-Out date updated to -",date2)
        if date1>date2:
          no_days= date1 - date2
          no_days=no_days.days
          c= c - no_days * d2[d1[x][5]][1]
          d1[x][4]=date2
          d1[x][7]=c
          mycursor=mydb.cursor()
          mycursor.execute("update Customer_Details set CheckOut_date='"+str(date2)+"' where Customer_ID='"+str(x)+"'")
          mycursor.execute("update Customer_Details set Payment_Pending='"+str(c)+"' where Customer_ID='"+str(x)+"'") 
          mydb.commit()
          print("Total Payment Pending -",c)
          print('Stay reduced by',no_days,'day(s)')
          print("Check-Out date updated to -",date2)
      if u==1:
        date_change()
        
      if u==2:
        room1=d1[x][5]
        c=d1[x][7]
        room2=int(input('''We have the following rooms available:

1. SPACIOUS LUXURY SUITE - KING BED --------- ₹ 5000 PER NIGHT

2. SPACIOUS LUXURY SUITE - QUEEN BED --------- ₹ 4500 PER NIGHT

3. STANDARD LUXURY SUITE - SINGLE BED --------- ₹ 3000 PER NIGHT

4. STANDARD AC SUITE - DOUBLE BED ----------- ₹ 2300 PER NIGHT

5. STANDARD AC SUITE - SINGLE BED ----------- ₹ 2000 PER NIGHT'''))
        if room1==room2:
          print("You current stay is already in the chosen room")
        else:
          newdate=input("Please enter the date on which you would like to move to your new room")
          o=newdate.split("/")
          from datetime import date
          date3=date(int(o[2]),int(o[1]),int(o[0]))
          if date3>d1[x][4]:
            z=int(input('''You have chosen a moving date which exceeds your checkout date.
To extend your checkout date press 1'''))
            if z==1:
              date_change()
            else:
              Make_Change()
          else:
            import random
            no_days2=d1[x][4] - date3
            no_days2=no_days2.days
            c= c-(no_days2 * d2[d1[x][5]][1])
            c= c+(no_days2 * d2[room2][1])
            d1[x][7]=c
            d1[x][5]=room2
            room=random.randint(0,52)
            room=rooms[room]
            mycursor=mydb.cursor()
            mycursor.execute("update Customer_Details set Room_Number='"+str(room)+"' where Customer_ID='"+str(x)+"'")
            mycursor.execute("update Customer_Details set Payment_Pending='"+str(c)+"' where Customer_ID='"+str(x)+"'")
            mycursor.execute("update Customer_Details set Room_type='"+str(room2)+"' where Customer_ID='"+str(x)+"'")
            mydb.commit()
            print("New Room Number-",room)
            print("Room update to :",d2[room2][0])
            print("Total payment to make - ₹",c)
    menuset()

def cst_det():
    cur=mydb.cursor()
    cur.execute("select * from Customer_Details")
    d1={}
    for entry in cur:
        
        p1=str(entry[4])
        p2=str(entry[5])
        i=p1.split("-")
        o=p2.split("-")
        from datetime import date
        indate=date(int(i[0]),int(i[1]),int(i[2]))
        outdate=date(int(o[0]),int(o[1]),int(o[2]))

        d1[entry[0]]=[entry[1],int(entry[2]),entry[3],indate,outdate,int(entry[6]),entry[7],entry[8],entry[9]]
    for x in d1:
       print('''---------------------------------------------------------------------------------------------------------
Customer ID''',x)
       print('Name-',d1[x][0],'''
''')
       print('Phone-',d1[x][1],'''
''')
       print('Email Address-',d1[x][2],'''
''')
       print('Check-In Date-',d1[x][3],'''
''')
       print('Check-Out Date-',d1[x][4],'''
''')
       print('Room type-',d1[x][5],"-",d2[d1[x][5]],'''
''')
       print('Room number-',d1[x][6],'''
''')
       print('Hotel Stay Bill-₹',d1[x][7])
       print('Room service bill-₹',d1[x][8])
       print('Payment Pending -₹',d1[x][7]+d1[x][8],'''
''')
       menuset()


def Room_Service():
    cur=mydb.cursor()
    cur.execute("select * from Customer_Details")
    d1={}
    for entry in cur:
        
        p1=str(entry[4])
        p2=str(entry[5])
        i=p1.split("-")
        o=p2.split("-")
        from datetime import date
        indate=date(int(i[0]),int(i[1]),int(i[2]))
        outdate=date(int(o[0]),int(o[1]),int(o[2]))

        d1[entry[0]]=[entry[1],int(entry[2]),entry[3],indate,outdate,int(entry[6]),entry[7],entry[8],entry[9]]

        

    x=int(input("Please Enter Customer ID"))
    b=0
    if x not in d1:
        print("Please enter Valid Customer ID")
        Room_Service()
    else:
        b=0
        g=[]
        cur=mydb.cursor()
        cur.execute("select * from Food_Menu")

        brkfast=[]
        brkprice=[]
        brksno=[]
        main=[]
        mainprice=[]
        mainsno=[]
        brd=[]
        brdprice=[]
        brdsno=[]
        sweet=[]
        sweetprice=[]
        sweetsno=[]
        price=[]
        items=[]
        nos=[]
        for i in cur:
            items.append(i[1])
            nos.append(i[0])
            price.append(i[2])

            

            if i[3]=='BREAKFAST':
                brkfast.append(i[1])
                brkprice.append('₹'+str(i[2]))
                brksno.append(i[0])
            elif i[3]=='MAIN_COURSE':
                main.append(i[1])
                mainprice.append('₹'+str(i[2]))
                mainsno.append(i[0])
            elif i[3]=='BREADS':
                brd.append(i[1])
                brdprice.append('₹'+str(i[2]))
                brdsno.append(i[0])
            elif i[3]=='SWEET':
                sweet.append(i[1])
                sweetprice.append('₹'+str(i[2]))
                sweetsno.append(i[0])
        

        from tabulate import tabulate
        menu1={'Sno.':brksno,'Breakfast':brkfast,"Price":brkprice}
        menu2={'Sno.':mainsno,'Main_Course':main,"Price":mainprice}
        menu3={'Sno.':brdsno,'Breads':brd,"Price":brdprice}
        menu4={'Sno.':sweetsno,'Sweet':sweet,"Price":sweetprice}
        g=tabulate(menu1,headers='keys',tablefmt='fancy_grid')
        h=tabulate(menu2,headers='keys',tablefmt='fancy_grid')
        f=tabulate(menu3,headers='keys',tablefmt='fancy_grid')
        e=tabulate(menu4,headers='keys',tablefmt='fancy_grid')
        print(g,h,f,e,sep="\n")
        

        V=list(zip(items,price))
        d3=dict(zip(nos,V))
        b=0
        g=[]
        def order(b,g):
            m=int(input('Enter your choice'))
            c=int(input('Enter quantity'))
            b+=c*d3[m][1]
            y=[m,c]
            g.append(y)
            l=int(input("Do you want to order more items : PRESS 1 FOR YES, PRESS 2 FOR NO"))
            if l==1:
                order(b,g)
            else:
                d1[x][8]+=b
                mycursor=mydb.cursor()
                mycursor.execute("update Customer_Details set Room_Service_Bill='"+str(d1[x][8])+"' where Customer_ID='"+str(x)+"'")
                mydb.commit()
                from tabulate import tabulate
                table=[['Item','Rate',"Quantity","Net Bill"]]
                for i in g:
                    j=[d3[i[0]][0],d3[i[0]][1],i[1],d3[i[0]][1]*i[1]]
                    table.append(j)
                print(tabulate(table,headers='firstrow',tablefmt='rst'))
                print('----------------------------------- ')
                print('Total Bill -----------------------₹',b)
                menuset()
        order(b,g)    

   

def payment():
    cur=mydb.cursor()
    cur.execute("select * from Customer_Details")
    d1={}
    for entry in cur:
        
        p1=str(entry[4])
        p2=str(entry[5])
        i=p1.split("-")
        o=p2.split("-")
        from datetime import date
        indate=date(int(i[0]),int(i[1]),int(i[2]))
        outdate=date(int(o[0]),int(o[1]),int(o[2]))

        d1[entry[0]]=[entry[1],int(entry[2]),entry[3],indate,outdate,int(entry[6]),entry[7],entry[8],entry[9]]

    from datetime import datetime
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    x=int(input("Enter Customer ID"))
    if x not in d1:
      print("Please enter Valid Customer ID")
      payment()
    else:
      print("Your Payment details:")
      print('Check-In Date-',d1[x][3],'''
''')
      print('Check-Out Date-',d1[x][4],'''
''')
      print('Net Payment pending -₹',d1[x][7]+d1[x][8],'''
''')
      w=int(input('''Would you like to pay your bill or extend your stay with us? Please choose from the following:
1. Extend Stay

2. Pay bill'''))
      if w==1:
          Make_Change()
      elif w==2:
        print('-------------------------------------------------------------')
        print('                         ARAM HOTEL                          ','                                                    PHONE SCREEN')
        print('-------------------------------------------------------------','                                   ------------------------------------------------')
        print('Customer ID-',x,'                            Served By: Umesh','                                   Dear Customer, Thank you for visiting ARAM HOTEL')
        print('Date:',d1[x][4],'                            Time:',current_time,'                                           We hope you enjoyed your stay')
        print('------------------------------------------------------------- ','''
''')
        print('Hotel Stay-',d2[d1[x][5]][0],'-------₹',d1[x][7])
        print('Room Service----------------------------------------₹',d1[x][8])
        print('Total Bill -----------------------------------------₹',d1[x][7]+d1[x][8],'''
''')
        print('-------------------------------------------------------------')
        print("            THANK YOU FOR VISITING ARAM HOTEL                ")
        print("                  PLEASE VISIT AGAIN                         ")







def Staff_Portal():
  staff={}
  cur=mydb.cursor()
  cur.execute("select * from Staff")

  for entry in cur:
    staff[entry[0]]=[entry[1],entry[2],entry[3],int(entry[4]),entry[5]]
    
  passw=''
  g=int(input("Enter Employee ID"))
  if g not in staff:
    print("Invalid ID")
    Staff_Portal()
  else:
    passw=input("Enter password")
  if passw!=staff[g][1]:
    print('Incorrect password')
    Staff_Portal()
  else:
    def update():
      choose=int(input('''Please choose from the following
1. Add new employee

2. Check/Update Customer Details Manually

3. Update Restaurant Menu

4. Back to Main Menu'''))
      if choose==1:
        x=input("Enter Employee Name")
        y=input("Enter Designation")
        z=int(input("Enter Contact Number"))
        i=int(input("Enter Salary"))
        q=input("Enter new password")

        import random

        l=random.randint(1001,9999) #EmpId
        while l in staff:
          l=random.randint(1001,9999)
        print("Employee ID is - ",l)
        print("Employee Successfully Added")
        myc=mydb.cursor()
        myc.execute("insert into staff values('"+str(l)+"','"+str(x)+"','"+str(q)+"','"+str(y)+"','"+str(z)+"','"+str(i)+"')")
        mydb.commit()
        update()
        

      if choose==2:
        cur=mydb.cursor()
        cur.execute("select * from Customer_Details")
        d1={}
        for entry in cur:
          p1=str(entry[4])
          p2=str(entry[5])
          i=p1.split("-")
          o=p2.split("-")
          from datetime import date
          indate=date(int(i[0]),int(i[1]),int(i[2]))
          outdate=date(int(o[0]),int(o[1]),int(o[2]))
            
          d1[entry[0]]=[entry[1],int(entry[2]),entry[3],indate,outdate,int(entry[6]),entry[7],entry[8],entry[9]]
          
        x=int(input("Enter Customer-Id"))
        if x not in d1:
          print("Please enter Valid Customer ID")
          update()
        else:
          print('''---------------------------------------------------------------------------------------------------------
Customer ID''',x)
          print('Name-',d1[x][0],'''
''')
          print('Phone-',d1[x][1],'''
''')
          print('Email Address-',d1[x][2],'''
''')
          print('Check-In Date-',d1[x][3],'''
''')
          print('Check-Out Date-',d1[x][4],'''
''')
          print('Room type-',d1[x][5],"-",d2[d1[x][5]],'''
''')
          print('Room number-',d1[x][6],'''
''')
          print('Hotel Stay Bill-₹',d1[x][7])
          print('Room service bill-₹',d1[x][8])
          print('Payment Pending -₹',d1[x][7]+d1[x][8],'''
''')
          choice2=int(input('''Please choose from the following

1. Make changes to Customer Details

2. Back'''))

          if choice2==2:
            update()
          else:
            print("WARNING: You are about to change Customer Details Manually, This is allowed for Authorised Personnel Only")
            def cust_change():
              choice3=int(input('''Choose the Detail you would like to make changes to
1. Customer NAME

2. Cutomer Contact Number

3. Customer Email ID

4. Customer Room_Number

5. Hotel Stay Bill

6. Room Service Bill Pending

7. Back'''))

              if choice3==1:
                c=input("Enter Customer's New Name")
                d1[x][0]=c

                myc=mydb.cursor()
                myc.execute("update Customer_Details set Name='"+str(d1[x][0])+"' where Customer_ID='"+str(x)+"'")
                mydb.commit()

                print("Name Succesfully updated",end="\n\n")

                ch=int(input("Do you wish to make more changes: PRESS 1 FOR YES , PRESS 2 FOR NO"))
                if ch==1:
                  cust_change()
                else:
                  update()
                  
              if choice3==2:
                c=input("Enter Customer's New Phone Number")
                d1[x][1]=c

                myc=mydb.cursor()
                myc.execute("update Customer_Details set Contact='"+str(d1[x][1])+"' where Customer_ID='"+str(x)+"'")
                mydb.commit()

                print("Phone Number Succesfully updated",end="\n\n")

                ch=int(input("Do you wish to make more changes: PRESS 1 FOR YES , PRESS 2 FOR NO"))
                if ch==1:
                  cust_change()
                else:
                  update()

              if choice3==3:
                c=input("Enter Customer's New Email-ID")
                d1[x][2]=c

                myc=mydb.cursor()
                myc.execute("update Customer_Details set Email='"+str(d1[x][2])+"' where Customer_ID='"+str(x)+"'")
                mydb.commit()

                print("Email-ID Succesfully updated",end="\n\n")

                ch=int(input("Do you wish to make more changes: PRESS 1 FOR YES , PRESS 2 FOR NO"))
                if ch==1:
                  cust_change()
                else:
                  update()
                  
              if choice3==4:
                c=input("Enter Customer's New Room Number")
                d1[x][6]=c

                myc=mydb.cursor()
                myc.execute("update Customer_Details set Room_Number='"+str(d1[x][6])+"' where Customer_ID='"+str(x)+"'")
                mydb.commit()

                print("Room Number Succesfully updated",end="\n\n")

                ch=int(input("Do you wish to make more changes: PRESS 1 FOR YES , PRESS 2 FOR NO"))
                if ch==1:
                  cust_change()
                else:
                  update()

              if choice3==5:
                c=float(input("Enter New amount"))
                d1[x][7]=c

                myc=mydb.cursor()
                myc.execute("update Customer_Details set Payment_Pending='"+str(d1[x][7])+"' where Customer_ID='"+str(x)+"'")
                mydb.commit()

                print("Database Succesfully updated",end="\n\n")

                ch=int(input("Do you wish to make more changes: PRESS 1 FOR YES , PRESS 2 FOR NO"))
                if ch==1:
                  cust_change()
                else:
                  update()

              if choice3==6:
                c=float(input("Enter New amount"))
                d1[x][8]=c

                myc=mydb.cursor()
                myc.execute("update Customer_Details set Room_Service_Bill='"+str(d1[x][8])+"' where Customer_ID='"+str(x)+"'")
                mydb.commit()

                print("Database Succesfully updated",end="\n\n")

                ch=int(input("Do you wish to make more changes: PRESS 1 FOR YES , PRESS 2 FOR NO"))
                if ch==1:
                  cust_change()
                else:
                  update()

              if choice3==7:
                update()
                


                
          cust_change()
          
      if choose==3:
        def menu_update():
          cur=mydb.cursor()
          cur.execute("select * from Food_Menu")

          brkfast=[]
          brkprice=[]
          brksno=[]
          main=[]
          mainprice=[]
          mainsno=[]
          brd=[]
          brdprice=[]
          brdsno=[]
          sweet=[]
          sweetprice=[]
          sweetsno=[]
          price=[]
          items=[]
          nos=[]
          types=[]
          for i in cur:
              items.append(i[1])
              nos.append(i[0])
              price.append(i[2])
              types.append(i[3])

            

              if i[3]=='BREAKFAST':
                brkfast.append(i[1])
                brkprice.append('₹'+str(i[2]))
                brksno.append(i[0])
              elif i[3]=='MAIN_COURSE':
                main.append(i[1])
                mainprice.append('₹'+str(i[2]))
                mainsno.append(i[0])
              elif i[3]=='BREADS':
                brd.append(i[1])
                brdprice.append('₹'+str(i[2]))
                brdsno.append(i[0])
              elif i[3]=='SWEET':
                sweet.append(i[1])
                sweetprice.append('₹'+str(i[2]))
                sweetsno.append(i[0])
        

          from tabulate import tabulate
          menu1={'Sno.':brksno,'Breakfast':brkfast,"Price":brkprice}
          menu2={'Sno.':mainsno,'Main_Course':main,"Price":mainprice}
          menu3={'Sno.':brdsno,'Breads':brd,"Price":brdprice}
          menu4={'Sno.':sweetsno,'Sweet':sweet,"Price":sweetprice}
          g=tabulate(menu1,headers='keys',tablefmt='fancy_grid')
          h=tabulate(menu2,headers='keys',tablefmt='fancy_grid')
          f=tabulate(menu3,headers='keys',tablefmt='fancy_grid')
          e=tabulate(menu4,headers='keys',tablefmt='fancy_grid')
          print(g,h,f,e,sep="\n")

          m=int(input('''Please choose the type of food you wish to add or delete

1. Breakfast

2. Main Course

3. Breads

4. Sweet

5. Delete an item'''))

          l1=len(brkfast)
          l2=len(main)+l1
          l3=len(brd)+l2
          l4=len(sweet)+l3

          if m==1:
            x=input("Enter item name(IN CAPS)")
            y=float(input("Enter Unit Price"))
            items.insert(l1,x)
            price.insert(l1,y)
            types.insert(l1,'BREAKFAST')
            nos.append(len(items))

          elif m==2:
            x=input("Enter item name(IN CAPS)")
            y=float(input("Enter Unit Price"))
            items.insert(l2,x)
            price.insert(l2,y)
            types.insert(l2,'MAIN_COURSE')
            nos.append(len(items))

          elif m==3:
            x=input("Enter item name(IN CAPS)")
            y=float(input("Enter Unit Price"))
            items.insert(l3,x)
            price.insert(l3,y)
            types.insert(l3,'BREADS')
            nos.append(len(items))

          elif m==4:
            x=input("Enter item name(IN CAPS)")
            y=float(input("Enter Unit Price"))
            items.insert(l4,x)
            price.insert(l4,y)
            types.insert(l4,'SWEET')
            nos.append(len(items))

          elif m==5:
            x=int(input("Enter Serial Number of the Item to be deleted"))
            a=nos.index(x)

            items.remove(items[a])
            price.remove(price[a])
            types.remove(types[a])
            nos.pop()

          else:
            print('Invalid Option')
            menu_update()
            
          V=list(zip(items,price,types))
          d3=dict(zip(nos,V))
         

          cur=mydb.cursor()
          cur.execute("Truncate Food_Menu")

          for u in d3:
            mycursor=mydb.cursor()
            mycursor.execute("insert into food_menu values('"+str(u)+"','"+str(d3[u][0])+"','"+str(d3[u][1])+"','"+str(d3[u][2])+"')")
            mydb.commit()
            
          print("Menu Successfully Updated")

          update()
            
          
        menu_update()



      if choose==4:
        menuset()

      if choose not in (1,2,3,4):
        print('Invalid Option')
        update()




    update()


          


def menuset():
  choice=int(input('''

Please choose from the following

1. Book new Room

2. Make changes to Current Stay

3. Room Service

4. Login to Staff Portal

5. Bill Payment'''))
  if choice==1:
    New_Room()
  if choice==2:
    Make_Change()
  if choice==3:
    Room_Service()
  if choice==4:
    Staff_Portal()
  if choice==5:
    payment()
menuset()





















                          
