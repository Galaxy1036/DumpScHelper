# -*- coding: utf-8 -*-
#Small utilities written by RoyaleTeam

import os
from sys import platform as _platform

print("""   

Programm made by:

  _____                   _   _______                   
 |  __ \                 | | |__   __|                  
 | |__) |___  _   _  __ _| | ___| | ___  __ _ _ __ ___  
 |  _  // _ \| | | |/ _` | |/ _ \ |/ _ \/ _` | '_ ` _ \ 
 | | \ \ (_) | |_| | (_| | |  __/ |  __/ (_| | | | | | |
 |_|  \_\___/ \__, |\__,_|_|\___|_|\___|\__,_|_| |_| |_|
               __/ |                                    
              |___/                                     

                                  """)
print("Youtube: https://www.youtube.com/channel/UCc2zwKEQiwuBd5b3g9nxdlA/featured / Twitter: https://twitter.com/RoyalTeamYT")

if _platform == "linux" or _platform == "linux2":
	# linux
	print("[+]Linux version detected")
	command = "find ./assets/sc -name *_tex.sc | xargs python dumpsc.py -o output_dir/"

elif _platform == "darwin":
	# MAC OS X
	print("[+]Mac Os version detected")
	command = "find ./assets/sc -name *_tex.sc | xargs python dumpsc.py -o output_dir/"

elif _platform == "win32":
	# Windows
	print("[+]Windows version detected")	
	command = "for %v in (*tex.sc) do python dumpsc.py %v"

def process():
	try:
	    print("Do you want to dump 1 file or all files ?")
	    print("1-One File")
	    print("2-All Files")
	    
	    choice = int(input())
	    if choice == 1:
	    	print("[+] Enter the name of your file ")
	    	try:
	    		filename = str(input(">>"))
	    		os.system("python dumpsc.py {}".format(filename))
	    	except ValueError:
	    		print("[+] Enter the filename please")
	    		process()

	    elif choice == 2:
	    	os.system("{}".format(command))
	    else:
	    	print("Enter a valid number please")
	    	process()
	except ValueError:
	    print("Enter a number please")
	    process()
	except KeyboardInterrupt:
		print("[+] Process stoped")

if __name__ == "__main__":
	process()



