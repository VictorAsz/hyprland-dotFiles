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
    # Nome
    magia["nome"] = linhas[i]
    i += 1

    # Escola e círculo
    escola_circulo = linhas[i]
    i += 1
    escola_tipo_match = re.match(r'(.+?)\s*-\s*(\d+)º círculo', escola_circulo, re.IGNORECASE)
    if escola_tipo_match:
        magia["escola"] = escola_tipo_match.group(1).strip()
        magia["circulo"] = int(escola_tipo_match.group(2))
    
    # Campos info
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
            pass  # Ignorado por enquanto
        i += 1

    # Descrição até encontrar "+X PM"
    descricao = []
    while i < len(linhas) and not linhas[i].startswith("+"):
        descricao.append(linhas[i])
        i += 1
    magia["descricao"] = ' '.join(descricao)

    # Melhoramentos
    while i < len(linhas):
        if linhas[i].startswith('+'):
            m = re.match(r"\+(\d+)\s*PM\s*:\s*(.*)", linhas[i])
            if m:
                custo = int(m.group(1))
                efeito = m.group(2).strip()
                magia["melhoramentos"].append({
                    "custo": custo,
                    "efeito": efeito
                })
        i += 1

    return magia

def ler_magias_do_arquivo(caminho):
    with open(caminho, 'r', encoding='utf-8') as f:
        conteudo = f.read()
    
    blocos = re.split(r'\n{2,}', conteudo.strip())  # separa por 2+ quebras de linha
    magias = {}
    id_contador = 1

    for bloco in blocos:
        magia = parse_magia(bloco, id_contador)
        chave = magia["nome"].lower().replace(' ', '_')
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
