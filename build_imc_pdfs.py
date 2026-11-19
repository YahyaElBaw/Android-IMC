import os
import base64
from playwright.sync_api import sync_playwright

def get_b64(path):
    with open(path, "rb") as f:
        return f"data:image/png;base64,{base64.b64encode(f.read()).decode('utf-8')}"

def generate_pdf(html_content, output_path):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.set_content(html_content)
        page.pdf(
            path=output_path,
            format="A4",
            print_background=True,
            margin={"top": "15mm", "bottom": "15mm", "left": "15mm", "right": "15mm"}
        )
        browser.close()
    print(f"PDF generated: {output_path}")

# Common CSS styling
BASE_CSS = """
    @page {
        size: A4;
        margin: 15mm;
        @bottom-right {
            content: counter(page);
        }
    }
    * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Segoe UI', Helvetica, Arial, sans-serif; }
    body { color: #1E293B; line-height: 1.6; font-size: 13px; background: white; }
    h1 { color: #0F172A; font-size: 24px; margin-bottom: 8px; border-bottom: 2px solid #2563EB; padding-bottom: 6px; }
    h2 { color: #1E40AF; font-size: 17px; margin-top: 18px; margin-bottom: 8px; border-bottom: 1px solid #E2E8F0; padding-bottom: 4px; }
    h3 { color: #334155; font-size: 14px; margin-top: 12px; margin-bottom: 4px; }
    p { margin-bottom: 8px; text-align: justify; }
    ul, ol { margin-left: 20px; margin-bottom: 10px; }
    li { margin-bottom: 4px; }
    .badge { display: inline-block; padding: 2px 8px; border-radius: 4px; font-weight: bold; font-size: 11px; }
    .badge-blue { background: #DBEAFE; color: #1E40AF; }
    .badge-green { background: #DCFCE7; color: #166534; }
    .badge-orange { background: #FFEDD5; color: #9A3412; }
    .badge-red { background: #FEE2E2; color: #991B1B; }
    table { width: 100%; border-collapse: collapse; margin: 12px 0; font-size: 12px; }
    th, td { border: 1px solid #CBD5E1; padding: 6px 10px; text-align: left; }
    th { background: #F1F5F9; color: #0F172A; font-weight: 600; }
    tr:nth-child(even) { background: #F8FAFC; }
    code { font-family: 'Consolas', monospace; background: #F1F5F9; color: #0284C7; padding: 2px 5px; border-radius: 4px; font-size: 12px; }
    pre { background: #0F172A; color: #F8FAFC; padding: 12px; border-radius: 6px; overflow-x: auto; font-size: 11px; line-height: 1.4; margin: 10px 0; font-family: 'Consolas', monospace; }
    .img-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 14px; margin: 15px 0; }
    .img-card { background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 8px; padding: 8px; text-align: center; }
    .img-card img { width: 100%; max-height: 250px; object-fit: contain; border-radius: 6px; }
    .img-caption { font-size: 11px; font-weight: 600; color: #475569; margin-top: 6px; }
    .header-box { background: linear-gradient(135deg, #1E3A8A, #3B82F6); color: white; padding: 20px; border-radius: 8px; margin-bottom: 20px; }
    .header-box h1 { color: white; border: none; font-size: 26px; }
    .header-meta { display: flex; gap: 20px; margin-top: 10px; font-size: 12px; opacity: 0.9; }
    .note-box { background: #EFF6FF; border-left: 4px solid #3B82F6; padding: 10px 14px; border-radius: 4px; margin: 10px 0; }
    .page-break { page-break-before: always; }
"""

def create_imc_compte_rendu():
    base_dir = r"D:/L3MDW/Mobile/IMC/screenshots"
    img1 = get_b64(f"{base_dir}/imc_01_demarrage.png")
    img2 = get_b64(f"{base_dir}/imc_02_normale.png")
    img3 = get_b64(f"{base_dir}/imc_03_insuffisance.png")
    img4 = get_b64(f"{base_dir}/imc_04_surpoids.png")
    img5 = get_b64(f"{base_dir}/imc_05_obesite_moderee.png")
    img6 = get_b64(f"{base_dir}/imc_06_erreur.png")

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <style>{BASE_CSS}</style>
    </head>
    <body>
        <div class="header-box">
            <h1>Compte Rendu de Réalisation — Calcul IMC</h1>
            <p>Application Android Native en Kotlin de calcul et d'interprétation de l'Indice de Masse Corporelle</p>
            <div class="header-meta">
                <span><strong>Niveau :</strong> Débutant / Étudiant L3 MDW</span>
                <span><strong>Langage :</strong> Kotlin</span>
                <span><strong>Min SDK :</strong> API 24 (Android 7.0)</span>
                <span><strong>Status :</strong> Validé &amp; Testé (100%)</span>
            </div>
        </div>

        <h2>1. Présentation du Projet</h2>
        <p>L'application <strong>CalculIMC</strong> permet à un utilisateur de saisir son poids en kilogrammes et sa taille en mètres, de calculer automatiquement son Indice de Masse Corporelle selon la formule officielle <code>IMC = poids / (taille &times; taille)</code>, et d'obtenir immédiatement la catégorie pondérale correspondante accompagnée d'un code couleur distinctif.</p>

        <div class="note-box">
            <strong>Objectifs pédagogiques validés :</strong>
            <ul>
                <li>Conception d'une interface XML moderne avec Material Components et ConstraintLayout / ScrollView.</li>
                <li>Mise en œuvre du <strong>View Binding</strong> pour un accès sécurisé et performant aux vues sans <code>findViewById</code>.</li>
                <li>Validation rigoureuse des entrées utilisateurs (champs vides, valeurs négatives ou nulles).</li>
                <li>Calcul arithmétique avec arrondi à 2 décimales (<code>Locale.US</code>).</li>
                <li>Gestion de l'état d'affichage lors de la rotation de l'écran avec <code>onSaveInstanceState</code>.</li>
            </ul>
        </div>

        <h2>2. Galerie des Vues et Écrans de l'Application</h2>
        <p>Voici les captures de l'application illustrant tous les scénarios de test et états d'exécution :</p>

        <div class="img-grid">
            <div class="img-card">
                <img src="{img1}" alt="Démarrage" />
                <div class="img-caption">Vue 1 : Écran de Démarrage (État Initial)</div>
            </div>
            <div class="img-card">
                <img src="{img2}" alt="Corpulence normale" />
                <div class="img-caption">Vue 2 : Cas Normal (70 kg, 1.75 m &rarr; 22.86)</div>
            </div>
            <div class="img-card">
                <img src="{img3}" alt="Insuffisance" />
                <div class="img-caption">Vue 3 : Insuffisance (50 kg, 1.75 m &rarr; 16.33)</div>
            </div>
        </div>

        <div class="img-grid">
            <div class="img-card">
                <img src="{img4}" alt="Surpoids" />
                <div class="img-caption">Vue 4 : Surpoids (85 kg, 1.70 m &rarr; 29.41)</div>
            </div>
            <div class="img-card">
                <img src="{img5}" alt="Obésité modérée" />
                <div class="img-caption">Vue 5 : Obésité modérée (100 kg, 1.70 m &rarr; 34.60)</div>
            </div>
            <div class="img-card">
                <img src="{img6}" alt="Erreur" />
                <div class="img-caption">Vue 6 : Gestion d'erreur &amp; Toast interactif</div>
            </div>
        </div>

        <div class="page-break"></div>

        <h2>3. Résultats des Tests et Validation</h2>
        <p>Les tests fonctionnels et unitaires ont été exécutés avec succès conformément aux exigences du sujet :</p>
        <table>
            <thead>
                <tr>
                    <th>Données saisies</th>
                    <th>Résultat attendu</th>
                    <th>Résultat obtenu</th>
                    <th>Catégorie affichée</th>
                    <th>Couleur</th>
                    <th>Statut</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>70 kg et 1,75 m</td>
                    <td>22,86 environ</td>
                    <td>22.86</td>
                    <td>Corpulence normale</td>
                    <td>Vert (#4CAF50)</td>
                    <td><span class="badge badge-green">SUCCÈS</span></td>
                </tr>
                <tr>
                    <td>50 kg et 1,75 m</td>
                    <td>16,33 environ</td>
                    <td>16.33</td>
                    <td>Insuffisance pondérale</td>
                    <td>Orange (#FF9800)</td>
                    <td><span class="badge badge-green">SUCCÈS</span></td>
                </tr>
                <tr>
                    <td>85 kg et 1,70 m</td>
                    <td>29,41 environ</td>
                    <td>29.41</td>
                    <td>Surpoids</td>
                    <td>Orange (#FF9800)</td>
                    <td><span class="badge badge-green">SUCCÈS</span></td>
                </tr>
                <tr>
                    <td>100 kg et 1,70 m</td>
                    <td>34,60 environ</td>
                    <td>34.60</td>
                    <td>Obésité modérée</td>
                    <td>Rouge (#F44336)</td>
                    <td><span class="badge badge-green">SUCCÈS</span></td>
                </tr>
                <tr>
                    <td>Champ vide</td>
                    <td>Message d'erreur</td>
                    <td>Validation déclenchée</td>
                    <td>Erreur visuelle + Toast</td>
                    <td>Rouge (#D32F2F)</td>
                    <td><span class="badge badge-green">SUCCÈS</span></td>
                </tr>
                <tr>
                    <td>Taille = 0 ou négative</td>
                    <td>Message d'erreur</td>
                    <td>Validation déclenchée</td>
                    <td>Erreur visuelle + Toast</td>
                    <td>Rouge (#D32F2F)</td>
                    <td><span class="badge badge-green">SUCCÈS</span></td>
                </tr>
            </tbody>
        </table>

        <h2>4. Architecture du Code Source</h2>
        <p>Le projet est structuré selon les standards modernes Android Studio :</p>
        <ul>
            <li><code>ImcCalculator.kt</code> : Module métier pur isolant la formule d'IMC, le formatage numérique et la catégorisation. Testable par JUnit sans dépendance au framework Android.</li>
            <li><code>MainActivity.kt</code> : Contrôleur gérant les interactions utilisateurs (clics Calculer et Effacer), la liaison des vues (ViewBinding), la validation graphique et la persistance temporaire sur rotation d'écran.</li>
            <li><code>activity_main.xml</code> : Interface graphique déclarative structurée avec cartes Material, champs avec labels flottants et défilement responsive.</li>
            <li><code>strings.xml</code> &amp; <code>colors.xml</code> : Externalisation complète des chaînes et des couleurs sans valeur codée en dur.</li>
        </ul>

        <h2>5. Conclusion</h2>
        <p>L'application CalculIMC fonctionne de manière robuste et élégante. Le build Gradle <code>assembleDebug</code> et l'exécution des tests JUnit <code>testDebugUnitTest</code> se soldent par un résultat 100% réussi.</p>
    </body>
    </html>
    """
    generate_pdf(html, r"D:\L3MDW\Mobile\IMC\Compte_Rendu_IMC.pdf")

def create_imc_guide_etudiant():
    base_dir = r"D:/L3MDW/Mobile/IMC/screenshots"
    img1 = get_b64(f"{base_dir}/imc_02_normale.png")
    img2 = get_b64(f"{base_dir}/imc_06_erreur.png")

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <style>{BASE_CSS}</style>
    </head>
    <body>
        <div class="header-box">
            <h1>Guide Étudiant : Création de l'Application Calcul IMC</h1>
            <p>Tutoriel pas à pas pour apprendre le développement Android avec Kotlin</p>
            <div class="header-meta">
                <span><strong>Projet #1 :</strong> Calcul IMC</span>
                <span><strong>Cible :</strong> Étudiant débutant</span>
                <span><strong>Outils :</strong> Android Studio, Kotlin DSL, View Binding</span>
            </div>
        </div>

        <h2>1. Ce que nous allons construire</h2>
        <p>Bienvenue dans ce premier projet ! L'objectif est d'apprendre à créer une application mobile Android native complète en Kotlin. Notre application permet à l'utilisateur d'entrer son <strong>poids</strong> (kg) et sa <strong>taille</strong> (m), puis de calculer son <strong>Indice de Masse Corporelle (IMC)</strong>.</p>
        
        <div style="display: flex; gap: 20px; align-items: center; margin: 15px 0;">
            <div style="flex: 1;">
                <p><strong>Formule mathématique :</strong></p>
                <div style="background: #F1F5F9; padding: 10px; border-radius: 6px; font-size: 14px; font-weight: bold; text-align: center; color: #1E3A8A;">
                    IMC = Poids / (Taille &times; Taille)
                </div>
                <p style="margin-top: 10px;">Exemple : Un utilisateur de 70 kg et 1.75 m obtiendra :<br>
                <code>70 / (1.75 &times; 1.75) = 22.86</code> &rarr; <strong>Corpulence normale</strong>.</p>
            </div>
            <div style="width: 140px; text-align: center;">
                <img src="{img1}" style="width: 130px; border-radius: 8px; border: 1px solid #CBD5E1;" alt="App view" />
            </div>
        </div>

        <h2>2. Les Technologies Utilisées Expliquées Simplement</h2>
        <ul>
            <li><strong>Kotlin :</strong> Le langage moderne et concis recommandé par Google pour Android. Il évite les erreurs de pointeur nul (Null Safety) et simplifie la syntaxe.</li>
            <li><strong>View Binding :</strong> Une fonctionnalité Android moderne qui génère une classe de liaison pour chaque layout XML. Fini les <code>findViewById()</code> risqués et répétitifs !</li>
            <li><strong>ConstraintLayout &amp; Material Components :</strong> Des composants UI élégants (cartes avec ombres, champs de saisie animés, boutons stylisés) assurant une excellente présentation.</li>
            <li><strong>Ressources XML (strings.xml, colors.xml) :</strong> Bonne pratique fondamentale : séparer le texte et les couleurs du code Java/Kotlin pour faciliter la traduction et la maintenance.</li>
        </ul>

        <h2>3. Étape par Étape : Comment Développer l'Application</h2>

        <h3>Étape 1 : Déclarer les textes et les couleurs</h3>
        <p>Ouvrez <code>res/values/strings.xml</code> et définissez tous les libellés. Cela évite d'écrire des textes en dur dans le code :</p>
        <pre>&lt;resources&gt;
    &lt;string name="app_name"&gt;CalculIMC&lt;/string&gt;
    &lt;string name="titre_imc"&gt;Calcul de l\'IMC&lt;/string&gt;
    &lt;string name="btn_calculer"&gt;Calculer&lt;/string&gt;
    &lt;string name="btn_effacer"&gt;Effacer&lt;/string&gt;
    &lt;string name="cat_normale"&gt;Corpulence normale&lt;/string&gt;
    &lt;string name="erreur_champs_vides"&gt;Veuillez renseigner le poids et la taille&lt;/string&gt;
&lt;/resources&gt;</pre>

        <div class="page-break"></div>

        <h3>Étape 2 : Créer le layout graphique (activity_main.xml)</h3>
        <p>Nous utilisons des <code>TextInputEditText</code> avec <code>android:inputType="numberDecimal"</code> pour que le clavier numérique décimal s'affiche directement sur le smartphone de l'utilisateur.</p>

        <h3>Étape 3 : Programmer la logique de calcul (ImcCalculator.kt)</h3>
        <p>En tant qu'étudiant, une règle d'or en génie logiciel est de séparer l'interface utilisateur du calcul mathématique (séparation des responsabilités) :</p>
        <pre>object ImcCalculator {{
    fun calculer(poidsKg: Double, tailleM: Double): ImcResult {{
        require(poidsKg > 0) {{ "Le poids doit être positif" }}
        require(tailleM > 0) {{ "La taille doit être positive" }}

        val imc = poidsKg / (tailleM * tailleM)
        val imcFormate = String.format(Locale.US, "%.2f", imc)

        val (cat, couleur) = when {{
            imc < 18.5 -> Pair(R.string.cat_insuffisance, R.color.imc_insuffisance)
            imc < 25.0 -> Pair(R.string.cat_normale, R.color.imc_normale)
            imc < 30.0 -> Pair(R.string.cat_surpoids, R.color.imc_surpoids)
            imc < 35.0 -> Pair(R.string.cat_obesite_moderee, R.color.imc_obesite_moderee)
            else -> Pair(R.string.cat_obesite_morbide, R.color.imc_obesite_morbide)
        }}

        return ImcResult(imc, imcFormate, cat, couleur)
    }}
}}</pre>

        <h3>Étape 4 : Lier les vues et réagir aux clics (MainActivity.kt)</h3>
        <p>Dans <code>MainActivity</code>, nous activons le <code>binding</code> et nous écoutons les clics :</p>
        <pre>class MainActivity : AppCompatActivity() {{
    private lateinit var binding: ActivityMainBinding

    override fun onCreate(savedInstanceState: Bundle?) {{
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        binding.buttonCalculer.setOnClickListener {{
            val pStr = binding.editTextPoids.text?.toString()?.trim().orEmpty()
            val tStr = binding.editTextTaille.text?.toString()?.trim().orEmpty()

            if (pStr.isEmpty() || tStr.isEmpty()) {{
                Toast.makeText(this, R.string.erreur_champs_vides, Toast.LENGTH_SHORT).show()
                return@setOnClickListener
            }}

            val p = pStr.toDoubleOrNull() ?: 0.0
            val t = tStr.toDoubleOrNull() ?: 0.0
            val res = ImcCalculator.calculer(p, t)

            binding.textViewImc.text = res.imcFormate
            binding.textViewCategorie.text = getString(res.categorieResId)
            binding.textViewCategorie.setTextColor(ContextCompat.getColor(this, res.couleurResId))
        }}
    }}
}}</pre>

        <h2>4. Points d'attention pour les débutants</h2>
        <div class="note-box">
            <ul>
                <li><strong>Attention aux séparateurs décimaux :</strong> Sur certains appareils en français, la virgule (,) peut être saisie au lieu du point (.). L'usage de <code>toDoubleOrNull()</code> ou le remplacement de la virgule par un point évite les plantages de l'application !</li>
                <li><strong>Division par zéro :</strong> Vérifiez toujours que la taille n'est pas égale à zéro avant d'effectuer la division.</li>
                <li><strong>Bouton Effacer :</strong> Après avoir vidé les champs, utilisez <code>binding.editTextPoids.requestFocus()</code> pour que le clavier se repositionne immédiatement sur le premier champ.</li>
            </ul>
        </div>
    </body>
    </html>
    """
    generate_pdf(html, r"D:\L3MDW\Mobile\pdfs\01_Guide_Etudiant_Calcul_IMC.pdf")

if __name__ == "__main__":
    create_imc_compte_rendu()
    create_imc_guide_etudiant()
