# INVENTORY REPORT 📑

## 📄 Sobre | About
<details>
  <summary>
    <strong>PT</strong>
  </summary><br>
   Gerador de relatórios criado usando Programação Orientada a Objetos(POO) que recebe como entrada arquivos com dados de um estoque e gera, como saída, um relatório.

  <br>

  🎯
  * Aplicar conceitos de Orientação a Objetos em Python;
  * Aplicar padrões de projeto;
  * Leitura e escrita de arquivos (XML, CSV, JSON).

  🧪 Tentes realizados para inventory_report/inventory/product.py (criação de produto) e inventory_report/reports/colored_report.py (geração de uma versão do relatório em cores) com pytest.<br>
</details>

<details>
  <summary>
    <strong>EN</strong>
  </summary><br>
  Report generator built with Object-Oriented Programming (OOP) that receives as entry files with data from and an inventory and generate, as output, a report.

  <br>

  🎯
  * Apply Object-Oriented concepts in Python;
  * Apply design patterns;
  * Reading and writing files (XML, CSV, JSON)

  🧪 Tests performed to inventory_report/inventory/product.py (product creation) and inventory_report/reports/colored_report.py (generating a color version of the report) with pytest. <br>
</details>
<br>

## 🛠️ Ferramentas | Tools
* [Python](https://www.python.org/)
* [Pytest](https://docs.pytest.org/en/7.2.x/)
<br>

---

## ⚙️Como rodar |  How to run:
<br>

Clone o repositório:
```
git clone git@github.com:queite/inventory-report.git
```
Entre na pasta raiz:
```
cd inventory-report
```
Crie o ambiente virtual:
```
python3 -m venv .venv && source .venv/bin/activate
```
Instale as dependências:
```
python3 -m pip install -r dev-requirements.txt
```
No terminal chame oo comando inventory_report passando seus argumentos:
```
inventory_report argumento1 argumento2
```
* argumento1 deve receber o caminho de um arquivo a ser importado. O arquivo pode ser um csv, json ou xml.

* argumento2 pode receber duas strings: simples ou completo, cada uma gerando o respectivo relatório. <br>
Ex.: `inventory_report inventory_report.data.inventory.csv simples`

Outra opção é invocar o comando assim:
```
python3 -m inventory_report.main argumento1 argumento2
```

<!-- Download the code:
```
git clone git@github.com:queite/inventory-report.git
```
Enter the root folder:
```
cd inventory-repor 
Install dependencies:
```
python3 -m pip install -r dev-requirements.txt
``` -->
---
PT<br>
Projeto desenvolvido durante o módulo de ciências da computação na [Trybe](https://www.betrybe.com/).<br/>
Todos os projetos da [Trybe](https://www.betrybe.com/) usam `linters`, `Git` and `GitHub`.<br/>

EN<br>
Project developed in the Computer Science Module at the [Trybe](https://www.betrybe.com/) course.<br/>
All [Trybe](https://www.betrybe.com/) projects use `linters`, `Git` and `GitHub`.<br/>
