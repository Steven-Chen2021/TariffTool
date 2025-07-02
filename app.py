from flask import Flask, request, jsonify, render_template
import xlwings as xw

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/calculate', methods=['POST'])
def calculate():
    product_coo = request.form.get('product_coo', '')
    hts_code = request.form.get('hts_code', '')

    wb = xw.Book('Tariff Lookup Tool.xlsx')
    sht = wb.sheets['Enter Importer Data Here']

    sht.range('C2').value = product_coo
    sht.range('D2').value = hts_code

    wb.app.calculate()

    cells = ['M2', 'Q2', 'T2', 'AV2', 'AE2', 'AF2']
    results = {cell: sht.range(cell).value for cell in cells}

    wb.save()
    wb.close()

    return jsonify(results)


if __name__ == '__main__':
    app.run(debug=True)
