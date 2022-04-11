## - Encoding: UTF-8 -*-
# changer pour changeurdimages

# Refactoriser pour lire le contenu de dossier

from tkinter import PhotoImage
# toutes les images devraient �tre ins�r�es ici

import os,os.path


def chargerimages2():
    images = {

        #teams
        'virus': PhotoImage(file='images/teams/virus.png'),
        'fungus': PhotoImage(file='images/teams/fungus.png'),
        'bacteria': PhotoImage(file='images/teams/bacteria.png'),
        'worm': PhotoImage(file='images/teams/worm.png'),

        # organes
        'coeur': PhotoImage(file='images/organe/coeur.png'),
        'cerveau': PhotoImage(file='images/organe/cerveau.png'),
        'poumon': PhotoImage(file='images/organe/poumon.png'),
        'reins': PhotoImage(file='images/organe/reins.png'),
        'intestins': PhotoImage(file='images/organe/intestin.png'),
        'foie': PhotoImage(file='images/organe/foie.png'),
        'estomac': PhotoImage(file='images/organe/estomac.png'),
        'oeil': PhotoImage(file='images/organe/oeil.png'),

        #ennemi
        "globrouges": PhotoImage(file='images/ennemi/globrouges.png'),
        # 'cellanimale': PhotoImage(file='images/ennemi/cellanimal.png'),
        "npc": PhotoImage(file="images/ennemi/npc.png"),

        #cellules blanches
        "monocyte": PhotoImage(file='images/cellblanc/monocyte.png'),
        'neutrophil': PhotoImage(file='images/cellblanc/neutrophil.png'),
        'lymphocyte': PhotoImage(file='images/cellblanc/lymphocyte.png'),

        #territoires
        't_virus': PhotoImage(file='images/territoire/t_virus.png'),
        't_fungus': PhotoImage(file='images/territoire/t_fungus.png'),
        't_bacteria': PhotoImage(file='images/territoire/t_bacteria.png'),
        't_worm': PhotoImage(file='images/territoire/t_worm.png'),

        #misc
        'seringue': PhotoImage(file='images/misc/seringe.png'),
        'dna': PhotoImage(file='images/misc/dna.png'),
        'beacon': PhotoImage(file='images/beacon/beacon.png'),

        #constructions
        'siteX': PhotoImage(file='images/divers/siteX.png'),
        'EnConstruction': PhotoImage(file='images/divers/EnConstruction.png'), #L
        'EnConstruction2': PhotoImage(file='images/divers/EnConstruction2.png'), #L

        #equipe virus
        'V_monocyte': PhotoImage(file='images/cellblanc/V_monocyte.png'),
        'V_neutrophil': PhotoImage(file='images/cellblanc/V_neutrophil.png'),
        'V_ballistaDH': PhotoImage(file='images/vert/V_ballistaDH.png'),
        'V_ballistaDB': PhotoImage(file='images/vert/V_ballistaDB.png'),
        'V_ballistaGH': PhotoImage(file='images/vert/V_ballistaGH.png'),
        'V_ballistaGB': PhotoImage(file='images/vert/V_ballistaGB.png'),
        'V_archerD': PhotoImage(file='images/vert/V_archerD.png'),
        'V_archerG': PhotoImage(file='images/vert/V_archerG.png'),
        'V_lymphocyte': PhotoImage(file='images/cellblanc/V_lymphocyte.png'),
        'V_chevalierD': PhotoImage(file='images/vert/V_chevalierD.png'),
        'V_chevalierG': PhotoImage(file='images/vert/V_chevalierG.png'),
        'V_druideD': PhotoImage(file='images/vert/V_druideD.png'),
        'V_druideG': PhotoImage(file='images/vert/V_druideG.png'),
        'V_maison': PhotoImage(file='images/vert/V_maison.png'),
        'V_ouvrierD': PhotoImage(file='images/vert/V_ouvrierD.png'),
        'V_ouvrierG': PhotoImage(file='images/vert/V_ouvrierG.png'),
        'V_soldatD': PhotoImage(file='images/vert/V_soldatD.png'),
        'V_soldatG': PhotoImage(file='images/vert/V_soldatG.png'),

        #equipe fungus
        'B_monocyte': PhotoImage(file='images/cellblanc/B_monocyte.png'),
        'B_neutrophil': PhotoImage(file='images/cellblanc/B_neutrophil.png'),
        'B_ballistaDH': PhotoImage(file='images/bleu/B_ballistaDH.png'),
        'B_ballistaDB': PhotoImage(file='images/bleu/B_ballistaDB.png'),
        'B_ballistaGH': PhotoImage(file='images/bleu/B_ballistaGH.png'),
        'B_ballistaGB': PhotoImage(file='images/bleu/B_ballistaGB.png'),
        'B_archerD': PhotoImage(file='images/bleu/B_archerD.png'),
        'B_archerG': PhotoImage(file='images/bleu/B_archerG.png'),
        'B_lymphocyte': PhotoImage(file='images/cellblanc/B_lymphocyte.png'),
        'B_chevalierD': PhotoImage(file='images/bleu/B_chevalierD.png'),
        'B_chevalierG': PhotoImage(file='images/bleu/B_chevalierG.png'),
        'B_druideD': PhotoImage(file='images/bleu/B_druideD.png'),
        'B_druideG': PhotoImage(file='images/bleu/B_druideG.png'),
        'B_maison': PhotoImage(file='images/bleu/B_maison.png'),
        'B_ouvrierD': PhotoImage(file='images/bleu/B_ouvrierD.png'),
        'B_ouvrierG': PhotoImage(file='images/bleu/B_ouvrierG.png'),
        'B_soldatD': PhotoImage(file='images/bleu/B_soldatD.png'),
        'B_soldatG': PhotoImage(file='images/bleu/B_soldatG.png'),

        #equipe worm
        'R_monocyte': PhotoImage(file='images/cellblanc/R_monocyte.png'),
        'R_neutrophil': PhotoImage(file='images/cellblanc/R_neutrophil.png'),
        'R_ballistaDH': PhotoImage(file='images/rouge/R_ballistaDH.png'),
        'R_ballistaDB': PhotoImage(file='images/rouge/R_ballistaDB.png'),
        'R_ballistaGH': PhotoImage(file='images/rouge/R_ballistaGH.png'),
        'R_ballistaGB': PhotoImage(file='images/rouge/R_ballistaGB.png'),
        'R_archerD': PhotoImage(file='images/rouge/R_archerD.png'),
        'R_archerG': PhotoImage(file='images/rouge/R_archerG.png'),
        'R_lymphocyte': PhotoImage(file='images/cellblanc/R_lymphocyte.png'),
        'R_chevalierD': PhotoImage(file='images/rouge/R_chevalierD.png'),
        'R_chevalierG': PhotoImage(file='images/rouge/R_chevalierG.png'),
        'R_druideD': PhotoImage(file='images/rouge/R_druideD.png'),
        'R_druideG': PhotoImage(file='images/rouge/R_druideG.png'),
        'R_maison': PhotoImage(file='images/rouge/R_maison.png'),
        'R_ouvrierD': PhotoImage(file='images/rouge/R_ouvrierD.png'),
        'R_ouvrierG': PhotoImage(file='images/rouge/R_ouvrierG.png'),
        'R_soldatD': PhotoImage(file='images/rouge/R_soldatD.png'),
        'R_soldatG': PhotoImage(file='images/rouge/R_soldatG.png'),

        #equipe bacterie
        'J_monocyte': PhotoImage(file='images/cellblanc/J_monocyte.png'),
        'J_neutrophil': PhotoImage(file='images/cellblanc/J_neutrophil.png'),
        'J_ballistaDH': PhotoImage(file='images/jaune/J_ballistaDH.png'),
        'J_ballistaDB': PhotoImage(file='images/jaune/J_ballistaDB.png'),
        'J_ballistaGH': PhotoImage(file='images/jaune/J_ballistaGH.png'),
        'J_ballistaGB': PhotoImage(file='images/jaune/J_ballistaGB.png'),
        'J_archeG': PhotoImage(file='images/jaune/J_archeG.png'),
        'J_archerD': PhotoImage(file='images/jaune/J_archerD.png'),
        'J_lymphocyte': PhotoImage(file='images/cellblanc/W_lymphocyte.png'),
        'J_chevalierD': PhotoImage(file='images/jaune/J_chevalierD.png'),
        'J_chevalierG': PhotoImage(file='images/jaune/J_chevalierG.png'),
        'J_druideD': PhotoImage(file='images/jaune/J_druideD.png'),
        'J_druideG': PhotoImage(file='images/jaune/J_druideG.png'),
        'J_maison': PhotoImage(file='images/jaune/J_maison.png'),
        'J_ouvrierD': PhotoImage(file='images/jaune/J_ouvrierD.png'),
        'J_ouvrierG': PhotoImage(file='images/jaune/J_ouvrierG.png'),
        'J_soldatD': PhotoImage(file='images/jaune/J_soldatD.png'),
        'J_soldatG': PhotoImage(file='images/jaune/J_soldatG.png'),

        ########################## TO BE WORKED ON IMAGES/OBJECTS ##########################
        ############## weapon

        'flecheGH': PhotoImage(file='images/divers/flecheGH.png'),
        'flecheGB': PhotoImage(file='images/divers/flecheGB.png'),
        'flecheDH': PhotoImage(file='images/divers/flecheDH.png'),
        'flecheDB': PhotoImage(file='images/divers/flecheDB.png'),
        'javelotGH': PhotoImage(file='images/divers/javelotGH.png'),
        'javelotGB': PhotoImage(file='images/divers/javelotGB.png'),
        'javelotDH': PhotoImage(file='images/divers/javelotDH.png'),
        'javelotDB': PhotoImage(file='images/divers/javelotDB.png'),

        ############# globule rouge
        'daimMORT': PhotoImage(file='images/animal/daimMORT.png'),
        'daimDB': PhotoImage(file='images/ennemi/bloodcell.png'),
        'daimDH': PhotoImage(file='images/ennemi/bloodcell.png'),
        'daimGB': PhotoImage(file='images/ennemi/bloodcell.png'),
        'daimGH': PhotoImage(file='images/ennemi/bloodcell.png'),
    }
    return images

images = {}


def chargerimages(chemin=None):
    if chemin==None:
        chemin=os.getcwd()
        chemin=chemin+"\\images"
    for i in os.listdir(chemin):
        che=chemin+"\\"+i
        if os.path.isdir(che):
            chargerimages(che)
        else:
            nom, ext=os.path.splitext(os.path.basename(i))
            if ".png"==ext:
                    images[nom]=PhotoImage(file=che) #.replace("\\","/")
    return images


def chargergifs():
    gifs = {}
    lesgifs = ["poissons.gif", "marche.gif"]
    for nom in lesgifs:
        listeimages = []
        testverite = 1
        noindex = 0
        while testverite:
            try:
                img = PhotoImage(file='./images/GIFS/' + nom, format="gif -index " + str(noindex))
                listeimages.append(img)
                noindex += 1
            except Exception:
                gifs[nom[:-4]] = listeimages
                testverite = 0
    return gifs


if __name__ == '__main__':
    images=chargerimages()

    for i in images.keys():
            print(i,images[i])

#asdsadsad