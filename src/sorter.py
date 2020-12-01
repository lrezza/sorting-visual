import tkinter as tk
import random

WIN_X, WIN_Y = 800, 500

def main():
    arr = list(range(0, 10))
    arrCopy = arr.copy()

    createWindow()
    
    print(arr)
    shuffle(arr)
    print(arr)

    badSort(arr)
    arrCopy.sort()
    print(arr)

    assert arr == arrCopy

def createWindow():
    root = tk.Tk()

    canvas = tk.Canvas(root, width=WIN_X, height=WIN_Y)
    canvas.pack()

    frame = tk.Frame(root, bg="gray")
    frame.place(relx = 0.025, rely = 0.025, relwidth=0.95, relheight=0.95)
    
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

    lbl_delay = tk.Label(frame, text="Delay:")
    lbl_delay.grid(row=0, column=7)
    ent_delay = tk.Entry(frame, width=6)
    ent_delay.grid(row=1, column=7)
    lbl_elems = tk.Label(frame, text="Elems:")
    lbl_elems.grid(row=0, column=8)
    ent_elems = tk.Entry(frame, width=6)
    ent_elems.grid(row=1, column=8)
    btn_sort = tk.Button(frame, text="Start sort")
    btn_sort.grid(row=0, column = 9)
    

    root.mainloop()

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