"""
Inter Process Communication Script
- Allows variables used both by the HourlyChimeWidget and the Timer4Action
- Saves variables that can be used in the data management portion of the program (in Excell)
"""
# ## Libraries ## #
import datetime

#Overides the old last trigger date with the new one
def UpdateLastTrigger():
    tmp_f = open('Last_Trigger.txt','w+')
    tmp_f.write(str(datetime.datetime.now()))
    tmp_f.close()

def GetLastTrigger():
    with open('Last_Trigger.txt') as tmp_f:
        str_t = tmp_f.readline()
        tmp_f.close()
        dat_t = datetime.datetime.fromisoformat(str_t)
        return dat_t

def UpdateLastInput():
    tmp_f = open('Last_Input.txt','w+')
    tmp_f.write(str(datetime.datetime.now()))
    tmp_f.close()

def GetLastInput():
    with open('Last_Input.txt') as tmp_f:
        str_t = tmp_f.readline()
        tmp_f.close()
        dat_t = datetime.datetime.fromisoformat(str_t)
        return dat_t
 
def HaveWePassedSix(): # This is just needed to determine if it is the first entry of the day. I might need a specialized message
# If today's hour is < 6 AM 
    dt6 = None #Empty var for later
    if datetime.datetime.now().hour < 6:
    # Create date object for today's year, month, day at 6 AM
        dt6 = datetime.datetime(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day, 6, 0, 0, 0)
# If today is past 6 AM, increment date by 1 day
    else:
    # Get 1 day duration to add
        #day = datetime.timedelta(days=1)
    # Generate tomorrow's datetime
        tomorrow = datetime.datetime.now() + datetime.timedelta(days=1)
    # Create new datetime object using tomorrow's year, month, day at 6 AM
        dt6 = datetime.datetime(tomorrow.year, tomorrow.month, tomorrow.day, 6, 0, 0, 0)
    
    #havewepassedsix = GetLastInput() < dt6 < datetime.datetime.now()
    return dt6
    #return havewepassedsix