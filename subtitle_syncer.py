import time
import tkinter as tk

class SubtitleSyncer:

    def __init__(self,root):

        self.running             = False
        self.start_time          = 0 
        self.elapsed_time        = 0
        self.started_buttom_name = ""

        self.description_dict    = {"audio"   :"late",
                                    "subtitle":"early"}
        
        top_frame = tk.Frame(root)
        top_frame.pack(fill="x")

        bot_frame = tk.Frame(root)
        bot_frame.pack(fill="x")


        self.description_label   = tk.Label(top_frame,
                                        text=f"subtitle is ...",
                                        font=("arial",15))
                                        
        self.description_label.pack(side="left",
                            pady=20,
                            padx=20)


        self.timer_label = tk.Label( top_frame,
                                text="00:00:00",
                                font=("arial",15))
        self.timer_label.pack(side="top",
                        pady=20)

        self.subtitle_button = tk.Button(bot_frame,
                                    text="Substitle",
                                    command=lambda:self.switch_start_stop(buttom_name="subtitle",root=root), 
                                    width=10, 
                                    font=("Helvetica", 15))

        self.subtitle_button.pack(side="left",
                            padx=20,
                            pady=20)

        self.audio_button = tk.Button(bot_frame,
                                text="Audio",
                                command=lambda:self.switch_start_stop(buttom_name="audio",root=root),
                                width=10,
                                font=("Helvetica", 14))

        self.audio_button.pack(side="right",
                        padx=20,
                        pady=20)

    def format_time(self,seconds):
        mins, secs = divmod(seconds, 60)
        return f"{int(mins):02}:{int(secs):02}:{int((seconds * 100) % 100):02} seconds"  # Formato MM:SS:MS

    def update_timer(self,root):
        
        if self.get_running():

            self.set_elapsed_time(time.time() - self.get_start_time())
            time_display = self.format_time(self.get_elapsed_time())

            self.timer_label.config(text=time_display)
            root.after(10, self.update_timer(root))    


    def start_timer(self,root):

        if not self.get_running():
            self.set_running(True)
            self.set_start_time(time.time() - self.get_elapsed_time())

            self.update_timer(root)

    def stop_timer(self):

        self.description_label.config(text=f"subtitle is {self.description_dict[self.get_started_buttom_name()]} ",
                                      font=("arial",15))
        self.description_label.update()

        self.reset()

    def switch_start_stop(self,buttom_name,root):

        if self.get_started_buttom_name() == "" and not self.get_running():

            self.set_started_buttom_name(buttom_name)

            self.start_timer(root)
        else:
            self.stop_timer()

    def reset(self):
        
        self.set_started_buttom_name("")
        self.set_running(False)
        self.set_start_time(0)
        self.set_elapsed_time(0)

    #getters and setters

    #running getter and setter
    def get_running(self):
        return self.running

    def set_running(self, value):
        if not isinstance(value, bool):
            raise ValueError("value of 'running' must be boolean (True ou False).")
        self.running = value

    #start time getter and setter
    def get_start_time(self):
        return self.start_time

    def set_start_time(self, value):
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("value of 'start_time' must be positive.")
        self.start_time = value

    
    #elapsed time getter and setter

    def get_elapsed_time(self):
        return self.elapsed_time

    def set_elapsed_time(self, value):
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("value of 'elapsed_time' must be positive.")
        self.elapsed_time = value

    #started buttom name getter and setter

    def get_started_buttom_name(self):
        return self.started_buttom_name

    def set_started_buttom_name(self, value):
        if not isinstance(value, str):
            raise ValueError("value of 'started_buttom_name' must be a string.")
        self.started_buttom_name = value


        ## bug pra amanah RecursionError: maximum recursion depth exceeded


