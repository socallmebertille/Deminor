

"""Premier exemple avec Tkinter.

On crée une fenêtre simple qui souhaite la bienvenue à l'utilisateur.

"""

# On importe Tkinter
from tkinter import *
from random import randrange


def Jouer(x, y) :
    global tresors_trouves
    global scoreA
    global scoreB
    global num
    global Joueur

    
    # print("Joueur = "+Joueur+"  score joueur A = "+str(scoreA)+"   score joueur B = "+str(scoreB)+"   num = "+str(num))

    if(my_grid[x][y]==0):
        boutons[x][y].config(background="black", text=str(my_grid[x][y]))
        if (Joueur=="A"):
            scoreA = scoreA+36
        elif (Joueur=="B"):
            scoreB=scoreB+36
        tresors_trouves += 1
    elif(my_grid[x][y]==1)or(my_grid[x][y]==2):
        boutons[x][y].config(background="red", text=str(my_grid[x][y]))
        if (Joueur=="A"):
            scoreA=scoreA+25
        elif (Joueur=="B"):
            scoreB=scoreB+25
    elif(my_grid[x][y]==3)or(my_grid[x][y]==4)or(my_grid[x][y]==5):
        boutons[x][y].config(background="yellow", text=str(my_grid[x][y]))
        if (Joueur=="A"):
            scoreA=scoreA+16
        elif (Joueur=="B"):
            scoreB=scoreB+16
    elif(my_grid[x][y]==6)or(my_grid[x][y]==7)or(my_grid[x][y]==8)or(my_grid[x][y]==9):
        boutons[x][y].config(background="green", text=str(my_grid[x][y]))
        if (Joueur=="A"):
            scoreA=scoreA+9
        elif (Joueur=="B"):
            scoreB=scoreB+9
    elif(my_grid[x][y]==10)or(my_grid[x][y]==11)or(my_grid[x][y]==12)or(my_grid[x][y]==13)or(my_grid[x][y]==14):
        boutons[x][y].config(background="blue", text=str(my_grid[x][y]))
        if (Joueur=="A"):
            scoreA=scoreA+4
        elif (Joueur=="B"):
            scoreB=scoreB+4
    elif(my_grid[x][y]>=15):
        boutons[x][y].config(background="grey", text=str(my_grid[x][y]))
        if (Joueur=="A"):
            scoreA=scoreA+1
        elif (Joueur=="B"):
            scoreB=scoreB+1
    boutons[x][y].config(state=DISABLED)

    if (num==0):
        num=num+1
        Joueur="B"
    elif (num==1):
        num=num+1
    elif (num==2)and(Joueur=="A"):
        num=1
        Joueur="B"
    elif (num==2)and(Joueur=="B"):
        num=1
        Joueur="A"

    global Label22
    global Label24
    global Label25
    Label22.configure(text=Joueur)
    Label24.configure(text=str(scoreA))
    Label25.configure(text=str(scoreB))

    # Vérifier si tous les trésors sont trouvés
    if tresors_trouves >= tresors:
        for ligne in range(lignes):
            for colonne in range(colonnes):
                boutons[ligne][colonne].config(state=DISABLED)
        from tkinter import messagebox
        if scoreA > scoreB:
            gagnant = PlayerA.get()
        elif scoreB > scoreA:
            gagnant = PlayerB.get()
        else:
            gagnant = "Égalité !"
        message = (
            f"Tous les trésors ont été trouvés !\n"
            f"Score {PlayerA.get()} : {scoreA}\n"
            f"Score {PlayerB.get()} : {scoreB}\n"
            f"Gagnant : {gagnant}"
        )
        messagebox.showinfo("Fin de partie", message)
        # Fermer la fenêtre de jeu
        Mafenetre2.destroy()

def CreerGrille():

    global colonnes 
    colonnes = int(nb_cols.get())
    global lignes 
    lignes = int(nb_rows.get())
    global tresors 
    tresors = int(nb_goals.get())
    global my_grid 
    my_grid = [] #creation de la grille
    big_grid=[]

    #def de la taille de la grille de jeu
    for i in range(lignes):
        my_grid.append([15] * colonnes) 

    for i in range(lignes+2):
        big_grid.append([15] * (colonnes+2)) 
    
    #placement des tresors au hasard dans la grille
    for k in range(tresors):
        my_grid[randrange(0, lignes,1)][randrange(0, colonnes,1)]=0
    
    for i in range(1,lignes+1):
        for j in range(1,colonnes+1):
            big_grid[i][j]=my_grid[i-1][j-1]

    
    #on definit la distance de chaque endroit au tresor
    for d in range(9):
        for i in range(1,lignes+1):
            for j in range(1, colonnes+1):
                if(big_grid[i-1][j]==d)or(big_grid[i][j-1]==d)or(big_grid[i+1][j]==d)or(big_grid[i][j+1]==d):
                    if (big_grid[i][j]>d)and(big_grid[i][j]!=0):
                        big_grid[i][j]=d+1

    for i in range(1,lignes+1):
        for j in range(1,colonnes+1):
            my_grid[i-1][j-1]=big_grid[i][j]


def LancerJeu():
    global Mafenetre2
    Mafenetre2 = Tk()
    Mafenetre2.title('DEMINOR')
    global tresors_trouves
    tresors_trouves = 0 

    CreerGrille()

    # Frame pour l'affichage des infos joueurs et scores
    info_frame = Frame(Mafenetre2, bg="#FFF")
    info_frame.pack(pady=10)

    # Nom joueur A
    label_playerA = Label(info_frame, text=PlayerA.get(), font=('Arial', 12, 'bold'), bg="#FFF", fg="maroon")
    label_playerA.grid(row=0, column=0, padx=10)

    # Score joueur A
    label_scoreA = Label(info_frame, text="0", font=('Arial', 12), bg="#FFF")
    label_scoreA.grid(row=0, column=1, padx=10)

    # Tour (A ou B)
    label_turn = Label(info_frame, text="A", font=('Arial', 12, 'bold'), bg="#000", fg="#FFF", width=5)
    label_turn.grid(row=0, column=2, padx=10)

    # Score joueur B
    label_scoreB = Label(info_frame, text="0", font=('Arial', 12), bg="#FFF")
    label_scoreB.grid(row=0, column=3, padx=10)

    # Nom joueur B
    label_playerB = Label(info_frame, text=PlayerB.get(), font=('Arial', 12, 'bold'), bg="#FFF", fg="maroon")
    label_playerB.grid(row=0, column=4, padx=10)

    # Pour pouvoir modifier ces labels dans Jouer()
    global Label22, Label24, Label25
    Label22 = label_turn
    Label24 = label_scoreA
    Label25 = label_scoreB

    global scoreA
    global scoreB
    scoreA = scoreB = 0
    
    
    global Joueur
    Joueur="A"

    global num
    num=0

    # texte_jeu = Canvas(Mafenetre2, bg="white", highlightbackground="white")
    # texte_jeu.pack()
    grille_jeu = Canvas(Mafenetre2, bg = "white", highlightbackground = "white")
    grille_jeu.pack()
    
    global boutons 
    boutons = []
    for i in range(lignes):
        boutons.append([Button] * (colonnes)) 

    for ligne in range(lignes):
       for colonne in range(colonnes):
            boutons[ligne][colonne] = Button(grille_jeu, width = 2, height = 1, bg = "grey", relief = "flat", command =lambda x=ligne, y=colonne: Jouer(x,y) )
            boutons[ligne][colonne].grid(row = ligne+2, column = colonne+1, padx = 3, pady = 3, in_ = grille_jeu)

    Mafenetre2.mainloop()

# Création de la fenêtre principale (main window)
Mafenetre = Tk()
Mafenetre.title('DEMINOR')
Mafenetre.configure(bg='#FFF')

# Frame pour le titre
fr1 = Frame(Mafenetre, bg='#FFF')
fr1.pack(pady=10)
Label(fr1, text='CONFIGURATION', bg='#000', fg='#FFF', font=('Arial', 14, 'bold'), width=30).pack()

# Frame pour les champs de configuration
fr2 = Frame(Mafenetre, bg='#FFF')
fr2.pack(padx=20, pady=10)

Label(fr2, text='Name of Player A :', bg='#FFF').grid(row=0, column=0, sticky='e', pady=5)
PlayerA = StringVar()
Champ1 = Entry(fr2, textvariable=PlayerA, bg='bisque', fg='maroon')
Champ1.grid(row=0, column=1, pady=5)
Champ1.focus_set()

Label(fr2, text='Name of Player B :', bg='#FFF').grid(row=1, column=0, sticky='e', pady=5)
PlayerB = StringVar()
Champ2 = Entry(fr2, textvariable=PlayerB, bg='bisque', fg='maroon')
Champ2.grid(row=1, column=1, pady=5)

Label(fr2, text='Number of rows :', bg='#FFF').grid(row=2, column=0, sticky='e', pady=5)
nb_rows = StringVar()
nb_rows.set(18)
rows = Scale(fr2, from_=12, to=24, orient=HORIZONTAL, length=200, width=15, variable=nb_rows, bg='#FFF')
rows.grid(row=2, column=1, pady=5)

Label(fr2, text='Number of cols :', bg='#FFF').grid(row=3, column=0, sticky='e', pady=5)
nb_cols = StringVar()
nb_cols.set(24)
cols = Scale(fr2, from_=12, to=36, orient=HORIZONTAL, length=200, width=15, variable=nb_cols, bg='#FFF')
cols.grid(row=3, column=1, pady=5)

Label(fr2, text='Number of goals :', bg='#FFF').grid(row=4, column=0, sticky='e', pady=5)
nb_goals = StringVar()
nb_goals.set(1)
goals = Scale(fr2, from_=1, to=12, orient=HORIZONTAL, length=200, width=15, variable=nb_goals, bg='#FFF')
goals.grid(row=4, column=1, pady=5)

# Frame pour le bouton
fr3 = Frame(Mafenetre, bg='#FFF')
fr3.pack(pady=10)
Bouton = Button(fr3, text='START', bg='#000', fg='#FFF', width=20, command=LancerJeu)
Bouton.pack()

Mafenetre.mainloop()

