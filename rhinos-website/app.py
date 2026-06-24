from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Struttura dati centralizzata (Espandibile in futuro con foglio dati esterno o DB)
DATA_STORE = {
    "agency_name": "Rhino's Agency",
    "established": "2026",
    "hero_title": "Eliminiamo le inefficienze. Tu pensa solo a em_performare_em.",
    "hero_sub": "Siamo il partner tecnico e gestionale d'élite che fa da ponte strategico tra il talento e le organizzazioni del settore gaming.",
    "stats": [
        {"value": "2", "label": "Brand attivi"},
        {"value": "3", "label": "Modelli di collaborazione"},
        {"value": "100%", "label": "Focus sulle performance"},
        {"value": "2026", "label": "Anno fondazione"}
    ],
    "ticker_items": [
        "Rhino's Agency", "RHA Esport", "Esports Management", 
        "Talent Development", "Performance Coaching", 
        "Digital Infrastructure", "Content Creation", "Scouting d'élite"
    ],
    "services": [
        {
            "id": "01",
            "icon": "ti-briefcase",
            "title": "Management Strategico",
            "desc": "Gestione quotidiana dei roster, logistica dei player, flussi comunicativi interni, negoziazione dei contratti e organizzazione eventi competitivi."
        },
        {
            "id": "02",
            "icon": "ti-activity",
            "title": "Performance & Coaching",
            "desc": "Analisi tecnica dei match e studio strategico del meta di gioco uniti a percorsi strutturati di mental coaching per la gestione dello stress da competizione."
        },
        {
            "id": "03",
            "icon": "ti-device-laptop",
            "title": "Infrastruttura Digitale",
            "desc": "Sviluppo landing page dedicate, cura dell'identità visiva del brand, asset grafici completi per stream e piani editoriali social mirati all'engagement."
        },
        {
            "id": "04",
            "icon": "ti-search",
            "title": "Scouting & Data Evaluation",
            "desc": "Selezione mirata di Player e Content Creator attraverso l'analisi di dati concreti: performance in-game, reach digitale ed effettive competenze tecniche."
        },
        {
            "id": "05",
            "icon": "ti-adjustments",
            "title": "Integrazione Tecnica",
            "desc": "Fornitura immediata al talento degli strumenti e delle competenze necessarie per scalare i propri progetti: setup, grafiche e supporto psicologico."
        },
        {
            "id": "06",
            "icon": "ti-trending-up",
            "title": "Modelli Flessibili",
            "desc": "Collaborazioni costruite su misura del progetto attraverso formule di Service Fee mirate, Management a Canone ricorrente o Revenue Sharing."
        }
    ],
    "partners": ["Saturlity", "W-Fox", "Edgarito"],
    "collaborations": [
        {
            "team": "Team Fulgur Esport",
            "date": "19/05/2026",
            "status": "Attiva",
            "type": "Partnership Ufficiale"
        }
    ],
    # Posizioni aperte estratte dalla grafica "We're Hiring!"
    "hiring_positions": [
        "Esports Performance Coach",
        "Social Media Manager (Gaming)",
        "Talent Scout",
        "Frontend Developer (Flask/Jinja)"
    ],
    "contacts": {
        "email": "rhinos.agency@gmail.com",
        "discord": "Discord Server — Canale Operativo",
        "web": "rhinos-agency.base44.app"
    }
}

@app.route('/')
def home():
    # Carica la sezione principale 'home'
    return render_template('index.html', page_id='home', data=DATA_STORE)

@app.route('/unisciti')
def unisciti():
    # Nuova macro-sezione condizionale dedicata al form di reclutamento ("We're Hiring!")
    return render_template('index.html', page_id='unisciti', data=DATA_STORE)

@app.route('/invia-candidatura', methods=['POST'])
def invia_candidatura():
    # Logica di ricezione e controllo del form dinamico (stile Insidious FC)
    nome = request.form.get('nome')
    email = request.form.get('email')
    posizione = request.form.get('posizione')
    piattaforma = request.form.get('piattaforma')
    disponibilita = request.form.get('disponibilita')
    messaggio = request.form.get('messaggio')
    
    # Qui i dati possono essere salvati o inviati via webhook / foglio di calcolo
    print(f"Nuova candidatura ricevuta per {posizione}: {nome} ({email}) - {piattaforma} - Disp: {disponibilita} giorni")
    
    return redirect(url_for('home', success=True))

if __name__ == '__main__':
    app.run(debug=True)
