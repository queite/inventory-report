from collections import Counter

from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def num_products_company(dict_list):
        return_str = "Produtos estocados por empresa:\n"

        company_names = [name["nome_da_empresa"] for name in dict_list]
        counter = Counter(company_names)

        for item in counter:
            return_str += f"- {item}: {counter.get(item)}\n"

        return return_str

    def generate(dict_list):
        return (
            f"{SimpleReport.generate(dict_list)}\n"
            f"{CompleteReport.num_products_company(dict_list)}"
        )
