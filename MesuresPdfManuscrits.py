# Conversion de mesures réalisées sur un pdf de manuscrit

hauteur_relle: float = input('Hauteur réelle du manuscrit = ')
hauteur_pdf: float = input('Hauteur du manuscrit sur le pdf = ')

mesure: str = 'vide'

while mesure != '!':
    mesure = input('Mesure sur le pdf = ')
    resultat: float = float(mesure) * hauteur_relle / floathauteur_pdf
    print('Mesure réelle = ',round(resultat, 1))
print('Fin')
