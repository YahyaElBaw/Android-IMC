package com.example.calculimc

import java.util.Locale

/**
 * Modèle représentant le résultat du calcul d'IMC.
 */
data class ImcResult(
    val imc: Double,
    val imcFormate: String,
    val categorieResId: Int,
    val couleurResId: Int
)

/**
 * Objet utilitaire pour le calcul et l'interprétation de l'Indice de Masse Corporelle (IMC).
 * Implémenté de façon claire et modulaire pour faciliter l'apprentissage étudiant et les tests unitaires.
 */
object ImcCalculator {

    /**
     * Calcule l'IMC selon la formule : poids / (taille * taille)
     * et détermine la catégorie et la couleur associée.
     *
     * @param poidsKg Poids en kilogrammes (doit être > 0)
     * @param tailleM Taille en mètres (doit être > 0)
     * @return ImcResult contenant la valeur calculée, la catégorie et la couleur
     * @throws IllegalArgumentException si le poids ou la taille sont inférieurs ou égaux à 0
     */
    fun calculer(poidsKg: Double, tailleM: Double): ImcResult {
        require(poidsKg > 0) { "Le poids doit être strictement supérieur à 0." }
        require(tailleM > 0) { "La taille doit être strictement supérieure à 0." }

        val imc = poidsKg / (tailleM * tailleM)
        // Arrondi à deux chiffres après la virgule
        val imcFormate = String.format(Locale.US, "%.2f", imc)
        val imcArrondi = imcFormate.toDouble()

        val (categorieResId, couleurResId) = when {
            imcArrondi < 18.5 -> Pair(R.string.cat_insuffisance, R.color.imc_insuffisance)
            imcArrondi < 25.0 -> Pair(R.string.cat_normale, R.color.imc_normale)
            imcArrondi < 30.0 -> Pair(R.string.cat_surpoids, R.color.imc_surpoids)
            imcArrondi < 35.0 -> Pair(R.string.cat_obesite_moderee, R.color.imc_obesite_moderee)
            imcArrondi < 40.0 -> Pair(R.string.cat_obesite_severe, R.color.imc_obesite_severe)
            else -> Pair(R.string.cat_obesite_morbide, R.color.imc_obesite_morbide)
        }

        return ImcResult(
            imc = imcArrondi,
            imcFormate = imcFormate,
            categorieResId = categorieResId,
            couleurResId = couleurResId
        )
    }
}
