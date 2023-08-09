import functools
import threading
import time
import tkinter.messagebox as msg
import customtkinter
import psutil as ps
from customtkinter import *
from PIL import Image

# main function changer label


def cpu_gpu(label1, label2):
    # infinity loop to get data every sec
    while True:
        try:
            # main funct
            cpu = ps.cpu_percent()
            mem = ps.virtual_memory().percent
            # changing the label objet's text and text color

            # cpu value and color
            if 50 < cpu < 80:

                label1.configure(text=f"CPU :%{cpu}", text_color="Orange")

            elif cpu < 50:

                label1.configure(text=f"CPU :%{cpu}", text_color="green")

            else:

                label1.configure(text=f"CPU :%{cpu}", text_color="red")

            # memory value and color
            if mem < 50:

                label2.configure(text=f"MEM :%{mem}", text_color="green")

            elif 50 <= mem < 80:

                label2.configure(text=f"MEM :%{mem}", text_color="Orange")

            else:

                label2.configure(text=f"MEM :%{mem}", text_color="red")
            # update the labels
            time.sleep(0.2)
            label1.update()
            label2.update()

        except RuntimeError:
            # give exiting
            msg.showinfo("ÇIKIŞ BAŞARILI","ÇIKIŞ BAŞARILI BİR ŞEKİLDE YAPILDI")
            exit()


def st_window_appearence():
    global tik
    tik += 1
    if tik % 2 == 0:
        customtkinter.set_appearance_mode("system")
    else:
        customtkinter.set_appearance_mode("dark")



# class for gui

main_window = CTk()

# apperance

tik = 0

# top tab

main_window.attributes("-topmost", True)

# window configuration

main_window.geometry("300x125+1250+20")

main_window.title("CODE-DEM CPU/RAM")

main_window.resizable(False, False)

customtkinter.set_appearance_mode("system")

# label for measurement

measurement_label_cpu = CTkLabel(main_window, font=CTkFont("Franklin Gothic Book", 15, weight="bold"), text="")
measurement_label_cpu.grid(row=0, column=2, padx=5, pady=10)

measurement_label_mem = CTkLabel(main_window, font=CTkFont("Franklin Gothic Book", 15, weight="bold"), text="")
measurement_label_mem.grid(row=1, column=2, padx=6, pady=10)

# images widgets

img_cpu = CTkImage(dark_image=Image.open("media_cpu_gpu/cpu.png"),
                   size=(45, 45))

img_mem = CTkImage(dark_image=Image.open("media_cpu_gpu/ram.png"),
                   size=(45, 45))

img_code_dem = CTkImage(dark_image=Image.open("media_cpu_gpu/icon.ico"),
                        size=(40, 40))

# images labels

label_img_cpu = CTkLabel(main_window, text="", image=img_cpu).grid(row=0, column=1, padx=5, pady=10)
label_img_mem = CTkLabel(main_window, text="", image=img_mem).grid(row=1, column=1, padx=5, pady=10)
label_img_code_dem = CTkLabel(main_window, text="", image=img_code_dem).place(x=210, y=20)

# appearance mode

button_appearance = CTkButton(master=main_window, text="Görünüm", command=st_window_appearence)
button_appearance.place(x=160, y=80)

# thread operation

func_thread = threading.Thread(target=cpu_gpu, args=(measurement_label_cpu, measurement_label_mem)).start()

main_window.mainloop()





