
peso = float(input('Digite seu peso: '))
consumo_arroz = float(input('Quantas gramas de arroz consome por dia: '))
consumo_ovo = float(input('Quantas gramas de ovo consome por dia: '))


def calcula_proteina(peso, arroz, ovo):
    proteina = peso * 1.5
    arroz = 2.5 * (consumo_arroz/100)
    ovo = 7 * (consumo_ovo/55)
    total = arroz + ovo
    print(f'Consumo de proteina diario deve ser {proteina:.2f}g '\n\n)
    print(f'Total de proteinas consumidas por dia: {total}g\n\n')
    

calcula_proteina(peso, consumo_arroz, consumo_ovo)
