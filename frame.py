import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

root = tk.Tk()
root.geometry("900x600")

s = ttk.Style()
s.configure("SelectedDish.TFrame", background='green')
s.configure("MainFrame.TFrame", background="#2B2B28")
s.configure("menuFrame.TFrame", background="#4A4A48")
s.configure("DisplayFrame.TFrame", background="#0F1110", width=30)
s.configure('OrderFrame.TFrame', background="#B7C4CF")
s.configure("DishFrame.TFrame", background="#4A4A48", relief="sunken")
s.configure('MenuLabel.TLabel',background="#0F1110",font=("Arial", 13, "italic"),foreground="white",padding=(10, 10),width=17)
s.configure('orderTotalLabel.TLabel',background="#0F1110",font=("Arial", 10, "bold"),foreground="white",padding=(2, 2, 2, 2),anchor="w")
s.configure('orderTransaction.TLabel',background="#4A4A48",font=('Helvetica', 12),foreground="white",wraplength=170,anchor="nw",padding=(3, 3, 3, 3))

# ================== section frames =============

mainFrame = ttk.Frame(root, width=800, height=580, style='MainFrame.TFrame')
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

coscosFrame = ttk.Frame(menuFrame, style="DishFrame.TFrame")
coscosFrame.grid(row=1, column=0, sticky="NSEW")

taginFrame = ttk.Frame(menuFrame, style="DishFrame.TFrame")
taginFrame.grid(row=2, column=0, sticky="NSEW")

baboushFrame = ttk.Frame(menuFrame, style="DishFrame.TFrame")
baboushFrame.grid(row=3, column=0, sticky="NSEW")

hsouyaFrame = ttk.Frame(menuFrame, style="DishFrame.TFrame")
hsouyaFrame.grid(row=4, column=0, sticky="NSEW")

pizzaFrame = ttk.Frame(menuFrame, style="DishFrame.TFrame")
pizzaFrame.grid(row=5, column=0, sticky="NSEW")

bananaFrame = ttk.Frame(menuFrame, style="DishFrame.TFrame")
bananaFrame.grid(row=6, column=0, sticky="NSEW")

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

coscosFramelabel = ttk.Label(coscosFrame, text="Cscou bdjaj  : 20", style='MenuLabel.TLabel')
coscosFramelabel.grid(row=0, column=0, padx=10, pady=10, sticky="W")

taginFrameleb = ttk.Label(taginFrame, text="atajin : 30", style='MenuLabel.TLabel')
taginFrameleb.grid(row=0, column=0, sticky="W", padx=10, pady=10)

baboushFrameleb = ttk.Label(baboushFrame, text="baboush miat : 50", style='MenuLabel.TLabel')
baboushFrameleb.grid(row=0, column=0, sticky="W", padx=10, pady=10)

hsouwaFrameleb = ttk.Label(hsouyaFrame, text="hsouwa : 60 ", style="MenuLabel.TLabel")
hsouwaFrameleb.grid(row=0, column=0, sticky='W', padx=10, pady=10)

pizzaframelab = ttk.Label(pizzaFrame, text="pizza fabor : 70 ", style="MenuLabel.TLabel")
pizzaframelab.grid(row=0, column=0, sticky='W', padx=10, pady=10)

bananaFrameleb = ttk.Label(bananaFrame, text="banana   : 100 ", style='MenuLabel.TLabel')
bananaFrameleb.grid(row=0, column=0, sticky='W', padx=10, pady=10)

# ==================== function ==============
index = 0
order = ""
total_amount = 0

prices = {
    "coscos":20,
    "Tajin":30,
    "baboush":50,
    "Hrira":60,
    "pizza":70,
    "banana":100
}
def displaycoscos():
    coscosFrame.configure(relief="sunken",style="SelectedDish.TFrame")
    
    defaultimagelab.configure(image=coscosImage,text="coscos",font=('Helvetica', 14, "bold"),foreground="white",compound="bottom",padding=(5, 5, 5, 5),background="#000")
    taginFrame.configure(relief="sunken",style="DishFrame.TFrame")
    baboushFrame.configure(relief="sunken",style="DishFrame.TFrame")
    hsouyaFrame.configure(relief="sunken",style="DishFrame.TFrame")
    pizzaFrame.configure(relief="sunken",style="DishFrame.TFrame")
    bananaFrame.configure(relief="sunken",style="DishFrame.TFrame")
    
    price = 20
    global index
    index = 1
    global order
    order = f"coscos prix :{price} DH"
    global total_amount
    total_amount += price



def displaytajin():
    taginFrame.configure(relief="sunken",style="SelectedDish.TFrame")
    
    defaultimagelab.configure(image=tajinImage,text="Tajin",font=('Helvetica', 14, "bold"),foreground="white",compound="bottom",padding=(5, 5, 5, 5),background="#000")
    coscosFrame.configure(relief="sunken",style="DishFrame.TFrame")
    baboushFrame.configure(relief="sunken",style="DishFrame.TFrame")
    hsouyaFrame.configure(relief="sunken",style="DishFrame.TFrame")
    pizzaFrame.configure(relief="sunken",style="DishFrame.TFrame")
    bananaFrame.configure(relief="sunken",style="DishFrame.TFrame")
    
    price = 30
    global index
    index = 1
    global order
    order = f"twijin prix :{price} DH"
    global total_amount
    total_amount += price



def displaybaboush():
    baboushFrame.configure(relief="sunken",style="SelectedDish.TFrame")
    
    defaultimagelab.configure(image=baboushImage,text="baboush",font=('Helvetica', 14, "bold"),foreground="white",compound="bottom", padding=(5, 5, 5, 5), background="#000")
    coscosFrame.configure(relief="sunken",style="DishFrame.TFrame")
    taginFrame.configure(relief="sunken",style="DishFrame.TFrame")
    hsouyaFrame.configure(relief="sunken",style="DishFrame.TFrame")
    pizzaFrame.configure(relief="sunken",style="DishFrame.TFrame")
    bananaFrame.configure(relief="sunken",style="DishFrame.TFrame")
    
    global price
    price = 50
    global index
    index = 1
    global order
    order = f"baboush prix :{price} DH"
    global total_amount
    total_amount += price


def displayhrira():
    hsouyaFrame.configure(relief="sunken",style="SelectedDish.TFrame")
    
    defaultimagelab.configure(image=hsouwaImage,text="Hrira",font=('Helvetica', 14, "bold"),foreground="white",compound="bottom",padding=(5, 5, 5, 5),background="#000")
    coscosFrame.configure(relief="sunken",style="DishFrame.TFrame")
    taginFrame.configure(relief="sunken",style="DishFrame.TFrame")
    baboushFrame.configure(relief="sunken",style="DishFrame.TFrame")
    pizzaFrame.configure(relief="sunken",style="DishFrame.TFrame")
    bananaFrame.configure(relief="sunken",style="DishFrame.TFrame")
    global price
    price = 60
    global index
    index = 1
    global order
    order = f"hrira prix :{price} DH"
    global total_amount
    total_amount += price

def displaypizza():
    pizzaFrame.configure(relief="sunken",style="SelectedDish.TFrame")
    
    defaultimagelab.configure(image=pizzaImage,text="pizza",font=('Helvetica', 14, "bold"),foreground="white",compound="bottom",padding=(5, 5, 5, 5),background="#000")
    coscosFrame.configure(relief="sunken",style="DishFrame.TFrame")
    taginFrame.configure(relief="sunken",style="DishFrame.TFrame")
    baboushFrame.configure(relief="sunken",style="DishFrame.TFrame")
    hsouyaFrame.configure(relief="sunken",style="DishFrame.TFrame")
    bananaFrame.configure(relief="sunken",style="DishFrame.TFrame")
    
    global price
    price = 70
    global index
    index = 1
    global order
    order = f"pizza prix :{price} DH"
    global total_amount
    total_amount += price


def displaybanan():
    bananaFrame.configure(relief = "sunken",style = "SelectedDish.TFrame")
    global dd
    dd= defaultimagelab.configure(image = bananaImage,text = "banana",font=('Helvetica', 14,"bold"),foreground="white",compound = "bottom",padding = (5, 5, 5, 5),background="#000")
    coscosFrame.configure(relief = "sunken",style="DishFrame.TFrame")
    taginFrame.configure(relief = "sunken",style="DishFrame.TFrame")
    baboushFrame.configure(relief = "sunken",style="DishFrame.TFrame")
    hsouyaFrame.configure(relief = "sunken",style="DishFrame.TFrame")
    pizzaFrame.configure(relief = "sunken",style="DishFrame.TFrame")
    
    
    price = 100
    global index
    index = 1
    global order
    order = f"banane prix :{price} DH"
    global total_amount
    total_amount += price

    
# def le_totale():
#         return orderTotalLabel.configure( text = f"TOTAL : {total_amount}", style = "orderTotalLabel.TLabel")

        
# def addorder():
#     if index == 0:
#         return        
#     else:
#         orderTransaction.config(text=order)
    
# def two_functions():
#     le_totale()
#     addorder()

# def removeorder():
#     global total_amount
#     total_amount -= price
#     if total_amount >= 0:
#         return orderTotalLabel.configure( text = f"TOTAL : {total_amount}", style = "orderTotalLabel.TLabel")
#     else:
#         return
# # def add():
# #     totalee=0
# #     to= dd.cget('text')
# #     print(to)
# # add()
def add():
    # updating the transaction label
    main_ttc = orderTransaction.cget("text")
    order_name_with_price = defaultimagelab.cget('text') +": "+str(prices[defaultimagelab.cget("text")])+" "*30
    list_order = main_ttc + order_name_with_price
    orderTransaction.configure(text=list_order)
# ============== Buttons =====================

coscosbutton = ttk.Button(coscosFrame,text="Display",command= displaycoscos) 
coscosbutton.grid(row = 0, column = 1, padx = 10)

taginbutton = ttk.Button(taginFrame,text="Display",command=displaytajin) 
taginbutton.grid(row = 0, column = 1, padx = 10)

babuoshbutton = ttk.Button(baboushFrame,text="Display",command=displaybaboush) 
babuoshbutton.grid(row = 0, column =1, padx = 10)

hsouwabutton = ttk.Button(hsouyaFrame,text="Display",command=displayhrira)
hsouwabutton.grid(row=0,column=1,padx=10,pady=10)

pizzabutton = ttk.Button(pizzaFrame,text="Display",command=displaypizza)
pizzabutton.grid(row=0,column=1,padx=10,pady=10)

bananabutton = ttk.Button(bananaFrame,text="Display",command=displaybanan)
bananabutton.grid(row=0,column=1,padx=10,pady=10)

# ==========================  display  images =================
defaultdisplayImage = Image.open("C:\\Users\\omarc\\Desktop\\github\\realrepo\\images\\default.png").resize((300,400))
defaultImage =ImageTk.PhotoImage(defaultdisplayImage)

coscosimg = Image.open("C:\\Users\\omarc\\Desktop\\github\\realrepo\\images\\coscos.png").resize((350,360))
coscosImage = ImageTk.PhotoImage(coscosimg)


tajinimg = Image.open("C:\\Users\\omarc\\Desktop\\github\\realrepo\\images\\tajin.png").resize((350,360))
tajinImage = ImageTk.PhotoImage(tajinimg)

baboushimg = Image.open("C:\\Users\\omarc\\Desktop\\github\\realrepo\\images\\baboush.png").resize((350,360))
baboushImage = ImageTk.PhotoImage(baboushimg)

hsouwaimg = Image.open("C:\\Users\\omarc\\Desktop\\github\\realrepo\\images\\hrira.png").resize((350,360))
hsouwaImage = ImageTk.PhotoImage(hsouwaimg)

pizzaimg = Image.open("C:\\Users\\omarc\\Desktop\\github\\realrepo\\images\\pizza.png").resize((350,360))
pizzaImage = ImageTk.PhotoImage(pizzaimg)

bananaimg = Image.open("C:\\Users\\omarc\\Desktop\\github\\realrepo\\images\\banana.png").resize((350,360))
bananaImage = ImageTk.PhotoImage(bananaimg)
# ============================label of display images ==================

defaultimagelab = ttk.Label(displayFrame,image=defaultImage)
defaultimagelab.grid(row=0,column=0,sticky='NSEW',columnspan=2)

addOrderButton = ttk.Button(displayFrame, text = "ADD TO ORDER")
addOrderButton.grid(row = 1, column = 0, padx = 2, sticky = "NSEW")

removeOrderButton = ttk.Button(displayFrame, text = "REMOVE")
removeOrderButton.grid(row = 1, column = 1, padx = 2, sticky = "NSEW")



# ========================display buttons ======================
addtorderbutton = ttk.Button(displayFrame,text="ADD TO ORDER",command=add)
addtorderbutton.grid(row=1,column=0,sticky='NSEW')

removebutton = ttk.Button(displayFrame,text="REMOVE")
removebutton.grid(row=1,column=1,sticky="NSEW")

# ====================== order =================
orderTitleLabel = ttk.Label(orderFrame, text = "ORDER")
orderTitleLabel.configure(foreground="white", background="black",font=("Helvetica", 14, "bold"), anchor = "center",padding = (5, 5, 5, 5),)
orderTitleLabel.grid(row = 0, column = 0, sticky = "EW")



orderTransaction = ttk.Label(orderFrame, style = 'orderTransaction.TLabel')
orderTransaction.grid(row = 2, column = 0, sticky = "NSEW")

orderTotalLabel = ttk.Label(orderFrame, text = "TOTAL : 0$", style = "orderTotalLabel.TLabel")
orderTotalLabel.grid(row = 3, column = 0, sticky = "EW")

orderButton = ttk.Button(orderFrame, text = "ORDER")
orderButton.grid(row = 4, column = 0, sticky = "EW")

# ============== grid configuration ==========

mainFrame.columnconfigure(2,weight=1)
mainFrame.rowconfigure(1,weight=1)
menuFrame.columnconfigure(0,weight=1)
menuFrame.rowconfigure(1,weight=1)
menuFrame.rowconfigure(2,weight=1)
menuFrame.rowconfigure(3,weight=1)
menuFrame.rowconfigure(4,weight=1)
menuFrame.rowconfigure(5,weight=1)
menuFrame.rowconfigure(6,weight=1)
orderFrame.columnconfigure(0,weight=1)
orderFrame.rowconfigure(2,weight=1)

root.mainloop()