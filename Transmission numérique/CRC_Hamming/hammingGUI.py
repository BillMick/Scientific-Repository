# Author : Bill AHOUANDJINOU
# April 2022

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from hamming import *

def Sent(button, entryData, labelS) :
    data = entryData.get_text()
    m = len(data)
    k = calcRedundantBits(m)
    sentData = posRedundantBits(data, k)
    sentData = calcParityBits(sentData, k)
    print(f'Sent Data = {sentData}')
    labelS.set_text(str(sentData))
    
def Received(button,entryData, labelR) :
    data = entryData.get_text()
    m = len(data)
    k = calcRedundantBits(m)
    sentData = posRedundantBits(data, k)
    sentData = calcParityBits(sentData, k)
    print(f'Sent Data = {sentData}')
    receivedData = entryData.get_text()
    print(f"Received Data is {receivedData}")
    position = detectError(receivedData, k)
    if position == 0 :
        print("There is no error in this transmission.")
        labelR.set_text("No error !")
    else :
        a = "Error in bit at position " + str(position)
        labelR.set_text(a)
    print(f"The position of error is {position}.")

def Clear(button, labelTM, labelPosition, entryData, entryMessage) :
    entryData.set_text('')
    entryMessage.set_text('')
    labelTM.set_text('Transmitted data')
    labelPosition.set_text('Error position')

def Hamming() :
    window = Gtk.Window()
    window.set_border_width(40)
    window.connect('delete-event', Gtk.main_quit)

    grid = Gtk.Grid()

    labelS = Gtk.Label(label = "Sender")
    entryData = Gtk.Entry()
    generate = Gtk.Button(label = "Generate TM")
    labelTM = Gtk.Label(label = "Transmitted Data")
    grid.attach(labelS, 0, 0, 10, 1)
    grid.attach(entryData, 2, 2, 3, 1)
    grid.attach(generate, 2, 4, 3, 1)
    grid.attach(labelTM, 2, 6, 3, 1)

    labelR = Gtk.Label(label = "Receiver")
    entryMessage = Gtk.Entry()
    control = Gtk.Button(label = "Control Transmission")
    labelPosition = Gtk.Label(label = "Error Position")
    grid.attach(labelR, 0, 9, 10, 2)
    grid.attach(entryMessage, 2, 11, 3, 1)
    grid.attach(control, 2, 13, 3, 1)
    grid.attach(labelPosition, 2, 15, 3, 1)

    clear = Gtk.Button(label = "Clear all")
    grid.attach(clear, 2, 17, 3, 1)
    clear.connect('clicked', Clear, labelTM, labelPosition, entryData, entryMessage)

    generate.connect('clicked', Sent, entryData, labelTM)
    control.connect('clicked', Received, entryMessage, labelPosition)

    window.add(grid)
    window.show_all()
    Gtk.main()

Hamming()