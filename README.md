# Curve-Tracer

Contributing Authors: Sinan Kekic, Mario Perez

Intent of Program: 
The Intent of these Programs is to create an automated Curve Tracer that recursively 
measures characteristic values for 4 electrical components and outputs them onto an excel sheet:
-> P-MOSFET
-> N-MOSFET
-> NPN-Transistor
-> PNP-Transistor

Further implementations of this program will allow users to remotely operate BenchVue 
electrical devices such as:
-> Keysight Triple Output Programmable DC Power Supply (E36312A)
-> Keysight Digital Storage Oscilloscope (DS0-X 2012A)
-> Keysight Data Acquisition System (DAQ970A)


Intended Software to be ran on: Keysight BenchVue

Within each folder, the Sequence file (.bvseq) is intended to be executed on BenchVue. When ran, the script file (.bat) is called, which executes the GUI (.py) file. The GUI that appears allows users to initialize values and set boundaries, depending on the specifications of the component they are intending to utilize. Upon submission of these values, the GUI closes and writes a text file (.txt) which is passed back to the BenchVue Sequence. The Program Recursively measures characteristic values for each device and plots the characteristic curve.

Example Data can be seen in the "data" folder.
