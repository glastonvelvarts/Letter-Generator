# -*- coding: utf-8 -*-
from datetime import date
import webbrowser
class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
ch='yes'
cstr=color.UNDERLINE + 'WELCOME TO LETTER GENERATOR' + color.DARKCYAN + color.BOLD + color.END
print(cstr.center(90),'\n')
while ch!='no':
    ch=input('press any key to continue or no to quit-')
    if ch=='no':
        i=color.DARKCYAN +'X_X_X_X_X_X_X_THANK YOU FOR USING OUR APPLICATION_X_X_X_X_X_X' + color.END
        print(i.center(100),'\n')
        break
    print('\nwhich letter do you want to write:')
    print('1.formal letter\n2.informal letter\n3.any other micellaneous')#please note when you select informal letter you have to make your own letter
    ch1=input('\nenter choice 1 or 2 or 3')
    if ch1=='1':
        print('you have selected formal letter')
        print('select which one would you like to access:\n1.to your principal\n2.to your boss')
        a='yes'
        while a!='4':
            a=input('enter option 1 to access letter to principal\n option 2 to access letter to boss\n3.to go back')
            if a=='1':
                ch='yes'
                while ch!='4':
                    ch=input('please enter one of the following option:\n1.leave\n2.backup class\n3.stream change\n:')
                    if ch=='1':
                        print('you have entered the topic of leave-')
                        file=open('user1','w+')
                        file1=open('principalleave.txt','r+')
                        h='letter to the principal'
                        h=h.upper()
                        h=color.UNDERLINE + h + color.BOLD + color.END
                        h=h.center(100)
                        sub=input('enter subject')
                        sub=sub.upper()
                        sub='subject: {}'.format(sub)
                        n=input('enter your name-')
                        add1=input('enter sender address line 1-')
                        add2=input('enter sender address line 2-')
                        add3=input('enter sender address line 3-')
                        rec1='THE PRINCIPAL'
                        rec2=input('enter receiver address line 2-')
                        rec3=input('enter receiver address line 3-')
                        today=date.today()
                        d1=today.strftime('%B%d,%Y')
                        N=n.upper()
                        cl=input('enter your class-')
                        sec=input('enter your section-')
                        nlt=input('enter number of leaves you want to take-')
                        rea=input('enter reason-')
                        sub=color.UNDERLINE + sub + color.END
                        a=color.DARKCYAN + n + color.END
                        s=add1+'\n'+add2+'\n'+add3+'\n\n'
                        r=rec1+'\n'+rec2+'\n'+rec3+'\n'
                        k=file1.read()
                        k=k.replace('<name>',n)
                        k=k.replace('<class>',cl)
                        k=k.replace('<section>',sec)
                        k=k.replace('<no. of leaves taken>',nlt)
                        k=k.replace('<reason>',rea)
                        file.write('\n'+h+'\n\n'+s+d1+'\n\n'+r+'\n\n'+sub+'\n'+k+'\n'+a+'\n'+N+'\n\n')
                        file.seek(0)
                        s=file.read()
                        print(s)
                        file.close()
                        file1.close()
                    elif ch=='2':
                        print('you have entered the topic of back up class')
                        file=open('user2.txt','w+')
                        file1=open('principalbackup.txt','r+')
                        sub=input('enter subject:')
                        sub=sub.upper()
                        sub='subject: {}'.format(sub)
                        n=input('enter your name:')
                        add1=input('enter sender address line 1-')
                        add2=input('enter sender address line 2-')
                        add3=input('enter sender address line 3-')
                        rec1='THE PRINCIPAL'
                        rec2=input('enter receiver address line 2-')
                        rec3=input('enter receiver address line 3-')
                        today=date.today()
                        d1=today.strftime('%B%d,%Y')
                        N=n.upper()
                        h='letter to the principal'
                        h=h.upper()
                        h=color.UNDERLINE + h + color.BOLD + color.END
                        h=h.center(100)
                        subject=input('enter the subject for which you need back up-')
                        cl=input('enter your class-')
                        sec=input('enter your section-')
                        date1=input('enter the start of your absence in the form of dd-mm-yyyy-')
                        date2=input('enter till when you were absent in the form of dd-mm-yyyy-')
                        rea=input('enter the reason-')
                        sub=color.UNDERLINE + sub + color.END
                        a=color.DARKCYAN + n + color.END
                        s=add1+'\n'+add2+'\n'+add3+'\n\n'
                        r=rec1+'\n'+rec2+'\n'+rec3+'\n'
                        k=file1.read()
                        k=k.replace('<name>',n)
                        k=k.replace('<class>',cl)
                        k=k.replace('<section>',sec)
                        k=k.replace('<subject>',subject)
                        k=k.replace('<reason>',rea)
                        k=k.replace('<date1>',date1)
                        k=k.replace('<date2>',date2)
                        file.write('\n'+h+'\n\n'+s+d1+'\n\n'+r+'\n\n'+sub+'\n'+k+'\n'+a+'\n'+N+'\n\n')
                        file.seek(0)
                        s=file.read()
                        print(s)
                        file.close()
                        file1.close()
                    elif ch=='3':
                        print('you have choosen the topic of changing the stream-')
                        file=open('user3.txt','w+')
                        file1=open('principalstream.txt','r+')
                        sub=input('enter subject of the letter-')
                        sub=sub.upper()
                        sub='subject: {}'.format(sub)
                        h='letter to the principal'
                        h=h.upper()
                        h=color.UNDERLINE + h + color.BOLD + color.END
                        h=h.center(100)
                        n=input('enter name to be inserted-')
                        cl=input('enter your class-')
                        sec=input('enter your section-')
                        add1=input('enter address line 1-')
                        add2=input('enter address line 2-')
                        add3=input('enter address line 3-')
                        rec1='THE PRINCIPAL'
                        rec2=input('enter receiver address line 2-')
                        rec3=input('enter receiver address line 3-')
                        today=date.today()
                        d1=today.strftime('%B%d,%Y')
                        N=n.upper()
                        stream1=input("enter the stream you have-")
                        stream2=input("enter the stream you want-")
                        sub=color.UNDERLINE + sub + color.END
                        a=color.DARKCYAN + n + color.END
                        s=add1+'\n'+add2+'\n'+add3+'\n\n'
                        r=rec1+'\n'+rec2+'\n'+rec3+'\n'
                        k=file1.read()
                        k=k.replace('<name>',n)
                        k=k.replace('<class>',cl)
                        k=k.replace('<section>',sec)
                        k=k.replace('<stream1>',stream1)
                        k=k.replace('<stream2',stream2)
                        file.write('\n'+h+'\n\n'+s+d1+'\n\n'+r+'\n\n'+sub+'\n'+k+'\n'+a+'\n'+N+'\n\n')
                        file.seek(0)
                        s=file.read()
                        print(s)
                        file.close()
                        file1.close()
            elif a=='2':
                print('you have selected letter to the boss')
                ch='yes'
                while ch!='4':
                    print('choose one of the following options to proceed:\n1.leave\n2.promotion\n3.resignation')
                    ch=input('\nenter one of the following-\n')
                    if ch=='1':
                        print('you have selected letter of leave to the boss')
                        file=open('user4.txt','w+')
                        file1=open('bossleave.txt','r+')
                        n=input('enter your name as an employee-')
                        h='letter to the boss'
                        h=h.upper()
                        h=color.UNDERLINE + h + color.BOLD + color.END
                        h=h.center(100)
                        sub=input('enter subject of the letter-')
                        sub=sub.upper()
                        sub='subject:{}'.format(sub)
                        ad1=input('enter senders address line 1-')
                        ad2=input('enter senders address line 2-')
                        ad3=input('enter senders address line 3-')
                        today=date.today()
                        d1=today.strftime('%B%d,%Y')
                        N=n.upper()
                        rec1='TO'
                        rec2=input('name of boss-')
                        rec3=input('enter designation of the boss-')
                        nc=input('enter name of the company/institute-')
                        nlt=input('enter no. of leaves you want to take-')
                        date1=input('enter the date from when you will be on a leave in the form of dd-mm-yyyy-')
                        rea=input('enter reason-')
                        date2=input('enter the date till which you are planning to take the leave in the form of dd-mm-yyyy-')
                        sub=color.UNDERLINE + sub + color.END
                        a=color.DARKCYAN + n + color.END
                        s=ad1+'\n'+ad2+'\n'+ad3
                        r=rec1+'\n\n'+rec2+'\n'+rec3+'\n'+nc
                        k=file1.read()
                        k=k.replace('<no. of leaves taken>',nlt)
                        k=k.replace('<reason>',rea)
                        k=k.replace('<date1>',date1)
                        k=k.replace('<date2>',date2)
                        file.write('\n'+h+'\n\n'+s+'\n'+d1+'\n\n'+r+'\n\n'+sub+'\n'+k+'\n'+a+'\n'+N+'\n\n')
                        file.seek(0)
                        s=file.read()
                        print(s)
                        file.close()
                        file1.close() 
                    elif ch=='2':
                        print('you have selected letter for promotion to the boss.')
                        file=open('user5.txt','w+')
                        file1=open('promotion.txt','r+')
                        n=input('enter the name  of the employee')
                        sub=input('enter subject of the letter ')
                        h='letter to the boss'
                        h=h.upper()
                        h=color.UNDERLINE + h + color.BOLD + color.END
                        h=h.center(100)
                        sub=sub.upper()
                        sub='subject:{}'.format(sub)
                        ad1=input('enter sender address line 1-')
                        ad2=input('enter sender address line 2-')
                        ad3=input('enter sender address line 3-')
                        today=date.today()
                        d1=today.strftime('%B%d,%Y')
                        N=n.upper()
                        rec1='TO'
                        rec2=input('enter name of boss-')
                        rec3=input('enter designation of boss-')
                        nc=input('enter the name of company/institution-')
                        today=date.today()
                        d1=today.strftime('%B%d,%Y')
                        N=n.upper()
                        job1=input('Please enter the post that you desire-')
                        job2=input('Please enter the post you currently have-')
                        sub=color.UNDERLINE + sub + color.END
                        a=color.DARKCYAN + n + color.END
                        s=ad1+'\n'+ad2+'\n'+ad3+'\n\n'
                        r=rec1+'\n'+rec2+'\n'+rec3+'\n'+nc
                        k=file1.read()
                        k=k.replace('<name>',n)
                        k=k.replace('<desired job title>',job1)
                        k=k.replace('<your current job title>',job2)
                        file.write('\n'+h+'\n\n'+s+d1+'\n\n'+r+'\n\n'+sub+'\n\n'+k+'\n'+a+'\n'+N+'\n\n')
                        file.seek(0)
                        s=file.read()
                        print(s)
                        file.close()
                        file1.close()
                    elif ch=='3':
                        print('you have selected letter for resignation to the boss-')
                        file=open('user6.txt','w+')
                        file1=open('resignation.txt','r+')
                        n=input('enter the name  of the employee-')
                        sub=input('enter subject of the letter-')
                        sub=sub.upper()
                        sub='subject:{}'.format(sub)
                        h='letter to the boss'
                        h=h.upper()
                        h=color.UNDERLINE + h + color.BOLD + color.END
                        h=h.center(100)
                        ad1=input('enter sender address line 1-')
                        ad2=input('enter sender address line 2-')
                        ad3=input('enter sender address line 3-')
                        N=n.upper()
                        rec1='TO'
                        rec2=input('enter name of boss-')
                        rec3=input('enter designation of boss-')
                        nc=input('enter name of company/institute-')
                        today=date.today()
                        d1=today.strftime('%B%d,%Y')
                        posname=input("enter your position name-")
                        sub=color.UNDERLINE + sub + color.END
                        a=color.DARKCYAN + n + color.END
                        s=ad1+'\n'+ad2+'\n'+ad3+'\n\n'
                        r=rec1+'\n\n'+rec2+'\n'+rec3+'\n'+nc
                        k=file1.read()
                        k=k.replace('(name)',n)
                        k=k.replace('(company name)',nc)
                        k=k.replace('(position name)',posname)
                        file.write('\n'+h+'\n\n'+s+d1+'\n\n'+r+'\n\n'+sub+'\n\n'+k+'\n'+a+'\n'+N+'\n\n')
                        file.seek(0)
                        s=file.read()
                        print(s)
                        file.close()
                        file1.close()
    elif ch1=='2':
          print('you have selected informal letter')
          print('\n')
          ch='yes'
          while ch!='no':
              ch=input('press any key to continue or no to stop-')
              file=open('custom.txt','w+')
              file1=open('informal.txt','r')
              if ch=='no':
                  i=color.DARKCYAN +'X_X_X_X_X_X_X_THANK YOU FOR USING OUR APPLICATION_X_X_X_X_X_X' + color.END
                  print(i.center(100),'\n')
                  break
              ad1=input('enter your address line 1-')
              ad2=input('enter your address line 2-')
              ad3=input('enter your address line 3-')
              name1=input("enter the name of relative to whom you are writing this letter")
              para1=input("enter the first paragraph of the letter-")
              para2=input("enter the second paragraph of the letter-")
              para3=input("enter the third paragraph of the letter-")
              n=input("enter your name-")
              h='informal letter'
              h=h.upper()
              h=color.UNDERLINE + h + color.BOLD + color.END
              h=h.center(100)
              a=color.DARKCYAN + n + color.END
              today=date.today()
              d1=today.strftime('%B%d,%Y')
              N=n.upper()
              s=ad1+'\n'+ad2+'\n'+ad3+'\n\n'
              k=file1.read()
              k=k.replace('<name1>',name1)
              k=k.replace('<para1>',para1)
              k=k.replace('<para2>',para2)
              k=k.replace('<para3>',para3)
              s=ad1+'\n'+ad2+'\n'+ad3+'\n\n'
              file.write('\n'+h+'\n\n'+s+ d1 +'\n\n'+ k +'\n'+a+'\n'+N+'\n\n')
              file.seek(0)
              s=file.read()
              print(s)
              file.close()
              file1.close()
    elif ch1=='3':
       webbrowser.open('https://www.a1letters.com/')
    else:
         i=color.DARKCYAN +'X_X_X_X_X_X_X_THANK YOU FOR USING OUR APPLICATION_X_X_X_X_X_X' + color.END
         print(i.center(100),'\n')
         break