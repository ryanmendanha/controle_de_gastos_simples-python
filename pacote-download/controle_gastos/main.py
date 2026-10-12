print(18*"-")
print("CONTROLE DE GASTOS")
print(18*"-")

gastos = []

while True:
    print("\n {1} - Adicionar Gastos\n", "{2} - Listar Gastos\n", "{3} - Ver Total\n", "{4} - Sair\n")
    try:
        opc = int(input("Bem vindo, senhor. Oque deseja fazer hoje?:\n\n"))
    except ValueError:
        print("Erro!, Tente Novamente.")
        continue

    match opc:
        case 1:
            descricao = input("\nDescrição do gasto: ")
            try:
                valor = float(input("Valor R$: "))
                categoria = input("Categoria: ")

                gasto = {
                    "descricao": descricao,
                    "valor": valor,
                    "categoria": categoria
                }
                gastos.append(gasto)
                print("Gasto adicionado com êxito senhor!")
            except ValueError:
                print("Erro!, tente novamente.")
        case 2:
            if len(gastos) == 0:
                print("Não há gastos adicionados.")
            else:
                for gasto in gastos:
                    print(
                        f"\nDescrição: {gasto['descricao']} | "
                        f"Valor R$: {gasto['valor']:.2f} | "
                        f"Categoria: {gasto['categoria']}")
        case 3:
            total = 0
            for gasto in gastos:
                total += gasto["valor"]
            print(f"Total R$: {total:.2f}")
        case 4:
            break
        case _:
            print("Opção inválida")

