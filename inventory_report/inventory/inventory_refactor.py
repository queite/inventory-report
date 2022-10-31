from typing import Iterable

from inventory_report.inventory.inventory_iterator import InventoryIterator
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class InventoryRefactor(Iterable):
    def __init__(self, importer):
        self.importer = importer
        self.data = []

    def __iter__(self):
        return InventoryIterator(self.data)

    def import_data(self, path: str, type: str):
        dict_list = self.importer.import_data(path)
        for item in dict_list:
            self.data.append(item)

        if type.lower() == "simples":
            return SimpleReport.generate(self.data)
        if type.lower() == "completo":
            return CompleteReport.generate(self.data)
