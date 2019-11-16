import tkinter as tk
from collections import Counter as count
import datetime
from tkinter import *

import os

        
class Item:
    def __init__(self, name, price, button):
        self.name = name
        self.price = price
        self.button = button

class Register:
    def __init__(self, parent):

        self.parent = parent
        parent.title('Point of Sale')
        parent.resizable(0, 0) 
        parent.config(background="#202020")
        parent.geometry("570x457")
        self.bglable=tk.Label(text="Point of Sale System", bg = "#020202", fg="#e75480",font=("Tahoma", 16,'bold'))
        self.bglable.place(x=0,y=0,width="570",height="60")
        
        self.bggcolor=tk.Label(bg="#161616")
        self.bggcolor.place(x=0,y=60,width="620",height="457")
        
      
        self.linebgs=tk.Label(text="",bg="#e75480")
        self.linebgs.place(x=570,y=30,width="2",height="340")
        self.linebg=tk.Label(text="",bg="#e75480")
        self.linebg.place(x=0,y=30,width="570",height="2")

        self.linebgtotal=tk.Label(text="",bg="#e75480")
        self.linebgtotal.place(x=0,y=390,width="900",height="2")
        self.font = ('Courier New', 12)
        self.till = 0
        self.TAX = 0.08
        self.items = {

                       
                      'Rocky Choco':Item('Rocky Choco', 7050,
                                      tk.Button(root,
                                      text='Rocky Choco',
                                      bg="#e75480",
                                      command=lambda: self.scan('Rocky Choco'),
                                      font=self.font)),
                      'Minty Choco':Item('Minty Choco', 5075,
                                              tk.Button(root,
                                              text='Minty Choco',
                                              bg="#e75480",
                                              command=lambda: self.scan('Minty Choco'),
                                              font=self.font)),
                       'Choco Burst':Item('Choco Burst', 5000,
                                     tk.Button(root,
                                     bg="#e75480",
                                     text='Choco Burst',
                                     command=lambda: self.scan('Choco Burst'),
                                     font=self.font)),
                      'Choco Chips':Item('Choco Chips', 6000,
                                     tk.Button(root,
                                     text='Choco Chips',
                                     bg="#e75480",
                                     command=lambda: self.scan('Choco Chips'),
                                     font=self.font)),
                       'Cream Brulee':Item('Cream Brulee', 6000,
                                     tk.Button(root,
                                     text='Cream Brulee',
                                     bg="#e75480",
                                     command=lambda: self.scan('Cream Brulee'),
                                     font=self.font))}
       

                    

        
        self.MAX_NAME_WIDTH = max(map(len, (item.name for item in self.items.values()))) + 3
        self.MAX_PRICE_WIDTH = 10
        self.server_label = tk.Label(root, text="Cashier: Anita", font=("Tahoma", 11,'bold'), bg="#020202",fg="#e75480")
        self.server_label.place(x=10, y=20)
        self.time_label = tk.Label(root, text='', font=("Tahoma", 11,'bold'),fg="#e75480")
        self.time_label.place(x=0,y=430)
        for idx,item in enumerate(self.items.values(), start=1):
            item.button.grid(row=idx, column=1, sticky='W')
        self.frame = tk.Frame(root)
        self.frame = tk.Frame(root)
        self.frame.grid(row=0, column=1, sticky='W', rowspan=idx+1, columnspan=4, padx=170, pady=120)
        self.scrollbar = tk.Scrollbar(self.frame, orient=tk.VERTICAL)
        self.box = tk.Listbox(self.frame,
                              yscrollcommand=self.scrollbar.set,
                              width=self.MAX_NAME_WIDTH + self.MAX_PRICE_WIDTH + 10,
                              font=self.font)
        self.scrollbar.config(command=self.box.yview)
        self.box.grid(row=0, column=1, sticky='NS')
        self.scrollbar.grid(row=0, column=2, sticky='NS')
        self.box.bind("<Double-Button-1>", self.modify_item)
        
        self.checkout_button = tk.Button(root, text='Checkout', command=self.checkout,font=("Tahoma", 10,'bold'),bg="#e75480")
        self.checkout_button.place(x=480,y=400, height=40,width=80)
        self.new_order_button = tk.Button(root, text='New order', command=self.new_order,font=("Tahoma", 10,'bold'),bg="#e75480")
        self.new_order_button.place(x=390,y=400, height=40,width=80)
        self.total_label = tk.Label(root, text='', font=self.font)
        self.total_label.grid(row=idx+2, column=4, sticky='E')
        self.new_order()
        self.tick()
    def modify_item(self, event=None):
        top = tk.Toplevel()
        entry = tk.Entry(top, font=self.font)
        entry.pack()
        entry.focus_set()
        def set_new_quantity():
            new_value = int(entry.get())
            idx = self.box.index(tk.ACTIVE)
            self.box.delete(idx)
            code = self.current_codes.pop(idx)
            self.current_order[code] -= 1
            for i in range(new_value):
                self.scan(code)
            top.destroy()
            self.update_totals()
        confirm = tk.Button(top, text='OK', command=set_new_quantity, font=self.font)
        confirm.pack()
    def update_totals(self):
    
        self.subtotal = sum(self.items[key].price * value for key,value in self.current_order.items())
        self.tax = round(self.subtotal * self.TAX)
        self.total = self.subtotal + self.tax
        self.total_label.config(text=f'{self.format_money(self.subtotal):>25}\n{self.format_money(self.total):>25}',font=("Tahoma",14,'bold'), bg="#161616",fg="#e75480")
        self.total_label.place(x=369,y=320)
        self.lbltotal=tk.Label(root,text='Total', font=("Tahoma", 11,'bold'), bg="#161616",fg="#e75480")
        self.lbltotal.place(x=397,y=322)
        self.lblsubtotal=tk.Label(root,text='Subtotal', font=("Tahoma", 11,'bold'), bg="#161616",fg="#e75480")
        self.lblsubtotal.place(x=397,y=350)
    def scan(self, code):
        self.current_order[code] += 1
        self.current_codes.append(code)
        name = self.items[code].name
        price = self.format_money(self.items[code].price)
        self.box.insert(tk.END, f'{name:<{self.MAX_NAME_WIDTH}}' + f'{price:>{self.MAX_PRICE_WIDTH+10}}')
        self.box.see(self.box.size()-1)
        self.update_totals()
    def format_money(self, cents):
        d,c = divmod(cents, 100)
        return f'₱{d}.{c:0>2}'
    def checkout(self):
        self.total_label.config(text=f'TOTAL: {self.format_money(self.total)}\n')
        for item in self.items.values():
            item.button.config(state=tk.DISABLED)
        top = tk.Toplevel()
        label = tk.Label(top, text='Input money: ',font=("Tahoma", 10,'bold'),fg="#161616")
        label.grid(row=0, column=0)
        text = tk.Entry(top,bg="#e75480",width=30)
        text.grid(row=0, column=1)
        text.focus_set()
        def pay(event=None):
            # tender is integer of pennies
            tender = int(text.get().replace('.', ''))
            change = tender - self.total
            label.config(text=f'Change: {self.format_money(change)}. Have a nice day!',font=("Tahoma", 10,'bold'),fg="#e75480")
            self.till += self.total
            self.new_order()
            text.config(state=tk.DISABLED)
            go.config(text='Close', command=top.destroy,fg="#e75480")
        go = tk.Button(top, text='Pay', command=pay,font=("Tahoma", 10,'bold'),fg="#161616")
        go.grid(row=0, column=2)
   
    def new_order(self, event=None):
        self.subtotal = self.tax = self.total = 0
        for item in self.items.values():
            item.button.config(state=tk.NORMAL)
        self.box.delete(0, tk.END)
        self.current_order = count()
        self.current_codes = []
        self.update_totals()
    def tick(self):
        self.time_label.config(text=str(datetime.datetime.now()).rpartition('.')[0])
        self.parent.after(1000, self.tick)
        


 
root=tk.Tk()
app=Register(root)
root.mainloop()

