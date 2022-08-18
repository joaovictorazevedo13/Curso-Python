def l():
    print('=' * 50)


def maior(* valores):
    l()
    print('Analisando valores passados...')
    for num in valores:
        print(f'{num}', end=' ')
    print(f"\nMaior numero informado foi o {max(valores)}.")


maior(5, 7, 9)
maior(9, 44, 55, 2, 5, 6)
maior(-55, -88, -20, -5)
l()