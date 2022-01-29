#!/usr/bin/env python
import os
import sys
import getpass
import subprocess as sp
import re

command = ' '.join(map(str, sys.argv[1:]))
username = getpass.getuser()
prompt = "[sudo] password for {0}: ".format(username)
wrong_password = "Try again [sudo] password for {0}: ".format(username)
password = ''
Flag = False

sudo = 'sudo' # change this to the the new name of the sudo binary

def Ver():
    check = sp.Popen('sudo -S id', shell=True,stdout=sp.PIPE,encoding='utf-8')
    if check.communicate():
        check.terminate()
        return True
    return False

def run(command):
    if command == 'su':
        print('this command not allow {}'.format(command))
        sys.exit(666)
    sp.call('sudo -S '+command, shell=True)

def byapss(password):
    Flag = True
    data = sp.Popen(['sudo', '-S', 'whoami'], stdin=sp.PIPE, stdout=sp.PIPE,
                            stderr=sp.PIPE, encoding='utf-8').communicate(input=password + '\n')
    # print(command,Ver,data)
    if re.search('root',data[0]):
        return True
    else:
       pass
    return False




def sudocmd(cmd, password=False):
    global Flag
    Flag = True
    wrapper = password
    if password and not type(password) == str:
        run(cmd)
    elif not password or type(password) == str:
        if byapss(wrapper):
            run(cmd)
    else:
        print('Worng Passwrod')


def main():
   global Flag
   Verify = Ver()
   if not Verify and not Flag:
       password = getpass.getpass(prompt)
       sudocmd(command, password)
   elif Flag:
       password = getpass.getpass(wrong_password)
       sudocmd(command, password)
   else:
       sudocmd(command,True)





if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()

