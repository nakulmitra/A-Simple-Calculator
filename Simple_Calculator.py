import tkinter as tk

def all_clear():
    ans.delete(0,"end")

def clear():
    text=ans.get()
    text=text[:-1]
    ans.delete(0,"end")
    ans.insert(0,text)

def op(event):
    e=event.widget
    text=e["text"]
    en=ans.get()
    try:
        if(text=="="):
            res=eval(str(en))
            
        elif(text=="sqrt"):
            res=float(en)**0.5
        
        ans.delete(0,"end")
        ans.insert(0,res)
        
    except:
        pass

def write(event):
    
    e=event.widget
    text=e['text']
    ans.insert("end",text)
    
root=tk.Tk()
root.title("Calculator")
root.config(bg="#ffff00")

ans=tk.Entry(root,justify="center")
ans.pack(side="top",padx=10,pady=10,fill="x")

f=tk.Frame()
f.pack(side="top",padx=10,fill="x")

sqrt=tk.Button(f,text="sqrt",relief="raise",width=14)
sqrt.pack(side="left")
sqrt.bind("<Button-1>",op)

mod=tk.Button(f,text="%",relief="raise",width=14)
mod.pack(side="right")
mod.bind("<Button-1>",write)

btn_frame=tk.Frame(root)
btn_frame.pack(side="top",padx=10,pady=10,fill="x")

lst=[7,4,1]

for i in range(3):
    val=lst[i]
    for j in range(3):
        bt=tk.Button(btn_frame,text=val,relief="raise",width=5)
        bt.grid(row=i,column=j)
        bt.bind("<Button-1>",write)
        val+=1

bt=tk.Button(root,text=0,relief="raise",width=5)
bt.pack(side="top",padx=10,fill="x")
bt.bind("<Button-1>",write)

div=tk.Button(btn_frame,text="/",relief="raise",width=5)
div.grid(row=0,column=3)
div.bind("<Button-1>",write)

mul=tk.Button(btn_frame,text="*",relief="raise",width=5)
mul.grid(row=0,column=4)
mul.bind("<Button-1>",write)

add=tk.Button(btn_frame,text="+",relief="raise",width=5)
add.grid(row=1,column=3)
add.bind("<Button-1>",write)

sub=tk.Button(btn_frame,text="-",relief="raise",width=5)
sub.grid(row=1,column=4)
sub.bind("<Button-1>",write)

dot=tk.Button(btn_frame,text=".",relief="raise",width=5)
dot.grid(row=2,column=3)
dot.bind("<Button-1>",write)

equal=tk.Button(btn_frame,text="=",relief="raise",width=5)
equal.grid(row=2,column=4)
equal.bind("<Button-1>",op)

a_clr=tk.Button(root,text="All Clear",relief="raise",width=13,command=all_clear)
a_clr.pack(side="left",padx=10,pady=10,fill="x")

clr=tk.Button(root,text="Clear",relief="raise",width=13,command=clear)
clr.pack(side="right",padx=10,pady=10,fill="x")

root.mainloop()

