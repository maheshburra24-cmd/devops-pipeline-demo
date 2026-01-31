import os
from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')

def read_file(filename):
    path = os.path.join(DATA_DIR, filename)
    if not os.path.exists(path):
        return []
    with open(path, 'r') as f:
        return [line.strip() for line in f.readlines()]

@app.route('/')
def index():
    return redirect(url_for('product'))

@app.route('/product')
def product():
    price_data = read_file('price.txt')
    deploy_info = read_file('deploy_info.txt')
    
    context = {
        'product_name': 'Premium Wireless Headphones',
        'current_price': price_data[0] if price_data else 'N/A',
        'last_updated': deploy_info[0] if deploy_info else 'N/A',
        'status': 'Updated via CI/CD Pipeline',
        'environment': 'Production – Live'
    }
    return render_template('product.html', **context)

@app.route('/pipeline')
def pipeline():
    deploy_info = read_file('deploy_info.txt')
    change_log = read_file('change_log.txt')
    
    # deploy_info format: timestamp, commit_hash, status, trigger
    # change_log format: old_price, new_price, message
    
    pipeline_data = {
        'status': deploy_info[2] if len(deploy_info) > 2 else 'UNKNOWN',
        'commit_hash': deploy_info[1] if len(deploy_info) > 1 else 'N/A',
        'trigger': deploy_info[3] if len(deploy_info) > 3 else 'GitHub Push',
        'last_updated': deploy_info[0] if deploy_info else 'N/A',
        'old_price': change_log[0] if len(change_log) > 0 else 'N/A',
        'new_price': change_log[1] if len(change_log) > 1 else 'N/A',
        'commit_message': change_log[2] if len(change_log) > 2 else 'N/A'
    }
    return render_template('pipeline.html', **pipeline_data)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
