"""
 2. Action commands. These include the Chime sounds of both the hour and for the user to input completed actions
    a. Widget for the numerical input of completed actions.
       Widget shows deadline and states the last time since calendar update.
    b. Widget asks user weather they want to input activities completed since the last update.
       And if not, asks weather that is the end of the day.
"""
# TODO --- Look into how to make it an integral part of the desktop
#  Make sure each month is saved in a different xlsx sheet and aggregate them in Excel itself.
#  Also include a way to signal start of the day.

# ## Libraries ## #
#region
import datetime
from tkinter import *
import sys
import Input_Widget
#endregion

# ## Settings ## #
Deadline = datetime.datetime(2021, 9, 14)  # Deadline for the CORE lab application

# ## GUI Initiation ## #
def main():
    root = Tk()
    root.title('Hourly Chime')

    # ## GUI functions ## #
    def CountDown():
        t = datetime.datetime.today()
        time_left = Deadline - t
        time_left = ChopMiroseconds(time_left)
        countdown_label.configure(text=time_left)
        root.after(1000, CountDown)

    def ChopMiroseconds(delta):
        return delta - datetime.timedelta(microseconds=delta.microseconds)

    def OpenInputWidget():  # This will connect to the next widget age which will contain input fields
        Input_Widget.Toplevel()

    def SleepTill6():
        pass #Here I will incorporate a command that stops the trigger event until a 6am hour is passed. Save the boolean in IPC

    def QuitProgram():  # Make sure this quits Timer4ActionTrigger, if running of course.
        sys.exit()


    # ## GUI Labels ## #
    #region
    deadline_name = Label(root, text='Time Left for CORE Lab Application', font=('Helvetica', 20), fg='darkorange', bg='gray')
    countdown_label = Label(root, text='', font=('Helvetica', 48), fg='darkorange', bg='gray')
    input_request_label = Label(root, text='Would you like to input new completed activities?', font=('Helvetica', 14))
    input_decline_label = Label(root, text='Shall I request input at a later time?', font=('Helvetica', 14))
    #endregion

    # ## GUI buttons ## #
    #region    
    input_accept_button = Button(root, text='Input Completed Tasks', font='sans 16 bold', command=OpenInputWidget, padx=5, pady=5, bg='forestgreen')
    input_decline_button_1 = Button(root, text="Snooze 30 minutes", command=root.destroy, padx=5, pady=5)
    input_decline_button_2 = Button(root, text="End of the day!", command= SleepTill6, padx=5, pady=5)
    quit_program_button = Button(root, text="Quit", command=QuitProgram, padx=5, pady=5)
    #endregion

    # ## Label and Button Locations ## #
    #region
    deadline_name.grid(row=0, column=0, columnspan=5, pady=30)
    countdown_label.grid(row=1, column=0, columnspan=5, pady=30)
    input_request_label.grid(row=2, column=0, columnspan=5, pady=15)
    input_accept_button.grid(row=3, column=0, columnspan=5)

    input_decline_label.grid(row=5, column=0, columnspan=5, pady=15)
    input_decline_button_1.grid(row=6, column=1)
    input_decline_button_2.grid(row=6, column=3)

    quit_program_button.grid(row=6, column=4, pady=15)
    #endregion


    # ## GUI termination ## #
    CountDown()
    root.mainloop()


if __name__ == "__main__":
    main()
