def soma(*valores):
    s = 0
    for num in valores:
        s = s + num
    print(f"Somando os valores {valores} temos {s}")


soma(1, 2)
soma(1, 2, 3)
