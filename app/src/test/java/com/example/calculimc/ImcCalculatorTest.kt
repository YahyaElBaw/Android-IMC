package com.example.calculimc

import org.junit.Assert.assertEquals
import org.junit.Assert.assertThrows
import org.junit.Test

/**
 * Tests unitaires validant l'ensemble des scénarios de test imposés par le TP Android Studio Calcul IMC.
 */
class ImcCalculatorTest {

    @Test
    fun testCas1_CorpulenceNormale() {
        // 70 kg et 1,75 m -> 22,86 environ, Corpulence normale
        val res = ImcCalculator.calculer(70.0, 1.75)
        assertEquals("22.86", res.imcFormate)
        assertEquals(R.string.cat_normale, res.categorieResId)
        assertEquals(R.color.imc_normale, res.couleurResId)
    }

    @Test
    fun testCas2_InsuffisancePonderale() {
        // 50 kg et 1,75 m -> 16,33 environ, Insuffisance pondérale
        val res = ImcCalculator.calculer(50.0, 1.75)
        assertEquals("16.33", res.imcFormate)
        assertEquals(R.string.cat_insuffisance, res.categorieResId)
        assertEquals(R.color.imc_insuffisance, res.couleurResId)
    }

    @Test
    fun testCas3_Surpoids() {
        // 85 kg et 1,70 m -> 29,41 environ, Surpoids
        val res = ImcCalculator.calculer(85.0, 1.70)
        assertEquals("29.41", res.imcFormate)
        assertEquals(R.string.cat_surpoids, res.categorieResId)
        assertEquals(R.color.imc_surpoids, res.couleurResId)
    }

    @Test
    fun testCas4_ObesiteModeree() {
        // 100 kg et 1,70 m -> 34,60 environ, Obésité modérée
        val res = ImcCalculator.calculer(100.0, 1.70)
        assertEquals("34.60", res.imcFormate)
        assertEquals(R.string.cat_obesite_moderee, res.categorieResId)
        assertEquals(R.color.imc_obesite_moderee, res.couleurResId)
    }

    @Test
    fun testCas5_PoidsOuTailleInvalide() {
        assertThrows(IllegalArgumentException::class.java) {
            ImcCalculator.calculer(-5.0, 1.75)
        }
        assertThrows(IllegalArgumentException::class.java) {
            ImcCalculator.calculer(70.0, 0.0)
        }
    }
}
