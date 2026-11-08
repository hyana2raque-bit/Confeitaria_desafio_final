# 🍰 Central de Atendimento & Gestão de Pedidos (Confeitaria)

Sistema de suporte e atendimento desenvolvido em Python para uma confeitaria, aplicando estruturas de dados fundamentais (Filas, Pilhas), algoritmos de ordenação, pesquisa binária e recursividade.

---

## 🚀 Funcionalidades Principais

* **Gestão de Fila (FIFO):** Registo e atendimento ordenado de novos pedidos ou chamados de suporte.
* **Histórico com Pilha (LIFO):** Permite desfazer o último atendimento realizado, devolvendo o pedido à primeira posição da fila sem perder a vez de espera.
* **Ordenação por Prioridade (Insertion Sort):** Lista os chamados pendentes de forma decrescente por grau de urgência (mantendo a estabilidade da ordem de chegada).
* **Busca Binária:** Pesquisa rápida de chamados através do número de protocolo.
* **Contagem Recursiva:** Conta a quantidade de chamados com uma determinada prioridade utilizando programação recursiva (sem laços de repetição).
* **Dados de Exemplo:** Opção rápida para carregar dados iniciais e testar o sistema de imediato.

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3.x
* **Conceitos aplicados:** 
  * Estruturas de Dados Lineares (Listas utilizadas como Filas e Pilhas)
  * Algoritmos de Ordenação (*Insertion Sort*)
  * Algoritmos de Pesquisa (*Binary Search*)
  * Funções Recursivas

---

## 📂 Estrutura do Projeto

```text
central-atendimento/
│
├── desafio_teste_final.py    # Código principal da aplicação
├── .gitignore                # Ficheiros ignorados pelo Git
└── README.md                 # Documentação do projeto
