from tkinter import *
from tkinter import ttk
import tkinter
import sys

# Creating the GUI object
root = Tk()
root.title("pMOS Curve Tracer")
root.geometry( "677x343" )
root.iconbitmap("pmos_icon.ico")

# Creating Lists for Units
unit_amp = [
  "uA",
  "mA",
  "A"
]

unit_volt = [
  "uV",
  "mV",
  "V"
]

# dictionary or unordered map of units
dict = {
  'u': "e-6", 
  'm': "e-3"
}

# get unit function
def get_unit(unit: str ) -> str:
  if unit[0] in dict:
    return dict[unit[0]]
  else:
    return "e-0"

# Creating an Image
photo = PhotoImage(file = "pmos_schematic.png")

# Creating a label widget
label_ID = Label(root, text = "   ID:")
label_VSG = Label(root, text = "VSG: ")
label_VSD = Label(root, text = "VSD: ")
label_photo = Label(root, image=photo)

# Create Entry w/ Place Holder Super Class 
class EntryWithPlaceholder(tkinter.Entry):
  def __init__(self, master=None, placeholder="PLACEHOLDER", color='grey', w= 7):
    super().__init__(master, width= w)
    self.placeholder = placeholder
    self.placeholder_color = color
    self.default_fg_color = self['fg']
    
    self.bind("<FocusIn>", self.foc_in)
    self.bind("<FocusOut>", self.foc_out)

    self.put_placeholder()

  def put_placeholder(self):
    self.insert(0, self.placeholder)
    self['fg'] = self.placeholder_color

  def foc_in(self, *args):
    if self['fg'] == self.placeholder_color:
      self.delete('0', 'end')
      self['fg'] = self.default_fg_color

  def foc_out(self, *args):
    if not self.get():
      self.put_placeholder()

# Creating Entry Widgets
entry_ID = EntryWithPlaceholder(root, "rating")

entry_VSG_initial = EntryWithPlaceholder(root, "start")
entry_VSG_final = EntryWithPlaceholder(root, "stop")
entry_VSG_increment = EntryWithPlaceholder(root, "step")

entry_VSD_initial = EntryWithPlaceholder(root, "start")
entry_VSD_final = EntryWithPlaceholder(root, "stop")
entry_VSD_increment = EntryWithPlaceholder(root, "step")

# Creating Dropdown Widgets
dropdown_ID = ttk.Combobox(root, value = unit_amp, width = 4, state='readonly')
dropdown_ID.current(1)

dropdown_VSG_initial = ttk.Combobox(root, value = unit_volt, width = 4, state='readonly')
dropdown_VSG_initial.current(2)
dropdown_VSG_final = ttk.Combobox(root, value = unit_volt, width = 4, state='readonly')
dropdown_VSG_final.current(2)
dropdown_VSG_increment = ttk.Combobox(root, value = unit_volt, width = 4, state='readonly')
dropdown_VSG_increment.current(2)

dropdown_VSD_initial = ttk.Combobox(root, value = unit_volt, width = 4, state='readonly')
dropdown_VSD_initial.current(2)
dropdown_VSD_final = ttk.Combobox(root, value = unit_volt, width = 4, state='readonly')
dropdown_VSD_final.current(2)
dropdown_VSD_increment = ttk.Combobox(root, value = unit_volt, width = 4, state='readonly')
dropdown_VSD_increment.current(2)

# write to a file
def write():
  outputFile = open("pmos_variables.txt", "w")   
  outputFile.write(entry_ID.get() + get_unit(dropdown_ID.get()) + '\n')
  outputFile.write(entry_VSG_initial.get() + get_unit(dropdown_VSG_initial.get()) + '\n')
  outputFile.write(entry_VSG_final.get() + get_unit(dropdown_VSG_final.get()) + '\n')
  outputFile.write(entry_VSG_increment.get() + get_unit(dropdown_VSG_increment.get()) + '\n')
  outputFile.write(entry_VSD_initial.get() + get_unit(dropdown_VSD_initial.get()) + '\n')
  outputFile.write(entry_VSD_final.get() + get_unit(dropdown_VSD_final.get()) + '\n')
  outputFile.write(entry_VSD_increment.get() + get_unit(dropdown_VSD_increment.get()))
  outputFile.close()

# check for float inputs
def isFloat(num):
  try:
    float(num)
  except ValueError:
    print("exit code 1")
    sys.exit(1)

def checkInputs():
  isFloat(entry_ID.get())
  isFloat(entry_VSG_initial.get())
  isFloat(entry_VSG_final.get())
  isFloat(entry_VSG_increment.get())
  isFloat(entry_VSD_initial.get())
  isFloat(entry_VSD_final.get())
  isFloat(entry_VSD_increment.get())

# button calling function
def run():
  checkInputs()
  write()
  print("exit code 0")
  sys.exit(0)

# Creating Button Widgets
button_run = Button(root, text = "run", state = ACTIVE, command = run) 

# Position Widgets 
label_photo.place(x = 210, y = 20)

label_ID.place(x = 200, y = 215)
entry_ID.place(x = 235, y = 215)
dropdown_ID.place(x = 275, y = 215)

label_VSG.place(x=200, y=242)
entry_VSG_initial.place(x= 235, y=242)
dropdown_VSG_initial.place(x=275, y=242)
entry_VSG_final.place(x=330, y=242)
dropdown_VSG_final.place(x = 370, y=242)
entry_VSG_increment.place(x=425, y=242)
dropdown_VSG_increment.place(x=465, y=242)

label_VSD.place(x=200, y=269)
entry_VSD_initial.place(x=235, y=269)
dropdown_VSD_initial.place(x=275, y=269)
entry_VSD_final.place(x=330, y=269)
dropdown_VSD_final.place(x=370, y=269)
entry_VSD_increment.place(x=425, y=269)
dropdown_VSD_increment.place(x=465, y=269)

button_run.place(x = 345, y=300)

# Closing the Window
def on_closing():
  root.destroy() 
  print("exit code -1")
  sys.exit(-1)
root.protocol("WM_DELETE_WINDOW", on_closing)

# Create Event Loop
root.mainloop() 
