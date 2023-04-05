
The EyeCareApp class now includes two new labels for displaying the remaining time for each timer, and two new buttons for pausing each timer.
The start_timer1 and start_timer2 methods now enable the corresponding pause button when the timer starts, and disable the start button. They also call the timer method with the appropriate duration, label, and message parameters.

The pause_timer1 and pause_timer2 methods disable the corresponding pause button and create a new Resume button, which calls the resume_timer_1 or resume_timer_2 methods when clicked.
The resume_timer_1 and resume_timer_2 methods destroy the Resume button and re-enable the corresponding pause button.
The timer method now updates the timer_label with the remaining time for each second that passes, and stops updating the label when the timer is finished.
With these changes, the user can start and pause each timer, and see the remaining time for each timer displayed in the GUI window.
