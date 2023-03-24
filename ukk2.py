import tkinter as tk
import tkinter.messagebox
from tkinter.constants import SUNKEN

window=tk.Tk()
window.title('Calculator')
frame=tk.Frame(master=window,bg="gray",padx=10)
frame.pack()
entry=tk.Entry(master=frame,relief=SUNKEN,borderwidth=3,width=30,font=("arial", 20))
entry.grid(row=0,column=0,columnspan=5,ipady=10,pady=20)

def myclick(value):
    text = entry.insert(tk.END,value)
    

def equal():
    text = str(entry.get())
    try:
        errors = ['**', '//', '-+', '---', '+--', '++']
        for eror in errors:
            if text.find(eror)>0:
                raise SyntaxError

        answer = eval(text)
        answer = round(answer,10)
        
        if float(answer).is_integer():
            answer = int(answer)
        
        clear()
        entry.insert(0, answer)
        entry['fg'] = "black"
        
    except(SyntaxError):
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")
        entry['fg'] = "red"
        
    except(ZeroDivisionError):
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Tidak Bisa Dibagi 0")
        entry['fg'] = "red"

def clear():
    entry.delete(0,tk.END)
    
def clear_e():
    entry.delete(len(entry.get())-1)
    
button_1=tk.Button(master=frame,text='1',width=5, height=1, font=("arial", 30),
       bd=1, fg="#17161b", bg="#F6F6F6",command=lambda:myclick(1))
button_1.grid(row=2,column=0,pady=2)
button_2=tk.Button(master=frame,text='2',width=5, height=1, font=("arial", 30),
       bd=1, fg="#17161b", bg="#F6F6F6",command=lambda:myclick(2))
button_2.grid(row=2,column=1,pady=2)
button_3=tk.Button(master=frame,text='3',width=5, height=1, font=("arial", 30),
       bd=1, fg="#17161b", bg="#F6F6F6",command=lambda:myclick(3))
button_3.grid(row=2,column=2,pady=2)
button_4=tk.Button(master=frame,text='4',width=5, height=1, font=("arial", 30),
       bd=1, fg="#17161b", bg="#F6F6F6",command=lambda:myclick(4))
button_4.grid(row=3,column=0,pady=2)
button_5=tk.Button(master=frame,text='5',width=5, height=1, font=("arial", 30),
       bd=1, fg="#17161b", bg="#F6F6F6",command=lambda:myclick(5))
button_5.grid(row=3,column=1,pady=2)
button_6=tk.Button(master=frame,text='6',width=5, height=1, font=("arial", 30),
       bd=1, fg="#17161b", bg="#F6F6F6",command=lambda:myclick(6))
button_6.grid(row=3,column=2,pady=2)
button_7=tk.Button(master=frame,text='7',width=5, height=1, font=("arial", 30),
       bd=1, fg="#17161b", bg="#F6F6F6",command=lambda:myclick(7))
button_7.grid(row=4,column=0,pady=2)
button_8=tk.Button(master=frame,text='8',width=5, height=1, font=("arial", 30),
       bd=1, fg="#17161b", bg="#F6F6F6",command=lambda:myclick(8))
button_8.grid(row=4,column=1,pady=2)
button_9=tk.Button(master=frame,text='9',width=5, height=1, font=("arial", 30),
       bd=1, fg="#17161b", bg="#F6F6F6",command=lambda:myclick(9))
button_9.grid(row=4,column=2,pady=2)
button_0=tk.Button(master=frame,text='0',width=5, height=1, font=("arial", 30),
       bd=1, fg="#17161b", bg="#F6F6F6",command=lambda:myclick(0))
button_0.grid(row=5,column=1,pady=2)
button_0=tk.Button(master=frame,text='.',width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#fff", bg="#FF961C",command=lambda:myclick("."))
button_0.grid(row=5,column=3,pady=2)


button_add=tk.Button(master=frame,text="+",width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#fff", bg="#FF961C",command=lambda:myclick('+'))
button_add.grid(row=2,column=3,pady=2)

button_subtract=tk.Button(master=frame,text="-",width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#fff", bg="#FF961C",command=lambda:myclick('-'))
button_subtract.grid(row=3,column=3,pady=2)

button_multiply=tk.Button(master=frame,text="*",width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#fff", bg="#FF961C",command=lambda:myclick('*'))
button_multiply.grid(row=1,column=3,pady=2)

button_div=tk.Button(master=frame,text="/",width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#fff", bg="#FF961C",command=lambda:myclick('/'))
button_div.grid(row=1,column=2,pady=2)

button_clear=tk.Button(master=frame,text="C",width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#fff", bg="#CD0000",command=clear)
button_clear.grid(row=1,column=0,pady=2)

button_clear=tk.Button(master=frame,text="CE",width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#fff", bg="#CD0000",command=clear_e)
button_clear.grid(row=1,column=1,pady=2)

button_equal=tk.Button(master=frame,text="=",width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#fff", bg="#FF961C",command=equal)
button_equal.grid(row=4,column=3,pady=2)

window.mainloop()