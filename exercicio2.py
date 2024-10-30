def contador():
    while True:
        print("Programa para contagem de caracteres ou número de palavras")
        print("1 - Contar número de caracteres")
        print("2 - Contar numero de palavras")
        print("3 -Sair do Sistema")

        escolha = input("\nDigite a sua opção")

        if(escolha == "3"):
            print("\n Fechando Sistema...")
            break
        elif escolha in {"1", "2"}:
            texto = input("\nDigite o seu texto").strip()

            if not texto:
                print("O texto não pode estar vazio. Tente novamente.")
                continue

            if escolha == "1":
                 texto_sem_espaços = texto.replace(" ", "")
                 qtd = len(texto_sem_espaços)
                 opcao = "Caracter(s)"
            if escolha == "2":
                palavra = texto.split()
                qtd =  len(palavra)
                opcao = " Palavra(s)"

            print(f"\nExistem {qtd} {opcao} no seu texto \n \n")
        else:
           print("Escolha uma opção valida")

contador()
