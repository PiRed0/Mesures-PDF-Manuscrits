# Conversion de mesures réalisées sur un pdf de manuscrit

hauteurRelle = input('Hauteur réelle du manuscrit = ')
hauteurPDF = input('Hauteur du manuscrit sur le pdf = ')

mesure = 'vide'

while mesure != '!':
    mesure = input('Mesure sur le pdf = ')
    resultat = float(mesure) * float(hauteurRelle) / float(hauteurPDF)
    print('Mesure réelle = ' + str(round(resultat, 1)))
print('Fin')
