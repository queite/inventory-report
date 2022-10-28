import csv
import json

import xmltodict

from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    # def import_csv(path: str):
    #     with open(path, encoding="utf8") as file:
    #         file_to_dict = csv.DictReader(file)
    #         dict_to_list = list(file_to_dict)
    #     return dict_to_list

    # def import_json(path: str):
    #     with open(path) as file:
    #         content = file.read()
    #         products = json.loads(content)
    #     return products

    # def import_xml(path: str):
    #     with open(path, "r") as file:
    #         read = file.read()
    #         dictionary = xmltodict.parse(read)
    #     return list(dictionary["dataset"]["record"])

    def read_data(path: str):
        dict_list = []
        with open(path) as file:
            if path.endswith("csv"):
                file_to_dict = csv.DictReader(file)
                dict_to_list = list(file_to_dict)
                dict_list = dict_to_list

            if path.endswith("json"):
                content = file.read()
                products = json.loads(content)
                dict_list = products

            if path.endswith("xml"):
                read = file.read()
                dictionary = xmltodict.parse(read)
                dict_list = list(dictionary["dataset"]["record"])

        return dict_list

    # def read_data(path: str):
    #     dict_list = []
    #     if path.endswith("csv"):
    #         dict_list = Inventory.import_csv(path)
    #     if path.endswith("json"):
    #         dict_list = Inventory.import_json(path)
    #     if path.endswith("xml"):
    #         dict_list = Inventory.import_xml(path)
    #     return dict_list

    def import_data(path: str, type: str):
        dict_list = Inventory.read_data(path)

        if type.lower() == "simples":
            return SimpleReport.generate(dict_list)
        if type.lower() == "completo":
            return CompleteReport.generate(dict_list)
