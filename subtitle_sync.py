import time
import tkinter as tk


#posso fazer uma classe pra gerir isso mas vou resolver apenas para fins praticos , por hora
running             = False
start_time          = 0 
elapsed_time        = 0
started_buttom_name = ""
description_dict    = {"audio"   :"late",
                       "subtitle":"early"}




def format_time(seconds):
    mins, secs = divmod(seconds, 60)
    return f"{int(mins):02}:{int(secs):02}:{int((seconds * 100) % 100):02} seconds"  # Formato MM:SS:MS

def update_timer():

    global elapsed_time

    if running:
        elapsed_time = time.time() - start_time
        time_display = format_time(elapsed_time)

        timer_label.config(text=time_display)
        main_app.after(10, update_timer)

def start_timer():
    global running,\
           start_time

    if not running:
        running = True
        start_time = time.time() - elapsed_time ##se eu tirar isso acho q só fica negativo

        update_timer()

def stop_timer():
    global started_buttom_name, \
           description_label    \

    description_label.config(text=f"subtitle is {description_dict[started_buttom_name]} ",
                             font=("arial",15))
    description_label.update()
    reset()

    
    ##implementar um reset da interface quando stop

    

def switch_start_stop(buttom_name):
    global running,                 \
           started_buttom_name

    if started_buttom_name == "" and not running:

        started_buttom_name = buttom_name
        start_timer()




    else:
        stop_timer()

def reset():
    global started_buttom_name, \
            running,            \
            start_time,         \
            elapsed_time

    started_buttom_name = ""
    running = False
    start_time          = 0 
    elapsed_time        = 0


    
    return timer_label

main_app = tk.Tk()

top_frame = tk.Frame(main_app)
top_frame.pack(fill="x")

bot_frame = tk.Frame(main_app)
bot_frame.pack(fill="x")


description_label   = tk.Label(top_frame,
                                text=f"subtitle is ...",
                                font=("arial",15))
                                
description_label.pack(side="left",
                       pady=20,
                       padx=20)


timer_label = tk.Label( top_frame,
                        text="00:00:00",
                        font=("arial",15))
timer_label.pack(side="top",
                 pady=20)

subtitle_button = tk.Button(bot_frame,
                            text="Substitle",
                            command=lambda:switch_start_stop(buttom_name="subtitle"), 
                            width=10, 
                            font=("Helvetica", 15))

subtitle_button.pack(side="left",
                      padx=20,
                      pady=20)

audio_button = tk.Button(bot_frame,
                          text="Audio",
                          command=lambda:switch_start_stop(buttom_name="audio"),
                          width=10,
                          font=("Helvetica", 14))

audio_button.pack(side="right",
                  padx=20,
                  pady=20)


main_app.mainloop()

