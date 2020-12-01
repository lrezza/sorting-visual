import tkinter as tk
import random
from base64 import b16encode
from functools import partial

WIN_X, WIN_Y = 800, 500
ARR_LEN = 500

def main():
    createWindow()

def createWindow():
    root = tk.Tk()

    canvas = tk.Canvas(root, width=WIN_X, height=WIN_Y)
    canvas.pack()
    canvas.create_rectangle(10, 60, 790, 490, fill ="#b3b3b3", outline = "#878787")

    frame = tk.Frame(root, bg = "#9e9e9e")
    frame.place(relx = 0.01, rely = 0.01, relwidth=0.98, relheight=0.1)
    
    btn1 = tk.Button(frame, text="Algorithm 1")
    btn1.grid(row=0, column=0)
    btn2 = tk.Button(frame, text="Algorithm 2")
    btn2.grid(row=0, column=1)
    btn3 = tk.Button(frame, text="Algorithm 3")
    btn3.grid(row=0, column=2)
    btn4 = tk.Button(frame, text="Algorithm 4")
    btn4.grid(row=0, column=3)
    btn5 = tk.Button(frame, text="Algorithm 5")
    btn5.grid(row=0, column=4)
    btn6 = tk.Button(frame, text="Algorithm 6")
    btn6.grid(row=0, column=5)
    btn7 = tk.Button(frame, text="Algorithm 7")
    btn7.grid(row=0, column=6)
    btn8 = tk.Button(frame, text="Algorithm 8")
    btn8.grid(row=0, column=7)

    lbl_delay = tk.Label(frame, text="Delay:")
    lbl_delay.grid(row=0, column=8)
    ent_delay = tk.Entry(frame, width=6)
    ent_delay.grid(row=1, column=8)
    lbl_elems = tk.Label(frame, text="Elems:")
    lbl_elems.grid(row=0, column=9)
    ent_elems = tk.Entry(frame, width=6)
    ent_elems.grid(row=1, column=9)

    btn1["command"] = partial(start_sort, "Starting algorithm 1", canvas, ent_elems)    

    arr = list(range(1, ARR_LEN + 1))
    draw_arr(arr, canvas)

    root.mainloop()

def start_sort(msg, canvas, ent_elems):
    global ARR_LEN
    print(msg)
    input = ent_elems.get()
    if input != "":
        ARR_LEN = int(input)

    draw_arr(list(range(1, ARR_LEN + 1)), canvas)

def draw_arr(arr, canvas):
    canvas.delete("arr_visual")
    max_height = 350
    width = 780/len(arr)

    for n in range(len(arr)):
        per = arr[n] / len(arr)
        height = per * max_height
        color = rgb_color((int(230 - 160*per), 50, int(80 + 160 * per)))
        canvas.create_rectangle(10 + n*width, 490-height, 10 + (n+1)*width, 490, fill=color, outline=color, tag="arr_visual")

def rgb_color(rgb):
    return(b'#' + b16encode(bytes(rgb)))

def badSort(arr):
    for n in range(len(arr)):
        min = n
        for i in range(n + 1, len(arr)):
            if arr[i] < arr[min]:
                min = i
        if min != n:
            t = arr[n]
            arr[n] = arr[min]
            arr[min] = t

def shuffle(arr):
    arrCopy = arr.copy()
    for n in range(len(arr)):
        r = random.randint(0, len(arrCopy) - 1)
        arr[n] = arrCopy.pop(r)

if __name__ == "__main__":
    main()