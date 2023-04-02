# use .update to dynamically add nodes (components) to circuit
# use tkinter for graphics
from tkinter import *
from turtle import *
root = Tk()
# inputs circuit graph and prints it out like a normal graph
def displayGraphRep(gph):
    print("")

# adds component (node) to graph
def addComponent(gph,backNode,frontNode,signature):
    gph.update({signature:frontNode}) # this is what the added component grabs in front of it
    gph.update({backNode:signature}) # this is what the added component is attached to

# tkints circuit diagram
def circuitGraphic(gph):
    lbl1 = Label(root,text="text here I am text")
    lbl2 = Label(root, text="text here I am text")
    img = PhotoImage(file="C:/Users/samty/Desktop/CircuitSimulator/resistor.png")
    lbl3 = Label(root, image=img)
    lbl3.pack()

    root.mainloop()


circuit = {'B':'R','R':'B'}
print(circuit)
addComponent(circuit,circuit['R'],circuit['R'],"R2")
print(circuit)


