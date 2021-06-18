# This file takes your raw pictures file and renames all the image files so that you can keep track of them more effectively.
import os
import tkinter as tk
from tkinter.filedialog import askdirectory
from tkinter import Button, Label, Entry

#function that renames all pictures in a given directory
def renamePictures(picture_directory, picture_name):
    picture_count = 1
    count_name = []

    # parses through the directory given to see if any pictures are already labelled
    for root, dirs, files in os.walk(picture_directory):
        for name in files:
            full_name = picture_name + '_'
            length_name = len(full_name)
    
            if (full_name in name) and name[length_name].isdigit() and name[length_name+1].isdigit() and name[length_name+2].isdigit() and name[length_name+3].isdigit():
                count_name.append(int(name[length_name] + name[length_name+1] + name[length_name+2] + name[length_name+3]))
            
            elif (full_name in name) and name[length_name].isdigit() and name[length_name+1].isdigit() and name[length_name+2].isdigit():
                count_name.append(int(name[length_name] + name[length_name+1] + name[length_name+2]))
            
            elif (full_name in name) and name[length_name].isdigit() and name[length_name+1].isdigit():
                count_name.append(int(name[length_name] + name[length_name+1]))
            
            elif (full_name in name) and name[length_name].isdigit():
                count_name.append(int(name[length_name]))

    if len(count_name) >= 1:
        picture_count = max(count_name) + 1
    else:
        picture_count = 1

    # parses through the directory given to rename the pictures
    for root, dirs, files in os.walk(picture_directory):
        for name in files:
            # checks to make sure the file is a JPG file
            if ('.jpg' in name or '.JPG' in name) and (full_name not in name):
                picture_count_str = str(picture_count)
                full_file_name = os.path.join(root, name)

                # renames the image file to 'ESC_Picture_#.jpg'
                os.rename(full_file_name, root + '/' + picture_name + '_' + picture_count_str + '.jpg')
                picture_count += 1


#creates the GUI
field = ('Picture Name', 'Picture Directory')
def get_picture_name(entries):
    picture_name = str(entries['Picture Name'].get())
    picture_directory = entries['Picture Directory']

    renamePictures(picture_directory, picture_name)

def makeform(root, field):
    entries = {}
    for i in field:
        if i == field[0]:
            lab = Label(root, width=30, text=field[0] +': ', anchor='w')
            ent = Entry(root, width=30)
            ent.insert(0, "")

            lab.grid(row=1, column=0, padx=10, pady=10)
            ent.grid(row=1, column=1, padx=10, pady=10)
            entries[i] = ent

        elif i == field[1]:
            lab = tk.Label(root, width=30, text=field[1] +': ', anchor='w')
            lab.grid(row=2, column=0, padx=10, pady=10)
            browsebutton = Button(root, text="Browse Folders", command=lambda: browsefunc(entries))
            browsebutton.grid(row=2, column=1, padx=10, pady=10)
    return entries

#opens up the folder browser when the button is clicked
def browsefunc(entries):
    picture_directory = askdirectory(title='Select Folder')
    entries['Picture Directory'] = picture_directory

if __name__ == '__main__':
    root = tk.Tk()
    root.title('Picture Renaming Tool')
    ents = makeform(root, field)
    b1 = tk.Button(root, text='Rename Pictures',
                   command=(lambda e=ents: get_picture_name(e)))
    b1.grid(row=6, column=0, padx=5, pady=5)
    b2 = tk.Button(root, text='Quit', command=root.quit)
    b2.grid(row=6, column=1)
    root.mainloop()

#test
