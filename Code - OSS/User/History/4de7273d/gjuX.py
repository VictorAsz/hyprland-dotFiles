import json
import re

def snake_case(text):
    return re.sub(r'\W+', '_', text.strip().lower()).strip('_')

def parse_magias_from_txt(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    blocos = re.split(r'\n(?=Convocação|Transmutação|Ilusão|Evocação|Abjuração|Necromancia|Adivinhação|Encantamento)', content)

    magias = {}
    id_counter = 1

    for bloco in blocos:
        linhas = bloco.strip().splitlines()
        if len(linhas) < 8:
            continue  # ignora blocos incompletos

        escola = linhas[0].strip()
        tipo_e_circulo = linhas[1].strip().split(' - ')
        tipo = tipo_e_circulo[0].strip()
        circulo = int(tipo_e_circulo[1].split('º')[0])

        info = {
            "execucao": linhas[3].split(':')[1].strip().capitalize(),
            "alcance": linhas[4].split(':')[1].strip().capitalize(),
            "duracao": linhas[5].split(':')[1].strip().capitalize(),
            "alvo": linhas[6].split(':')[1].strip(),
            "resistencia": linhas[7].split(':')[1].strip().capitalize()
        }

        # nome da magia é a primeira linha após "Publicação"
        for i, linha in enumerate(linhas):
            if linha.startswith('Publicação'):
                nome = linhas[i+1].strip()
                descricao_e_melhoramentos = "\n".join(linhas[i+2:]).strip()
                break
        else:
            continue

        # separa melhoramentos usando regex de "+X PM:"
        partes = re.split(r'\n\+(\d+)\s*PM:', descricao_e_melhoramentos)
        descricao = partes[0].strip()
        melhoramentos = []
        for i in range(1, len(partes), 2):
            custo = int(partes[i])
            efeito = parts[i+1].strip().replace('\n', ' ')
            melhoramentos.append({
                "custo": custo,
                "efeito": efeito
            })

        magias[snake_case(nome)] = {
            "id": id_counter,
            "nome": nome,
            "tipo": tipo,
            "circulo": circulo,
            "escola": escola,
            "info": info,
            "descricao": descricao,
            "truque": {
                "existe": False,
                "descricao": ""
            },
            "melhoramentos": melhoramentos
        }

        id_counter += 1

    return magias

if __name__ == '__main__':
    entrada = 'magias.txt'
    saida = 'magias.json'
    magias = parse_magias_from_txt(entrada)
    with open(saida, 'w', encoding='utf-8') as f:
        json.dump(magias, f, ensure_ascii=False, indent=2)
    print(f'{len(magias)} magias convertidas e salvas em {saida}.')
import json
import re

def snake_case(text):
    return re.sub(r'\W+', '_', text.strip().lower()).strip('_')

def parse_magias_from_txt(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    blocos = re.split(r'\n(?=Convocação|Transmutação|Ilusão|Evocação|Abjuração|Necromancia|Adivinhação|Encantamento)', content)

    magias = {}
    id_counter = 1

    for bloco in blocos:
        linhas = bloco.strip().splitlines()
        if len(linhas) < 8:
            continue  # ignora blocos incompletos

        escola = linhas[0].strip()
        tipo_e_circulo = linhas[1].strip().split(' - ')
        tipo = tipo_e_circulo[0].strip()
        circulo = int(tipo_e_circulo[1].split('º')[0])

        info = {
            "execucao": linhas[3].split(':')[1].strip().capitalize(),
            "alcance": linhas[4].split(':')[1].strip().capitalize(),
            "duracao": linhas[5].split(':')[1].strip().capitalize(),
            "alvo": linhas[6].split(':')[1].strip(),
            "resistencia": linhas[7].split(':')[1].strip().capitalize()
        }

        # nome da magia é a primeira linha após "Publicação"
        for i, linha in enumerate(linhas):
            if linha.startswith('Publicação'):
                nome = linhas[i+1].strip()
                descricao_e_melhoramentos = "\n".join(linhas[i+2:]).strip()
                break
        else:
            continue

        # separa melhoramentos usando regex de "+X PM:"
        partes = re.split(r'\n\+(\d+)\s*PM:', descricao_e_melhoramentos)
        descricao = partes[0].strip()
        melhoramentos = []
        for i in range(1, len(partes), 2):
            custo = int(partes[i])
            efeito = parts[i+1].strip().replace('\n', ' ')
            melhoramentos.append({
                "custo": custo,
                "efeito": efeito
            })

        magias[snake_case(nome)] = {
            "id": id_counter,
            "nome": nome,
            "tipo": tipo,
            "circulo": circulo,
            "escola": escola,
            "info": info,
            "descricao": descricao,
            "truque": {
                "existe": False,
                "descricao": ""
            },
            "melhoramentos": melhoramentos
        }

        id_counter += 1

    return magias

if __name__ == '__main__':
    entrada = 'magias.txt'
    saida = 'magias.json'
    magias = parse_magias_from_txt(entrada)
    with open(saida, 'w', encoding='utf-8') as f:
        json.dump(magias, f, ensure_ascii=False, indent=2)
    print(f'{len(magias)} magias convertidas e salvas em {saida}.')
