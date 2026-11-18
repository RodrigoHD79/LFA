import re
import sys
from pathlib import Path

if getattr(sys, "frozen", False):
    PASTA_PROGRAMA = Path(sys.executable).parent
else:
    PASTA_PROGRAMA = Path(__file__).parent

ARQUIVO_PALAVRAS = PASTA_PROGRAMA / "palavras_suspeitas.txt"

def carregar_palavras():
    """Carrega as palavras cadastradas do arquivo, se ele existir."""
    if not ARQUIVO_PALAVRAS.exists():
        return []

    with ARQUIVO_PALAVRAS.open("r", encoding="utf-8") as arquivo:
        return [
            linha.strip().lower()
            for linha in arquivo
            if linha.strip()
        ]


def salvar_palavras(palavras):
    """Salva todas as palavras cadastradas no arquivo."""
    with ARQUIVO_PALAVRAS.open("w", encoding="utf-8") as arquivo:
        for palavra in palavras:
            arquivo.write(palavra + "\n")


def analisar_mensagem(mensagem, palavras_cadastradas):
    """Analisa a mensagem e devolve a classificação e os motivos."""
    mensagem = mensagem.lower()
    motivos = []

    # Regras fixas da base de conhecimento

    if "senha" in mensagem:
        motivos.append("A mensagem menciona uma senha.")

    if "prêmio" in mensagem or "premio" in mensagem:
        motivos.append("A mensagem fala de um prêmio.")

    if "urgente" in mensagem:
        motivos.append("A mensagem usa a palavra 'urgente'.")

    if "bloqueada" in mensagem:
        motivos.append("A mensagem fala de uma conta bloqueada.")

    if (
        "dados bancários" in mensagem
        or "dados bancarios" in mensagem
        or "conta bancária" in mensagem
        or "conta bancaria" in mensagem
    ):
        motivos.append("A mensagem menciona dados bancários.")

    if "pagamento urgente" in mensagem or "pagar urgente" in mensagem:
        motivos.append("A mensagem pede um pagamento urgente.")

    links = re.findall(r"https?://\S+|www\.\S+", mensagem)

    if len(links) >= 3:
        motivos.append("A mensagem contém três ou mais links.")

    # Verifica as palavras e expressões cadastradas pelo usuário

    for palavra in palavras_cadastradas:
        if palavra in mensagem:
            motivos.append(
                f"A mensagem contém a palavra suspeita cadastrada: '{palavra}'."
            )

    # Motor de inferência: decide a classificação

    if motivos:
        classificacao = "indesejada"
    else:
        classificacao = "suspeita"
        motivos.append("Nenhuma regra conhecida foi encontrada.")

    return classificacao, motivos


def cadastrar_palavras(palavras_cadastradas):
    """Cadastra uma ou mais palavras antes de voltar ao menu."""
    while True:
        palavra = input(
            "\nDigite a palavra ou expressão suspeita: "
        ).strip().lower()

        if not palavra:
            print("Nenhuma palavra foi cadastrada: o campo estava vazio.")
        elif palavra in palavras_cadastradas:
            print(f"'{palavra}' já está cadastrada.")
        else:
            palavras_cadastradas.append(palavra)
            salvar_palavras(palavras_cadastradas)
            print(f"'{palavra}' foi cadastrada e salva.")

        while True:
            resposta = input(
                "\nDeseja cadastrar uma nova palavra?\n"
                "1 - Sim\n"
                "2 - Não\n"
                "Digite 1, 2, sim ou não: "
            ).strip().lower()

            if resposta in ("1", "sim"):
                break  # Volta a pedir uma palavra

            if resposta in ("2", "não", "nao"):
                return  # Volta ao menu principal

            print("Resposta inválida. Digite 1, 2, sim ou não.")


def mostrar_palavras(palavras_cadastradas):
    """Mostra as palavras cadastradas."""
    if not palavras_cadastradas:
        print("\nAinda não há palavras cadastradas.")
        return

    print("\nPalavras suspeitas cadastradas:")
    for palavra in palavras_cadastradas:
        print(f"- {palavra}")


def excluir_palavra(palavras_cadastradas):
    """Exclui uma palavra cadastrada e atualiza o arquivo."""
    if not palavras_cadastradas:
        print("\nNão há palavras cadastradas para excluir.")
        return

    mostrar_palavras(palavras_cadastradas)

    palavra = input(
        "\nDigite a palavra ou expressão que deseja excluir: "
    ).strip().lower()

    if palavra in palavras_cadastradas:
        palavras_cadastradas.remove(palavra)
        salvar_palavras(palavras_cadastradas)
        print(f"'{palavra}' foi excluída e removida do arquivo.")
    else:
        print(f"'{palavra}' não foi encontrada na lista.")


# Carrega as palavras salvas quando o programa começa

palavras_cadastradas = carregar_palavras()
print(f"{len(palavras_cadastradas)} palavra(s) suspeita(s) carregada(s).")


# Menu principal

while True:
    print("\n=== FILTRADOR DE MENSAGENS ===")
    print("1 - Analisar uma mensagem")
    print("2 - Cadastrar palavra(s) suspeita(s)")
    print("3 - Mostrar palavras cadastradas")
    print("4 - Excluir uma palavra cadastrada")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        mensagem = input("\nDigite a mensagem para analisar: ")

        classificacao, motivos = analisar_mensagem(
            mensagem,
            palavras_cadastradas
        )

        print(f"\nClassificação: {classificacao}")

        for motivo in motivos:
            print(f"Motivo: {motivo}")

        if classificacao == "suspeita":
            print("A mensagem precisa ser verificada por uma pessoa.")

    elif opcao == "2":
        cadastrar_palavras(palavras_cadastradas)

    elif opcao == "3":
        mostrar_palavras(palavras_cadastradas)

    elif opcao == "4":
        excluir_palavra(palavras_cadastradas)

    elif opcao == "5":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida. Escolha um número de 1 a 5.")