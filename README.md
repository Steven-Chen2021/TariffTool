# TariffTool 專案

此專案示範如何透過 Python Flask 結合 Excel 進行計算。程式會讀取 `workbook.xlsx` 中的公式，依使用者輸入的數值回傳計算結果。資料夾內亦包含較完整的 `Tariff Lookup Tool.xlsx`，可作為關稅查詢的範例。

## 內容
- `app.py`：Flask 應用程式，提供 `/` 表單頁面及 `/calculate` 計算路由。
- `templates/index.html`：簡易前端表單，讓使用者輸入兩個參數。
- `workbook.xlsx`：包含 A1+B1 公式的工作表，程式將兩個輸入寫入 A1、B1，並取回 C1 結果。
- `Tariff Lookup Tool.xlsx`：另一個較完整的 Excel 工具，內含更多資料與計算邏輯。

## 執行方式
1. 安裝依賴：需安裝 `flask` 及 `xlwings` 套件。
2. 執行 `python app.py` 啟動伺服器。
3. 瀏覽 `http://localhost:5000`，填入參數後即可取得計算結果。

此專案主要作為範例，展示如何將 Excel 公式整合至 Flask 應用程式中。

## 功能改進
- 前端表單使用表格呈現結果，更易閱讀。
- 結果顯示含鋼鋁等多種關稅計算，並以百分比格式呈現。
