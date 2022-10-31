import csv

from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @staticmethod
    def import_data(path):
        if not path.endswith(".csv"):
            raise ValueError("Arquivo inválido")
        else:
            with open(path, encoding="utf8") as file:
                file_to_dict = csv.DictReader(file)
                dict_to_list = list(file_to_dict)
        return dict_to_list
