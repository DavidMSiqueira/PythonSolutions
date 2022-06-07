import re

frase = "  Os espaços são>@  um problema  °  , entendeu?"
frase = re.sub('[@>°]', '', frase)

data = " ".join(frase.split())


print(data)