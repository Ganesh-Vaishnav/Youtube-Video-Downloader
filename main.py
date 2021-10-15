from pytube import YouTube
from tkinter import *
import requests
from PIL import ImageTk, Image
SAVE_PATH = "C:\\Users\\DELL_ADMIN\\Downloads"

def get_video_image():
    get_video_image.file = open("thumb_nail.png", "wb")
    get_video_image.file.write(start.thumb_nail.content)
    get_video_image.file.close()
    get_video_image.thumb_nail_image = Image.open("thumb_nail.png")
    get_video_image.thumb_nail_image = get_video_image.thumb_nail_image.resize((150, 150), Image.ANTIALIAS)
    get_video_image.my_image = ImageTk.PhotoImage(get_video_image.thumb_nail_image)
    thumb_image.place(x=100, y=390)
    thumb_image.config(image=get_video_image.my_image)


def start():
    global SAVE_PATH
    mp4_button.config(state = NORMAL)
    mp3_button.config(state=NORMAL)
    start_button.config(state=DISABLED)
    url_entry.config(state=DISABLED)
    start.link = url_entry.get()
    try :
        start.yt = YouTube(start.link)
        start.thumb_nail = requests.get(start.yt.thumbnail_url)
        get_video_image()
        video_title.config(text = start.yt.title)
        mp4_button.place(x = 550,y = 470)
        mp3_button.place(x=650, y=470)
    except Exception as e:
        print(str(e))
        video_title.config(fg = "red",text = "Invalid link ! Please try Again \nOr Check your Connection")

    finally:
        try_again_button.config(state = NORMAL)

def download_mp4():
    download_mp4.file_name = ''.join(char for char in start.yt.title if char.isalnum() or char == ' ')
    try:

        download_mp4.mp4files = start.yt.streams.filter(progressive=True,
                                              file_extension="mp4") \
            .first(). \
            download(output_path=SAVE_PATH, filename=download_mp4.file_name+".mp4")
        final_label.config(text="Your video has been downloaded at "+SAVE_PATH,
                           fg="White")
    except Exception as e:
        final_label.config(text = "Can't Download ! Try Again",
                           fg = "Red")
        print(str(e))
    mp4_button.config(state = DISABLED)
    mp3_button.config(state=DISABLED)
def download_mp3():

    try:
        download_mp3.mp3files = start.yt.streams.filter(progressive=True,
                                              file_extension="mp4") \
            .last(). \
            download(output_path=SAVE_PATH, filename=start.yt.title+".mp3")
        final_label.config(text="Your audio has been downloaded at "+SAVE_PATH,
                           fg="White")
    except Exception as e:
        final_label.config(text = "Can't Download ! Try Again",
                           fg = "Red")
        print(str(e))
    mp4_button.config(state=DISABLED)
    mp3_button.config(state = DISABLED)
def try_again():
    thumb_image.place_forget()
    start_button.config(state = NORMAL)
    url_entry.config(state=NORMAL)
    url_entry.delete(0,END)
    video_title.config(text = "",
                       fg = "White")

    final_label.config(text = "",
                       fg = "White")
    mp4_button.place_forget()
    mp3_button.place_forget()

window = Tk()

window.geometry("1300x700+0+0")
window.title("YouTube Video Downloader  ")
window.config(background="Black")
icon = PhotoImage(file="youtube photo.png")
yt = PhotoImage(file="YT.png")


window.iconphoto(True, icon)

#canvas = Canvas(window,width = 200,height = 200,bg = "black")
#canvas.create_image(100,150,image = thumb_nail_image)
#canvas.place(x=100,y=390)
title = Label(window,
                  text="        YOUTUBE VIDEO DOWNLOADER  ",
                  font=("Classic", 30, "bold"),
                  background="black",
                  foreground="Green",
                  image=yt,
                  compound='bottom'
                  )

title.place(x=100, y=30)

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
start_button.place(x=860, y=300)
video_title = Label(window,
                    font = ("",20,""),
                    background = "Black",
                    fg = "White")

video_title.place(x =300,y = 400 )
mp4_button = Button(window,
                         text = "mp4",
                         font=("", 18, "bold"),
                         background="Black",
                         fg="White",
                         activeforeground="White",
                         activebackground="Grey",
                         command=download_mp4
                         )

mp4_button.place_forget()
mp3_button = Button(window,
                         text = "mp3",
                         font=("", 18, "bold"),
                         background="Black",
                         fg="White",
                         activeforeground="White",
                         activebackground="Grey",
                         command=download_mp3
                         )

mp3_button.place_forget()

final_label = Label(window,
                      font = ("",20,""),
                    background = "Black",
                    fg = "White"
                    )
final_label.place(x = 100,y= 600)
try_again_button = Button(window,
                          text = "Go Back",
                          font=("", 18, "bold"),
                         background="Black",
                         fg="White",
                         activeforeground="White",
                         activebackground="Grey",
                         command = try_again
                          )
try_again_button.place(x = 960,y = 300)

thumb_image = Label(window)

window.mainloop()




