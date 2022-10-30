import json

from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    def import_data(path):
        if not path.endswith(".json"):
            raise ValueError("Arquivo inválido")
        else:
            with open(path) as file:
                content = file.read()
                products = json.loads(content)
        return products
