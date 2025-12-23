import re
from collections import deque

def ler_producoes(entrada):
    """
    Aceita uma lista de strings ou uma única string multilinhas.
    Remove comentários após ':' e trata símbolos de vacuidade.
    """
    # Se a entrada for uma única string multilinhas, divide em lista
    if isinstance(entrada, str):
        linhas = entrada.strip().split('\n')
    else:
        linhas = entrada

    producoes = []
    for linha in linhas:
        # Remove comentários e espaços extras
        corpo = linha.split(":")[0].strip()
        if not corpo or "->" not in corpo:
            continue
        
        esquerdo, direito = corpo.split("->")
        esquerdo = esquerdo.strip()
        direito = direito.strip()

        # Tratamento de palavra vazia
        if direito in ["ε", "λ", "epsilon"]:
            direito = ""
        
        producoes.append((esquerdo, direito))
    return producoes

def parser_gramatica(producoes, alvo, max_passos=100):
    """
    Simula gramáticas de Tipo 0, 1, 2 e 3 usando BFS.
    """
    simbolo_inicial = "S"
    # O tamanho máximo permite que a string cresça um pouco antes de reduzir (Tipo 0)
    max_tamanho = max(len(alvo) + 10, 20) 

    fila = deque([(simbolo_inicial, [simbolo_inicial], 0)])
    visitados = {simbolo_inicial}

    while fila:
        atual, derivacao, passos = fila.popleft()

        # Sucesso
        if atual == alvo:
            print(f"Sim, pertence a L(G)")
            print("Derivação:", " ⇒ ".join(derivacao), "\n")
            return True

        if passos >= max_passos:
            continue

        for esq, dir_prod in producoes:
            # Requisito para Sensível ao Contexto: busca todas as ocorrências do lado esquerdo
            for match in re.finditer(re.escape(esq), atual):
                nova_string = atual[:match.start()] + dir_prod + atual[match.end():]
                
                # Regra de poda: evita explosão de memória e loops
                if len(nova_string) <= max_tamanho and nova_string not in visitados:
                    visitados.add(nova_string)
                    fila.append((nova_string, derivacao + [nova_string], passos + 1))

    print(f"Não, '{alvo}' não foi reconhecida nos limites do parser.\n")
    return False

# --- Execução dos seus Cenários ---
if __name__ == "__main__":
    # Teste FNC (Aninhamento)
    fnc_grammar = """
    L1 -> (
    R1 -> )
    L2 -> [
    R2 -> ]
    S -> SS
    S -> L1R1
    S -> L2R2
    S -> L1C1
    C1 -> SR1
    S -> L2C2
    C2 -> SR2
    """
    print("--- Teste Q3: FNC ---")
    parser_gramatica(ler_producoes(fnc_grammar), "([()])")

    # Teste Sensível ao Contexto (a^n b^n c^n)
    csg_grammar = """
    S -> aSBC
    S -> aBC
    CB -> BC
    aB -> ab
    bB -> bb
    bC -> bc
    cC -> cc
    """
    print("--- Teste Cenário 3: Sensível ao Contexto ---")
    parser_gramatica(ler_producoes(csg_grammar), "aabbcc")

    # Teste Tipo 0 (Irrestrita)
    unrestricted = """
    S -> abCde
    bCd -> X
    aXe -> afinal
    """
    print("--- Teste Cenário 4: Irrestrita ---")
    parser_gramatica(ler_producoes(unrestricted), "afinal")
