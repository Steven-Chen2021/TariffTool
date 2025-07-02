from flask import Flask, request, jsonify, render_template
import xlwings as xw

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/calculate', methods=['POST'])
def calculate():
    coo_list = request.form.getlist('product_coo[]')
    hts_list = request.form.getlist('hts_code[]')

    wb = xw.Book('Tariff Lookup Tool.xlsx')
    sht = wb.sheets['Enter Importer Data Here']

    start_row = 2
    for idx, (coo, hts) in enumerate(zip(coo_list, hts_list)):
        row = start_row + idx
        sht.range(f'C{row}').value = coo
        sht.range(f'D{row}').value = hts

    wb.app.calculate()

    rows = []
    for idx, (coo, hts) in enumerate(zip(coo_list, hts_list)):
        row = start_row + idx
        cells = {
            'coo': coo,
            'hts': hts,
            'steel': sht.range(f'M{row}').value,
            'aluminum': sht.range(f'Q{row}').value,
            'tariff_301': sht.range(f'T{row}').value,
            'china20': sht.range(f'AB{row}').value,
            'reciprocal': sht.range(f'AE{row}').value,
            'total_new_duty': sht.range(f'AF{row}').value,
        }
        rows.append(cells)

    wb.save()
    wb.close()

    return jsonify(rows)


if __name__ == '__main__':
    app.run(debug=True)
