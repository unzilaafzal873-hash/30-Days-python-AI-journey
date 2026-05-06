# Day 4: Contact Book Bot by Unzila - Upgraded
# Date: 6 May 2026

contacts = {} # Khali contact book

def add_contact(name, number):
    contacts[name] = number
    print(name, "ka number save ho gaya!")

def show_contacts():
    print("\n--- Meri Contact Book ---")
    for name in contacts:
        print(name, ":", contacts[name])

# Bot chala rahe hain
add_contact("Ammi", "0300-0000000")
add_contact("Fiverr Client", "0311-1234567")
show_contacts()

# Naya contact add karte hain
naya_naam = input("\nNaye client ka naam: ")
naya_number = input("Number: ")
add_contact(naya_naam, naya_number)

print("\nUpdated list:")
show_contacts()
