# Recurso Criativo: Adicionei uma funcionalidade na opção de calcular o total 
# que também exibe a quantidade total de itens únicos cadastrados no carrinho.

def main():
    # Listas para armazenar os dados do carrinho
    nomes_itens = []
    precos_itens = []
    
    opcao = 0
    
    print("Bem-vindos ao Programa de Carrinho de Compras!")
    
    while opcao != 5:
        print("\nSelecione uma das seguintes ações:")
        print("1. Adicionar item")
        print("2. Ver carrinho")
        print("3. Remover item")
        print("4. Calcular o total")
        print("5. Sair")
        
        opcao = int(input("Por favor, insira uma ação: "))
        
        # Opção 1: Adicionar item
        if opcao == 1:
            nome = input("Qual item você gostaria de adicionar? ")
            preco = float(input(f"Qual é o preço de '{nome}'? "))
            
            nomes_itens.append(nome)
            precos_itens.append(preco)
            
            print(f"O item '{nome}' foi adicionado ao carrinho.")
            
        # Opção 2: Ver carrinho
        elif opcao == 2:
            if len(nomes_itens) == 0:
                print("\nO seu carrinho está vazio.")
            else:
                print("\nO conteúdo do carrinho de compras é:")
                # Usando enumerate para começar a exibição a partir do 1
                for i, (nome, preco) in enumerate(zip(nomes_itens, precos_itens)):
                    numero_exibicao = i + 1
                    print(f"{numero_exibicao}. {nome} - R$ {preco:.2f}")
                    
        # Opção 3: Remover item
        elif opcao == 3:
            if len(nomes_itens) == 0:
                print("\nO carrinho está vazio, não há o que remover.")
            else:
                print("\nO conteúdo do carrinho de compras é:")
                for i, (nome, preco) in enumerate(zip(nomes_itens, precos_itens)):
                    print(f"{i + 1}. {nome} - R$ {preco:.2f}")
                
                escolha = int(input("\nQual item você gostaria de remover? "))
                indice = escolha - 1
                
                # Verificando se o índice está dentro dos limites da lista
                if indice >= 0 and indice < len(nomes_itens):
                    nomes_itens.pop(indice)
                    precos_itens.pop(indice)
                    print("Item removido.")
                else:
                    print("Desculpe, esse número de item não é válido.")
                    
        # Opção 4: Calcular o total
        elif opcao == 4:
            total = 0
            for preco in precos_itens:
                total += preco
                
            quantidade_itens = len(nomes_itens)
            print(f"\nO preço total dos itens no carrinho de compras é de R$ {total:.2f}")
            print(f"(Você possui {quantidade_itens} tipo(s) de item(ns) no carrinho).")
            
        # Opção 5: Sair
        elif opcao == 5:
            print("\nObrigado. Até mais.")
            
        else:
            print("\nOpção inválida. Por favor, escolha um número de 1 a 5.")

if __name__ == "__main__":
    main()