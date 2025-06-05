import re
import json

def parse_magias(texto):
    magias = []
    blocos = re.split(r'\n(?=Convocação)', texto.strip())
    for bloco in blocos:
        linhas = bloco.strip().split('\n')
        if not linhas:
            continue

        # Identificar escola e tipo
        escola_tipo = linhas[0].strip()
        if ' - ' in escola_tipo:
            escola, tipo_circulo = escola_tipo.split(' - ')
            tipo, circulo_str = tipo_circulo.strip().split('º')
            circulo = int(circulo_str.strip().split()[0])
        else:
            escola = escola_tipo.strip()
            tipo = ''
            circulo = 0

        # Inicializar campos
        info = {
            "execucao": "",
            "alcance": "",
            "duracao": "",
            "alvo": "",
            "resistencia": ""
        }
        descricao = ""
        melhoramentos = []

        i = 1
        # Extrair informações
        while i < len(linhas):
            linha = linhas[i].strip()
            if linha.startswith("Execução:"):
                info["execucao"] = linha.split(":", 1)[1].strip()
            elif linha.startswith("Alcance:"):
                info["alcance"] = linha.split(":", 1)[1].strip()
            elif linha.startswith("Duração:"):
                info["duracao"] = linha.split(":", 1)[1].strip()
            elif linha.startswith("Alvo/Área/Efeito:"):
                info["alvo"] = linha.split(":", 1)[1].strip()
            elif linha.startswith("Resistência:"):
                info["resistencia"] = linha.split(":", 1)[1].strip()
            elif linha.startswith("Publicação:"):
                publicacao = linha.split(":", 1)[1].strip()
            elif linha == "":
                pass
            else:
                break
            i += 1

        # Nome da magia
        nome = linhas[i].strip()
        i += 1

        # Descrição e melhoramentos
        descricao_linhas = []
        while i < len(linhas):
            linha = linhas[i].strip()
            if re.match(r'^\+\d+ PM:', linha):
                partes = linha.split(":", 1)
                custo = int(partes[0].strip().replace("+", "").replace("PM", "").strip())
                efeito = partes[1].strip()
                melhoramentos.append({"custo": custo, "efeito": efeito})
            else:
                descricao_linhas.append(linha)
            i += 1
        descricao = " ".join(descricao_linhas)

        magia = {
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
        magias.append(magia)
    return magias

# Exemplo de uso
entrada = """
Convocação
Arcana - 1º círculo

Execução:
    padrão 
Alcance:
    pessoal 
Duração:
    sustentada 
Alvo/Área/Efeito:
    açoite de chamas criado em sua mão (veja texto) 
Resistência:
    Reflexos reduz parcial 
Publicação:
    Ameaças de Arton 

Açoite Flamejante

Um açoite de fogo surge em uma de suas mãos com a qual possa empunhar uma arma (essa mão fica ocupada pela duração da magia). Você pode usar uma ação padrão para causar 2d6 pontos de dano de fogo com o açoite em uma criatura em alcance curto e deixá-la em chamas e enredada enquanto estiver em chamas dessa forma. Passar na resistência reduz o dano à metade e evita as chamas.

+2 PM: muda a execução para movimento.

+2 PM: muda o dano para 4d6. Requer 2° círculo.

+5 PM: muda o dano para 6d6. Requer 3° círculo.
"""

magias = parse_magias(entrada)
print(json.dumps(magias, indent=4, ensure_ascii=False))
