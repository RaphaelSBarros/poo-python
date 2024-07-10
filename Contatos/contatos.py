"""Desafio Python Rocketseat
"""

contacts = []

def add_contact(name: str, phone: str, email: str, favorite: bool = False):
    """_summary_

    Args:
        name (str): Contact's name
        phone (str): Contact's phone number
        email (str): Contact's email address
        favorite (bool, optional): Favorite contact. Defaults to False.
    """
    contacts.append({"ID":len(contacts),
                     "Name":name,
                     "Phone":phone,
                     "Email":email,
                     "Favorite":favorite})
    
def show_contacts():
    """Show all added contacts
    """
    for contact in contacts:
        print(f"ID: {contact["ID"]},",
              f"Nome: {contact["Name"]},",
              f"Telefone: {contact["Phone"]},",
              f"E-mail: {contact["Email"]},",
              f"Favorito: {contact["Favorite"]}")

def show_favorites():
    """Show favorite contacts
    """
    for contact in contacts:
        if contact["Favorite"] is True:
            print(f"ID: {contact["ID"]},",
                f"Nome: {contact["Name"]},",
                f"Telefone: {contact["Phone"]},",
                f"E-mail: {contact["Email"]},")

def add_favorite(contact_id: int):
    """_summary_

    Args:
        contact_id (int): Contact ID
    """
    contacts[contact_id]["Favorite"] = True

while True:
    choice = input("O que deseja fazer?\n1-Adicionar Contato\n2-Listar Contatos\n3-Listar Favoritos\n4-Adicionar aos Favoritos")