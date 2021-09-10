"""
Core timer that 'Triggers' the chime and GUI:
    Programmable intervals: 1. On the hour the 'Chime' will activate, which both rings the chime sound and runst the HourlyChimeWidget 
                            2. It checks for sleep and if 6am has been passed, it shows a 'new day' message and activates
"""
# ## Libraries ## #
#region 
import os
from win10toast import ToastNotifier
import datetime
import time
import winsound
import HourlyChimeWidget
import IPC
#endregion

# ## Windows Notification and Execution on startup aid ## #
#region
toast = ToastNotifier()
toast.show_toast("Timer4Action", "The process has started :D", duration=15, threaded=True)

# ## Changing cmd directory ## #
os.chdir("C:/Users/rodri/PycharmProjects/HourlyChimeProject")
#endregion

# ## Variable Settings ## #
# Time Variables - These are relative to when the program is initialized
LastTrigger = IPC.GetLastTrigger()
PinHour = datetime.datetime.now().strftime('%H')

# ## Chime ## #
def ChimeSound():
    frequency = 440  # Hz Captain Crunch hacking frequency is 2600 in case you want to hear it :p
    duration = 1100  # ms
    winsound.Beep(frequency, duration)

# ## Checking for sleep and new day ## #
while True:
    time.sleep(1)
    diff1 = (datetime.datetime.now() - PinTime).total_seconds()
    if diff1 > 10:
        #Checking for a new day
        time.sleep(10) #lil buffer to avoid slowing down my PC
        if IPC.GetLastTrigger() > IPC.HaveWePassedSix() == True:
            ChimeSound()
            HourlyChimeWidget.main()
            IPC.UpdateLastTrigger()

    PinTime = datetime.datetime.now()

# ## Chime on the hour ## #
    if PinHour != datetime.datetime.now().strftime('%H'):
        ChimeSound()
        print('How the time flies...')
        HourlyChimeWidget.main()
        IPC.UpdateLastTrigger()

        PinHour = datetime.datetime.now().strftime('%H')

