import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import pillow_avif
import os

# create a new Tkinter window
gui = tk.Tk()

# prompts the user to select a file
def select_file():
    file_path = filedialog.askopenfilename()
    return file_path

# prompts the user to select a file
def select_folder():
    selected_folder = filedialog.askdirectory()
    return selected_folder

# convert selected file to the wished for file type 
def convert():
    completed_label = tk.Label(gui, text="Your file has been converted!")
    file_path = select_file()
    image = Image.open(file_path)

    # get the selected format and set the output extension and file extension
    _userInput = userInput.get()
    fileExt = ".jpg"
    if _userInput == "jpg": 
        fileExt = ".jpg" # if the selected format is jpg, set the output extension to .jpg
    elif _userInput == "png": 
        fileExt = ".png" # if the selected format is png, set the output extension to .png

    if _userInput == "jpg":
        fileAdd = "_emoji" # if the selected format is jpg, add _jpg to the file name
    elif _userInput == "png": 
        fileAdd = "_sticker" # if the selected format is png, add _sticker to the file name

    # determine the output file name and path based on the source file path and output extension
    directory = os.path.dirname(file_path) # get the directory of the source file path
    file_name = os.path.splitext(os.path.basename(file_path))[0] + fileAdd + fileExt # get the file name of the source file path without the extension and add the chosen file extension and file extension modifier
    new_path = os.path.join(directory, file_name) # combine the directory and file name to create a new file path for the output image

    if image.mode == 'RGBA':
        image = image.convert('RGB') # if the image mode is RGBA (red, green, blue, alpha), convert it to RGB (red, green, blue)
    
    # resize and save the image
    if _userInput == "jpg":
        image = image.resize((108, 108)) # if the selected format is png, resize the image to 108x108 pixels
    elif _userInput == "png":
        image = image.resize((512, 512)) # if the selected format is png, resize the image to 512x512 pixels
    image.save(new_path, optimize=True, quality=50) # save the image at the new file path with 50% quality and optimized file size

    # update the image label
    converted_image = ImageTk.PhotoImage(image) # create a Tkinter-compatible image object from the Pillow image object
    image_label.configure(image=converted_image) # configure the image label to display the converted image
    image_label.image = converted_image # keep a reference to the image object
    completed_label.pack()

def batchConvert():
    selected_folder = select_folder()

    completed_label = tk.Label(gui, text="Your file has been converted!")
    for root, dirs, files in os.walk(selected_folder):
        for file in files:
            image = Image.open(os.path.join(root, file))

            _userInput = userInput.get()
            fileExt = ".jpg"
            if _userInput == "jpg": 
                fileExt = ".jpg" 
            elif _userInput == "png": 
                fileExt = ".png" 

            if _userInput == "jpg":
                fileAdd = "_Emoji" 
            elif _userInput == "png": 
                fileAdd = "_sticker" 


            directory = selected_folder 
            file_name = os.path.splitext(os.path.basename(file))[0] + fileAdd + fileExt 
            new_path = os.path.join(directory, file_name)

            if image.mode == 'RGBA':
                image = image.convert('RGB') 
            
        
            if _userInput == "jpg":
                image = image.resize((108, 108)) 
            elif _userInput == "png":
                image = image.resize((512, 512)) 
            image.save(new_path, optimize=True, quality=50) 

      
            converted_image = ImageTk.PhotoImage(image) 
            image_label.configure(image=converted_image) 
            image_label.image = converted_image 
    completed_label.pack()

# create a label to prompt the user to select the output format
format_label = tk.Label(gui, text="Select the output format:")
format_label.pack()


# create a StringVar to store the selected format and set the default value to "jpg"
userInput = tk.StringVar()
userInput.set("jpg")

# create radio buttons to allow the user to select the output format
emoji_radio = tk.Radiobutton(gui, text="Emoji!", variable=userInput, value="jpg")
sticker_button = tk.Radiobutton(gui, text="Sticker!", variable=userInput, value="png")
emoji_radio.pack()
sticker_button.pack()

# create a button to prompt the user to select a file and convert it
convert_button = tk.Button(gui, text='Select a File and Convert!', command=convert)
convert_button.pack()

# create a button to prompt user for batch conversion
convert_button = tk.Button(gui, text='Select a Folder and Convert multiple!', command=batchConvert)
convert_button.pack()

# create a label to display
image_label = tk.Label(gui)
image_label.pack()

# launches GUI
gui.mainloop()