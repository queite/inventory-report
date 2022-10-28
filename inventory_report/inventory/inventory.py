import csv
import json

from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    def import_csv(path: str):
        with open(path, encoding="utf8") as file:
            file_to_dict = csv.DictReader(file)
            dict_to_list = list(file_to_dict)
        return dict_to_list

    def import_json(path: str):
        with open(path) as file:
            content = file.read()
            products = json.loads(content)
        return products

    def import_data(path: str, type: str):
        dict_list = []
        if path.endswith("csv"):
            dict_list = Inventory.import_csv(path)
        elif path.endswith("json"):
            dict_list = Inventory.import_json(path)

        if type.lower() == "simples":
            return SimpleReport.generate(dict_list)
        if type.lower() == "completo":
            return CompleteReport.generate(dict_list)
