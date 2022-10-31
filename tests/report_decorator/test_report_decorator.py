from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport

dict_list_mock = [
    {
        "id": "1",
        "nome_do_produto": "Nicotine Polacrilex",
        "nome_da_empresa": "Target Corporation",
        "data_de_fabricacao": "2021-02-18",
        "data_de_validade": "2023-09-17",
        "numero_de_serie": "CR25 1551 4467 2549 4402 1",
        "instrucoes_de_armazenamento": "instrucao 1",
    },
    {
        "id": "2",
        "nome_do_produto": "fentanyl citrate",
        "nome_da_empresa": "Target Corporation",
        "data_de_fabricacao": "2020-12-06",
        "data_de_validade": "2023-12-25",
        "numero_de_serie": "FR29 5951 7573 74OY XKGX 6CSG D20",
        "instrucoes_de_armazenamento": "instrucao 2",
    },
]

BLUE = "\033[36m"
GREEN = "\033[32m"
RED = "\033[31m"
RESET = "\033[0m"

expected = (
    f"{GREEN}Data de fabricação mais antiga:{RESET} {BLUE}2020-12-06{RESET}\n"
    f"{GREEN}Data de validade mais próxima:{RESET} {BLUE}2023-09-17{RESET}\n"
    f"{GREEN}Empresa com mais produtos:{RESET} {RED}Target Corporation{RESET}"
)


def test_decorar_relatorio():
    color_report = ColoredReport(SimpleReport)
    report_result = color_report.generate(dict_list_mock)
    assert report_result == expected
