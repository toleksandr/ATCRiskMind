from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from flask_babel import Babel
import numpy as np
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)
babel = Babel(app, locale_selector=lambda: session.get('lang', 'uk'))

@app.route('/')
def index():
    session['lang'] = request.args.get('lang', session.get('lang', 'uk'))
    return render_template('index.html')

@app.route('/set-language/<lang>')
def set_language(lang):
    session['lang'] = lang
    return redirect(request.referrer or url_for('index'))

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    ranges = {k: [data.get(f'{k}{i}_range', []) for i in range(1, 6)] for k in ('l', 'r')}
    
    fatigue_data = data.get('fatigue_data', {})
    fa_values = {d: np.mean([float(v) for v in times.values() if v]) if any(times.values()) else 0
                 for d, times in fatigue_data.items()}
    
    mental_health_data = data.get('mental_health_data', {})
    l_values = {d: sum(int(v) for v in crit.values() if v) for d, crit in mental_health_data.items()}
    
    lambda_mh_values = {d: 1.0 if l <= 10 else 1 - (l - 10) ** 2 / 1800 if l <= 40 else
                        (70 - l) ** 2 / 1800 if l < 70 else 0.0 for d, l in l_values.items()}
    
    def find_level(val, range_list, prefix):
        for i, (low, high) in enumerate(range_list, 1):
            if low < val <= high:
                return f"{prefix}{i}"
        return "Unknown"
    
    l_mh_values = {d: find_level(l, ranges['l'], 'L') for d, l in lambda_mh_values.items()}
    
    r_values = {}
    for d, l_mh in l_mh_values.items():
        fa = fa_values.get(d, 0)
        lvl = int(l_mh[1]) if l_mh != "Unknown" else 0
        if lvl:
            r_values[d] = (np.sqrt(fa/2) + (5-lvl))/5 if fa <= 0.5 else ((6-lvl) - np.sqrt((1-fa)/2))/5
        else:
            r_values[d] = 0
    
    r_linguistic = {d: find_level(r, ranges['r'], 'R') for d, r in r_values.items()}
    
    lambda_mh_treemap = [{'id': d, 'value': round(v, 3), 'level': l_mh_values[d]} for d, v in lambda_mh_values.items()]
    l_mh_treemap = [{'id': d, 'level': l_mh_values[d], 'risk_level': r_linguistic[d], 'risk_value': round(r_values[d], 3)} for d in l_mh_values]
    
    return jsonify({
        'fa_values': {k: round(v, 3) for k, v in fa_values.items()},
        'l_values': l_values,
        'lambda_mh_values': {k: round(v, 3) for k, v in lambda_mh_values.items()},
        'l_mh_values': l_mh_values,
        'r_values': {k: round(v, 3) for k, v in r_values.items()},
        'r_linguistic': r_linguistic,
        'lambda_mh_treemap': lambda_mh_treemap,
        'l_mh_treemap': l_mh_treemap
    })

if __name__ == '__main__':
    app.run(debug=True)
