import sys

from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.inventory.inventory_refactor import InventoryRefactor


def importer_strategy(path):
    importer = ""
    if path.endswith(".csv"):
        importer = CsvImporter
    if path.endswith(".json"):
        importer = JsonImporter
    if path.endswith(".xml"):
        importer = XmlImporter
    return importer


def main():
    try:
        path = sys.argv[1]
        report_type = sys.argv[2]
        report = []
        importer = importer_strategy(path)
        inventory = InventoryRefactor(importer)
        report = inventory.import_data(path, report_type)
        sys.stdout.write(report)
    except IndexError:
        sys.stderr.write("Verifique os argumentos\n")
