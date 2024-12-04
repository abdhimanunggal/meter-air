from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')  # Halaman input data

@app.route('/calculate', methods=['POST'])
def calculate():
    awal_pembacaan = int(request.form['awal'])
    akhir_pembacaan = int(request.form['akhir'])
    
    # Hitung penggunaan dan biaya
    penggunaan_total = abs(akhir_pembacaan - awal_pembacaan)
    beban_default = 3000
    biaya_pelayanan = 1000
    tarif_1, tarif_2, tarif_3 = 2000, 2500, 3000

    penggunaan_1 = min(10, penggunaan_total) * tarif_1
    penggunaan_2 = min(10, max(0, penggunaan_total - 10)) * tarif_2
    penggunaan_3 = max(0, penggunaan_total - 20) * tarif_3

    biaya_total = penggunaan_1 + penggunaan_2 + penggunaan_3 + beban_default + biaya_pelayanan

    return jsonify({"biaya_total": f"Rp{biaya_total}"})

if __name__ == '__main__':
    app.run(debug=True)
