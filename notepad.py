from tkinter import *
from tkinter import scrolledtext, Menu, Tk, BOTH, filedialog, END
from tkinter.ttk import Frame
import os

class Example(Frame):

	def __init__(self):
		super().__init__()

		self.initUI()


	def newfile():
			pass
	# def openfile():
	# 		filename = filedialog.askopenfilename(parent=self.master)
	# 		f = open(filename)
	# 		f.read()
	# 		for line in f:
	# 			print (line)

	def initUI(self):
		self.master.title("Untitled")

		self.w = scrolledtext.ScrolledText()
		self.w.pack(fill=BOTH, expand=1) #size of the window to the given text

		menubar = Menu(self.master)
		self.master.config(menu=menubar)
		menu_file = Menu(menubar, tearoff=0)
		menu_file.add_command(label='New', command = self.whileNew)
		menu_file.add_command(label='Open', command =self.whileOpen)
		menu_file.add_command(label='Save', command = self.whileSaveAs)
		menu_file.add_separator()
		menu_file.add_command(label='Exit', command = self.master.destroy)
		menubar.add_cascade(label='File', menu= menu_file)

		menu_edit = Menu(menubar, tearoff=0)	
		menu_edit.add_command(label='Copy', command = self.copy)
		menu_edit.add_command(label='Cut', command = self.cut)
		menu_edit.add_command(label='Paste', command = self.paste)
		menubar.add_cascade(label='Edit',menu=menu_edit)


	def whileNew(self):
		self.w.delete(1.0, END)
		self.master.title('Untitled')

	def whileOpen(self):
		filetyp = [('Text Files', '*.txt'), ('Python files', '*.py'), ('All files','*')]
		t = filedialog.Open(self, filetypes = filetyp)
		file = t.show()

		if file != '':
			self.w.delete(1.0, END)
			text = self.readFile(file)
			self.w.insert(END,text)
			self.master.title(os.path.basename(file))

	def readFile(self, filename):

		with open(filename, "r") as f:
			text = f.read()

		return text

	def whileSaveAs(self):
		filetyp = [('Text Files', '*.txt'), ('Python files', '*.py'), ('All files','*')]
		t = filedialog.SaveAs(self, defaultextension='txt',filetypes = filetyp)
		file = t.show()

		if file !='':
			newfile = open(file, 'w')
			newfile.write(self.w.get(1.0,END))
			newfile.close()
			self.master.title(os.path.basename(file))

	def cut(self):
		self.w.event_generate("<<Cut>>")
	def copy(self):
		self.w.event_generate("<<Copy>>")
	def paste(self):
		self.w.event_generate("<<Paste>>")


def main():

	root = Tk()
	root.geometry("250x150+300+300")
	program = Example()
	root.mainloop()

if __name__ == '__main__':
	main()