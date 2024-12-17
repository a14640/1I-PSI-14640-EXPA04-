
            atualizar_estado(pedidos)
        elif opcao == "4":
            exibir_pedidos(pedidos)
        elif opcao == "5":
            eliminar_pedidos(pedidos)Esta função serve para registrar os pedidos:

def registar_pedido(pedidos):
        id_pedido = len(pedidos) + 1
        descricao = input("Descrição do problema: ")
        estado = "Pendente"
        pedidos[id_pedido] = {"descricao": descricao, "estado": estado}
        print(f"Pedido #{id_pedido} registado com sucesso!")

-Estas linhas fazem com que o utilizador registre o pedido e diz como esta o estado do pedido:
O +1 serve para adicionar um ID aos pedidos todos.

Esta função serve para consultar os pedidos:
    def consultar_pedido(pedidos):
        id_pedido = int(input("ID do pedido a consultar: "))
        if id_pedido in pedidos:
            pedido = pedidos[id_pedido]
            print(f"Pedido #{id_pedido} - Descrição: {pedido['descricao']}, Estado: {pedido['estado']}")
        else:
            print("Pedido não encontrado.")

If in pedidos- Se o id do pedido estiver no pedido então esta correto e funciona perfeitamente, se não esta errado o codigo.

Esta função serve para atualizar o estado dos pedidos:
   def atualizar_estado(pedidos):
        id_pedido = int(input("ID do pedido a atualizar: "))
        if id_pedido in pedidos:
            novo_estado = input("Novo estado (Pendente/Em Andamento/Concluído): ")
            if novo_estado in ["Pendente", "Em Andamento", "Concluído"]:
                pedidos[id_pedido]["estado"] = novo_estado
                print(f"Estado do pedido #{id_pedido} atualizado para '{novo_estado}'.")
            else:
                print("Estado inválido.")
        else:
            print("Pedido não encontrado.")

Esta função serve para exibir os pedidos.

 
    def exibir_pedidos(pedidos):
        print("\nLista de Pedidos:")
        print("ID\tDescrição\t\tEstado")
        print("-" * 40)
        for id_pedido, info in pedidos.items():
            print(f"{id_pedido}\t{info['descricao'][:15]}\t\t{info['estado']}")


Esta função retira os pedidos da lista e utilizando um print mostra os pedidos da lista e o estado de cada um.

Esta função serve para eliminar pedidos
def eliminar_pedidos(pedidos):
    id_pedido = int(input("ID do pedido a eliminar: "))
    if id_pedido in pedidos:
        del pedidos[id_pedidos]
        print(f"O Pedido selecionado foi eliminado.")
    else:
        print("Pedido não encontrado!")
 

Utilizando um print escolhe-se o pedido que queres retirar, se o pedido nao estiver na lista de pedidos, nao funciona.


Este é o menu que serve como base de orientação para o utilizador
para escolher o que quiser, por exemplo, se quer registrar algum pedido, consultar algum pedido…

def main():
    pedidos = {}
    while True:
        print("\nSistema de Gestão de Pedidos - Manutenção")
        print("1. Registar Pedido")
        print("2. Consultar Pedido")
        print("3. Atualizar Estado")
        print("4. Exibir Todos os Pedidos")
        print("5. Eliminar Pedidos")
        print("6. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            registar_pedido(pedidos)
        elif opcao == "2":
            consultar_pedido(pedidos)
        elif opcao == "3":
 
