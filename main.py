import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk, Image, ImageFont,ImageDraw
import os


window = Tk()
window.title("Image Watermarking App")
window.configure(pady=20,padx=20)
window.geometry("300x100")

canvas = Canvas(window)
canvas.grid(column=0,row=0)

def open_file_watermarked():
    file_name = filedialog.askopenfilename()

    file_opened.configure(text="File Opened: "+file_name)

    main_image = Image.open(file_name).convert("RGBA")

    i_x = main_image.size[0]
    i_y = main_image.size[1]
    window.geometry(f"{i_x+305}x{i_y+i_y}")
    print(main_image.size)
    print(file_name)
    print(len(file_name))
    print(file_name[28:36])

    if i_x > 800 or i_x > 800:
        i_x = int(i_x/2)
        i_y = int(i_y/2)

        resized = main_image.resize((i_x,i_y))
        i_image = ImageTk.PhotoImage(resized)
        label1 = tkinter.Label(canvas,image=i_image)
        label1.image = i_image

        label1.grid(column=1, row=1)

        watermarked_img = resized.copy()

    else:
        i_image = ImageTk.PhotoImage(main_image)
        label1 = tkinter.Label(canvas,image=i_image)
        label1.image = i_image

        label1.grid(column=1,row=1)

        watermarked_img = main_image.copy()

    txt = Image.new('RGBA', watermarked_img.size, (255, 255, 255, 0))

    draw = ImageDraw.Draw(txt)

    font = ImageFont.truetype("impact.ttf", 20)

    for inc_y in range(0, 500, 100):
        for inc_x in range(0, 800, 200):
            draw.text((inc_x, inc_y), "Charm", font=font, fill=(0, 0, 0, 90))

    # draw.text((i_x/2, i_y/2), "Elreen", font=font, fill=(0, 0, 0, 70))

    combined = Image.alpha_composite(watermarked_img, txt)

    watermarked_image_new = ImageTk.PhotoImage(combined)
    label2 = tkinter.Label(canvas,image=watermarked_image_new)
    label2.image = watermarked_image_new

    label2.grid(column=1, row=2)

    new_file_name = file_name[28:36]+"_watermarked2.jpg"

    conv_rgb = combined.convert('RGB')
    def save():
        save_image = conv_rgb.save(os.path.join("os_path_directory_to where save new image as is",new_file_name),"JPEG")
        save_image_button.configure(fg="green")

    save_image_button = Button(canvas,text="Save Image?",command=save)
    save_image_button.grid(column=2,row=0)


#Buttons
open_file_button = Button(canvas,text="Open File to Watermark", command=open_file_watermarked)
open_file_button.grid(column=0,row=0)

file_opened = Label(canvas,text="File Name", fg="red")
file_opened.grid(column=1, row=0)

# Future upgrades
# input for text watermark
# select color for text watermark
# enter specific file name to be saved

















window.mainloop()