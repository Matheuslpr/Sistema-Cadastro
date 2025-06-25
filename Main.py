import json
import os

arquivos = {
    "estudantes": "estudantes.json",
    "professores": "professores.json",
    "disciplinas": "disciplinas.json",
    "turmas": "turmas.json",
    "matriculas": "matriculas.json"

}

CAMPOS = {
    "estudantes": {"Código": int, "Nome": str, "CPF": str},
    "professores": {"Código": int, "Nome": str, "CPF": str},
    "disciplinas": {"Código": int, "Nome": str},
    "turmas": {"Código": int, "Código Professor": int, "Código Disciplina": int},
    "matriculas": {"Código Turma": int, "Código Estudante": int}
}


# Funções
def carregar_dados(entidade):
    if not os.path.exists(arquivos[entidade]):
        return []
    with open(arquivos[entidade], 'r', encoding='utf-8') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


def salvar_dados(entidade, dados):
    with open(arquivos[entidade], 'w', encoding='utf-8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)


def codigo_existe(entidade, codigo):
    return any(str(item['Código']) == str(codigo) for item in carregar_dados(entidade))


def mostrar_menu(titulo, opcoes):
    print(f"\n====== {titulo} ======")
    for i, opcao in enumerate(opcoes, 1):
        print(f"({i}) {opcao}")
    try:
        return int(input("Digite o número da opção: "))
    except ValueError:
        return -1


def incluir(entidade):
    dados = carregar_dados(entidade)
    novo = {}

    for campo, tipo in CAMPOS[entidade].items():
        while True:
            valor = input(f"{campo}: ").strip()
            if not valor:
                print("Campo obrigatório.")
                continue
            if tipo == int:
                if not valor.isdigit():
                    print("O código deve ser um número, Digite novamente!")
                    continue
                valor = int(valor)
                if campo == 'Código' and codigo_existe(entidade, valor):
                    print("O código já existe.")
                    continue
            novo[campo] = valor
            break

    dados.append(novo)
    salvar_dados(entidade, dados)
    print("Adicionado com sucesso.")


def listar(entidade):
    dados = carregar_dados(entidade)
    if not dados:
        print("Nenhum registro encontrado.")
        return

    for item in dados:
        print(" | ".join(f"{k}: {v}" for k, v in item.items()))


def atualizar(entidade):
    dados = carregar_dados(entidade)
    listar(entidade)
    if not dados:
        return

    codigo = input("Digite o código que deseja editar: ").strip()
    if not codigo:
        return

    for item in dados:
        if str(item['Código']) == codigo:
            for campo, tipo in CAMPOS[entidade].items():
                if campo == 'Código':
                    continue
                novo = input(f"{campo} ({item[campo]}): ").strip()
                if novo:
                    if tipo == int and not novo.isdigit():
                        print("Digite um valor valido.")
                        continue
                    item[campo] = int(novo) if tipo == int else novo
            salvar_dados(entidade, dados)
            print("Registro atualizado.")
            return
    print("Código não foi encontrado.")


def excluir(entidade):
    dados = carregar_dados(entidade)
    listar(entidade)
    if not dados:
        return

    codigo = input("Digite o código que  deseja excluir:  ").strip()
    if not codigo:
        return

    for i, item in enumerate(dados):
        if str(item['Código']) == codigo:
            dados.pop(i)
            salvar_dados(entidade, dados)
            print("Registro excluído.")
            return
    print("Código não encontrado.")


def validar_relacao(entidade, codigo):
    if not codigo_existe(entidade, codigo):
        print(f"{entidade.capitalize()} não encontrado.")
        return False
    return True


def incluir_turma():
    dados = carregar_dados("turmas")
    try:
        codigo = int(input("Código da Turma: "))
        if codigo_existe("turmas", codigo):
            print("Turma já existe!")
            return

        prof = int(input("Código do Professor: "))
        disc = int(input("Código da Disciplina: "))

        if validar_relacao("professores", prof) and validar_relacao("disciplinas", disc):
            dados.append({"Código": codigo, "Código Professor": prof, "Código Disciplina": disc})
            salvar_dados("turmas", dados)
            print("Turma criada.")
    except ValueError:
        print("Digite números válidos.")


def incluir_matricula():
    dados = carregar_dados("matriculas")
    try:
        turma = int(input("Código da Turma: "))
        estudante = int(input("Código do Estudante: "))

        if any(m['Código Turma'] == turma and m['Código Estudante'] == estudante for m in dados):
            print("Matrícula já existe")
            return

        if validar_relacao("turmas", turma) and validar_relacao("estudantes", estudante):
            dados.append({"Código Turma": turma, "Código Estudante": estudante})
            salvar_dados("matriculas", dados)
            print("Matrícula criada!")
    except ValueError:
        print("Digite números válidos")

# Loop

def main():
    while True:
        loop = mostrar_menu("Menu Principal",
                          ["Estudantes", "Professores", "Disciplinas", "Turmas", "Matrículas", "Sair"])

        if loop == 6:
            print("Saindo do sistema...")
            break

        entidades = ["estudantes", "professores", "disciplinas", "turmas", "matriculas"]
        entidade = entidades[loop - 1]

        while True:
            sub_opcao = mostrar_menu("Operações",
                                  ["Incluir", "Listar", "Atualizar", "Excluir", "Voltar"])

            if sub_opcao == 5:
                break
            elif sub_opcao == 1:
                if entidade == "turmas":
                    incluir_turma()
                elif entidade == "matriculas":
                    incluir_matricula()
                else:
                    incluir(entidade)
            elif sub_opcao == 2:
                listar(entidade)
            elif sub_opcao == 3:
                atualizar(entidade)
            elif sub_opcao == 4:
                excluir(entidade)


if __name__ == "__main__":
    main()