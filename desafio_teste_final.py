"""
Desafio Final — Central de Atendimento (Confeitaria / Suporte)
Estruturas de Dados: Filas, Pilhas, Ordenação, Busca Binária e Recursão.
"""

# Estruturas Globais
fila_chamados = []        # Fila FIFO para atendimento
pilha_atendidos = []      # Pilha LIFO para desfazer atendimentos



def abrir_chamado(protocolo, descricao, prioridade):
    """
    Adiciona um novo chamado ao final da fila (FIFO).
    Cada chamado é representado como um dicionário.
    """
    chamado = {
        'protocolo': protocolo,
        'descricao': descricao,
        'prioridade': prioridade
    }
    fila_chamados.append(chamado)
    return chamado


def atender_proximo():
    """
    Remove e retorna o primeiro chamado da fila (FIFO).
    Guarda o chamado atendido na pilha para permitir 'desfazer'.
    """
    if not fila_chamados:
        return None
    
    chamado_atendido = fila_chamados.pop(0)
    pilha_atendidos.append(chamado_atendido)
    return chamado_atendido


def desfazer_atendimento():
    """
    Retira o último chamado atendido da pilha e o insere de volta
    na PRIMEIRA posição da fila, sem perder a vez de espera.
    """
    if not pilha_atendidos:
        return None
    
    ultimo_atendido = pilha_atendidos.pop()
    fila_chamados.insert(0, ultimo_atendido)
    return ultimo_atendido




def ordenar_por_prioridade(lista):
    """
    Ordena uma cópia da lista por prioridade (decrescente/maior prioridade primeiro)
    utilizando Insertion Sort. Garante estabilidade (mantém a ordem de chegada).
    """
    lista_ordenada = lista.copy()
    n = len(lista_ordenada)
    
    for i in range(1, n):
        pivo = lista_ordenada[i]
        j = i - 1
        # Compara prioridades: move elementos menores para a direita
        while j >= 0 and lista_ordenada[j]['prioridade'] < pivo['prioridade']:
            lista_ordenada[j + 1] = lista_ordenada[j]
            j -= 1
        lista_ordenada[j + 1] = pivo
        
    return lista_ordenada




def buscar_protocolo(lista, protocolo_alvo):
    """
    Realiza a busca binária na lista (que deve estar ordenada por protocolo).Retorna o chamado se encontrado, ou None caso contrário.
    """
    inicio = 0
    fim = len(lista) - 1
    
    while inicio <= fim:
        meio = (inicio + fim) // 2
        protocolo_atual = lista[meio]['protocolo']
        
        if protocolo_atual == protocolo_alvo:
            return lista[meio]
        elif protocolo_atual < protocolo_alvo:
            inicio = meio + 1
        else:
            fim = meio - 1
            
    return None


def contar_por_prioridade(lista, prioridade_alvo):
    """
    Conta quantos chamados possuem a prioridade desejada de forma RECURSIVA.
    Não utiliza laços (for/while) nem funções prontas (sum/len/count).
    """
    # Caso Base: lista vazia
    if not lista:
        return 0
    
    # Passo Indutivo
    primeiro = lista[0]
    restante = lista[1:]
    
    coincidencia = 1 if primeiro['prioridade'] == prioridade_alvo else 0
    
    return coincidencia + contar_por_prioridade(restante, prioridade_alvo)




def menu():
    while True:
        print("\n--- CENTRAL DE ATENDIMENTO / PEDIDOS ---")
        print("1. Abrir Chamado/Pedido")
        print("2. Atender Próximo")
        print("3. Desfazer Último Atendimento")
        print("4. Listar Pendentes por Urgência")
        print("5. Buscar Chamado por Protocolo")
        print("6. Contar Chamados por Prioridade (Recursivo)")
        print("0. Sair")
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == '1':
            try:
                prot = int(input("Número do Protocolo: "))
                desc = input("Descrição do Pedido/Problema: ")
                prio = int(input("Prioridade (1-Baixa, 2-Média, 3-Alta): "))
                abrir_chamado(prot, desc, prio)
                print("✓ Chamado registrado com sucesso!")
            except ValueError:
                print("⚠️ Erro: Entrada inválida.")
                
        elif opcao == '2':
            atendido = atender_proximo()
            if atendido:
                print(f"✓ Atendendo Protocolo #{atendido['protocolo']}: {atendido['descricao']}")
            else:
                print("⚠️ Nenhum chamado pendente na fila.")
                
        elif opcao == '3':
            desfeito = desfazer_atendimento()
            if desfeito:
                print(f"✓ Atendimento do Protocolo #{desfeito['protocolo']} desfeito! Devolvido ao topo da fila.")
            else:
                print("⚠️ Nenhum atendimento para desfazer.")
                
        elif opcao == '4':
            if not fila_chamados:
                print("⚠️ Fila vazia.")
            else:
                ordenados = ordenar_por_prioridade(fila_chamados)
                print("\n--- PEDIDOS POR ORDEM DE URGÊNCIA ---")
                for item in ordenados:
                    print(f"Protocolo: {item['protocolo']} | Prioridade: {item['prioridade']} | Descrição: {item['descricao']}")
                    
        elif opcao == '5':
            try:
                prot_busca = int(input("Digite o número do protocolo para buscar: "))
                # Ordena a lista por protocolo antes da busca binária
                lista_ordenada_prot = sorted(fila_chamados, key=lambda x: x['protocolo'])
                resultado = buscar_protocolo(lista_ordenada_prot, prot_busca)
                if resultado:
                    print(f"✓ Encontrado: Protocolo #{resultado['protocolo']} | Prioridade: {resultado['prioridade']} | Desc: {resultado['descricao']}")
                else:
                    print("⚠️ Protocolo não encontrado.")
            except ValueError:
                print("⚠️ Erro: Informe um número de protocolo válido.")
                
        elif opcao == '6':
            try:
                prio_busca = int(input("Digite a prioridade desejada para contar: "))
                total = contar_por_prioridade(fila_chamados, prio_busca)
                print(f"✓ Total de chamados com prioridade {prio_busca}: {total}")
            except ValueError:
                print("⚠️ Erro: Informe um número inteiro de prioridade.")
                
        elif opcao == '0':
            print("Saindo do sistema...")
            break
        else:
            print("⚠️ Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()