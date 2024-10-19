def contarQtdA(entrada):
    qtd = 0
    for i in range(len(entrada)):
        if(entrada[i] == "a" or entrada[i] == "A"):
            qtd += 1
    return qtd

resultado = contarQtdA(input("Digite uma string: "))
print(f"Quantidade total da letra 'a' na string: {resultado}")
   