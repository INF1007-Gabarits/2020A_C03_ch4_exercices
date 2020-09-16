#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import unittest

import exercice


class TestExercice(unittest.TestCase):
    def test_pair(self):
        values = ["hey jad!", "abcdefg", "0"]

        output = [exercice.is_even_len(v) for v in values]
        answer = [len(v) % 2 == 0 for v in values]

        self.assertListEqual(
            output,
            answer,
            'Mauvaise identification de la parité de la longueur de la chaine'
        )

    def test_remove_third_char(self):
        values = ["hey jad!", "abcdefg", "01234"]

        output = [exercice.remove_third_char(v) for v in values]
        answer = [v[0:2] + v[3:] for v in values]

        self.assertListEqual(
            output,
            answer,
            'Retrait du mauvais caractère'
        )

    def test_replace_char(self):
        values = [
            ("hey jad!", "j", "y"),
            ("aaaaab", "a", "b"),
            ("01234", "0", "a")
        ]

        output = [exercice.replace_char(v[0], v[1], v[2]) for v in values]
        answer = [v[0].replace(v[1], v[2]) for v in values]

        self.assertListEqual(
            output,
            answer,
            'Erreur dans le remplacement de caractère'
        )
    
    def test_get_nb_char(self):
        values = [
            ("aaaa123", "a"),
            ("athse wqc re", "s"),
            ("aaaa", "x")
        ]

        output = [exercice.get_nb_char(v[0], v[1]) for v in values]
        answer = [v[0].count(v[1]) for v in values]

        self.assertListEqual(
            output,
            answer,
            "Mauvais calcul du nombre d'occurences du caractère"
        )

    def test_get_nb_words(self):
        values = [
            ("Comment allez vous aller chez vous"),
            ("Bonjour hello ok salut merci"),
            ("The 2006 Subway 500 was the 32nd stock car race of the 2006 NASCAR Nextel Cup Series and the sixth in the ten-race Chase for the Nextel Cup.")
        ]

        output = [exercice.get_nb_words(v[0], v[1]) for v in values]
        answer = [len(v.split()) for v in values]

        self.assertListEqual(
            output,
            answer,
            "Mauvais calcul du nombre de mots dans une phrase."
        )


if __name__ == '__main__':
    if not os.path.exists('logs'):
        os.mkdir('logs')
    with open('logs/tests_results.txt', 'w') as f:
        loader = unittest.TestLoader()
        suite = loader.loadTestsFromModule(sys.modules[__name__])
        unittest.TextTestRunner(f, verbosity=2).run(suite)