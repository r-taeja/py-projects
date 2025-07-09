# Importing tkinter
import os
import tkinter as tk
from PIL import ImageTk, Image


# Adding text on top (like a label)
# label1 = tk.Label(root, text = "Rohit", font = ('Arial', 20))
# label1.pack(pady = 50)

# Adding a textbox (big, can change size)
# textbox = tk.Text(root)
# textbox.pack()

# Adding an entry (just adds a small box where you can add some entry)
# my_entry = tk.Entry(root)
# my_entry.pack()

# Function to get image paths into a list
def get_imagepaths():
    # Getting Artwork directory path
    artworkpath = os.path.join("/", "Users", "r_taeja", "Desktop", "Artworks")

    # Creating list of image paths
    imgpath = []

    # Filtering paths that contain '.jpg'
    for i in os.listdir(artworkpath):
        if i.endswith(".jpg"):
            imgpath.append(os.path.join(artworkpath, i))

    return imgpath

# Function to show next image when button is clicked
def nextim():
    global img_index
    print("Next button pressed.")

    img_index += 1

    if img_index > len(imgpaths)-1:
        img_index = 0  # wrap around

    print("Loading image:", imgpaths[img_index])

    art = ImageTk.PhotoImage(Image.open(imgpaths[img_index]).resize((800, 700)))
    label.config(image = art)
    label.image = art


# Main body

# Creating a basic file or whatev the root is (root ig lol)
root = tk.Tk()

# Dimensions and name
root.geometry("1080x720")
root.title("My favourite artworks")

# Storing image paths into a list
imgpaths = get_imagepaths()
print(imgpaths)

# Index to iterate over list of image paths
img_index = 0

# Convert image to photoImage object (coz das how it works in tkinter)
art = ImageTk.PhotoImage(Image.open(imgpaths[img_index]).resize((800, 700)))

# Create label to display image (coz das how it works in tkinter)
label = tk.Label(root, image = art)
label.image = art
label.pack()

# Adding a button which will bring up next image
button = tk.Button(root, text = '>', command = nextim)
button.pack()

# Running the GUI
root.mainloop()