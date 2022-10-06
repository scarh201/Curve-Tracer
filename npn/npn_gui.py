from tkinter import *
from tkinter import ttk
import tkinter
import sys

# Creating the GUI object
root = Tk()
root.title("NPN Curve Tracer")
root.geometry("677x343")
root.iconbitmap("npn_icon.ico")

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

# Dictionary
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

# Photo
photo = PhotoImage(file = "npn_schematic.png")
label_photo = Label(root, image=photo)
    
# Creating Label Widgets
label_IC = Label(root, text="IC:")
label_IB = Label(root, text="IB:")
label_VBB = Label(root, text="VBB:")
label_VCE = Label(root, text="VCE:")

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
entry_IC = EntryWithPlaceholder(root, "rating")
entry_IB = EntryWithPlaceholder(root, "limit")

entry_VBB_initial = EntryWithPlaceholder(root, "start")
entry_VBB_final = EntryWithPlaceholder(root, "stop")
entry_VBB_increment = EntryWithPlaceholder(root, "step")

entry_VCE_initial = EntryWithPlaceholder(root, "start")
entry_VCE_final = EntryWithPlaceholder(root, "stop")
entry_VCE_increment = EntryWithPlaceholder(root, "step")

# Creating Dropdown Widgets
dropdown_IC = ttk.Combobox(root, value = unit_amp, width = 4, state='readonly')
dropdown_IC.current(1)

dropdown_IB = ttk.Combobox(root, value = unit_amp, width = 4, state='readonly')
dropdown_IB.current(0)

dropdown_VBB_initial = ttk.Combobox(root, value = unit_volt, width = 4, state='readonly')
dropdown_VBB_initial.current(2)
dropdown_VBB_final = ttk.Combobox(root, value = unit_volt, width = 4, state='readonly')
dropdown_VBB_final.current(2)
dropdown_VBB_increment = ttk.Combobox(root, value = unit_volt, width = 4, state='readonly')
dropdown_VBB_increment.current(2)

dropdown_VCE_initial = ttk.Combobox(root, value = unit_volt, width = 4, state='readonly')
dropdown_VCE_initial.current(2)
dropdown_VCE_final = ttk.Combobox(root, value = unit_volt, width = 4, state='readonly')
dropdown_VCE_final.current(2)
dropdown_VCE_increment = ttk.Combobox(root, value = unit_volt, width = 4, state='readonly')
dropdown_VCE_increment.current(2)

# Write to a File
def write():
  outputFile = open("npn_variables.txt", "w")   
  outputFile.write(entry_IC.get() + get_unit(dropdown_IC.get()) + '\n')
  outputFile.write(entry_IB.get() + get_unit(dropdown_IB.get()) + '\n')
  outputFile.write(entry_VBB_initial.get() + get_unit(dropdown_VBB_initial.get()) + '\n')
  outputFile.write(entry_VBB_final.get() + get_unit(dropdown_VBB_final.get()) + '\n')
  outputFile.write(entry_VBB_increment.get() + get_unit(dropdown_VBB_increment.get()) + '\n')
  outputFile.write(entry_VCE_initial.get() + get_unit(dropdown_VCE_initial.get()) + '\n')
  outputFile.write(entry_VCE_final.get() + get_unit(dropdown_VCE_final.get()) + '\n')
  outputFile.write(entry_VCE_increment.get() + get_unit(dropdown_VCE_increment.get()))
  outputFile.close()

# check for float inputs
def isFloat(num):
  try:
    float(num)
  except ValueError:
    print("exit code 1")
    sys.exit(1)

def checkInputs():
  isFloat(entry_IC.get())
  isFloat(entry_IB.get())
  isFloat(entry_VBB_initial.get())
  isFloat(entry_VBB_final.get())
  isFloat(entry_VBB_increment.get())
  isFloat(entry_VCE_initial.get())
  isFloat(entry_VCE_final.get())
  isFloat(entry_VCE_increment.get())

# button calling function
def run():
  checkInputs()
  write()
  print("exit code 0")
  sys.exit(0)

# Creating Button Widgets
button_run = Button(root, text = "run", state = ACTIVE, command = run) 

# Position Widgets
label_photo.place(x = 180, y = 15)

label_IC.place(x = 200, y = 188)
entry_IC.place(x = 235, y = 188)
dropdown_IC.place(x = 275, y = 188)

label_IB.place(x = 200, y = 215)
entry_IB.place(x = 235, y = 215)
dropdown_IB.place(x = 275, y = 215)

label_VBB.place(x=200, y=242)
entry_VBB_initial.place(x= 235, y=242)
dropdown_VBB_initial.place(x=275, y=242)
entry_VBB_final.place(x=330, y=242)
dropdown_VBB_final.place(x = 370, y=242)
entry_VBB_increment.place(x=425, y=242)
dropdown_VBB_increment.place(x=465, y=242)

label_VCE.place(x=200, y=269)
entry_VCE_initial.place(x=235, y=269)
dropdown_VCE_initial.place(x=275, y=269)
entry_VCE_final.place(x=330, y=269)
dropdown_VCE_final.place(x=370, y=269)
entry_VCE_increment.place(x=425, y=269)
dropdown_VCE_increment.place(x=465, y=269)

button_run.place(x = 345, y=300)

# Closing the Window
def on_closing():
  root.destroy() 
  print("exit code -1")
  sys.exit(-1)
root.protocol("WM_DELETE_WINDOW", on_closing)

# Create Event Loop
root.mainloop()