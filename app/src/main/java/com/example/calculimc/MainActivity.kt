package com.example.calculimc

import android.os.Bundle
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import androidx.core.content.ContextCompat
import com.example.calculimc.databinding.ActivityMainBinding

/**
 * Activité principale de l'application Calcul de l'IMC.
 * Développée avec View Binding conformément aux bonnes pratiques Android Studio.
 */
class MainActivity : AppCompatActivity() {

    private lateinit var binding: ActivityMainBinding

    companion object {
        private const val KEY_RESULTAT_IMC = "key_resultat_imc"
        private const val KEY_RESULTAT_CAT = "key_resultat_cat"
        private const val KEY_RESULTAT_COULEUR = "key_resultat_couleur"
    }

    private var couleurActuelleResId: Int = R.color.text_primary

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        // Configuration des écouteurs d'événements
        binding.buttonCalculer.setOnClickListener {
            calculerImc()
        }

        binding.buttonEffacer.setOnClickListener {
            effacerChamps()
        }

        // Restauration d'état après rotation si disponible
        savedInstanceState?.let { bundle ->
            val imcTexte = bundle.getString(KEY_RESULTAT_IMC)
            val catTexte = bundle.getString(KEY_RESULTAT_CAT)
            couleurActuelleResId = bundle.getInt(KEY_RESULTAT_COULEUR, R.color.text_primary)

            if (!imcTexte.isNullOrEmpty() && imcTexte != getString(R.string.valeur_imc_defaut)) {
                binding.textViewImc.text = imcTexte
                binding.textViewCategorie.text = catTexte
                binding.textViewCategorie.setTextColor(ContextCompat.getColor(this, couleurActuelleResId))
            }
        }
    }

    /**
     * Valide les saisies, effectue le calcul d'IMC et met à jour l'interface.
     */
    private fun calculerImc() {
        val textePoids = binding.editTextPoids.text?.toString()?.trim().orEmpty()
        val texteTaille = binding.editTextTaille.text?.toString()?.trim().orEmpty()

        // 1. Vérification que les champs ne sont pas vides
        if (textePoids.isEmpty() || texteTaille.isEmpty()) {
            if (textePoids.isEmpty()) {
                binding.editTextPoids.error = getString(R.string.erreur_champs_vides)
            }
            if (texteTaille.isEmpty()) {
                binding.editTextTaille.error = getString(R.string.erreur_champs_vides)
            }
            Toast.makeText(this, R.string.erreur_champs_vides, Toast.LENGTH_SHORT).show()
            return
        }

        // 2. Conversion et validation numérique
        val poids = textePoids.toDoubleOrNull()
        val taille = texteTaille.toDoubleOrNull()

        if (poids == null || poids <= 0) {
            binding.editTextPoids.error = getString(R.string.erreur_poids_invalide)
            Toast.makeText(this, R.string.erreur_poids_invalide, Toast.LENGTH_SHORT).show()
            return
        }

        if (taille == null || taille <= 0) {
            binding.editTextTaille.error = getString(R.string.erreur_taille_invalide)
            Toast.makeText(this, R.string.erreur_taille_invalide, Toast.LENGTH_SHORT).show()
            return
        }

        // 3. Calcul via la classe métier
        try {
            val resultat = ImcCalculator.calculer(poids, taille)

            // 4. Affichage du résultat et de la catégorie
            binding.textViewImc.text = resultat.imcFormate
            binding.textViewCategorie.text = getString(resultat.categorieResId)

            couleurActuelleResId = resultat.couleurResId
            val couleur = ContextCompat.getColor(this, resultat.couleurResId)
            binding.textViewCategorie.setTextColor(couleur)

            // Effacer d'éventuelles erreurs précédentes sur les champs
            binding.editTextPoids.error = null
            binding.editTextTaille.error = null
        } catch (e: Exception) {
            Toast.makeText(this, e.message ?: "Erreur de calcul", Toast.LENGTH_LONG).show()
        }
    }

    /**
     * Réinitialise les champs de saisie, les résultats et replace le curseur sur le poids.
     */
    private fun effacerChamps() {
        binding.editTextPoids.text?.clear()
        binding.editTextTaille.text?.clear()
        binding.editTextPoids.error = null
        binding.editTextTaille.error = null

        binding.textViewImc.text = getString(R.string.valeur_imc_defaut)
        binding.textViewCategorie.text = getString(R.string.categorie_defaut)
        couleurActuelleResId = R.color.text_primary
        binding.textViewCategorie.setTextColor(ContextCompat.getColor(this, R.color.text_primary))

        // Replacer le focus dans le champ poids
        binding.editTextPoids.requestFocus()
    }

    override fun onSaveInstanceState(outState: Bundle) {
        super.onSaveInstanceState(outState)
        outState.putString(KEY_RESULTAT_IMC, binding.textViewImc.text.toString())
        outState.putString(KEY_RESULTAT_CAT, binding.textViewCategorie.text.toString())
        outState.putInt(KEY_RESULTAT_COULEUR, couleurActuelleResId)
    }
}
