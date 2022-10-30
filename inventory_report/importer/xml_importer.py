import xmltodict

from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    def import_data(path):
        if not path.endswith(".xml"):
            raise ValueError("Arquivo inválido")
        else:
            with open(path, "r") as file:
                read = file.read()
                dictionary = xmltodict.parse(read)
        return list(dictionary["dataset"]["record"])
