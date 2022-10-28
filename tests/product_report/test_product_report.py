from inventory_report.inventory.product import Product


def test_relatorio_produto():
    expected_return = (
        "O produto Product Name fabricado em 2020-12-25 "
        "por Company Name com validade até 2022-12-02 "
        "precisa ser armazenado keep in cool place."
    )

    product = Product(
        2,
        "Product Name",
        "Company Name",
        "2020-12-25",
        "2022-12-02",
        "123456789",
        "keep in cool place",
    )

    assert str(product) == expected_return
