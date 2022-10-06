from tkinter import *
from tkinter import ttk
import tkinter
import sys

# Creating the GUI object
root = Tk()
root.title("nMOS Curve Tracer")
root.geometry( "677x343" )
root.iconbitmap("nmos_icon.ico")

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
photo = PhotoImage(file = "nmos_schematic.png")

# Creating a label widget
label_ID = Label(root, text = "   ID:")
label_VGS = Label(root, text = "VGS: ")
label_VDS = Label(root, text = "VDS: ")
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

entry_VGS_initial = EntryWithPlaceholder(root, "start")
entry_VGS_final = EntryWithPlaceholder(root, "stop")
entry_VGS_increment = EntryWithPlaceholder(root, "step")

entry_VDS_initial = EntryWithPlaceholder(root, "start")
entry_VDS_final = EntryWithPlaceholder(root, "stop")
entry_VDS_increment = EntryWithPlaceholder(root, "step")

# Creating Dropdown Widgets
dropdown_ID = ttk.Combobox(root, value = unit_amp, width = 4, state='readonly')
dropdown_ID.current(1)

dropdown_VGS_initial = ttk.Combobox(root, value = unit_volt, width = 4, state='readonly')
dropdown_VGS_initial.current(2)
dropdown_VGS_final = ttk.Combobox(root, value = unit_volt, width = 4, state='readonly')
dropdown_VGS_final.current(2)
dropdown_VGS_increment = ttk.Combobox(root, value = unit_volt, width = 4, state='readonly')
dropdown_VGS_increment.current(2)

dropdown_VDS_initial = ttk.Combobox(root, value = unit_volt, width = 4, state='readonly')
dropdown_VDS_initial.current(2)
dropdown_VDS_final = ttk.Combobox(root, value = unit_volt, width = 4, state='readonly')
dropdown_VDS_final.current(2)
dropdown_VDS_increment = ttk.Combobox(root, value = unit_volt, width = 4, state='readonly')
dropdown_VDS_increment.current(2)

# write to a file
def write():
  outputFile = open("nmos_variables.txt", "w")   
  outputFile.write(entry_ID.get() + get_unit(dropdown_ID.get()) + '\n')
  outputFile.write(entry_VGS_initial.get() + get_unit(dropdown_VGS_initial.get()) + '\n')
  outputFile.write(entry_VGS_final.get() + get_unit(dropdown_VGS_final.get()) + '\n')
  outputFile.write(entry_VGS_increment.get() + get_unit(dropdown_VGS_increment.get()) + '\n')
  outputFile.write(entry_VDS_initial.get() + get_unit(dropdown_VDS_initial.get()) + '\n')
  outputFile.write(entry_VDS_final.get() + get_unit(dropdown_VDS_final.get()) + '\n')
  outputFile.write(entry_VDS_increment.get() + get_unit(dropdown_VDS_increment.get()))
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
  isFloat(entry_VGS_initial.get())
  isFloat(entry_VGS_final.get())
  isFloat(entry_VGS_increment.get())
  isFloat(entry_VDS_initial.get())
  isFloat(entry_VDS_final.get())
  isFloat(entry_VDS_increment.get())

# button calling function
def run():
  checkInputs()
  write()
  print("exit code 0")
  sys.exit(0)

# Creating Button Widgets
button_run = Button(root, text = "run", state = ACTIVE, command = run) 

# Position Widgets 
label_photo.place(x = 210, y = 15)

label_ID.place(x = 200, y = 215)
entry_ID.place(x = 235, y = 215)
dropdown_ID.place(x = 275, y = 215)

label_VGS.place(x=200, y=242)
entry_VGS_initial.place(x= 235, y=242)
dropdown_VGS_initial.place(x=275, y=242)
entry_VGS_final.place(x=330, y=242)
dropdown_VGS_final.place(x = 370, y=242)
entry_VGS_increment.place(x=425, y=242)
dropdown_VGS_increment.place(x=465, y=242)

label_VDS.place(x=200, y=269)
entry_VDS_initial.place(x=235, y=269)
dropdown_VDS_initial.place(x=275, y=269)
entry_VDS_final.place(x=330, y=269)
dropdown_VDS_final.place(x=370, y=269)
entry_VDS_increment.place(x=425, y=269)
dropdown_VDS_increment.place(x=465, y=269)

button_run.place(x = 345, y=300)

# Closing the Window
def on_closing():
  root.destroy() 
  print("exit code -1")
  sys.exit(-1)
root.protocol("WM_DELETE_WINDOW", on_closing)

# Create Event Loop
root.mainloop() 
