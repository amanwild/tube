# Importing Libraries Required For Code
# codewithcurious.com
from tkinter import *
from speedtest import *
import speedtest  

# Creation OF Function
def update_text():
    speed_test =speedtest.Speedtest()
    download = speed_test.download()
    upload = speed_test.upload()
    download_speed = round(download / (10**6), 2)
    upload_speed = round(upload / (10**6), 2)
    down_label.config(text= "Download Speed - " + str(download_speed) + "Mbps")
    up_label.config(text= "Upload Speed - " + str(upload_speed) + "Mbps")


# Creation OF GUI
window = Tk()
window.title("Internet Speed Testing")
window.geometry('420x250+250+150')
button = Button(window, text="Press Here to Check Speed", width=50, command=update_text,background = '#49A')
button.pack()
down_label = Label(window, text="")
down_label.pack()
up_label = Label(window, text="")
up_label.pack()

# Closing of GUI
window.mainloop()