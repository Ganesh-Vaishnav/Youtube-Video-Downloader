from pytube import YouTube    # for accessing youtube videos and features
from tkinter import *         # for GUI Interface
import requests               # to access the image through url
from PIL import ImageTk, Image      #to edit the thumb_nail image of video
SAVE_PATH = "C:\\Users\\DELL_ADMIN\\Downloads"   # video will be saved at this location
# function for getting an title image of the video to ensure that you are downloading the right video
'''
To understand the code better !
Start through the line 91 first and follow the functions as they are called
'''
def get_video_image():
    get_video_image.file = open("thumb_nail.png", "wb")   # create a file for storing the image inside the project
    get_video_image.file.write(start.thumb_nail.content)    # access the content of the file
    get_video_image.file.close()
    # for adjusting and editing the image inside the GUI Page
    get_video_image.thumb_nail_image = Image.open("thumb_nail.png")
    get_video_image.thumb_nail_image = get_video_image.thumb_nail_image.resize((150, 150), Image.ANTIALIAS)
    get_video_image.my_image = ImageTk.PhotoImage(get_video_image.thumb_nail_image)
    thumb_image.place(x=100, y=390)
    thumb_image.config(image=get_video_image.my_image)


def start():
    global SAVE_PATH
    mp4_button.config(state = NORMAL)
    mp3_button.config(state=NORMAL)
    start_button.config(state=DISABLED)    # user can't click the button again as of now
    url_entry.config(state=DISABLED)       # user can't write in the entry box as of now
    start.link = url_entry.get()       # get the link from the entry box
    try :
        start.yt = YouTube(start.link)
        start.thumb_nail = requests.get(start.yt.thumbnail_url)  # get the link of the thumbnail of the image
        get_video_image()                              # show the title image i.e. thumbnail of the video
        video_title.config(text = start.yt.title)     # show the title of the video
        mp4_button.place(x = 550,y = 470)
        mp3_button.place(x=650, y=470)
    except Exception as e:
        print(str(e))
        video_title.config(fg = "red",text = "Invalid link ! Please try Again \nOr Check your Connection")

    finally:
        try_again_button.config(state = NORMAL)
# download the video(mp4)
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
# to download as audio(mp3)
def download_mp3():
    download_mp3.file_name = ''.join(char for char in start.yt.title if char.isalnum() or char == ' ')
    try:
        download_mp3.mp3files = start.yt.streams.filter(progressive=True,
                                              file_extension="mp4") \
            .last(). \
            download(output_path=SAVE_PATH, filename=download_mp3.file_name+".mp3")
        final_label.config(text="Your audio has been downloaded at "+SAVE_PATH,
                           fg="White")
    except Exception as e:
        final_label.config(text = "Can't Download ! Try Again",
                           fg = "Red")
        print(str(e))
    mp4_button.config(state=DISABLED)
    mp3_button.config(state = DISABLED)
# to clear all previous operation
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
window.geometry("1300x700+0+0")  # size of the page
window.title("YouTube Video Downloader  ")
window.config(background="Black")
icon = PhotoImage(file="youtube photo.png")  # for title image of the GUI Page
yt = PhotoImage(file="YT.png")
window.iconphoto(True, icon)   # set the title of the image
# Label
title = Label(window,
                  text="        YOUTUBE VIDEO DOWNLOADER  ",
                  font=("Classic", 30, "bold"),
                  background="black",
                  foreground="Green",
                  image=yt,
                  compound='bottom'
                  )

title.place(x=100, y=30)
# Label
paste = Label(window,
                  text="Paste your URL link Here ⬇ ",
                  font=("Classic", 20, "bold"),
                  background="Black",
                  foreground="Green",

                  )
paste.place(x=100, y=250)
# Label
download_place = Label(window,
                     text="Confirm your video  Here  ",
                     font=("Classic", 20, "bold"),
                     background="Black",
                     foreground="Green",

                     )
download_place.place(x=100, y=350)
# Entry to enter the link of the url
url_entry = Entry(window,
                      font=("", 18, ""),
                      width=60,
                      background="Silver",
                  )
url_entry.place(height=50, x=100, y=300)
# Button to start accessing for the name and other details of the video
start_button = Button(window,
                          text="START",
                          font=("", 18, "bold"),
                          background="Black",
                          fg="White",
                          activeforeground="White",
                          activebackground="Black",
                          command=start    # refer the start function
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




