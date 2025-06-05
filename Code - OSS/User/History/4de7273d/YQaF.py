import json
import re

def parse_magia(bloco, id_inicial=1):
    linhas = [linha.strip() for linha in bloco.strip().split('\n') if linha.strip()]
    
    if len(linhas) < 2:
        print(f"Aviso: bloco incompleto ignorado:\n{bloco[:60]}...\n")
        return None

    magia = {
        "id": id_inicial,
        "nome": "",
        "tipo": "",
        "circulo": 0,
        "escola": "",
        "info": {
            "execucao": "",
            "alcance": "",
            "alvo": "",
            "duracao": "",
            "resistencia": ""
        },
        "descricao": "",
        "truque": {
            "existe": False,
            "descricao": ""
        },
        "melhoramentos": []
    }

    i = 0
    magia["nome"] = linhas[i]
    i += 1

    escola_circulo = linhas[i]
    i += 1
    escola_tipo_match = re.match(r'(.+?)\s*-\s*(\d+)º círculo', escola_circulo, re.IGNORECASE)
    if escola_tipo_match:
        magia["escola"] = escola_tipo_match.group(1).strip()
        magia["circulo"] = int(escola_tipo_match.group(2))

    while i < len(linhas) and ':' in linhas[i]:
        chave, valor = linhas[i].split(':', 1)
        chave = chave.strip().lower()
        valor = valor.strip()

        if chave.startswith("execução"):
            magia["info"]["execucao"] = valor
        elif chave.startswith("alcance"):
            magia["info"]["alcance"] = valor
        elif chave.startswith("alvo") or chave.startswith("área") or chave.startswith("efeito"):
            magia["info"]["alvo"] = valor
        elif chave.startswith("duração"):
            magia["info"]["duracao"] = valor
        elif chave.startswith("resistência"):
            magia["info"]["resistencia"] = valor
        elif chave.startswith("publicação"):
            pass  # Ignora
        i += 1

    descricao = []
    while i < len(linhas) and not re.match(r'^\+\d+\s*PM\s*:', linhas[i]):
        descricao.append(linhas[i])
        i += 1
    magia["descricao"] = ' '.join(descricao)

    while i < len(linhas):
        if re.match(r'^\+\d+\s*PM\s*:', linhas[i]):
            m = re.match(r'^\+(\d+)\s*PM\s*:\s*(.*)', linhas[i])
            if m:
                custo = int(m.group(1))
                efeito = m.group(2).strip()

                # Agrupa linhas do efeito que continuarem embaixo
                i += 1
                while i < len(linhas) and not re.match(r'^\+\d+\s*PM\s*:', linhas[i]):
                    efeito += ' ' + linhas[i]
                    i += 1
                magia["melhoramentos"].append({
                    "custo": custo,
                    "efeito": efeito.strip()
                })
                continue  # já avançamos o índice no loop interno
        i += 1

    return magia

def ler_magias_do_arquivo(caminho):
    with open(caminho, 'r', encoding='utf-8') as f:
        conteudo = f.read()

    blocos = re.split(r'\n{2,}', conteudo.strip())
    magias = {}
    id_contador = 1

    for bloco in blocos:
        magia = parse_magia(bloco, id_contador)
        if not magia:
            continue  # pula blocos inválidos
        chave = magia["nome"].lower().replace(' ', '_')
        if chave in magias:
            continue  # ignora duplicatas
        magias[chave] = magia
        id_contador += 1

    return magias


def salvar_json(dados, caminho_saida):
    with open(caminho_saida, 'w', encoding='utf-8') as f:
        json.dump(dados, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    caminho_txt = "magias.txt"
    caminho_json = "magias_convertidas.json"
    magias = ler_magias_do_arquivo(caminho_txt)
    salvar_json(magias, caminho_json)
    print(f"{len(magias)} magias convertidas com sucesso para {caminho_json}")
import json
import re

def parse_magia(bloco, id_inicial=1):
    linhas = [linha.strip() for linha in bloco.strip().split('\n') if linha.strip()]

    magia = {
        "id": id_inicial,
        "nome": "",
        "tipo": "",
        "circulo": 0,
        "escola": "",
        "info": {
            "execucao": "",
            "alcance": "",
            "alvo": "",
            "duracao": "",
            "resistencia": ""
        },
        "descricao": "",
        "truque": {
            "existe": False,
            "descricao": ""
        },
        "melhoramentos": []
    }

    i = 0
    magia["nome"] = linhas[i]
    i += 1

    escola_circulo = linhas[i]
    i += 1
    escola_tipo_match = re.match(r'(.+?)\s*-\s*(\d+)º círculo', escola_circulo, re.IGNORECASE)
    if escola_tipo_match:
        magia["escola"] = escola_tipo_match.group(1).strip()
        magia["circulo"] = int(escola_tipo_match.group(2))

    while i < len(linhas) and ':' in linhas[i]:
        chave, valor = linhas[i].split(':', 1)
        chave = chave.strip().lower()
        valor = valor.strip()

        if chave.startswith("execução"):
            magia["info"]["execucao"] = valor
        elif chave.startswith("alcance"):
            magia["info"]["alcance"] = valor
        elif chave.startswith("alvo") or chave.startswith("área") or chave.startswith("efeito"):
            magia["info"]["alvo"] = valor
        elif chave.startswith("duração"):
            magia["info"]["duracao"] = valor
        elif chave.startswith("resistência"):
            magia["info"]["resistencia"] = valor
        elif chave.startswith("publicação"):
            pass  # Ignora
        i += 1

    descricao = []
    while i < len(linhas) and not re.match(r'^\+\d+\s*PM\s*:', linhas[i]):
        descricao.append(linhas[i])
        i += 1
    magia["descricao"] = ' '.join(descricao)

    while i < len(linhas):
        if re.match(r'^\+\d+\s*PM\s*:', linhas[i]):
            m = re.match(r'^\+(\d+)\s*PM\s*:\s*(.*)', linhas[i])
            if m:
                custo = int(m.group(1))
                efeito = m.group(2).strip()

                # Agrupa linhas do efeito que continuarem embaixo
                i += 1
                while i < len(linhas) and not re.match(r'^\+\d+\s*PM\s*:', linhas[i]):
                    efeito += ' ' + linhas[i]
                    i += 1
                magia["melhoramentos"].append({
                    "custo": custo,
                    "efeito": efeito.strip()
                })
                continue  # já avançamos o índice no loop interno
        i += 1

    return magia

def ler_magias_do_arquivo(caminho):
    with open(caminho, 'r', encoding='utf-8') as f:
        conteudo = f.read()

    blocos = re.split(r'\n{2,}', conteudo.strip())
    magias = {}
    id_contador = 1

    for bloco in blocos:
        magia = parse_magia(bloco, id_contador)
        chave = magia["nome"].lower().replace(' ', '_')
        if chave in magias:
            continue  # ignora duplicatas
        magias[chave] = magia
        id_contador += 1

    return magias

def salvar_json(dados, caminho_saida):
    with open(caminho_saida, 'w', encoding='utf-8') as f:
        json.dump(dados, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    caminho_txt = "magias.txt"
    caminho_json = "magias_convertidas.json"
    magias = ler_magias_do_arquivo(caminho_txt)
    salvar_json(magias, caminho_json)
    print(f"{len(magias)} magias convertidas com sucesso para {caminho_json}")
import json
import re

def parse_magia(bloco, id_inicial=1):
    linhas = [linha.strip() for linha in bloco.strip().split('\n') if linha.strip()]

    magia = {
        "id": id_inicial,
        "nome": "",
        "tipo": "",
        "circulo": 0,
        "escola": "",
        "info": {
            "execucao": "",
            "alcance": "",
            "alvo": "",
            "duracao": "",
            "resistencia": ""
        },
        "descricao": "",
        "truque": {
            "existe": False,
            "descricao": ""
        },
        "melhoramentos": []
    }

    i = 0
    magia["nome"] = linhas[i]
    i += 1

    escola_circulo = linhas[i]
    i += 1
    escola_tipo_match = re.match(r'(.+?)\s*-\s*(\d+)º círculo', escola_circulo, re.IGNORECASE)
    if escola_tipo_match:
        magia["escola"] = escola_tipo_match.group(1).strip()
        magia["circulo"] = int(escola_tipo_match.group(2))

    while i < len(linhas) and ':' in linhas[i]:
        chave, valor = linhas[i].split(':', 1)
        chave = chave.strip().lower()
        valor = valor.strip()

        if chave.startswith("execução"):
            magia["info"]["execucao"] = valor
        elif chave.startswith("alcance"):
            magia["info"]["alcance"] = valor
        elif chave.startswith("alvo") or chave.startswith("área") or chave.startswith("efeito"):
            magia["info"]["alvo"] = valor
        elif chave.startswith("duração"):
            magia["info"]["duracao"] = valor
        elif chave.startswith("resistência"):
            magia["info"]["resistencia"] = valor
        elif chave.startswith("publicação"):
            pass  # Ignora
        i += 1

    descricao = []
    while i < len(linhas) and not re.match(r'^\+\d+\s*PM\s*:', linhas[i]):
        descricao.append(linhas[i])
        i += 1
    magia["descricao"] = ' '.join(descricao)

    while i < len(linhas):
        if re.match(r'^\+\d+\s*PM\s*:', linhas[i]):
            m = re.match(r'^\+(\d+)\s*PM\s*:\s*(.*)', linhas[i])
            if m:
                custo = int(m.group(1))
                efeito = m.group(2).strip()

                # Agrupa linhas do efeito que continuarem embaixo
                i += 1
                while i < len(linhas) and not re.match(r'^\+\d+\s*PM\s*:', linhas[i]):
                    efeito += ' ' + linhas[i]
                    i += 1
                magia["melhoramentos"].append({
                    "custo": custo,
                    "efeito": efeito.strip()
                })
                continue  # já avançamos o índice no loop interno
        i += 1

    return magia

def ler_magias_do_arquivo(caminho):
    with open(caminho, 'r', encoding='utf-8') as f:
        conteudo = f.read()

    blocos = re.split(r'\n{2,}', conteudo.strip())
    magias = {}
    id_contador = 1

    for bloco in blocos:
        magia = parse_magia(bloco, id_contador)
        chave = magia["nome"].lower().replace(' ', '_')
        if chave in magias:
            continue  # ignora duplicatas
        magias[chave] = magia
        id_contador += 1

    return magias

def salvar_json(dados, caminho_saida):
    with open(caminho_saida, 'w', encoding='utf-8') as f:
        json.dump(dados, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    caminho_txt = "magias.txt"
    caminho_json = "magias_convertidas.json"
    magias = ler_magias_do_arquivo(caminho_txt)
    salvar_json(magias, caminho_json)
    print(f"{len(magias)} magias convertidas com sucesso para {caminho_json}")
