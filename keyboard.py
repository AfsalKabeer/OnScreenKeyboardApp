import tkinter as tk

Keyboard_App = tk.Tk()
Keyboard_App.title('On Screen Keyboard')

keys = ['1','2','3','4','5','6','7','8','9','0','=',
        'q','w','e','r','t','y','u','i','o','p','DEL',
        'a','s','d','f','g','h','j','k','l',';','"',
        'z','x','c','v','b','n','m',',','.','!','TAB',
        'SPACE']

curBut = [-1, -1]
buttonL = [[]]
entr = tk.Text(Keyboard_App, width=100, height=8)
entr.grid(row=0, columnspan=15)

varRow = 1
varColoumn = 0

def leftKey(event):
    if curBut == [-1, -1]:
        curBut[:] = [0,0]
        buttonL[0][0].configure(highlightbackground="Red")
    elif curBut[0] == 4:
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground="Red")
        curBut[:] = [0, 10]
        buttonL[0][10].configure(highlightbackground="Red")
    else:
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground="Red")
        curBut[:] = [curBut[0],(curBut[1]-1)%11]
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground="Red")
    buttonL[curBut[0]][curBut[1]].focus_set()
def rightKey(event):
    if curBut == [-1, -1]:
        curBut[:] = [0,0]
        buttonL[0][0].configure(highlightbackground="Red")
    elif curBut[0] == 4:
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground="Red")
        curBut[:] = [0, 0]
        buttonL[0][0].configure(highlightbackground="Red")
    else:
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground="Red")
        curBut[:] = [curBut[0],(curBut[1]+1)%11]
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground="Red")
    buttonL[curBut[0]][curBut[1]].focus_set()

def upKey(event):
    if curBut == [-1, -1]:
        curBut[:] = [0, 0]
        buttonL[0][0].configure(highlightbackground="Red")
    elif curBut[0] == 0:
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground="Red")
        curBut[:] = [(curBut[0]-1)%5, 0]
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground="Red")
    elif curBut[0] == 4:
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground="Red")
        curBut[:] = [(curBut[0]-1)%5, 5]
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground="Red")
    else:
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground="Red")
        curBut[:] = [(curBut[0]-1)%5,curBut[1]]
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground="Red")
    buttonL[curBut[0]][curBut[1]].focus_set()



def downKey(event):
    if curBut == [-1, -1]:
        curBut[:] = [0, 0]
        buttonL[0][0].configure(highlightbackground="Red")
    elif curBut[0] == 3:
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground="Red")
        curBut[:] = [(curBut[0]+1)%5, 0]
        buttonL[curBut[0]][curBut[1]%11].configure(highlightbackground="Red")
    elif curBut[0] == 4:
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground="Red")
        curBut[:] = [(curBut[0]+1)%5, 5]
        buttonL[curBut[0]][curBut[1]%11].configure(highlightbackground="Red")
    else:
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground="Red")
        curBut[:] = [(curBut[0]+1)%5,curBut[1]]
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground="Red")
    buttonL[curBut[0]][curBut[1]].focus_set()

def select(value, x, y):
    if curBut != [-1, 1]:
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground="red")
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground="red")
    curBut[:] = [x,y]
    buttonL[x][y].configure(highlightbackground="red")
    buttonL[x][y].configure(highlightcolor="red")

    if value == 'DEL':
        input_val = entr.get("1.0", "end-2c")
        entr.delete("1.0","end")
        entr.insert("1.0", input_val, "end")
    elif value == "SPACE":
        entr.insert("insert"," ")
    elif value == 'TAB':
        entr.insert("insert", "    ")
    else:
        entr.insert("end", value)


for buttons in keys:
    if buttons != 'SPACE':
        but = tk.Button(Keyboard_App, text=buttons, width=5, bg="Black", fg="White", highlightthickness=4, activeforeground="Red",
                        activebackground="Gray", highlightcolor="red", relief="raised", padx=12, pady=4, bd=4, command= lambda  x=buttons, i=varRow-1, j=varColoumn: select(x,i,j))
        but.bind('<Return>',lambda event, x=buttons, i=varRow-1, j=varColoumn: select(x,i,j))
        buttonL[varRow-1].append(but)
        but.grid(row=varRow, column=varColoumn)
    if buttons == "SPACE":
        but = tk.Button(Keyboard_App, text=buttons, width=60, bg="Black", fg="White", highlightthickness=4,
                        activeforeground="Red",
                        activebackground="Gray65", highlightcolor="red", relief="raised", padx=4, pady=4, bd=4,
                        command=lambda x=buttons, i=varRow - 1, j=varColoumn: select(x, i, j))
        but.bind('<Return>', lambda event, x=buttons, i=varRow - 1, j=varColoumn: select(x, i, j))
        buttonL[varRow - 1].append(but)
        but.grid(row=6, columnspan=16)
    varColoumn += 1
    if varColoumn > 10:
        varColoumn = 0
        varRow +=1
        buttonL.append([])

Keyboard_App.bind('<Left>', leftKey)
Keyboard_App.bind('<Right>', rightKey)
Keyboard_App.bind('<Up>', upKey)
Keyboard_App.bind('<Down>', downKey)


Keyboard_App.mainloop()
