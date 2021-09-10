# HourlyChime---Tracking-Widgit
Simple program that, on the hour, makes a chime sound and opens an intuitive GUI that allows the user to input their completed activities. The input gets stored in a CSV file which is annotated and ready for processing in Excell.

The HourlyChime program will track 2 time parameters. Hour change and sleep. After your PC comes out of sleep, the HourlyChime will open automatically (this feature can be suspended). It will aslo keep track of the last time it chimed and the last time the user gave a completed activities input.

By default, the activities for which the user can input completed time are: Science, Finance, Manuten, Research, Workout, and Art.
The GUI works by prompting the user to declair the activities they worked on since the last chime, providing also a timer showing the time passed since their last input. Then, sliders will appear for each activity the user declairs. With these, the user can declair the amount of hours they worked on each task (possibility to change to minutes too).

The user input will be saved in a CSV file.
