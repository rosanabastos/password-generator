import random
import string


def generate_password(length=8) :
    """ Gera uma senha aleatória com letras, números e símbolos."""
characters = string.ascii_letters + string.digits + string.punctuation
paswodr = ''.join(random.choice(characters) for _ in range(length))
return password 

if__name__ == "__main__" :
    print("Bem-vindo ao Gerador de Senhas!")
  try:
    length = int(input("Digite o comprimento da senha (número inteiro): "))
     if length < 1:
       print("Por favor, insira um número maior que zero.")
else: 
    senha = generate_password(length)
    print(f"Sua senha gerada é: {senha}")
except ValueError:
    print("Entrada inválida. Por favor, insira um número inteiro.")


