# VARIABILI
nome_negoziante = "Pietro"
tastiera_economica = "tastiera trust"
tastiera_medio_prezzo = "tastiera msi"
tastiera_costosa = "tastiera logitech"
tastiere = ["tastiera trust", "tastiera msi", "tastiera logitech"]
prezzo_tastiera_economica = "20 euro"
prezzo_tastiera_medio_prezzo = "50 euro"
prezzo_tastiera_costosa = "100 euro"

# INIZIO PROGRAMMA
print("Benvenuto nel mio negozio!")
print("Molto piacere, mi chiamo " + nome_negoziante + "... E sono pronto a servirti!")
print("\nDato che abbiamo aperto da poco, abbiamo solo 3 tastiere:")
print("Quella della Trust, quella della MSI e quella della Logitech!")
print("\nLa tastiera più costosa che abbiamo è la " + tastiera_costosa)
print("Ora che te le ho descritte, dimmi, quale preferisci?")
tastiera_richiesta = input()
print("Hai scelto la" + str(tastiera_richiesta))
if tastiera_richiesta == tastiera_economica:
    print("Il prezzo è di " + prezzo_tastiera_economica)
elif tastiera_richiesta == tastiera_medio_prezzo:
    print("Il prezzo di questa tastiera è di " + prezzo_tastiera_medio_prezzo)
elif tastiera_richiesta == tastiera_costosa:
    print("Il prezzo di questa tastiera è di " + prezzo_tastiera_costosa)
else:
    print("Purtroppo non abbiamo quella tastiera, riavvia il programma e scegline un'altra!")
