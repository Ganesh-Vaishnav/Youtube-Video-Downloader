from pytube import YouTube
from tkinter import *
SAVE_PATH = "C:\\Users\\DELL_ADMIN\\Downloads"

def start():
    global SAVE_PATH
    download_button.config(state = NORMAL)
    start_button.config(state=DISABLED)
    url_entry.config(state=DISABLED)
    start.link = url_entry.get()
    try :
        start.yt = YouTube(start.link)
        video_title.config(text = start.yt.title)
        download_button.place(x=750, y=400)
    except Exception as e:
        print(str(e))
        video_title.config(fg = "red",text = "Invalid link ! Please try Again \nOr Check your Connection")

    finally:
        try_again_button.config(state = NORMAL)

def download():

    try:
        download.mp4files = start.yt.streams.filter(progressive=True,
                                              file_extension="mp4") \
            .first(). \
            download(output_path=SAVE_PATH, filename=start.yt.title+".mp4")
        final_label.config(text="Your video has been downloaded at "+SAVE_PATH,
                           fg="White")
    except Exception as e:
        final_label.config(text = "Can't Download ! Try Again",
                           fg = "Red")
        print(str(e))
    download_button.config(state = DISABLED)
def try_again():
    start_button.config(state = NORMAL)
    url_entry.config(state=NORMAL)
    url_entry.delete(0,END)
    video_title.config(text = "",
                       fg = "White")

    final_label.config(text = "",
                       fg = "White")
    download_button.place_forget()

window = Tk()
window.geometry("1100x700+0+0")
window.title("YouTube Video Downloader  ")
window.config(background="Black")
icon = PhotoImage(file="youtube photo.png")
yt = PhotoImage(file="YT.png")
window.iconphoto(True, icon)

title = Label(window,
                  text="        YOUTUBE VIDEO DOWNLOADER  ",
                  font=("Classic", 30, "bold"),
                  background="Black",
                  foreground="Green",
                  image=yt,
                  compound='bottom'
                  )
title.place(x=100, y=50)
paste = Label(window,
                  text="Paste your URL link Here ⬇ ",
                  font=("Classic", 20, "bold"),
                  background="Black",
                  foreground="Green",

                  )
paste.place(x=100, y=250)
download_place = Label(window,
                     text="Confirm your video name Here  ",
                     font=("Classic", 20, "bold"),
                     background="Black",
                     foreground="Green",

                     )
download_place.place(x=100, y=350)
url_entry = Entry(window,
                      font=("", 18, ""),
                      width=60,
                      background="Silver",
                      #state = ACTIVE
                  )
url_entry.place(height=50, x=100, y=300)
start_button = Button(window,
                          text="START",
                          font=("", 18, "bold"),
                          background="Black",
                          fg="White",
                          activeforeground="White",
                          activebackground="Black",
                          #state = ACTIVE,
                          command=start
                          )
start_button.place(x=780, y=352)
video_title = Label(window,
                    font = ("",20,""),
                    background = "Black",
                    fg = "White")

video_title.place(x = 100,y = 390 )
download_button = Button(window,
                         text = "Download",
                         font=("", 18, "bold"),
                         background="Black",
                         fg="White",
                         activeforeground="White",
                         activebackground="Grey",
                         command=download
                         )
download_button.place(x = 750,y = 400)
download_button.place_forget()
final_label = Label(window,
                      font = ("",20,""),
                    background = "Black",
                    fg = "White"
                    )
final_label.place(x = 100,y= 460)
try_again_button = Button(window,
                          text = "Go Back",
                          font=("", 18, "bold"),
                         background="Black",
                         fg="White",
                         activeforeground="White",
                         activebackground="Grey",
                         command = try_again
                          )
try_again_button.place(x = 650,y = 352)
window.mainloop()




