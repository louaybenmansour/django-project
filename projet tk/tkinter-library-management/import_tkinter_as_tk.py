import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3


conn = sqlite3.connect('bibliotheque.db')
cursor = conn.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS livres (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
               
    titre TEXT NOT NULL,
    auteur TEXT NOT NULL,
    quantite INTEGER NOT NULL,
    isbn TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS membres (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT NOT NULL,
    prenom TEXT NOT NULL,
    contact TEXT NOT NULL
)
''')




class GestionnaireBibliotheque:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestionnaire de Bibliothèque")
        self.root.geometry("1000x700")
        self.root.configure(bg="#f0f0f0")

        
        self.style = ttk.Style()
        self.style.theme_use("clam")  
        self.style.configure("TFrame", background="#f0f0f0")
        self.style.configure("TButton", font=("Arial", 10), padding=5, background="#4CAF50", foreground="white")
        self.style.map("TButton", background=[("active", "#45a049")])
        self.style.configure("Treeview", font=("Arial", 10), rowheight=25)
        self.style.configure("Treeview.Heading", font=("Arial", 12, "bold"))
        self.style.configure("TLabel", font=("Arial", 12), background="#f0f0f0")

     
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.frame_livres = ttk.Frame(self.notebook)
        self.notebook.add(self.frame_livres, text="Livres")

        self.tree_livres = ttk.Treeview(self.frame_livres, columns=("ID", "Titre", "Auteur",  "quantite", "ISBN"), show="headings")
        self.tree_livres.heading("ID", text="ID")
        self.tree_livres.heading("Titre", text="Titre")
        self.tree_livres.heading("Auteur", text="Auteur")
        self.tree_livres.heading("quantite", text="quantite")
        self.tree_livres.heading("ISBN", text="ISBN")
        self.tree_livres.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.btn_ajouter_livre = ttk.Button(self.frame_livres, text="Ajouter un Livre", command=self.ajouter_livre)
        self.btn_ajouter_livre.pack(side=tk.LEFT, padx=10, pady=10)

        self.btn_supprimer_livre = ttk.Button(self.frame_livres, text="Supprimer un Livre", command=self.supprimer_livre)
        self.btn_supprimer_livre.pack(side=tk.LEFT, padx=10, pady=10)

        self.charger_livres()

        
        self.frame_membres = ttk.Frame(self.notebook)
        self.notebook.add(self.frame_membres, text="Membres")

        self.tree_membres = ttk.Treeview(self.frame_membres, columns=("ID", "Nom", "Prénom", "Contact"), show="headings")
        self.tree_membres.heading("ID", text="ID")
        self.tree_membres.heading("Nom", text="Nom")
        self.tree_membres.heading("Prénom", text="Prénom")
        self.tree_membres.heading("Contact", text="Contact")
        self.tree_membres.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.btn_ajouter_membre = ttk.Button(self.frame_membres, text="Ajouter un Membre", command=self.ajouter_membre)
        self.btn_ajouter_membre.pack(side=tk.LEFT, padx=10, pady=10)

        self.btn_supprimer_membre = ttk.Button(self.frame_membres, text="Supprimer un Membre", command=self.supprimer_membre)
        self.btn_supprimer_membre.pack(side=tk.LEFT, padx=10, pady=10)

        self.charger_membres()

      
        self.btn_theme = ttk.Button(root, text="Thème Sombre", command=self.changer_theme)
        self.btn_theme.pack(side=tk.BOTTOM, pady=10)

    def charger_livres(self):
        for row in self.tree_livres.get_children():
            self.tree_livres.delete(row)
        cursor.execute("SELECT * FROM livres")
        for row in cursor.fetchall():
            self.tree_livres.insert("", tk.END, values=row)

    def ajouter_livre(self):
        def sauvegarder():
            titre = entry_titre.get()
            auteur = entry_auteur.get()
            quantite = entry_quantite.get()
            isbn = entry_isbn.get()  
            if titre and auteur and quantite and isbn:
                cursor.execute("INSERT INTO livres (titre, auteur, quantite, isbn) VALUES (?,?,?,?)",
                               (titre, auteur, quantite, isbn))
                conn.commit()
                self.charger_livres()
                top.destroy()
            else:
                messagebox.showwarning("Erreur", "Tous les champs sont obligatoires")

        top = tk.Toplevel()
        top.title("Ajouter un Livre")
        top.configure(bg="#f0f0f0")

        tk.Label(top, text="Titre", bg="#f0f0f0").grid(row=0, column=0, padx=10, pady=10)
        entry_titre = tk.Entry(top)
        entry_titre.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(top, text="Auteur", bg="#f0f0f0").grid(row=1, column=0, padx=10, pady=10)
        entry_auteur = tk.Entry(top)
        entry_auteur.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(top, text="Quantité", bg="#f0f0f0").grid(row=2, column=0, padx=10, pady=10)
        entry_quantite = tk.Entry(top)
        entry_quantite.grid(row=2, column=1, padx=10, pady=10)

        tk.Label(top, text="ISBN", bg="#f0f0f0").grid(row=3, column=0, padx=10, pady=10)
        entry_isbn = tk.Entry(top)
        entry_isbn.grid(row=3, column=1, padx=10, pady=10)

        ttk.Button(top, text="Sauvegarder", command=sauvegarder).grid(row=4, column=0, columnspan=2, pady=10)

    def supprimer_livre(self):
        selected = self.tree_livres.selection()
        if selected:
            livre_id = self.tree_livres.item(selected, "values")[0]
            cursor.execute("DELETE FROM livres WHERE id=?", (livre_id,))
            conn.commit()
            self.charger_livres()
        else:
            messagebox.showwarning("Erreur", "Veuillez sélectionner un livre")

    def charger_membres(self):
        for row in self.tree_membres.get_children():
            self.tree_membres.delete(row)
        cursor.execute("SELECT * FROM membres")
        for row in cursor.fetchall():
            self.tree_membres.insert("", tk.END, values=row)

    def ajouter_membre(self):
        def sauvegarder():
            nom = entry_nom.get()
            prenom = entry_prenom.get()
            contact = entry_contact.get()
            if nom and prenom and contact:
                cursor.execute("INSERT INTO membres (nom, prenom, contact) VALUES (?, ?, ?)",
                               (nom, prenom, contact))
                conn.commit()
                self.charger_membres()
                top.destroy()
            else:
                messagebox.showwarning("Erreur", "Tous les champs sont obligatoires")

        top = tk.Toplevel()
        top.title("Ajouter un Membre")
        top.configure(bg="#f0f0f0")

        tk.Label(top, text="Nom", bg="#f0f0f0").grid(row=0, column=0, padx=10, pady=10)
        entry_nom = tk.Entry(top)
        entry_nom.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(top, text="Prénom", bg="#f0f0f0").grid(row=1, column=0, padx=10, pady=10)
        entry_prenom = tk.Entry(top)
        entry_prenom.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(top, text="Contact", bg="#f0f0f0").grid(row=2, column=0, padx=10, pady=10)
        entry_contact = tk.Entry(top)
        entry_contact.grid(row=2, column=1, padx=10, pady=10)

        ttk.Button(top, text="Sauvegarder", command=sauvegarder).grid(row=3, column=0, columnspan=2, pady=10)

    def supprimer_membre(self):
        selected = self.tree_membres.selection()
        if selected:
            membre_id = self.tree_membres.item(selected, "values")[0]
            cursor.execute("DELETE FROM membres WHERE id=?", (membre_id,))
            conn.commit()
            self.charger_membres()
        else:
            messagebox.showwarning("Erreur", "Veuillez sélectionner un membre")

    def changer_theme(self):
        if self.btn_theme.cget("text") == "Thème Sombre":
            self.style.theme_use("alt")  
            self.root.configure(bg="#2d2d2d")
            self.style.configure("TFrame", background="#2d2d2d")
            self.style.configure("TLabel", background="#2d2d2d", foreground="white")
            self.style.configure("Treeview", background="#3d3d3d", foreground="white", fieldbackground="#3d3d3d")
            self.style.configure("Treeview.Heading", background="#4d4d4d", foreground="white")
            self.btn_theme.config(text="Thème Clair")
        else:
            self.style.theme_use("clam") 
            self.root.configure(bg="#f0f0f0")
            self.style.configure("TFrame", background="#f0f0f0")
            self.style.configure("TLabel", background="#f0f0f0", foreground="black")
            self.style.configure("Treeview", background="white", foreground="black", fieldbackground="white")
            self.style.configure("Treeview.Heading", background="#f0f0f0", foreground="black")
            self.btn_theme.config(text="Thème Sombre")



if __name__ == "__main__":
    root = tk.Tk()
    app = GestionnaireBibliotheque(root)
    root.mainloop()
