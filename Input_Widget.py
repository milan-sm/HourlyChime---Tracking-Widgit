from tkinter import *
import IPC
import datetime
import pandas as pd
import numpy
import csv

# Settings
interval_setting = 0.25 #Setting in hours 0.25 = 15minutes

# ## Initializing Variables ## #

slider_counter = 2
activity_list = []

# ## Main ## #
def Toplevel():
    Input_Widget = Tk()
    Input_Widget.title('Completed Activities Input')
    Input_Widget.focus_force()

    def ChopMiroseconds(delta):
        return delta - datetime.timedelta(microseconds=delta.microseconds)

    t_delta = datetime.datetime.now()-IPC.GetLastInput()
    t_delta = ChopMiroseconds(t_delta)
    delta_hours = (t_delta.days*24) + ((t_delta.seconds/3600))
    interval_list = numpy.arange(0, delta_hours, interval_setting)
    interval_list = list(interval_list)
    
    # ## Class for activities completed ## #
    class Activity:
        # Initializing the Activity class with an activity and a hotkey to be bound with
        def __init__(self, activity):
            global slider_counter
            self.activity = activity
            self.scale = 0

        def _label_n_slider(self):
            # Makes label using the activity name
            activity_label = Label(Input_Widget, text=str(self.activity))
            activity_label.grid(row=slider_counter, column=0, columnspan=1, pady=30)
        
            # Creates intervals in sliders
            def _time_interval(event):
                new_value = min(interval_list, key=lambda x: abs(x - float(event)))
                horizontal_slider.set(new_value)
                self.scale = horizontal_slider.get()

            # Makes the slider
            horizontal_slider = Scale(Input_Widget, from_=min(interval_list), to=max(interval_list),
                                  command=_time_interval, orient=HORIZONTAL, length=300, digits=4, resolution=0.25)
            horizontal_slider.grid(row=slider_counter, column=1, columnspan=1, pady=30)

        def get_info(self):
            return self.scale

# Making classes for each activity
#region
    s_activity = Activity("Science")
    f_activity = Activity("Finance")
    m_activity = Activity("Manuten")
    r_activity = Activity("Research")
    w_activity = Activity("Workout")
    a_activity = Activity("Art")
#endregion


    def _new_slider(event):
        #Inporting variables from outside this function
        global slider_counter
        global activity_list

        #Uses activity class to change the name of the labels associated with each slider
        if event.char == '1':
            slider_counter += 1
            s_activity._label_n_slider()

        if event.char == '2':
            slider_counter += 1
            f_activity._label_n_slider()

        if event.char == '3':
            slider_counter += 1
            m_activity._label_n_slider()

        if event.char == '4':
            slider_counter += 1
            r_activity._label_n_slider()

        if event.char == '5':
            slider_counter += 1
            w_activity._label_n_slider()

        if event.char == '6':
            slider_counter += 1
            a_activity._label_n_slider()

    Input_Widget.bind("<Key>", _new_slider) #Bind it to the window

    def get_all_info():
        rows =[]
        lst = [s_activity, f_activity, m_activity, r_activity, w_activity, a_activity]
        for i in lst:
            rows.append(i.get_info())
        #df = pd.DataFrame(rows,index=["Science","Finacne","Manuten","Research", "Workout", "Art"], 
        #                  columns=['Hours completed'])
        #print(rows)
        #print(df)

        #Writing input to csv file
        rows.append(IPC.GetLastInput())
        with open('input.csv', 'a', newline='') as csvfile:
            my_writer = csv.writer(csvfile, delimiter=' ')
            my_writer.writerow(rows)

        IPC.UpdateLastInput()
        Input_Widget.destroy()

# ## Buttons
    since_lst_input_label = Label(Input_Widget,text='Time since your last entry> ' + str(t_delta), font=14,fg='darkorange',bg='gray')
    since_lst_input_label.grid(row=0, column=0, columnspan=4, pady=30)

    key_label = Label(Input_Widget, text='Add the activities completed and time dedicated to each be pressing the numbers outlined below \n \n 1:Sciecne \t 2:Finance \t 3:Manuten\n 4:Research \t 5:Workout \t 6:Art',
                    font=12,)
    key_label.grid(row=1, column=0, columnspan=4, pady=40)

    input_button = Button(Input_Widget, text='Input', font=12, command= get_all_info)
    input_button.grid(row=2, column=0, columnspan=4, pady=40)

    Input_Widget.mainloop()
    
if __name__ == "__input_widget__":
    Toplevel()
