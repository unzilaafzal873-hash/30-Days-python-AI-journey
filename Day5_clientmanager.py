# Day 5 - Final Project
print("=== Fiverr Client Manager ===")

clients = [] # Ye list hai. 4 din pe seekha tha

for i in range(3): # 3 clients ka data lenge
    print(f"\nClient {i+1} ka data daalo:")
    name = input("Client ka naam: ")
    order = input("Order kitne ka tha $: ")
    work = input("Kaam kya tha: ")
    
    client_data = {"naam": name, "paisa": order, "kaam": work}
    clients.append(client_data) # List mein add kar diya

print("\n=== SARE CLIENTS KI LIST ===")
total = 0
for c in clients:
    print(f"Naam: {c['naam']} | ${c['paisa']} | Kaam: {c['kaam']}")
    total = total + int(c['paisa'])

print(f"\nTotal Earning: ${total}")
print("Shabash Unzila! Tu ne Python ka 5 din ka course khatam kar liya 🎉")
