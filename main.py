from flask import Flask, request, jsonify
import os
from utils import process_file, detect_outliers, save_outliers_to_csv

app = Flask(__name__)

@app.route('/api/extract', methods=['POST'])
def extract_data():
    data_file = request.json.get('filename')
    if not data_file or not os.path.exists(data_file):
        return jsonify({'error': 'File not found'}), 400
    
    try:
        data_points = process_file(data_file)
        return jsonify({'data': data_points})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/outliers', methods=['POST'])
def find_outliers():
    data = request.json.get('data')
    if not data:
        return jsonify({'error': 'No data provided'}), 400

    try:
        outliers = detect_outliers(data)
        save_outliers_to_csv(outliers, 'outliers/report.csv')
        return jsonify({'outliers': outliers})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
