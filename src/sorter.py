import tkinter as tk
import random
import time
from base64 import b16encode
from functools import partial

WIN_X, WIN_Y = 800, 500
ARR_LEN = 500
DELAY = 100 #ms


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

    btn1["command"] = partial(start_sort, "Starting algorithm 1", canvas, ent_elems, ent_delay)    
    nums = list(range(1, ARR_LEN + 1))
    draw_reset(nums, canvas)
    root.mainloop()
    
def start_sort(msg, canvas, ent_elems, ent_delay):
    global ARR_LEN, DELAY
    print(msg)
    input_ent_elems = ent_elems.get()
    input_ent_delay = ent_delay.get()

    if input_ent_elems != "":
        ARR_LEN = int(input_ent_elems)
    if input_ent_delay != "":
        DELAY = int(input_ent_delay)
        
    nums = list(range(1, ARR_LEN + 1))
    shuffle(nums)
    val_pairs = draw_reset(nums, canvas)

    selection_sort(val_pairs, canvas)
    
def draw_reset(nums, canvas):
    canvas.delete("visual")
    max_height = 350
    width = 780/len(nums)

    for n in range(len(nums)):
        per = nums[n] / len(nums)
        height = per * max_height
        color = rgb_color((int(230 - 160*per), 50, int(80 + 160 * per)))
        canvas.create_rectangle(10 + n*width, 490, 10 + (n+1)*width, 490-height, fill=color, outline=color, tag="visual")

    return list(zip(nums, canvas.find_withtag("visual")))
        
def rgb_color(rgb):
    return(b'#' + b16encode(bytes(rgb)))

def swap(i1, i2, val_pairs, canvas):
    width = 780/len(val_pairs)
    canvas.move(val_pairs[i1][1], (i2-i1)*width, 0)
    canvas.move(val_pairs[i2][1], (i1-i2)*width, 0)
    val_pairs[i1], val_pairs[i2] = val_pairs[i2], val_pairs[i1]

def selection_sort(val_pairs, canvas):
    for n in range(len(val_pairs)):
        min = n
        for i in range(n + 1, len(val_pairs)):
            if val_pairs[i][0] < val_pairs[min][0]:
                min = i
        if min != n:
            swap(min, n, val_pairs, canvas)
            time.sleep(DELAY/1000)
            canvas.update()

def shuffle(arr):
    arrCopy = arr.copy()
    for n in range(len(arr)):
        r = random.randint(0, len(arrCopy) - 1)
        arr[n] = arrCopy.pop(r)

if __name__ == "__main__":
    main()