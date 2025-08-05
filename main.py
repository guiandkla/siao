name = input("Digite seu nome: ")
message = "Hello World!"

status = []

if name == 'Guilherme':
    status = "Aprovado! Esse é o cara (risos)"
else:
    status = "Reprovado"

print(message)
print("O aluno " + name + " está " + status + ". Me siga para mais dicas de programação em Python.")