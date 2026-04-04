import tkinter as tk 
root = tk.Tk()
root.title("calculator")
root.geometry("320x500")
root.resizable(False,False)
root.config(bg="#1e1e2e")
exp = ""
dis_var = tk.StringVar()
dis_var.set("0")
def press(value):
    print(value)
    global exp 
    if value == "=":
        try:
            result = str(eval(exp))
            dis_var.set(result)
            exp = result
            return  
        except:
            dis_var.set("error")
            exp = ""
            return
    elif value == "c":
        exp = ""
        dis_var.set("0")
        return
    elif value == "backspace":
        exp = exp[:-1]
        dis_var.set(exp if exp else 0)
        return
    elif value == "%":
        try:
            exp = str(eval(exp)/100)
            dis_var.set(exp)
            return
        except:
            dis_var.set("error")
            exp = ""
            return
    elif value == "+/-":
        try:
            exp = str(eval(exp)*-1)
            dis_var.set(exp)
            return
        except:
            dis_var.set("ERROR")
            EXP = "" 
            return
    else:
        if exp == "" or exp == "0":
           if value in "+-*/.":
               exp = "0"+ value
           else:
            exp =value
        else:
         exp += value
    dis_var.set(exp) 
scr_frame = tk.Frame(root , bg="#1e1e2e" ,pady=10)
scr_frame.pack(fill="both", padx=15)
expr_label = tk.Label(scr_frame,textvariable=dis_var,font=("arial",36,"bold"),bg= "#1e1e2e",fg="#ffffff",anchor="e",padx=10)
expr_label.pack(fill="both", ipady=20)
tk.Frame(root,bg="#313244",height=2).pack(fill="x",padx=15)
buttons = [["C",   "+/-", "%",  "÷"],
    ["7",   "8",   "9",  "×"],
    ["4",   "5",   "6",  "−"],
    ["1",   "2",   "3",  "+"],
    ["backspace",  "0",   ".",  "="],
]
def get_colour(val):
    if val in ["C", "+/-", "%"]:
        return "#282D90", "#cdd6f4"
    elif val in ["÷", "×", "−", "+", "="]:
        return "#cba6f7", "#1e1e2e"
    elif val in "backspace":
       return   "#f38ba8", "#1e1e2e"
    else:
        return "#01020c", "#253b83"
def map_value(val):
    maping = {"÷": "/", "×": "*", "−": "-"}
    return maping.get(val,val)
b_frame =  tk.Frame(root , bg="#1e1e2e",pady = 10)
b_frame.pack(fill = "both", expand = True, padx = 15)
for row_list in buttons:
    row_frame=tk.Frame(b_frame,bg="#1e1e2e")
    row_frame.pack(fill="both" , expand=True , pady=4)
    for val in row_list:
        bg , fg = get_colour(val)
        btn = tk.Button(row_frame,text=val,font=("Arial", 18, "bold"),
                        bg=bg,fg=fg,activebackground=fg,activeforeground=bg,
                        relief="flat",cursor="hand2",
                        command=lambda v= val:press(map_value(v)))
        btn.pack(side="left",fill="both",expand=True, padx=4)
        btn.bind("<Enter>", lambda e, b=btn, f=fg, bg2=bg: b.config(bg=f,fg=bg2))
        btn.bind("<Leave>", lambda e, b=btn,bg2=bg,  f=fg: b.config(bg=bg2, fg=f))
root.mainloop()


        
        
    
     



    




