from flask import Flask, render_template

app = Flask(__name__)

# Simulazione dei dati esterni (che poi leggeremo dal foglio dati come su Insidious)
DATA_STORE = {
    "agency_name": "Rhino's Agency",
    "established": "2026",
    "stats": {
        "brands": 2,
        "models": 3,
        "performance": "100%",
        "year": 2026
    },
    "partners": ["Saturlity", "W-Fox", "Edgarito"]
}

@app.route('/')
def home():
    # Passiamo i dati dinamici e il page_id al template Jinja2
    return render_template('index.html', page_id='home', data=DATA_STORE)

if __name__ == '__main__':
    app.run(debug=True)