import stegno as core
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from tkinter.filedialog import askopenfile
contentImage = None
enterText = None

def clicked():
	global contentImage
	filename = askopenfile(mode='r',title="Choose a file",filetypes=[('all files', '.*'),
	('text files', '.txt'),
	('image files', '.png'),
	('image files', '.jpg'),
	])

	if(filename != None):
		contentImage = filename.name

def messageToHide(textWidget):
	return textWidget.get()

def guiEncrypt():
	global contentImage
	if(contentImage == None and enterText.get() != ''):
		messagebox.showerror('No image specified', 'You must first select an image in which the data is to be encrypted.')
	elif(contentImage != None and enterText.get() == ''):
		messagebox.showerror('No text specified', 'Please enter some text that you want to hide inside the specified image')
	elif(contentImage == None and enterText.get() == ''):
		messagebox.showerror('No image and text specified', 'You have not specified any valid image and text')
	else:
		if(core.hide(contentImage,enterText.get()) == 'Completed'):
			messagebox.showinfo('Success', 'Your text has been successfully hidden inside the specified image')
			contentImage = None
		else:
			messagebox.showinfo('Failed', 'Incorrect Image Opening Mode')
			contentImage = None

def guiDecrypt():
	global contentImage
	if(contentImage == None):
		messagebox.showerror('No image specified', 'Please specify an image you want to decrypt')
	else:
		if(core.retr(contentImage) == 'failed'):
			messagebox.showerror('Failed', 'Incorrect Image Mode detected')
		else:
			messagebox.showinfo('Success', 'Here is your data :-' + core.retr(contentImage))
			contentImage = None

def start():
	global enterText
	mainWindow = Tk()
	mainWindow.title("Stegnography")
	#photo = PhotoImage(file='icon.png')
	#mainWindow.iconphoto(False,photo)
	headLabel = Label(mainWindow,text="Quickly hide text inside images" ,font=("Arial",20)).pack()
	bt = Button(mainWindow,text="Browse Image",command=lambda:clicked()).pack()
	enterText = Entry(mainWindow)
	enterText.pack()
	encryptbt = Button(mainWindow,text="Encrypt",command=guiEncrypt).pack()
	decryptbt = Button(mainWindow,text="Decrypt", command=guiDecrypt).pack()
	mainWindow.geometry('800x400')
	mainWindow.mainloop()

if(__name__ == '__main__'):
	start()
