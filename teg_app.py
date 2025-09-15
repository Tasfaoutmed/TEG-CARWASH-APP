import tkinter as tk
from tkinter import messagebox
import barcode
from barcode.writer import ImageWriter
from datetime import datetime
import os

# Dossier où les tickets seront enregistrés
SAVE_DIR = "tickets"
if not os.path.exists(SAVE_DIR):
    os.makedirs(SAVE_DIR)

def generate_ticket():
    client = entry_client.get()
    car_type = entry_type.get()
    car_brand = entry_brand.get()
    car_plate = entry_plate.get()

    if not client or not car_type or not car_brand or not car_plate:
        messagebox.showerror("Erreur", "Veuillez remplir toutes les informations du client.")
        return

    # Identifiant unique basé sur la date et l’heure
    ticket_id = datetime.now().strftime("%Y%m%d%H%M%S")

    # Créer le code-barres
    code_class = barcode.get_barcode_class('code128')
    barcode_obj = code_class(ticket_id, writer=ImageWriter())

    file_path = os.path.join(SAVE_DIR, f"{ticket_id}.png")
    barcode_obj.save(file_path)

    # Sauvegarder les infos du client
    with open(os.path.join(SAVE_DIR, f"{ticket_id}.txt"), "w", encoding="utf-8") as f:
        f.write(f"Client: {client}\n")
        f.write(f"Type de voiture: {car_type}\n")
        f.write(f"Marque: {car_brand}\n")
        f.write(f"Matricule: {car_plate}\n")
        f.write(f"ID Ticket: {ticket_id}\n")

    messagebox.showinfo("Succès", f"Ticket généré et sauvegardé : {file_path}")

# Interface Tkinter
root = tk.Tk()
root.title("TEG Carwash - Générateur de Tickets")

tk.Label(root, text="Nom du client:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_client = tk.Entry(root)
entry_client.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Type de voiture:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_type = tk.Entry(root)
entry_type.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Marque:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
entry_brand = tk.Entry(root)
entry_brand.grid(row=2, column=1, padx=5, pady=5)

tk.Label(root, text="Matricule:").grid(row=3, column=0, padx=5, pady=5, sticky="e")
entry_plate = tk.Entry(root)
entry_plate.grid(row=3, column=1, padx=5, pady=5)

tk.Button(root, text="🎟 Générer Ticket", command=generate_ticket).grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()
