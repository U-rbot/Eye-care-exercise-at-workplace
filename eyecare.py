import tkinter as tk
import time

class EyeCareApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Eye Care App")
        self.window.geometry("300x200")
        
        # Create the UI elements
        self.label1 = tk.Label(self.window, text="20-20-20 Rule")
        self.label1.pack()
        self.start_button1 = tk.Button(self.window, text="Start", command=self.start_timer1)
        self.start_button1.pack()
        self.pause_button1 = tk.Button(self.window, text="Pause", state="disabled", command=self.pause_timer1)
        self.pause_button1.pack()
        self.label2 = tk.Label(self.window, text="Activity Reminder")
        self.label2.pack()
        self.start_button2 = tk.Button(self.window, text="Start", command=self.start_timer2)
        self.start_button2.pack()
        self.pause_button2 = tk.Button(self.window, text="Pause", state="disabled", command=self.pause_timer2)
        self.pause_button2.pack()
        
        self.timers = []
        self.paused_timers = []
        self.window.mainloop()
    
    def start_timer1(self):
        self.start_button1.config(state="disabled")
        self.pause_button1.config(state="normal")
        timer = self.create_timer(20*60, self.label1, "Look away for 20 seconds")
        self.timers.append(timer)
    
    def start_timer2(self):
        self.start_button2.config(state="disabled")
        self.pause_button2.config(state="normal")
        timer = self.create_timer(30*60, self.label2, "Take a break and do an activity")
        self.timers.append(timer)
    
    def create_timer(self, duration, label, message):
        timer = Timer(duration, label, message)
        timer.start()
        return timer
    
    def pause_timer1(self):
        self.pause_button1.config(state="disabled")
        self.start_button1.config(state="normal")
        timer = self.timers.pop(0)
        timer.pause()
        self.paused_timers.append(timer)
    
    def pause_timer2(self):
        self.pause_button2.config(state="disabled")
        self.start_button2.config(state="normal")
        timer = self.timers.pop(0)
        timer.pause()
        self.paused_timers.append(timer)

class Timer:
    def __init__(self, duration, label, message):
        self.duration = duration
        self.remaining = duration
        self.label = label
        self.message = message
        self.paused = False
    
    def start(self):
        self.start_time = time.monotonic()
        self.update_label()
    
    def update_label(self):
        if not self.paused:
            time_elapsed = time.monotonic() - self.start_time
            time_remaining = max(self.remaining - time_elapsed, 0)
            minutes, seconds = divmod(time_remaining, 60)
            time_str = f"{minutes:02d}:{seconds:02d}"
            self.label.config(text=f"{self.message} ({time_str} remaining)")
            if time_remaining > 0:
                self.label.after(1000, self.update_label)
            else:
                self.label.config(text=self.message)
    
    def pause(self):
        self.remaining = max(self.remaining - (time.monotonic() - self.start_time), 0)
        self.paused = True
    
    def resume(self):
        self.start_time = time.monotonic()
        self.paused = False
        self.update_label()

if __name__ == "__main__":
    app = EyeCareApp()
``
