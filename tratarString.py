import re


def clean(tratarStr):
    tratarStr = re.sub('[-@&<>\"\'°ªº]', '', tratarStr)
    data = " ".join(tratarStr.split())
    print(f'\n{data}')


frase = str(input("Frase para ser tratada: "))

clean(frase)

'''
Texto que pode ser usado como referencia para testes:
Copiar após o fim da frase para pegar os espaços vazios no final da frase.
    Os espaços são>@  um p'rob"le-ma" nºª°25  , entendeu?     
'''
