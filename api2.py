import requests
resposta = requests.get("https://economia.awesomeapi.com.br/json/last/USD-BRL")
dados = resposta.json()
#print(dados)

dolar = dados["USDBRL"]

high = dolar["high"]
low = dolar["low"]
variacao = dolar["varBid"]
variacao_percentual = dolar["pctChange"]
valor_dolar = dolar["bid"]
venda_dolar = dolar["ask"]
horario_cotação = dolar["timestamp"]
data_hora = dolar["create_date"]

while True: 
    print("\nO que deseja verificar? ")

    opcao=int(input("\n1 - Maior valor do dólar nesse dia e o menor valor\n2 - Variação no valor da compra e variação percentual\n3 - Valor da compra\n4 - valor da venda\n5 - Horário da cotação\n6 - Data e hora da cotação\nEscolha: "))

    match opcao:
        case 1:
            print(f"\nMaior valor:{high}")
            print(f"Menor valor:{low}")
            print("")
        case 2:
            print(f"\nVariação valor da compra:{variacao}")
            print(f"\nVariação percentual: {variacao_percentual}")
        case 3:
            print(f"\nValor da compra: {valor_dolar}")
        case 4:
            print(f"\nValor venda: {venda_dolar}")
        case 5:
            print(f"\nHorário da cotação: {horario_cotação}")
        case 6:
            print(f"\nData e Hora da cotação: {data_hora}")
        case _:
            print("Opção inválida!")
    
    escolha=input(("\nDeseja encerrar ?\ns - sim |n-não ")).lower()
    if escolha == "n":
        print("\nContinuando...")
    elif escolha == "s":
        print("Programa encerrando...")
        break      