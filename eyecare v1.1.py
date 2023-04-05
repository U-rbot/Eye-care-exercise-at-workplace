import tkinter as tk
import time

class EyeCareApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Eye Care App")
        self.window.geometry("300x150")
        
        # Create the UI elements
        self.label1 = tk.Label(self.window, text="20-20-20 Rule")
        self.label1.pack()
        self.timer1 = tk.Label(self.window, text="")
        self.timer1.pack()
        self.button1 = tk.Button(self.window, text="Start", command=self.start_timer1)
        self.button1.pack(side=tk.LEFT)
        self.pause1 = tk.Button(self.window, text="Pause", command=self.pause_timer1, state="disabled")
        self.pause1.pack(side=tk.LEFT)
        self.label2 = tk.Label(self.window, text="Activity Reminder")
        self.label2.pack()
        self.timer2 = tk.Label(self.window, text="")
        self.timer2.pack()
        self.button2 = tk.Button(self.window, text="Start", command=self.start_timer2)
        self.button2.pack(side=tk.LEFT)
        self.pause2 = tk.Button(self.window, text="Pause", command=self.pause_timer2, state="disabled")
        self.pause2.pack(side=tk.LEFT)
        
        self.window.mainloop()
    
    def start_timer1(self):
        self.button1.config(state="disabled")
        self.pause1.config(state="normal")
        self.timer(20*60, self.label1, self.timer1, "Look away for 20 seconds")
        self.button1.config(state="normal")
        self.pause1.config(state="disabled")
    
    def start_timer2(self):
        self.button2.config(state="disabled")
        self.pause2.config(state="normal")
        self.timer(30*60, self.label2, self.timer2, "Take a break and do an activity")
        self.button2.config(state="normal")
        self.pause2.config(state="disabled")
    
    def pause_timer1(self):
        self.pause1.config(state="disabled")
        self.resume_timer1 = tk.Button(self.window, text="Resume", command=self.resume_timer_1)
        self.resume_timer1.pack(side=tk.LEFT)
    
    def pause_timer2(self):
        self.pause2.config(state="disabled")
        self.resume_timer2 = tk.Button(self.window, text="Resume", command=self.resume_timer_2)
        self.resume_timer2.pack(side=tk.LEFT)
    
    def resume_timer_1(self):
        self.resume_timer1.destroy()
        self.pause1.config(state="normal")
    
    def resume_timer_2(self):
        self.resume_timer2.destroy()
        self.pause2.config(state="normal")
    
    def timer(self, duration, label, timer_label, message):
        remaining = duration
        while remaining > 0:
            minutes, seconds = divmod(remaining, 60)
            time_str = f"{minutes:02d}:{seconds:02d}"
            label.config(text=f"{message} ({time_str} remaining)")
            timer_label.config(text=f"Time left: {time_str}")
            time.sleep(1)
            remaining -= 1
        label.config(text=message)
        timer_label.config(text="")
    
if __name__ == "__main__":
    app = EyeCareApp()
