from datetime import datetime
from typing import Counter


class SimpleReport:
    def oldest_manufacture(dict_list):
        ordenar = sorted(dict_list, key=lambda row: row["data_de_fabricacao"])
        return ordenar[0]["data_de_fabricacao"]

    def closest_expiration(dict_list):
        curr_data = datetime.today().date()
        no_expired_products = [
            product
            for product in dict_list
            if product["data_de_validade"] > str(curr_data)
        ]

        ordenar = sorted(
            no_expired_products, key=lambda row: row["data_de_validade"]
        )
        return ordenar[0]["data_de_validade"]

    def more_products_company(dict_list):
        company_names = [name["nome_da_empresa"] for name in dict_list]
        counter = Counter(company_names)
        return max(counter, key=counter.get)

    def generate(dict_list):
        oldest_manufacture = SimpleReport.oldest_manufacture(dict_list)
        closest_expiration = SimpleReport.closest_expiration(dict_list)
        more_products_company = SimpleReport.more_products_company(dict_list)
        return (
            f"Data de fabricação mais antiga: {oldest_manufacture}\n"
            f"Data de validade mais próxima: {closest_expiration}\n"
            f"Empresa com mais produtos: {more_products_company}"
        )
