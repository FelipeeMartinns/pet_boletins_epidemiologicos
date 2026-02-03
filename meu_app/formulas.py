import pandas as pd

class Formulas:

    def taxa_de_incidencia_tb(casos_novos, populacao):
        casos_novos = int(casos_novos)
        populacao = int(populacao)

        if populacao == 0:
            return None

        return (casos_novos / populacao) * 100000


    def taxa_de_mortalidade_tb(obitos_por_tb, populacao):
        obitos_por_tb = int(obitos_por_tb)
        populacao = int(populacao)

        if populacao == 0:
            return None

        return (obitos_por_tb / populacao) * 100000


    def proporcao_de_casos_com_confirmacao_laboratorial(casos_confirmados_por_exame, total_de_casos):
        casos_confirmados_por_exame = int(casos_confirmados_por_exame)
        total_de_casos = int(total_de_casos)

        if total_de_casos == 0:
            return None

        return (casos_confirmados_por_exame / total_de_casos) * 100


    def proporcao_de_uso_do_teste_rapido_molecular_trm_tb(casos_com_TRM_realizado, numero_total_casos):
        casos_com_TRM_realizado = int(casos_com_TRM_realizado)
        numero_total_casos = int(numero_total_casos)

        if numero_total_casos == 0:
            return None

        return (casos_com_TRM_realizado / numero_total_casos) * 100


    def proporcao_de_cura(casos_curados, casos_encerrados):
        casos_curados = int(casos_curados)
        casos_encerrados = int(casos_encerrados)

        if casos_encerrados == 0:
            return None

        return (casos_curados / casos_encerrados) * 100


    def proporcao_de_abandono_tratamento(casos_abandono, casos_encerrados):
        casos_abandono = int(casos_abandono)
        casos_encerrados = int(casos_encerrados)

        if casos_encerrados == 0:
            return None

        return (casos_abandono / casos_encerrados) * 100


    def proporcao_retratamento(casos_retratamento, total_casos):
        casos_retratamento = int(casos_retratamento)
        total_casos = int(total_casos)

        if total_casos == 0:
            return None

        return (casos_retratamento / total_casos) * 100


    def proporcao_coinfeccao_tb_hiv(casos_tb_hiv_positivo, total_casos):
        casos_tb_hiv_positivo = int(casos_tb_hiv_positivo)
        total_casos = int(total_casos)

        if total_casos == 0:
            return None

        return (casos_tb_hiv_positivo / total_casos) * 100


    def casos_populacao_vulneraveis(situacao_rua, privadas_liberdade, indigenas):
        situacao_rua = int(situacao_rua)
        privadas_liberdade = int(privadas_liberdade)
        indigenas = int(indigenas)

        return situacao_rua + privadas_liberdade + indigenas


    def proporcao_de_contatos_investigados(contatos_examinados, contatos_registrados):
        contatos_examinados = int(contatos_examinados)
        contatos_registrados = int(contatos_registrados)

        if contatos_registrados == 0:
            return None

        return (contatos_examinados / contatos_registrados) * 100


    def casos_populacao_vulneraveis(situacao_rua,privadas_liberdade,indigenas):
        situacao_rua=int(situacao_rua)
        privadas_liberdade=int(privadas_liberdade)
        indigenas=int(indigenas)

        resultado=situacao_rua+privadas_liberdade+indigenas

        return resultado

    def proporcao_de_contatos_investigados(contatos_examinados,contatos_registrados):
        contatos_examinados=int(contatos_examinados)
        contatos_registrados=int(contatos_registrados)

        resultado=contatos_examinados/(contatos_registrados*100)

        return resultado



def pegar_valor(valor):
    ...