t=[]
for i in range(1):
    t.append(input(f"Donner le nom de client n {i+1}:"))
    nbr=int(input(f"Donner le nombre d’article pour le client n`{i+1}:"))
    s=0
    prix_totale=0
    for j in range(nbr):
        v=float(input(f"Donner le prix de l’article n{j+1}:"))
        s+=v
        tva=s*0.15
        prix_totale=s-(s*0.02)+tva
print("-----------------------------------------------------------")
print("Facture")
print("-----------------------------------------------------------")
print("Le totale à payer pour le client",t[i],"est :",prix_totale,"DH")
        
