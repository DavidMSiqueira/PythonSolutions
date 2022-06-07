import re


def clean(tratar):
    tratar = re.sub('[-@&<>"]', '', tratar)
    data = " ".join(tratar.split())
    print(data)


frase = str(input("Frase para ser tratada: "))

clean(frase)

'''
Texto que pode ser usado como referencia para testes:
Copiar após o fim da frase para pegar os espaços vazios no final da frase.
    Os espaços são>@  um prob"le-ma"  , entendeu?   
'''
