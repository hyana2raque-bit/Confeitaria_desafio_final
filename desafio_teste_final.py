"""Central de atendimento para uma confeitaria ou equipe de suporte.

O programa demonstra fila FIFO, pilha LIFO, ordenacao estavel,
busca binaria e recursao sem depender de bibliotecas externas.
"""

from typing import TypedDict


class Chamado(TypedDict):
    protocolo: int
    descricao: str
    prioridade: int


fila_chamados: list[Chamado] = []
pilha_atendidos: list[Chamado] = []

PRIORIDADES = {
    1: "Baixa",
    2: "Media",
    3: "Alta",
}


def abrir_chamado(protocolo: int, descricao: str, prioridade: int) -> Chamado:
    """Adiciona um chamado ao final da fila e retorna o registro criado."""
    if protocolo <= 0:
        raise ValueError("O protocolo deve ser um numero positivo.")
    if not descricao.strip():
        raise ValueError("A descricao nao pode ficar vazia.")
    if prioridade not in PRIORIDADES:
        raise ValueError("A prioridade deve ser 1, 2 ou 3.")
    if any(
        chamado["protocolo"] == protocolo
        for chamado in fila_chamados + pilha_atendidos
    ):
        raise ValueError("Esse protocolo ja foi utilizado.")

    chamado: Chamado = {
        "protocolo": protocolo,
        "descricao": descricao.strip(),
        "prioridade": prioridade,
    }
    fila_chamados.append(chamado)
    return chamado


def atender_proximo() -> Chamado | None:
    """Remove o primeiro chamado da fila e o guarda na pilha de atendidos."""
    if not fila_chamados:
        return None

    chamado_atendido = fila_chamados.pop(0)
    pilha_atendidos.append(chamado_atendido)
    return chamado_atendido


def desfazer_atendimento() -> Chamado | None:
    """Devolve o ultimo atendimento ao inicio da fila."""
    if not pilha_atendidos:
        return None

    ultimo_atendido = pilha_atendidos.pop()
    fila_chamados.insert(0, ultimo_atendido)
    return ultimo_atendido


def ordenar_por_prioridade(lista: list[Chamado]) -> list[Chamado]:
    """Retorna uma copia ordenada por prioridade decrescente e de forma estavel."""
    lista_ordenada = lista.copy()

    for indice in range(1, len(lista_ordenada)):
        pivo = lista_ordenada[indice]
        posicao = indice - 1
        while (
            posicao >= 0
            and lista_ordenada[posicao]["prioridade"] < pivo["prioridade"]
        ):
            lista_ordenada[posicao + 1] = lista_ordenada[posicao]
            posicao -= 1
        lista_ordenada[posicao + 1] = pivo

    return lista_ordenada


def buscar_protocolo(
    lista: list[Chamado], protocolo_alvo: int
) -> Chamado | None:
    """Busca um protocolo em uma lista previamente ordenada por protocolo."""
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        protocolo_atual = lista[meio]["protocolo"]

        if protocolo_atual == protocolo_alvo:
            return lista[meio]
        if protocolo_atual < protocolo_alvo:
            inicio = meio + 1
        else:
            fim = meio - 1

    return None


def contar_por_prioridade(
    lista: list[Chamado], prioridade_alvo: int
) -> int:
    """Conta recursivamente os chamados que possuem a prioridade informada."""
    def contar(indice: int) -> int:
        if indice == len(lista):
            return 0

        corresponde = 1 if lista[indice]["prioridade"] == prioridade_alvo else 0
        return corresponde + contar(indice + 1)

    return contar(0)


def ler_inteiro(mensagem: str) -> int:
    """Le um inteiro, reapresentando a pergunta ate a entrada ser valida."""
    while True:
        try:
            return int(input(mensagem).strip())
        except ValueError:
            print("Entrada invalida. Informe um numero inteiro.")


def ler_prioridade(mensagem: str) -> int:
    """Le e valida uma prioridade entre 1 e 3."""
    while True:
        prioridade = ler_inteiro(mensagem)
        if prioridade in PRIORIDADES:
            return prioridade
        print("Prioridade invalida. Informe 1, 2 ou 3.")


def exibir_chamado(chamado: Chamado) -> None:
    """Exibe um chamado em um formato padronizado."""
    prioridade = PRIORIDADES[chamado["prioridade"]]
    print(
        f"Protocolo: #{chamado['protocolo']} | "
        f"Prioridade: {prioridade} ({chamado['prioridade']}) | "
        f"Descricao: {chamado['descricao']}"
    )


def carregar_dados_exemplo() -> int:
    """Carrega chamados de exemplo sem duplicar protocolos existentes."""
    exemplos = [
        (101, "Bolo de casamento atrasado", 3),
        (102, "Duvida sobre sabores de docinhos", 1),
        (103, "Pedido de torta de limao", 2),
        (104, "Vazamento no topper de bolo", 3),
    ]
    protocolos_existentes = {
        chamado["protocolo"] for chamado in fila_chamados + pilha_atendidos
    }
    carregados = 0

    for protocolo, descricao, prioridade in exemplos:
        if protocolo not in protocolos_existentes:
            abrir_chamado(protocolo, descricao, prioridade)
            protocolos_existentes.add(protocolo)
            carregados += 1

    return carregados


def exibir_status_sistema() -> None:
    """Exibe a fila de espera e o historico de atendimentos."""
    print("\n--- FILA DE ESPERA (FIFO) ---")
    if not fila_chamados:
        print("Fila de espera vazia.")
    else:
        for posicao, chamado in enumerate(fila_chamados, start=1):
            print(f"{posicao}. ", end="")
            exibir_chamado(chamado)

    print("\n--- HISTORICO DE ATENDIMENTOS (PILHA LIFO) ---")
    if not pilha_atendidos:
        print("Nenhum chamado no historico de atendimentos.")
    else:
        for posicao, chamado in enumerate(reversed(pilha_atendidos), start=1):
            print(f"{posicao}. ", end="")
            exibir_chamado(chamado)


def menu() -> None:
    """Executa o menu interativo da central de atendimento."""
    print("Seja bem-vindo à Central de Atendimento!")

    while True:
        print(
            "\n--- CENTRAL DE ATENDIMENTO / PEDIDOS ---\n"
            "1. Abrir chamado/pedido\n"
            "2. Atender proximo\n"
            "3. Desfazer ultimo atendimento\n"
            "4. Listar pendentes por urgencia\n"
            "5. Buscar chamado por protocolo\n"
            "6. Contar chamados por prioridade (recursivo)\n"
            "7. Exibir fila e historico\n"
            "8. Carregar dados de exemplo\n"
            "0. Sair"
        )
        opcao = input("Escolha uma opcao: ").strip()

        if opcao == "1":
            protocolo = ler_inteiro("Numero do protocolo: ")
            descricao = input("Descricao do pedido/problema: ")
            prioridade = ler_prioridade(
                "Prioridade (1-Baixa, 2-Media, 3-Alta): "
            )
            try:
                abrir_chamado(protocolo, descricao, prioridade)
            except ValueError as erro:
                print(f"Erro: {erro}")
            else:
                print("Chamado registrado com sucesso!")

        elif opcao == "2":
            chamado = atender_proximo()
            if chamado is None:
                print("Nenhum chamado pendente na fila.")
            else:
                print("Atendendo:")
                exibir_chamado(chamado)

        elif opcao == "3":
            chamado = desfazer_atendimento()
            if chamado is None:
                print("Nenhum atendimento para desfazer.")
            else:
                print("Atendimento desfeito e devolvido ao topo da fila:")
                exibir_chamado(chamado)

        elif opcao == "4":
            if not fila_chamados:
                print("Fila vazia.")
            else:
                print("\n--- PEDIDOS POR ORDEM DE URGENCIA ---")
                for chamado in ordenar_por_prioridade(fila_chamados):
                    exibir_chamado(chamado)

        elif opcao == "5":
            protocolo = ler_inteiro("Numero do protocolo para buscar: ")
            lista_ordenada = sorted(
                fila_chamados, key=lambda chamado: chamado["protocolo"]
            )
            resultado = buscar_protocolo(lista_ordenada, protocolo)
            if resultado is None:
                print("Protocolo nao encontrado na fila de pendentes.")
            else:
                print("Chamado encontrado:")
                exibir_chamado(resultado)

        elif opcao == "6":
            prioridade = ler_prioridade(
                "Prioridade para contar (1, 2 ou 3): "
            )
            total = contar_por_prioridade(fila_chamados, prioridade)
            print(f"Total de chamados com prioridade {prioridade}: {total}")

        elif opcao == "7":
            exibir_status_sistema()

        elif opcao == "8":
            total = carregar_dados_exemplo()
            print(f"{total} chamado(s) de exemplo carregado(s).")

        elif opcao == "0":
            print("Saindo do sistema...")
            break
        else:
            print("Opcao invalida. Tente novamente.")


if __name__ == "__main__":
    menu()
    
