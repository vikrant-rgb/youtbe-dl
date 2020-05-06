import tkinter as tk
from pytube import YouTube
def downloadVideo():
    global E1
    string = E1.get()
    yt = YouTube(string)
    num = 1
    for s in yt.streams.all():
        print(str(num) + ". " + str(s))
        num += 1
    
    n = int(input("Enter your resolution:  "))
    stream = yt.streams[n-1]
    destination = str(input("Enter your destination:  "))
    stream.download(destination)
    print(str(yt.title) + " has been added to " + destination)

root=tk.Tk()

w = tk.Label(root, text="Youtube Downloader")
w.pack()


E1 = tk.Entry(root, bd=5)
E1.pack(side=tk.TOP)

button = tk.Button(root, text="Download", fg="red", command= downloadVideo)
button.pack(side=tk.BOTTOM)

root.mainloop()