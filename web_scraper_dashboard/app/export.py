from app.models import Product
from flask import send_file
import csv

def export_products():
    # Recuperando todos os produtos
    products = Product.query.all()

    # Gerando o nome do arquivo CSV
    filename = 'products.csv'

    # Configurando o cabeçalho do arquivo CSV
    fieldnames = ['Title', 'Description', 'Price']

    # Gerando o conteúdo do arquivo CSV
    rows = [{'Title': product.title, 'Description': product.description, 'Price': product.price} for product in products]

    # Escrevendo os dados no arquivo CSV
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    # Retornando o arquivo CSV para download
    return send_file(filename, as_attachment=True)