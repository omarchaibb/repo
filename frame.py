import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from datetime import datetime

root = tk.Tk()
root.geometry("900x560")
root.resizable(False,False)

s = ttk.Style()
s.configure("SelectedDish.TFrame", background='green')
s.configure("MainFrame.TFrame", background="#2B2B28")
s.configure("menuFrame.TFrame", background="#4A4A48")
s.configure("DisplayFrame.TFrame", background="#0F1110", width=30)
s.configure('OrderFrame.TFrame', background="#B7C4CF")
s.configure("DishFrame.TFrame", background="#4A4A48", relief="sunken")
s.configure('MenuLabel.TLabel',background="#0F1110",font=("Arial", 13, "italic"),foreground="white",padding=(10, 10),width=17)
s.configure('orderTotalLabel.TLabel',background="#0F1110",font=("Arial", 10, "bold"),foreground="white",padding=(2, 2, 2, 2),anchor="w")
s.configure('orderTransaction.TLabel',background="#4A4A48",font=('Helvetica', 12),foreground="white",wraplength=160,anchor="nw",padding=(3, 3, 3, 3))

# ================== section frames =============

mainFrame = ttk.Frame(root, width=800, height=560, style='MainFrame.TFrame')
mainFrame.grid(row=0, column=0, sticky="NSEW")

topBannerFrame = ttk.Frame(mainFrame)
topBannerFrame.grid(row=0, column=0, sticky="NSEW", columnspan=3)

menuFrame = ttk.Frame(mainFrame, style='menuFrame.TFrame')
menuFrame.grid(row=1, column=0, padx=3, pady=3, sticky="NSEW")

displayFrame = ttk.Frame(mainFrame, style="DisplayFrame.TFrame")
displayFrame.grid(row=1, column=1, padx=3, pady=3, sticky="NSEW")

orderFrame = ttk.Frame(mainFrame, style="OrderFrame.TFrame")
orderFrame.grid(row=1, column=2, padx=3, pady=3, sticky="NSEW")

# =================== dish frames ===========

tajinFrame = ttk.Frame(menuFrame, style="DishFrame.TFrame")
tajinFrame.grid(row=1, column=0, sticky="NSEW")

spagettiFrame = ttk.Frame(menuFrame, style="DishFrame.TFrame")
spagettiFrame.grid(row=2, column=0, sticky="NSEW")

QuesadillaFrame = ttk.Frame(menuFrame, style="DishFrame.TFrame")
QuesadillaFrame.grid(row=3, column=0, sticky="NSEW")

burgerFrame = ttk.Frame(menuFrame, style="DishFrame.TFrame")
burgerFrame.grid(row=4, column=0, sticky="NSEW")

pizzaFrame = ttk.Frame(menuFrame, style="DishFrame.TFrame")
pizzaFrame.grid(row=5, column=0, sticky="NSEW")

tacosFrame = ttk.Frame(menuFrame, style="DishFrame.TFrame")
tacosFrame.grid(row=6, column=0, sticky="NSEW")

# ==================== images ================
logoimageObject = Image.open("C:\\Users\\omarc\\Desktop\\github\\realrepo\\images\\logo.png").resize((120, 120))
logoImage = ImageTk.PhotoImage(logoimageObject)

topFrameImage = Image.open("C:\\Users\\omarc\\Desktop\\github\\realrepo\\images\\res.png").resize((780, 120))
topimage = ImageTk.PhotoImage(topFrameImage)

# ================ images lables =============
labellogo = ttk.Label(topBannerFrame, image=logoImage)
labellogo.grid(row=0, column=0, sticky="W")

labelresimage = ttk.Label(topBannerFrame, image=topimage, background="black")
labelresimage.grid(row=0, column=1, sticky="NSEW")

# =============== Menu label =================
labelMenu = ttk.Label(menuFrame, text="Menu", style='MenuLabel.TLabel')
labelMenu.grid(row=0, column=0, columnspan=2, sticky="NSEW")
labelMenu.configure(anchor="center", font=("Helvetica", 14, "bold"))

# ================ dish labels ===============
tajinFramelabel = ttk.Label(tajinFrame, text="Tajin  : 20 dh", style='MenuLabel.TLabel')
tajinFramelabel.grid(row=1, column=0, padx=10, pady=10, sticky="W")

spagettiFrameleb = ttk.Label(spagettiFrame, text="Spagetti : 30dh", style='MenuLabel.TLabel')
spagettiFrameleb.grid(row=2, column=0, sticky="W", padx=10, pady=10)

quesadillaFramelab = ttk.Label(QuesadillaFrame, text="Quesadilla : 50dh", style='MenuLabel.TLabel')
quesadillaFramelab.grid(row=3, column=0, sticky="W", padx=10, pady=10)

burgerFramelab = ttk.Label(burgerFrame, text="Burger: 60dh ", style="MenuLabel.TLabel")
burgerFramelab.grid(row=4, column=0, sticky='W', padx=10, pady=10)

pizzaframelab = ttk.Label(pizzaFrame, text="Pizza : 70dh ", style="MenuLabel.TLabel")
pizzaframelab.grid(row=5, column=0, sticky='W', padx=10, pady=10)

tacosFrameleb = ttk.Label(tacosFrame, text="tacos : 100dh ", style='MenuLabel.TLabel')
tacosFrameleb.grid(row=6, column=0, sticky='W', padx=10, pady=10)

# ==================== function ==============


prices = {
    "Tajin":20,
    "Spagetti":30,
    "Quesadilla":50,
    "Burger":60,
    "Pizza":70,
    "Tacos":100
}
def displayTajin():
    tajinFrame.configure(relief="sunken",style="SelectedDish.TFrame")
    
    defaultimagelab.configure(image=tajinImage,text="Tajin",font=('Helvetica', 14, "bold"),foreground="white",compound="bottom",padding=(5, 5, 5, 5),background="#000")
    spagettiFrame.configure(relief="sunken",style="DishFrame.TFrame")
    QuesadillaFrame.configure(relief="sunken",style="DishFrame.TFrame")
    burgerFrame.configure(relief="sunken",style="DishFrame.TFrame")
    pizzaFrame.configure(relief="sunken",style="DishFrame.TFrame")
    tacosFrame.configure(relief="sunken",style="DishFrame.TFrame")
    

def displaySpagetti():
    spagettiFrame.configure(relief="sunken",style="SelectedDish.TFrame")
    
    defaultimagelab.configure(image=spagettiImage,text="Spagetti",font=('Helvetica', 14, "bold"),foreground="white",compound="bottom",padding=(5, 5, 5, 5),background="#000")
    tajinFrame.configure(relief="sunken",style="DishFrame.TFrame")
    QuesadillaFrame.configure(relief="sunken",style="DishFrame.TFrame")
    burgerFrame.configure(relief="sunken",style="DishFrame.TFrame")
    pizzaFrame.configure(relief="sunken",style="DishFrame.TFrame")
    tacosFrame.configure(relief="sunken",style="DishFrame.TFrame")
    
def displayQuesadilla():
    QuesadillaFrame.configure(relief="sunken",style="SelectedDish.TFrame")
    
    defaultimagelab.configure(image=quesadillaImage,text="Quesadilla",font=('Helvetica', 14, "bold"),foreground="white",compound="bottom", padding=(5, 5, 5, 5), background="#000")
    tajinFrame.configure(relief="sunken",style="DishFrame.TFrame")
    spagettiFrame.configure(relief="sunken",style="DishFrame.TFrame")
    burgerFrame.configure(relief="sunken",style="DishFrame.TFrame")
    pizzaFrame.configure(relief="sunken",style="DishFrame.TFrame")
    tacosFrame.configure(relief="sunken",style="DishFrame.TFrame")

def displayBurger():
    burgerFrame.configure(relief="sunken",style="SelectedDish.TFrame")
    
    defaultimagelab.configure(image=burgerImage,text="Burger",font=('Helvetica', 14, "bold"),foreground="white",compound="bottom",padding=(5, 5, 5, 5),background="#000")
    tajinFrame.configure(relief="sunken",style="DishFrame.TFrame")
    spagettiFrame.configure(relief="sunken",style="DishFrame.TFrame")
    QuesadillaFrame.configure(relief="sunken",style="DishFrame.TFrame")
    pizzaFrame.configure(relief="sunken",style="DishFrame.TFrame")
    tacosFrame.configure(relief="sunken",style="DishFrame.TFrame")

def displaypizza():
    pizzaFrame.configure(relief="sunken",style="SelectedDish.TFrame")
    
    defaultimagelab.configure(image=pizzaImage,text="Pizza",font=('Helvetica', 14, "bold"),foreground="white",compound="bottom",padding=(5, 5, 5, 5),background="#000")
    tajinFrame.configure(relief="sunken",style="DishFrame.TFrame")
    spagettiFrame.configure(relief="sunken",style="DishFrame.TFrame")
    QuesadillaFrame.configure(relief="sunken",style="DishFrame.TFrame")
    burgerFrame.configure(relief="sunken",style="DishFrame.TFrame")
    tacosFrame.configure(relief="sunken",style="DishFrame.TFrame")

def displayTacos():
    tacosFrame.configure(relief = "sunken",style = "SelectedDish.TFrame")
    
    defaultimagelab.configure(image = tacosImage,text ="Tacos",font=('Helvetica', 14,"bold"),foreground="white",compound = "bottom",padding = (5, 5, 5, 5),background="#000")
    tajinFrame.configure(relief = "sunken",style="DishFrame.TFrame")
    spagettiFrame.configure(relief = "sunken",style="DishFrame.TFrame")
    QuesadillaFrame.configure(relief = "sunken",style="DishFrame.TFrame")
    burgerFrame.configure(relief = "sunken",style="DishFrame.TFrame")
    pizzaFrame.configure(relief = "sunken",style="DishFrame.TFrame")
    
liste_of_orders = []
totale = 0
def add():
    main_ttc = orderTransaction.cget("text")
    order_name_with_price = defaultimagelab.cget('text') +": "+str(prices[defaultimagelab.cget("text")])+"dh"+" "*30
    
    list_order = main_ttc + order_name_with_price
    
    orderTransaction.configure(text=list_order)
    
    global totale
    
    totale += prices[defaultimagelab.cget("text")]
    
    orderTotalLabel.configure(text=f"TOTAL : {totale}dh")
    
    liste_of_orders.append(order_name_with_price)

def remove():
    global totale
    liste_of_orders.pop(-1)
    orderTransaction.configure(text=" ".join(liste_of_orders))
    totale -= prices[defaultimagelab.cget("text")]
    orderTotalLabel.configure(text=f"TOTAL :{totale}dh")
        
def order():
    if not liste_of_orders:
        return
    noww = datetime.now()
    order_file = f"your_order_{str(noww).replace(" ","_").replace(":",";")}.txt"
    with open(order_file, "w") as file:
        file.write("your order is :")
        file.write("\n")
        for ele in liste_of_orders:
            file.write(ele)
            file.write("\n")
        
        file.write("\n")
        file.write(f"{orderTotalLabel.cget("text")}")

# ============== Buttons =====================

tajinbutton = ttk.Button(tajinFrame,text="Display",command= displayTajin) 
tajinbutton.grid(row = 1, column = 1, padx = 10)

spaggetibutton = ttk.Button(spagettiFrame,text="Display",command=displaySpagetti) 
spaggetibutton.grid(row = 2, column = 1, padx = 10)

quesadillabutton = ttk.Button(QuesadillaFrame,text="Display",command=displayQuesadilla) 
quesadillabutton.grid(row = 3, column =1, padx = 10)

burgerbutton = ttk.Button(burgerFrame,text="Display",command=displayBurger)
burgerbutton.grid(row=4,column=1,padx=10,pady=10)

pizzabutton = ttk.Button(pizzaFrame,text="Display",command=displaypizza)
pizzabutton.grid(row=5,column=1,padx=10,pady=10)

tacosbutton = ttk.Button(tacosFrame,text="Display",command=displayTacos)
tacosbutton.grid(row=6,column=1,padx=10,pady=10)

# ==========================  display  images =================
defaultdisplayImage = Image.open("C:\\Users\\omarc\\Desktop\\github\\realrepo\\images\\default.png").resize((340,400))
defaultImage =ImageTk.PhotoImage(defaultdisplayImage)

tajinimg = Image.open("C:\\Users\\omarc\\Desktop\\github\\realrepo\\images\\tajin.png").resize((360,360))
tajinImage = ImageTk.PhotoImage(tajinimg)

spagettiimg = Image.open("C:\\Users\\omarc\\Desktop\\github\\realrepo\\images\\spagetti.png").resize((360,360))
spagettiImage = ImageTk.PhotoImage(spagettiimg)

quesadillaimg = Image.open("C:\\Users\\omarc\\Desktop\\github\\realrepo\\images\\quesadilla.png").resize((360,360))
quesadillaImage = ImageTk.PhotoImage(quesadillaimg)

burgerimg = Image.open("C:\\Users\\omarc\\Desktop\\github\\realrepo\\images\\burger.png").resize((350,360))
burgerImage = ImageTk.PhotoImage(burgerimg)

pizzaimg = Image.open("C:\\Users\\omarc\\Desktop\\github\\realrepo\\images\\pizza.png").resize((350,360))
pizzaImage = ImageTk.PhotoImage(pizzaimg)

tacosimg = Image.open("C:\\Users\\omarc\\Desktop\\github\\realrepo\\images\\tacos.png").resize((350,360))
tacosImage = ImageTk.PhotoImage(tacosimg)

# ============================label and button display frame ==================
defaultimagelab = ttk.Label(displayFrame,image=defaultImage)
defaultimagelab.grid(row=0,column=0,sticky='NSEW',columnspan=2)

# ======================== display buttons ======================
addtorderbutton = ttk.Button(displayFrame,text="ADD TO ORDER",command=add)
addtorderbutton.grid(row=1,column=0,sticky='NSEW')

removebutton = ttk.Button(displayFrame,text="REMOVeE",command=remove)
removebutton.grid(row=1,column=1,sticky="NSEW")

# ====================== order =================
orderTitleLabel = ttk.Label(orderFrame, text = "ORDER")
orderTitleLabel.configure(foreground="white", background="black",font=("Helvetica", 14, "bold"), anchor = "center",padding = (5, 5, 5, 5),)
orderTitleLabel.grid(row = 0, column = 0, sticky = "EW")

orderTransaction = ttk.Label(orderFrame, style = 'orderTransaction.TLabel')
orderTransaction.grid(row = 2, column = 0, sticky = "NSEW")

orderTotalLabel = ttk.Label(orderFrame, text = "TOTAL : 0dh", style = "orderTotalLabel.TLabel")
orderTotalLabel.grid(row = 3, column = 0, sticky = "EW")

orderButton = ttk.Button(orderFrame, text = "ORDER",command=order)
orderButton.grid(row = 4, column = 0, sticky = "EW")

# ============== grid configuration ==========
mainFrame.columnconfigure(2,weight=1)
orderFrame.columnconfigure(0,weight=1)
orderFrame.rowconfigure(2,weight=1)

root.mainloop()