def classificarProdutos():
    try:
        produto = input("Qual o nome do produto?")
        valor = int(input("Qual o valor do produto?"))

        if(valor > 100):
            print(f" O produto {produto} é classificado como caro.")
        elif(valor >= 50):
            print(f" O produto {produto} é classificado como médio.")
        else:
            print(f" O produto {produto} é classificado como barato.")
    except:
        print("Você precisa informar um valor válido")

classificarProdutos()                        
