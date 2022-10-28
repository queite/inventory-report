from datetime import datetime
from typing import Counter


class SimpleReport:
    def fabricacao_mais_antiga(list_dict):
        ordenar = sorted(list_dict, key=lambda row: row["data_de_fabricacao"])
        return ordenar[0]["data_de_fabricacao"]

    def validade_mais_proxima(list_dict):
        curr_data = datetime.today().date()
        no_expired_products = [
            product
            for product in list_dict
            if product["data_de_validade"] > str(curr_data)
        ]

        ordenar = sorted(
            no_expired_products, key=lambda row: row["data_de_validade"]
        )
        return ordenar[0]["data_de_validade"]

    def empresa_mais_produtos(list_dict):
        company_names = [name["nome_da_empresa"] for name in list_dict]
        counter = Counter(company_names)
        return max(counter, key=counter.get)

    def generate(list_dict):
        fabricacao_mais_antiga = SimpleReport.fabricacao_mais_antiga(list_dict)
        validade_mais_proxima = SimpleReport.validade_mais_proxima(list_dict)
        empresa_mais_produtos = SimpleReport.empresa_mais_produtos(list_dict)
        return (
            f"Data de fabricação mais antiga: {fabricacao_mais_antiga}\n"
            f"Data de validade mais próxima: {validade_mais_proxima}\n"
            f"Empresa com mais produtos: {empresa_mais_produtos}"
        )
