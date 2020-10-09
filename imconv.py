from tkinter import*
from tkinter import filedialog
from PIL import Image
import re
re_str=r"[/|\\]([0-9a-zA-Z_\-]+)\."
def convertImage(path,fm,dest):
    im=Image.open(path)
    nim=im.convert('RGB')
    name=re.findall(re_str,path)[0]
    print(name)
    nim.save("{}/{}.{}".format(dest,name,fm))
def selectFile(en):
    en.delete(0,'end')
    filename=filedialog.askopenfilename(initialdir="C:\\Users\\{Your USERNAME}\\Desktop",
                                        title="Select an Image",
                                        filetypes=(("JPEG files", 
                                                        "*.jpeg*"), 
                                                       ("all files", 
                                                        "*.*")))
    en.insert(END,filename)
    
def selectFolder(idir):
    idir.delete(0,'end')
    foldername=filedialog.askdirectory()
    idir.insert(END,foldername)
root = Tk()
tkvar=StringVar(root)
tkvar.set('png')


iFile=Label(root,text="Image File:")
iFile.pack()
ifEntry=Entry(root,width=50)
ifEntry.pack()

sButton=Button(root,text="Select File",command=lambda:selectFile(ifEntry))
sButton.pack()

iDestination=Label(root,text="Destination Folder:")
iDestination.pack()


idEntry=Entry(root,width=50)
idEntry.insert(END,"C:/Users/{your USERNAME}/Desktop/")
idEntry.pack()

sButton=Button(root,text="Select Folder",command=lambda:selectFolder(idEntry))
sButton.pack()

formatLabel=Label(root,text="Select a format")
formatLabel.pack()
formatMenu=OptionMenu(root,tkvar,'png','jpeg','jpg','tiff','gif')
formatMenu.pack()


cButton=Button(root,text="Convert",command=lambda: convertImage(ifEntry.get(),
                                                                tkvar.get(),
                                                                idEntry.get()))
cButton.pack()


root.mainloop()
