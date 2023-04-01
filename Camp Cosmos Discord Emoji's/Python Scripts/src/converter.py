import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import pillow_avif
import os

# create a new Tkinter window
root = tk.Tk()

# define a function to prompt the user to select a file
def select_file():
    file_path = filedialog.askopenfilename()
    return file_path

# define a function to convert the selected file to the chosen format
def convert_file():
    file_path = select_file()
    image = Image.open(file_path)

    # get the selected format and set the output extension and file extension
    format_value = format_var.get()
    output_ext = ".jpg"
    if format_value == "gif": 
        output_ext = ".jpg" # if the selected format is gif, set the output extension to .jpg
    elif format_value == "png": 
        output_ext = ".png" # if the selected format is png, set the output extension to .png

    if format_value == "gif":
        file_extension = "_gif" # if the selected format is gif, add _gif to the file name
    elif format_value == "png": 
        file_extension = "_sticker" # if the selected format is png, add _sticker to the file name

    # determine the output file name and path based on the source file path and output extension
    directory = os.path.dirname(file_path) # get the directory of the source file path
    file_name = os.path.splitext(os.path.basename(file_path))[0] + file_extension + output_ext # get the file name of the source file path without the extension and add the chosen file extension and file extension modifier
    new_path = os.path.join(directory, file_name) # combine the directory and file name to create a new file path for the output image

    
    if image.mode == 'RGBA':
        image = image.convert('RGB') # if the image mode is RGBA (red, green, blue, alpha), convert it to RGB (red, green, blue)
    
    # resize and save the image
    if format_value == "gif":
        image = image.resize((108, 108)) # if the selected format is png, resize the image to 108x108 pixels
    elif format_value == "png":
        image = image.resize((512, 512)) # if the selected format is png, resize the image to 512x512 pixels
    image.save(new_path, optimize=True, quality=50) # save the image at the new file path with 50% quality and optimized file size

    # update the image label
    converted_image = ImageTk.PhotoImage(image) # create a Tkinter-compatible image object from the Pillow image object
    image_label.configure(image=converted_image) # configure the image label to display the converted image
    image_label.image = converted_image # keep a reference to the image object

# create a label to prompt the user to select the output format
format_label = tk.Label(root, text="Select the output format:")
format_label.pack()

# create a StringVar to store the selected format and set the default value to "jpg"
format_var = tk.StringVar()
format_var.set("jpg")

# create radio buttons to allow the user to select the output format
gif_radio = tk.Radiobutton(root, text="GIF", variable=format_var, value="gif")
png_radio = tk.Radiobutton(root, text="Sticker", variable=format_var, value="png")
gif_radio.pack()
png_radio.pack()

# create a button to prompt the user to select a file and convert it
convert_button = tk.Button(root, text='Select a File and Convert!', command=convert_file)
convert_button.pack()

# create a label to display
image_label = tk.Label(root)
image_label.pack()

# launches GUI
root.mainloop()