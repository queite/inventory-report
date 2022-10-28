from inventory_report.inventory.product import Product


def test_cria_produto():
    product_data = [
        2,
        "Product Name",
        "Company Name",
        "2020-12-25",
        "2022-12-02",
        "123456789",
        "keep in cool place",
    ]

    product = Product(*product_data)

    assert product.id == product_data[0]
    assert product.nome_do_produto == product_data[1]
    assert product.nome_da_empresa == product_data[2]
    assert product.data_de_fabricacao == product_data[3]
    assert product.data_de_validade == product_data[4]
    assert product.numero_de_serie == product_data[5]
    assert product.instrucoes_de_armazenamento == product_data[6]
