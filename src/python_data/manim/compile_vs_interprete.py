from manim import *

# Couleurs personnalisées
CODE_COLOR = "#4A90D9"
COMPILER_COLOR = "#E67E22"
INTERPRETER_COLOR = "#27AE60"
BINARY_COLOR = "#8E44AD"
OUTPUT_COLOR = "#C0392B"
CPU_COLOR = "#34495E"


class CompileVsInterprete(Scene):
    def construct(self):
        # ======================================================
        # PARTIE 1 — TITRE
        # ======================================================
        titre = Text("Compilé vs Interprété", font_size=48, weight=BOLD)
        sous_titre = Text(
            "Comment un programme devient exécutable ?",
            font_size=28,
            color=GREY_B,
        ).next_to(titre, DOWN, buff=0.5)

        self.play(Write(titre))
        self.play(FadeIn(sous_titre, shift=UP))
        self.wait(2)
        self.play(FadeOut(titre), FadeOut(sous_titre))

        # ======================================================
        # PARTIE 2 — LANGAGE COMPILÉ
        # ======================================================
        titre_comp = Text("1. Langage compilé (C, C++)", font_size=36, weight=BOLD)
        titre_comp.to_edge(UP)
        self.play(Write(titre_comp))

        # Code source
        code_src = self._creer_fichier("code.c", CODE_COLOR, "int main() { ... }")
        code_src.shift(LEFT * 4 + DOWN * 0.5)
        self.play(FadeIn(code_src, shift=RIGHT))

        # Compilateur
        compilateur = self._creer_boite("Compilateur", COMPILER_COLOR, width=3, height=1.2)
        compilateur.move_to(DOWN * 0.5)
        self.play(FadeIn(compilateur, shift=RIGHT))

        # Flèche code -> compilateur
        fleche1 = Arrow(
            code_src.get_right(),
            compilateur.get_left(),
            buff=0.1,
            color=YELLOW,
        )
        label1 = Text("compilation", font_size=20, color=YELLOW).next_to(fleche1, UP, buff=0.1)
        self.play(GrowArrow(fleche1), FadeIn(label1))
        self.wait(1)

        # Binaire
        binaire = self._creer_fichier("programme.exe", BINARY_COLOR, "01001010...")
        binaire.shift(RIGHT * 4 + DOWN * 0.5)
        fleche2 = Arrow(
            compilateur.get_right(),
            binaire.get_left(),
            buff=0.1,
            color=YELLOW,
        )
        self.play(GrowArrow(fleche2), FadeIn(binaire, shift=LEFT))
        self.wait(1)

        # Exécution directe
        cpu = self._creer_boite("CPU", CPU_COLOR, width=2, height=1)
        cpu.shift(DOWN * 2.5 + RIGHT * 4)
        fleche3 = Arrow(
            binaire.get_bottom(),
            cpu.get_top(),
            buff=0.1,
            color=OUTPUT_COLOR,
        )
        label3 = Text("exécution", font_size=20, color=OUTPUT_COLOR).next_to(fleche3, RIGHT, buff=0.1)
        self.play(GrowArrow(fleche3), FadeIn(cpu), FadeIn(label3))
        self.wait(1)

        # Encadré "une seule fois"
        note_comp = Text(
            "Compilation : une seule fois, avant l'exécution",
            font_size=22,
            color=COMPILER_COLOR,
        ).to_edge(DOWN)
        self.play(Write(note_comp))
        self.wait(3)

        self.play(
            FadeOut(code_src), FadeOut(compilateur), FadeOut(binaire),
            FadeOut(cpu), FadeOut(fleche1), FadeOut(fleche2), FadeOut(fleche3),
            FadeOut(label1), FadeOut(label3), FadeOut(note_comp), FadeOut(titre_comp),
        )

        # ======================================================
        # PARTIE 3 — LANGAGE INTERPRÉTÉ
        # ======================================================
        titre_interp = Text("2. Langage interprété (Python)", font_size=36, weight=BOLD)
        titre_interp.to_edge(UP)
        self.play(Write(titre_interp))

        # Code source
        code_py = self._creer_fichier("code.py", CODE_COLOR, "print('hello')")
        code_py.shift(LEFT * 4 + DOWN * 0.5)
        self.play(FadeIn(code_py, shift=RIGHT))

        # Interpréteur
        interpreteur = self._creer_boite("Interpréteur\nPython", INTERPRETER_COLOR, width=3, height=1.5)
        interpreteur.move_to(DOWN * 0.5)
        self.play(FadeIn(interpreteur, shift=RIGHT))

        # Flèche code -> interpréteur
        fleche_i1 = Arrow(
            code_py.get_right(),
            interpreteur.get_left(),
            buff=0.1,
            color=YELLOW,
        )
        self.play(GrowArrow(fleche_i1))
        self.wait(0.5)

        # Boucle ligne par ligne
        lignes = VGroup(
            Text("ligne 1", font_size=18, color=WHITE),
            Text("ligne 2", font_size=18, color=WHITE),
            Text("ligne 3", font_size=18, color=WHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        lignes.next_to(interpreteur, RIGHT, buff=1.5)

        for ligne in lignes:
            fleche_lecture = Arrow(
                interpreteur.get_right(),
                ligne.get_left(),
                buff=0.1,
                color=INTERPRETER_COLOR,
                stroke_width=3,
            )
            self.play(GrowArrow(fleche_lecture), FadeIn(ligne), run_time=0.6)
            self.play(FadeOut(fleche_lecture), run_time=0.3)

        # Résultat
        resultat = self._creer_boite("Résultat", OUTPUT_COLOR, width=2.5, height=1)
        resultat.shift(DOWN * 2.5 + RIGHT * 4)
        fleche_i2 = Arrow(
            interpreteur.get_bottom(),
            resultat.get_top(),
            buff=0.1,
            color=OUTPUT_COLOR,
        )
        self.play(GrowArrow(fleche_i2), FadeIn(resultat))
        self.wait(1)

        # Encadré "à chaque exécution"
        note_interp = Text(
            "Interprétation : à chaque exécution, ligne par ligne",
            font_size=22,
            color=INTERPRETER_COLOR,
        ).to_edge(DOWN)
        self.play(Write(note_interp))
        self.wait(3)

        self.play(
            FadeOut(code_py), FadeOut(interpreteur), FadeOut(resultat),
            FadeOut(fleche_i1), FadeOut(fleche_i2), FadeOut(lignes),
            FadeOut(note_interp), FadeOut(titre_interp),
        )

        # ======================================================
        # PARTIE 4 — LA NUANCE (Java / JVM)
        # ======================================================
        titre_nuance = Text("3. La nuance : Java et la JVM", font_size=36, weight=BOLD)
        titre_nuance.to_edge(UP)
        self.play(Write(titre_nuance))

        # Code Java
        code_java = self._creer_fichier("code.java", CODE_COLOR, "public class ...")
        code_java.shift(LEFT * 5 + DOWN * 0.5)
        self.play(FadeIn(code_java, shift=RIGHT))

        # Compilateur Java
        comp_j = self._creer_boite("Compilateur\nJava", COMPILER_COLOR, width=2.5, height=1.5)
        comp_j.shift(LEFT * 1.5 + DOWN * 0.5)
        self.play(FadeIn(comp_j))

        # Bytecode
        bytecode = self._creer_fichier("bytecode", BINARY_COLOR, ".class")
        bytecode.shift(RIGHT * 2 + DOWN * 0.5)
        self.play(FadeIn(bytecode, shift=LEFT))

        # JVM
        jvm = self._creer_boite("JVM", INTERPRETER_COLOR, width=2, height=1.5)
        jvm.shift(RIGHT * 5 + DOWN * 0.5)
        self.play(FadeIn(jvm, shift=LEFT))

        # Flèches
        f1 = Arrow(code_java.get_right(), comp_j.get_left(), buff=0.1, color=YELLOW)
        f2 = Arrow(comp_j.get_right(), bytecode.get_left(), buff=0.1, color=YELLOW)
        f3 = Arrow(bytecode.get_right(), jvm.get_left(), buff=0.1, color=YELLOW)

        self.play(GrowArrow(f1))
        self.play(GrowArrow(f2))
        self.play(GrowArrow(f3))
        self.wait(1)

        note_nuance = Text(
            "Java compile une fois, puis la JVM interprète (ou compile à la volée)",
            font_size=20,
            color=GREY_B,
        ).to_edge(DOWN)
        self.play(Write(note_nuance))
        self.wait(4)

        self.play(
            FadeOut(code_java), FadeOut(comp_j), FadeOut(bytecode),
            FadeOut(jvm), FadeOut(f1), FadeOut(f2), FadeOut(f3),
            FadeOut(note_nuance), FadeOut(titre_nuance),
        )

    # ==========================================================
    # HELPERS
    # ==========================================================
    def _creer_fichier(self, titre, couleur, contenu):
        """Crée une représentation visuelle d'un fichier."""
        titre_txt = Text(titre, font_size=22, weight=BOLD, color=WHITE)
        contenu_txt = Text(contenu, font_size=18, color=GREY_B)
        inner = VGroup(titre_txt, contenu_txt).arrange(DOWN, buff=0.15)

        boite = Rectangle(
            width=3,
            height=1.5,
            color=couleur,
            stroke_width=3,
        )
        inner.move_to(boite.get_center())

        return VGroup(boite, inner)

    def _creer_boite(self, texte, couleur, width=2.5, height=1.2):
        """Crée une boîte avec un label centré."""
        boite = RoundedRectangle(
            width=width,
            height=height,
            corner_radius=0.15,
            color=couleur,
            stroke_width=3,
        )
        label = Text(texte, font_size=22, weight=BOLD, color=WHITE, line_spacing=1.2)
        label.move_to(boite.get_center())
        return VGroup(boite, label)
