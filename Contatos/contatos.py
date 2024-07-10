"""Desafio Python Rocketseat
"""

contacts = []

def create_contact(name: str, phone: str, email: str, favorite: bool = False):
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

def read_contacts():
    """Show all added contacts
    """
    for contact in contacts:
        print(f"ID: {contact["ID"]},",
              f"Nome: {contact["Name"]},",
              f"Telefone: {contact["Phone"]},",
              f"E-mail: {contact["Email"]},",
              f"Favorito: {contact["Favorite"]}")

def read_favorites():
    """Show favorite contacts
    """
    for contact in contacts:
        if contact["Favorite"] is True:
            print(f"ID: {contact["ID"]},",
                f"Nome: {contact["Name"]},",
                f"Telefone: {contact["Phone"]},",
                f"E-mail: {contact["Email"]},")

def toggle_favorite(contact_id: int):
    """_summary_

    Args:
        contact_id (int): Contact ID
    """

    if contact_id >= len(contacts):
        return "Esse ID não existe!"

    if contacts[contact_id]["Favorite"] is True:
        contacts[contact_id]["Favorite"] = False
    else:
        contacts[contact_id]["Favorite"] = True

def update_contact(contact_id: int, n: str, p: str, e: str):
    """Update contacts on the list

    Args:
        contact_id (int): Contact's identifier
        n (str): Contact's name
        p (str): Contact's phone number
        e (str): Contact's email address
    """
    if contact_id >= len(contacts):
        print("Esse ID não existe!")

    contacts[contact_id]["Name"] = n
    contacts[contact_id]["Phone"] = p
    contacts[contact_id]["Email"] = e

while True:
    print("\n",
          "1 - Adicionar Contato\n",
          "2 - Listar Contatos\n",
          "3 - Listar Favoritos\n",
          "4 - Adicionar aos Favoritos\n",
          "5 - Editar Contato\n",
          "0 - Cancelar")
    choice = input("O que deseja fazer? ")
    match choice:
        case "1":
            na = input("Informe o nome do contato\n")
            ph = input("Informe o telefone do contato\n")
            em = input("informe o email do contato\n")
            fa = input("Deseja salvar como favorito?s/n\n")
            if fa == "s":
                create_contact(na, ph, em, True)
            else:
                create_contact(na, ph, em)
        case "2":
            read_contacts()
        case "3":
            read_favorites()
        case "4":
            ID = int(input("Informe o ID do contato que deseja favoritar ou desfavoritar\n"))
            toggle_favorite(ID)
        case "5":
            ID = int(input("Informe o ID do contato que deseja favoritar\n"))
            na = input("Informe o nome do contato\n")
            ph = input("Informe o telefone do contato\n")
            em = input("informe o email do contato\n")
            update_contact(ID, na, ph, em)
        case "0":
            break
