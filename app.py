from flask import Flask, request, jsonify
import xlwings as xw

app = Flask(__name__)  # ✅ 定義 app 變數

@app.route('/')
def index():
    return '''
        <form method="post" action="/calculate">
            A: <input name="param1"><br>
            B: <input name="param2"><br>
            <button type="submit">Calculate</button>
        </form>
    '''

@app.route('/calculate', methods=['POST'])
def calculate():
    a = float(request.form['param1'])
    b = float(request.form['param2'])

    wb = xw.Book('workbook.xlsx')  # 確保同資料夾中有這個檔案
    sht = wb.sheets[0]

    sht.range('A1').value = a
    sht.range('B1').value = b

    wb.app.calculate()  # 讓 Excel 運算公式

    result = sht.range('C1').value

    wb.save()
    wb.close()

    return jsonify({'result': result})
if __name__ == "__main__":
    app.run(debug=True)