from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    def read_data(path: str):
        dict_list = []
        if path.endswith("csv"):
            dict_list = CsvImporter.import_data(path)

        if path.endswith("json"):
            dict_list = JsonImporter.import_data(path)

        if path.endswith("xml"):
            dict_list = XmlImporter.import_data(path)

        return dict_list

    def import_data(path: str, type: str):
        dict_list = Inventory.read_data(path)

        if type.lower() == "simples":
            return SimpleReport.generate(dict_list)
        if type.lower() == "completo":
            return CompleteReport.generate(dict_list)
