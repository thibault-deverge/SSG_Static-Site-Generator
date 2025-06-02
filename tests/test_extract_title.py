import unittest
import textwrap
from src.utils.extracters import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_single_h1_at_top(self):
        md = textwrap.dedent(
            """
            # Titre Principal

            Contenu du document.
        """
        )
        title = extract_title(md)
        self.assertEqual(title, "Titre Principal")

    def test_single_h1_with_surrounding_whitespace(self):
        md = textwrap.dedent(
            """

            #   Mon Titre Avec Espaces

            Du texte en dessous.
        """
        )
        title = extract_title(md)
        self.assertEqual(title, "Mon Titre Avec Espaces")

    def test_h1_not_at_top(self):
        md = textwrap.dedent(
            """
            Contenu initial.

            # Section Titre

            Autre contenu.
        """
        )
        title = extract_title(md)
        self.assertEqual(title, "Section Titre")

    def test_multiple_h1_raises(self):
        md = textwrap.dedent(
            """
            # Premier Titre
            # Deuxième Titre
        """
        )
        with self.assertRaises(Exception) as cm:
            extract_title(md)
        self.assertIn("must have one H1", str(cm.exception))

    def test_no_h1_raises(self):
        md = textwrap.dedent(
            """
            ## Pas un h1, un h2

            ### Pas non plus
        """
        )
        with self.assertRaises(Exception) as cm:
            extract_title(md)
        self.assertIn("must have one H1", str(cm.exception))

    def test_ignores_h2_and_h3(self):
        md = textwrap.dedent(
            """
            ## Sous-titre
            # H1 Valide
            ### Un autre sous-niveau
        """
        )
        title = extract_title(md)
        self.assertEqual(title, "H1 Valide")

    def test_h1_with_following_text_on_same_line(self):
        md = "#TitreSansEspace"
        with self.assertRaises(Exception):
            extract_title(md)

    def test_h1_with_extra_hashes(self):
        md = textwrap.dedent(
            """
            ### Pas un h1
            ## Non plus
            # Vrai H1
        """
        )
        title = extract_title(md)
        self.assertEqual(title, "Vrai H1")

    def test_h1_with_special_characters(self):
        md = "# Titre avec !@#€*()[] caractères spéciaux"
        title = extract_title(md)
        self.assertEqual(title, "Titre avec !@#€*()[] caractères spéciaux")
