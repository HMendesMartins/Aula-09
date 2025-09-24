import datetime
hoje = datetime.date.today()
nome = input("Insira quando precisa devolver o livro: ")
nome2 = datetime.datetime.strptime(nome,'%d/%m/%Y').date()
print(hoje.strftime('%d/%m/%Y'))
diferenca = nome2 -hoje
if diferenca.days > 0:
    print(f"Faltam {diferenca.days} dias para entregar")
elif diferenca.days < 0:
    print(f"A entrega está atrasada em {diferenca.days} dias")
else:
    print("A entrega é hoje!")