import json
import re

def parse_magias_from_txt(conteudo):
    blocos = re.split(r'\n{2,}', conteudo.strip())
    magias = {}
    id_counter = 1

    i = 0
    while i < len(blocos):
        cabecalho = blocos[i].strip().splitlines()
        descricao_linhas = []
        melhoramentos = []

        # Skip blocos incompletos
        if len(cabecalho) < 2 or '-' not in cabecalho[1]:
            i += 1
            continue

        escola = cabecalho[0].strip().capitalize()
        tipo, circulo = [p.strip() for p in cabecalho[1].split('-')]
        nome = blocos[i + 1].strip().splitlines()[0].strip()
        nome_id = nome.lower().replace(' ', '_')

        info_raw = blocos[i + 1].splitlines()[1:7]
        info = {}
        for linha in info_raw:
            if ':' in linha:
                chave, valor = linha.split(':', 1)
                chave = chave.strip().lower()
                valor = valor.strip().capitalize()
                if chave.startswith("exec"):
                    info["execucao"] = valor
                elif chave == "alcance":
                    info["alcance"] = valor
                elif chave in ["alvo", "área", "alvo/área/efeito"]:
                    info["alvo"] = valor
                elif chave == "duração":
                    info["duracao"] = valor
                elif chave == "resistência":
                    info["resistencia"] = valor

        # Descrição e melhoramentos
        descricao_linhas = []
        i += 2
        while i < len(blocos) and not re.match(r'^[A-Z][a-z]+$', blocos[i].strip()):
            for linha in blocos[i].strip().splitlines():
                if re.match(r'^\+\d+ PM:', linha.strip()):
                    custo = int(re.search(r'\+(\d+) PM', linha).group(1))
                    efeito = linha.split(':', 1)[1].strip().capitalize()
                    melhoramentos.append({"custo": custo, "efeito": efeito})
                else:
                    descricao_linhas.append(linha.strip())
            i += 1

        magias[nome_id] = {
            "id": id_counter,
            "nome": nome,
            "tipo": tipo,
            "circulo": int(circulo[0]),
            "escola": escola,
            "info": info,
            "descricao": " ".join(descricao_linhas).strip(),
            "truque": {
                "existe": False,
                "descricao": ""
            },
            "melhoramentos": melhoramentos
        }
        id_counter += 1

    return magias

if __name__ == "__main__":
    with open("magias.txt", "r", encoding="utf-8") as f:
        conteudo = f.read()

    magias = parse_magias_from_txt(conteudo)

    with open("saida.json", "w", encoding="utf-8") as f:
        json.dump(magias, f, ensure_ascii=False, indent=2)

    print("Arquivo 'saida.json' criado com sucesso.")
