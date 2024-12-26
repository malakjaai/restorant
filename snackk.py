import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def panierajout(article, prix, panier, tot_tmn):
    panier.append((article, prix))
    panieraff(panier, tot_tmn)

def panieraff(panier, tot_tmn):
    liste_panier.delete(0, tk.END)
    for article, prix in panier:
        liste_panier.insert(tk.END, article + " - " + str(prix) + " MAD")
    total = sum(prix for _, prix in panier)
    tot_tmn.config(text="Total : " + str(total) + " MAD")

def cmddazt(panier, tot_tmn):
    if panier:
        total = sum(prix for _, prix in panier)
        cmd = "\n".join([article + " - " + str(prix) + " MAD" for article, prix in panier])
        messagebox.showinfo("Votre commande est validée :)", "Votre commande est celle-ci :\n" + cmd + "\n\nTotal : " + str(total) + " MAD")
        panier.clear()
        panieraff(panier, tot_tmn)
    else:
        messagebox.showwarning("Votre panier est vide :(", "Veuillez le remplir avant de valider votre commande!")

def ajouter_article(article, prix):
    def ajouter():
        panierajout(article, prix, panier, tot_tmn)
    return ajouter

pr = tk.Tk()
pr.title("Votre Snack Préféré")
pr.geometry("600x600")
pr.iconbitmap("p.ico")

panier = []

label_menu = tk.Label(pr, text="Menu", font=("Arial", 18, "bold"))
label_menu.pack(pady=10)

lista = [
    {"nom": "Limonade", "prix": 3, "image": "Limonada.jpg"},
    {"nom": "Soda", "prix": 2, "image": "Soda.jpg"},
    {"nom": "Nuggets", "prix": 5, "image": "Nuggets.jpg"},
    {"nom": "Pizza", "prix": 10, "image": "Pizza.jpg"},
    {"nom": "Sandwich", "prix": 6, "image": "Sandwich.jpg"},
    {"nom": "Tacos", "prix": 8, "image": "tacos.jpg"},
    {"nom": "Frites", "prix": 4, "image": "Frites.jpg"},
]

cadre_menu = tk.Frame(pr)
cadre_menu.pack(pady=10)

for item in lista:
    article = item["nom"]
    prix = item["prix"]
    image_path = item["image"]

    cadre_article = tk.Frame(cadre_menu, borderwidth=2, padx=10, pady=10)
    cadre_article.pack(side=tk.LEFT, padx=10, pady=10)

    image = Image.open(image_path)
    image = image.resize((100, 100))
    img = ImageTk.PhotoImage(image)
    label_image = tk.Label(cadre_article, image=img)
    label_image.image = img  
    label_image.pack()

    nm = tk.Label(cadre_article, text=article + "\n" + str(prix) + " MAD", font=("Arial", 12))
    nm.pack()

    bouton = tk.Button(
        cadre_article, 
        text="Ajouter", 
        command=ajouter_article(article, prix)
    )
    bouton.pack()

cadre_panier = tk.Frame(pr, borderwidth=2, padx=10, pady=10)
cadre_panier.pack(pady=20, fill=tk.BOTH, expand=True)

label_panier = tk.Label(cadre_panier, text="Votre Panier", font=("Arial", 14, "bold"))
label_panier.pack()

liste_panier = tk.Listbox(cadre_panier, height=10, font=("Arial", 12))
liste_panier.pack(pady=10)

tot_tmn = tk.Label(pr, text="Total : 0 MAD", font=("Arial", 14, "bold"))
tot_tmn.pack()

def valider_commande(): 
    cmddazt(panier, tot_tmn)

def reset_panier():
    panier.clear()
    panieraff(panier, tot_tmn)

btn_valider = tk.Button(pr, text="Valider la commande", bg="green", fg="white", font=("Arial", 12), command=valider_commande,)
btn_valider.pack(pady=10)

btn_reset = tk.Button(pr, text="Réinitialiser le panier", bg="red", fg="white", font=("Arial", 12), command=reset_panier,height=2,  width=20, padx=10,pady=10 )
btn_reset.pack(pady=5)

pr.mainloop()