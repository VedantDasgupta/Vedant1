from tkinter import*
from tkinter import filedialog
import os
from PIL import ImageTk, Image
from tkinter import messagebox 

root = Tk()
root.minsize(650, 650)
root.maxsize(650, 650)
root.configure(background = "gray87")

open_img = ImageTk.PhotoImage(Image.open ("open.png"))
save_img = ImageTk.PhotoImage(Image.open ("save.png"))
exit_img = ImageTk.PhotoImage(Image.open ("exit.jpg"))      

label_file_name = Label(root, text = "File Name")
label_file_name.place(relx = 0.28, rely = 0.03, anchor = CENTER)

input_file_name = Entry(root)
input_file_name.place(relx = 0.46, rely = 0.03, anchor = CENTER)

my_text = Text(root, height = 35, width = 80)
my_text.place(relx = 0.5, rely = 0.55, anchor = CENTER)




name = ""
def openFile():
    global name
    my_text.delete(1.0, END)
    
    input_file_name.delete(0, END)
    html_file = filedialog.askopenfilename(title = "Open Text File", filetypes = (("html files", "*.html"), ))
    
    print(html_file)
    name = os.path.basename(html_file)
    formated_name = name.split('.')[0]
    input_file_name.insert(END, formated_name)
    
    root.title(formated_name)
    html_file = open(name, 'r')
    paragraph = html_file.read()    
    my_text.insert(END, paragraph)
    html_file.close()
    open_button=Button(root,image=open_img,text="OpenFile", command=openFile) 
    open_button.place(relx=0.05,rely=0.03,anchor=CENTER)
    
def save():
    input_name = input_file_name.get()
    file = open(input_name + ".html", "w")
    data = my_text.get("1.0", END)
    print(data)
    file.write(data)
    input_file_name.delete(0, END)
    my_text.delete(1.0, END)
    messagebox.showinfo("update", "Success")
   
def closeWindow():
    root.destroy()
    
open_button=Button(root,image=open_img,text="OpenFile", command=openFile) 
open_button.place(relx=0.05,rely=0.03,anchor=CENTER)
    
save_button = Button(root, image = save_img, text = "SaveFile", command=save)
save_button.place(relx = 0.11, rely = 0.03, anchor= CENTER)

exit_button = Button(root,image=exit_img,text="ExitFile", command=closeWindow)
exit_button.place(relx = 0.17, rely = 0.03, anchor = CENTER)
root.mainloop() 
                       
