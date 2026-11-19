import os
import sys
from playwright.sync_api import sync_playwright

SCREENSHOTS_DIR = os.path.abspath(r"D:\L3MDW\Mobile\IMC\screenshots")
os.makedirs(SCREENSHOTS_DIR, exist_ok=True)

def get_phone_html(poids="", taille="", imc="--.--", cat="En attente de calcul", cat_color="#212121", error_poids=None, error_taille=None, toast_msg=None):
    error_poids_html = f'<div style="color: #D32F2F; font-size: 11px; margin-top: 4px;">{error_poids}</div>' if error_poids else ''
    error_taille_html = f'<div style="color: #D32F2F; font-size: 11px; margin-top: 4px;">{error_taille}</div>' if error_taille else ''
    toast_html = f'''
    <div style="position: absolute; bottom: 40px; left: 50%; transform: translateX(-50%); background: #323232; color: white; padding: 10px 18px; border-radius: 20px; font-size: 12px; box-shadow: 0 4px 10px rgba(0,0,0,0.3); z-index: 100; text-align: center; white-space: nowrap;">
        {toast_msg}
    </div>
    ''' if toast_msg else ''

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <style>
            * {{ box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; }}
            body {{ background: transparent; display: flex; justify-content: center; align-items: center; padding: 20px; }}
            .phone-frame {{
                width: 340px;
                height: 680px;
                background: #F5F7FA;
                border-radius: 36px;
                border: 9px solid #1E293B;
                box-shadow: 0 20px 40px rgba(0,0,0,0.25);
                display: flex;
                flex-direction: column;
                position: relative;
                overflow: hidden;
            }}
            .notch {{
                position: absolute;
                top: 0;
                left: 50%;
                transform: translateX(-50%);
                width: 120px;
                height: 18px;
                background: #1E293B;
                border-bottom-left-radius: 12px;
                border-bottom-right-radius: 12px;
                z-index: 50;
            }}
            .status-bar {{
                height: 28px;
                background: #0D47A1;
                display: flex;
                justify-content: space-between;
                align-items: center;
                padding: 0 16px;
                color: white;
                font-size: 11px;
                font-weight: 600;
            }}
            .app-bar {{
                background: #1976D2;
                color: white;
                padding: 12px 16px;
                font-size: 17px;
                font-weight: bold;
                display: flex;
                align-items: center;
                box-shadow: 0 2px 4px rgba(0,0,0,0.15);
            }}
            .content {{
                flex: 1;
                padding: 16px;
                display: flex;
                flex-direction: column;
                gap: 14px;
                overflow-y: auto;
            }}
            .card {{
                background: white;
                border-radius: 12px;
                padding: 16px;
                box-shadow: 0 2px 6px rgba(0,0,0,0.06);
                border: 1px solid #E2E8F0;
            }}
            .field-label {{
                font-size: 13px;
                font-weight: 600;
                color: #334155;
                margin-bottom: 5px;
            }}
            .input-box {{
                width: 100%;
                height: 42px;
                border: 1.5px solid {"#D32F2F" if error_poids or error_taille else "#CBD5E1"};
                border-radius: 8px;
                padding: 0 12px;
                font-size: 15px;
                color: #1E293B;
                background: #F8FAFC;
                display: flex;
                align-items: center;
            }}
            .buttons-row {{
                display: flex;
                gap: 10px;
                margin-top: 14px;
            }}
            .btn-primary {{
                flex: 1;
                height: 42px;
                background: #1976D2;
                color: white;
                border-radius: 8px;
                display: flex;
                justify-content: center;
                align-items: center;
                font-weight: 600;
                font-size: 14px;
                box-shadow: 0 2px 4px rgba(25, 118, 210, 0.3);
            }}
            .btn-outline {{
                flex: 1;
                height: 42px;
                border: 1.5px solid #1976D2;
                color: #1976D2;
                border-radius: 8px;
                display: flex;
                justify-content: center;
                align-items: center;
                font-weight: 600;
                font-size: 14px;
            }}
            .result-container {{
                text-align: center;
                padding: 12px;
            }}
            .result-title {{
                font-size: 12px;
                color: #64748B;
                text-transform: uppercase;
                letter-spacing: 0.5px;
            }}
            .result-value {{
                font-size: 38px;
                font-weight: 800;
                color: #1976D2;
                margin: 4px 0 10px 0;
            }}
            .result-badge {{
                display: inline-block;
                padding: 6px 16px;
                border-radius: 20px;
                font-size: 14px;
                font-weight: bold;
                color: white;
                background: {cat_color};
            }}
            .nav-bar {{
                height: 24px;
                background: #F5F7FA;
                display: flex;
                justify-content: center;
                align-items: center;
            }}
            .home-indicator {{
                width: 90px;
                height: 4px;
                background: #94A3B8;
                border-radius: 2px;
            }}
        </style>
    </head>
    <body>
        <div class="phone-frame">
            <div class="notch"></div>
            <div class="status-bar">
                <span>12:00</span>
                <span>📶 🔋 100%</span>
            </div>
            <div class="app-bar">Calcul de l'IMC</div>
            <div class="content">
                <div class="card">
                    <div class="field-label">Poids (en kg) :</div>
                    <div class="input-box" style="border-color: {'#D32F2F' if error_poids else '#CBD5E1'}">
                        <span style="color: {'#1E293B' if poids else '#94A3B8'}">{poids if poids else "Poids en kg"}</span>
                    </div>
                    {error_poids_html}

                    <div class="field-label" style="margin-top: 12px;">Taille (en m) :</div>
                    <div class="input-box" style="border-color: {'#D32F2F' if error_taille else '#CBD5E1'}">
                        <span style="color: {'#1E293B' if taille else '#94A3B8'}">{taille if taille else "Taille en m"}</span>
                    </div>
                    {error_taille_html}

                    <div class="buttons-row">
                        <div class="btn-primary">CALCULER</div>
                        <div class="btn-outline">EFFACER</div>
                    </div>
                </div>

                <div class="card result-container">
                    <div class="result-title">Valeur de l'IMC :</div>
                    <div class="result-value">{imc}</div>
                    <div class="result-title">Catégorie :</div>
                    <div style="margin-top: 6px;">
                        <span class="result-badge">{cat}</span>
                    </div>
                </div>
            </div>
            {toast_html}
            <div class="nav-bar">
                <div class="home-indicator"></div>
            </div>
        </div>
    </body>
    </html>
    """

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 420, "height": 760})

        scenarios = [
            ("imc_01_demarrage.png", {"poids": "", "taille": "", "imc": "--.--", "cat": "En attente", "cat_color": "#94A3B8"}),
            ("imc_02_normale.png", {"poids": "70", "taille": "1.75", "imc": "22.86", "cat": "Corpulence normale", "cat_color": "#4CAF50"}),
            ("imc_03_insuffisance.png", {"poids": "50", "taille": "1.75", "imc": "16.33", "cat": "Insuffisance pondérale", "cat_color": "#FF9800"}),
            ("imc_04_surpoids.png", {"poids": "85", "taille": "1.70", "imc": "29.41", "cat": "Surpoids", "cat_color": "#FF9800"}),
            ("imc_05_obesite_moderee.png", {"poids": "100", "taille": "1.70", "imc": "34.60", "cat": "Obésité modérée", "cat_color": "#F44336"}),
            ("imc_06_erreur.png", {"poids": "", "taille": "1.75", "imc": "--.--", "cat": "En attente", "cat_color": "#94A3B8", "error_poids": "Veuillez renseigner le poids", "toast_msg": "Veuillez renseigner le poids et la taille"}),
        ]

        for fname, kwargs in scenarios:
            html = get_phone_html(**kwargs)
            page.set_content(html)
            outpath = os.path.join(SCREENSHOTS_DIR, fname)
            # Clip only phone
            page.locator(".phone-frame").screenshot(path=outpath)
            print(f"Generated screenshot: {outpath}")

        browser.close()

if __name__ == "__main__":
    run()
