import datetime

hoje = datetime.date.today()
data_nascimento = input("Insira sua data de nascimento: ")
data_nascimento2 = datetime.datetime.strptime(data_nascimento, '%d/%m/%Y')
ano = hoje.year
ano_nascimento = data_nascimento2.year
anof = ano - ano_nascimento
print(f"Sua idade: {anof}")