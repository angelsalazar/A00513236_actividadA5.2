""" Compute Sales """

import sys
import json
import time

start_time = time.time()

if __name__ == '__main__':
    # reading arguments
    [_, product_list_file_name, * sale_file_names] = sys.argv

    products_by_name = {}
    summaries = [
        '\tTOTAL'
    ]

    with open(product_list_file_name, 'r', encoding='UTF-8') as file:
        products = json.loads(file.read())
        for product in products:
            products_by_name[product['title']] = product
    for file_name in sale_file_names:
        TOTAL = 0
        with open(file_name, 'r', encoding='UTF-8') as file:
            sales = json.loads(file.read())
            for sale in sales:
                if sale['Product'] not in products_by_name:
                    print(f"{sale['Product']} not found")
                    continue

                product = products_by_name[sale['Product']]
                TOTAL += sale['Quantity'] * product['price']
        summaries.append(
            '\t'.join([
                file_name.replace('.Sales.json', ''),
                f"{TOTAL:.2f}"
            ])
        )
    summaries.append('execution time: ' + str(time.time() - start_time) + 's')
    SUMMARY = '\n'.join(summaries)
    print(SUMMARY)
    with open('SalesResults.txt', 'w', encoding='UTF-8') as file:
        file.write(SUMMARY)
