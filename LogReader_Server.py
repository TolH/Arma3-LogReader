#//=======================================================//
import sys, time, os, glob#, psutil
#//=======================================================//
#                  §§§ CONFIGS START HERE §§§
#//=======================================================//
#
# (SET YOUR OWN PATH TO SERVER .rpt FILE!) AUTO OPEN LATEST CREATED .RPT FROM SERVER, NO FILE NEED TO BE CREATED!
Server_RPT_location = 'D:/SteamLibrary/steamapps/common/Arma 3/SC_0908_MAIN/*.rpt'
# (SET YOUR OWN PATH TO SERVER .err FILE!) YOU HAVE TO CREATE THE FILE FIRST!
Error_logs = 'D:/SteamLibrary/steamapps/common/Arma 3/SC_0908_MAIN/-=ERRORS_LOGS=-.err'
# (SET YOUR OWN PATH TO SERVER .tck FILE!) YOU HAVE TO CREATE THE FILE FIRST!
Tickets_logs = 'D:/SteamLibrary/steamapps/common/Arma 3/SC_0908_MAIN/-=TICKETS_LOGS=-.tck'
#
#//=======================================================//
#                   §§§ CONFIGS END HERE §§§
#//=======================================================//
os.system("")
class ColorStyle():
    RED = '\033[91m'
    GREEN = '\033[92m'
    BLUE = '\033[0;94m'
    YELLOW = '\033[0;93m'
    BLACK='\033[0;90m'
    PURPLE='\033[0;95m'
    CYAN='\033[0;96m'
    WHITE='\033[0;97m'
    RESET = '\033[0m'
#//=======================================================//
print (ColorStyle.YELLOW + '''
 ______ ______ ______ ______ ______ ______ ______ ______ ______ ______ ______ ______
|      |      |      |      |      |      |      |      |      |      |	     |	    |
 _                 _____                _              _____           _       _
| |               |  __ \              | |            / ____|         (_)     | |
| |     ___   __ _| |__) |___  __ _  __| | ___ _ __  | (___   ___ _ __ _ _ __ | |_
| |    / _ \ / _` |  _  // _ \/ _` |/ _` |/ _ \ '__|  \___ \ / __| '__| | '_ \| __|
| |___| (_) | (_| | | \ \  __/ (_| | (_| |  __/ |     ____) | (__| |  | | |_) | |_
|______\___/ \__, |_|  \_\___|\__,_|\__,_|\___|_|    |_____/ \___|_|  |_| .__/ \__|
	      __/ |                                                     | |
	     |___/                                                      |_|
|______|______|______|______|______|______|______|______|______|______|______|______|
''')
#//=======================================================//
array_char_sel = ['.',':']
time_cnt = 0
log_delay = 30 #wait 15 seconds so server can create .log files first before starting main loop
sys.stdout.write('Loading latest Arma3_server log:')
#
for tick_range in range(log_delay):
    sys.stdout.write (array_char_sel[0])
    sys.stdout.flush()
    time.sleep(0.5)
    time_cnt = time_cnt + 1
    #
    if (time_cnt == log_delay):
        sys.stdout.write (array_char_sel[1])
        print(ColorStyle.GREEN + "\n")
    #
#
#//=======================================================//
open_Server_RPT_location = open(max(glob.glob(Server_RPT_location),key=os.path.getctime), 'r') #read latest .rpt log file from server
keep_reading_loop = 1
read_speed = 0.010 #DEFAULT 0.010
#//=======================================================//
# SERVER HAS BEEN STARTED AND LOGS SHOULD BE AVAILABLE, STRATING LOOP
while (keep_reading_loop == 1):
    #
    Server_RPT = open_Server_RPT_location.readline() #read latest .rpt file from server
    open_Error_RPT_location = open(Error_logs, 'a') #append latest .err errors file from server
    write_Tickets_logs = open(Tickets_logs,'a') #append latest .tck tickets file from server
    #
    #if Server_RPT.isascii(): #Returns True if all characters in the string are ascii characters
    if Server_RPT.find(":")  != -1:
        time.sleep(read_speed)
        print(Server_RPT.strip ("\n"))
        # 
        if (Server_RPT.find("ERROR") != -1) or (Server_RPT.find("Error") != -1) or (Server_RPT.find("error") != -1):
            print(ColorStyle.RED + Server_RPT.strip ("\n") + ColorStyle.GREEN)
            open_Error_RPT_location.write("%s %s" % (time.strftime("%Y-%m-%d %H:%M"), Server_RPT))
        # 
        if Server_RPT.find("PLAYER CONNECTED") != -1 or Server_RPT.find("PLAYER DISCONNECTED") != -1 or Server_RPT.find("SL_Zeus") != -1:
            print(ColorStyle.BLUE + Server_RPT.strip ("\n") + ColorStyle.GREEN)
        # 
        if Server_RPT.find("TIMSBR SUBMITBOX:") != -1:
            print(ColorStyle.YELLOW + Server_RPT.strip ("\n") + ColorStyle.GREEN)
            write_Tickets_logs.write("%s %s" % (time.strftime("%Y-%m-%d %H:%M"), Server_RPT))
        # 
        if Server_RPT.find("Class CBA_Extended_EventHandlers_base destroyed with lock count") != -1:
            keep_reading_loop = 0
        #
    else:
        #Arma3server_Running = "arma3server_x64.exe" in (p.name() for p in psutil.process_iter())
        time.sleep(0.5)
        #if (Arma3server_Running == False):
            #keep_reading_loop = 0
    #
#//=======================================================//
open_Server_RPT_location.close()
open_Error_RPT_location.close()
write_Tickets_logs.close()
loopEnded = input(ColorStyle.RED + '                      -=============(ARMA3 SERVER IS NOT RUNNING OR CRASHED!!! Press enter to exit or restart)=============-' + ColorStyle.RESET)
#//=======================================================//
# TODO ADD CHOICE TO EITHER EXIT OR RESTART THE SERVER
#os.startfile('D:\SteamLibrary\steamapps\common\Arma 3\SC_0908_MAIN\LogReader_Server.py')