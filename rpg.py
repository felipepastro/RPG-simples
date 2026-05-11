import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random, time, pygame
pygame.init()
pygame.mixer.init()

nomee = ""
classe = ""
Dificuldade = ""

def habilidade_guerreiro_jogador():
    global vidainimigo, inimigovaierrar
    inimigovaierrar = True
    vidainimigo -= forhabjogador
def habilidade_arqueiro():
    global vidainimigo
    vidainimigo -= forhabjogador
    if random.random() < 0.25:
        vidainimigo *= 0.3
def habilidade_mago():
    global vidainimigo, inimigovaierrar
    inimigovaierrar = True
    vidainimigo -= forhabjogador
def habilidade_zoio_jogador():
    global vidainimigo, forcainimigo
    vidainimigo -= forhabjogador
    forcainimigo *= 0.1
def habilidade_alek_jogador():
    global vidainimigo, forcainimigo
    vidainimigo -= forhabjogador
    if personagembot == "Proerd":
        forcainimigo *= 0.75
    else:
        forcainimigo *= 0.5
def habilidade_proerd_jogador():
    global vidainimigo, inimigovaierrar
    vidainimigo -= forhabjogador
    if personagembot == "Capitão Pátria" or personagembot == "Alek":
        vidainimigo -= 10
    if random.random() < 0.7:
        inimigovaierrar = True
def habilidade_hatsunemiku():
    global vidainimigo, inimigovaierrar
    vidainimigo -= forhabjogador
    if random.random() < 0.9:
        inimigovaierrar = True
def habilidade_capitaopatria_jogador():
    global vidainimigo
    vidainimigo -= forhabjogador
    contador = 1
    while contador <= 5:
        time.sleep(1)
        vidainimigo -= 5
        contador += 1
def habilidade_manuelgomes():
    global forcainimigo, forhabinimigo, vidainimigo
    vidainimigo -= forhabjogador
    forhabinimigo -= 5
    forcainimigo -= 5
def habilidade_dilma_jogador():
    global jogadordesviou, vidainimigo
    vidainimigo -= forhabjogador
    jogadordesviou = True
def habilidade_alek_bot():
    global vidajogador, forcajogador
    vidajogador -= forhabinimigo
    if classe == "Proerd":
        forcajogador *= 0.75
    else:
        forcajogador *= 0.5
def habilidade_dilma_bot():
    global botdesviou, vidajogador
    vidajogador -= forcainimigo
    botdesviou = True
def habilidade_guerreiro_bot():
    global vidajogador, jogadorvaierrar
    jogadorvaierrar = True
    vidajogador -= forhabinimigo
def habilidade_proerd_bot():
    global vidajogador, jogadorvaierrar
    vidajogador -= forhabinimigo
    if classe == "Capitão Pátria" or classe == "Alek":
        vidajogador -= 10
    if random.random() < 0.7:
        jogadorvaierrar = True
def habilidade_zoio_bot():
    global vidajogador, forcajogador
    vidajogador -= forhabinimigo
    forcajogador *= 0.1
def habilidade_capitaopatria_bot():
    global vidajogador
    vidajogador -= forhabinimigo
    contador = 1
    while contador <= 5:
        time.sleep(1)
        vidajogador -= 5
        contador += 1

habilidade_bot = {"Alek": habilidade_alek_bot,
                  "Dilma": habilidade_dilma_bot,
                  "Guerreiro": habilidade_guerreiro_bot,
                  "Proerd": habilidade_proerd_bot,
                  "Zoio": habilidade_zoio_bot,
                  "Capitão Pátria": habilidade_capitaopatria_bot
                  }

# Nome da classe, Vida, Força, Habilidade Especial, Força da habilidade, Efeito da Habilidade, fotonormal, fotohabilidade, Som habilidade, funcao habilidade
classes = {
        "Guerreiro": {"Vida": 80, "Força": 60, "Habilidade Especial": "Faca Venenosa", "Força da Habilidade": 8, "Efeito da Habilidade": "Inimigo Errar a habilidade na próxima jogada", "fotonormal": "imagens\imagem guerreiro.png", "fotohabilidade": "imagens\Guerreiro habilidade.png", "Som Habilidade": r"sons/outros.mp3", "funcao habilidade": habilidade_guerreiro_jogador},
        "Arqueiro": {"Vida": 60, "Força": 70, "Habilidade Especial": "Flecha dupla", "Força da Habilidade": 10, "Efeito da Habilidade": r"25% de chance de tirar 70% da vida do inimigo", "fotonormal": "imagens\imagem arqueiro.png", "fotohabilidade": "imagens\Arqueiro habilidade.png", "Som Habilidade": r"sons/crq.mp3", "funcao habilidade": habilidade_arqueiro},
        "Mago": {"Vida": 50, "Força": 35, "Habilidade Especial": "Raio das Trevas", "Força da Habilidade": 30, "Efeito da Habilidade": "Inimigo perde a próxima jogada", "fotonormal": "imagens\imagem mago.png", "fotohabilidade": "imagens\mago habilidade.png", "Som Habilidade": r"sons/clash-royale-evo-wizard_o6x7iWd.mp3", "funcao habilidade": habilidade_mago},
        "Zoio": {"Vida": 70, "Força":75, "Habilidade Especial": "Marreta", "Força da Habilidade": 15, "Efeito da Habilidade": r"Inimigo perde 90% da força de ataque na proxima jogada", "fotonormal": "imagens\zoio normal.png", "fotohabilidade": "imagens\Zoio habilidade especial.png", "Som Habilidade": r"sons/everson-zoio-e-a-sua-ultima-marreta.mp3", "funcao habilidade": habilidade_zoio_jogador},
        "Alek": {"Vida":45, "Força": 30, "Habilidade Especial": "Fumaça", "Força da Habilidade": 35, "Efeito da Habilidade": r"Inimigo perde 50% da força na proxima(proerd 25%)", "fotonormal": "imagens\Alek normal.png", "fotohabilidade": "imagens\Alek habilidade especial.png", "Som Habilidade": r"sons/Audio-alek.mp3", "funcao habilidade": habilidade_alek_jogador},
        "Proerd": {"Vida": 85, "Força": 55, "Habilidade Especial": "Combater noia", "Força da Habilidade": 12, "Efeito da Habilidade": r"Causa 10 a mais de dano em personagem usuarios e 70% do inimigo errar o proximo golpe", "fotonormal": "imagens\proerdnormal.png", "fotohabilidade": "imagens\Proerd habilidade.png", "Som Habilidade": r"sons/proerd.mp3", "funcao habilidade": habilidade_proerd_jogador},
        "Hatsune Miku": {"Vida": 55, "Força": 35, "Habilidade Especial": "Ipnotização de gado", "Força da Habilidade": 28, "Efeito da Habilidade": r"ipnotiza o adversario fazendo ter 90% de chance de errar", "fotonormal": "imagens\HatsuneMikunormal.png", "fotohabilidade": "imagens\Hatsune Miku habilidade.png", "Som Habilidade": r"sons/hatsune-miku-gasolina.mp3", "funcao habilidade": habilidade_hatsunemiku},
        "Capitão Pátria": {"Vida": 75, "Força":70, "Habilidade Especial": "Raio Lazer", "Força da Habilidade": 25, "Efeito da Habilidade": r"coloca fogo no inimigo fazendo ele perder -5 vida/s por 5 segundos", "fotonormal": "imagens\capitao patria.png", "fotohabilidade": "imagens\capitao patria habilidade.png", "Som Habilidade": r"sons/olha-pra-cara-de-voces-capitao-patria.mp3", "funcao habilidade": habilidade_capitaopatria_jogador},
        "Manuel Gomes": {"Vida": 60, "Força": 45, "Habilidade Especial": "Caneta Azul", "Força da Habilidade": 25, "Efeito da Habilidade": "faz o adversário perder 5 de dano(geral) na proxima jogada", "fotonormal": "imagens\manuelgomes.png", "fotohabilidade": "imagens\manuelgomes habilidade.png", "Som Habilidade": r"sons/caneta-azul-refrao.mp3", "funcao habilidade": habilidade_manuelgomes},
        "Dilma": {"Vida": 65, "Força": 30, "Habilidade Especial": "Desvio", "Força da Habilidade": 25, "Efeito da Habilidade": "desvia de qualquer ataque do inimigo na proxima jogada", "fotonormal": "imagens\dilma.png", "fotohabilidade": "imagens\Dilma habilidade.png", "Som Habilidade": r"sons/dilma_4.mp3", "funcao habilidade": habilidade_dilma_jogador}
    }

Dificuldades = {"Muito Fácil": {"Personagem": "Alek"},
                "Fácil": {"Personagem": "Dilma"},
                "Médio": {"Personagem": "Guerreiro"},
                "Difícil": {"Personagem": "Proerd"},
                "Muito difícil": {"Personagem": "Zoio"},
                "Impossível": {"Personagem": "Capitão Pátria"}
                }

def janelaregras():
    janeladasregras = tk.Toplevel()
    janeladasregras.title("Regras do RPG")
    janeladasregras.geometry("720x500")
    janeladasregras.config(bg="black")
    textoregras = """
    Regras do RPG
    1 - Não use xit
    2 - Sem xingamentus!
    3 - Escreva direito
    4 - IMPORTANTE: Não se preucupe com o minerador de bitcoin no seu computador!!!
    Clique no botão abaixo para aceitar as regras!
    """

    def aceitar_regras():
        messagebox.showinfo("Regras aceitas", "Você aceitou as regras! não se preucupe com o spyware")
        janeladasregras.destroy()

    Labelregras = tk.Label(janeladasregras, text=textoregras, justify="left", bg="black", fg="white", font=("Comic Sans MS", 12, "normal"), padx=10, pady=10)
    Labelregras.pack()

    botao_aceitar_regras = tk.Button(janeladasregras, text="Aceitar Regras(não vai matar seu pc :)", font=("Comic Sans MS", 12, "normal"), fg="white", bg="black", command=aceitar_regras)
    botao_aceitar_regras.pack(pady=50)

def janelaclasses():
    janeladasclasses = tk.Toplevel()
    janeladasclasses.title("Escolher Classes")
    janeladasclasses.geometry("720x520")
    janeladasclasses.config(bg="black")

    textodasclasses = """
    Escolha um Nome para seu Personagem e sua respectiva Classe
    """
    def confirmar_info():
        global nomee, classe
        nome = digitar_nome.get()

        selecao = listaclasses.curselection()
        indice = selecao[0]
        classe_escolhida = listaclasses.get(indice)
        if nome != "":
            messagebox.showinfo("Sucesso!", "Nome e Classe escolhidas com sucesso!")
            janeladasclasses.destroy()
            nomee = nome
            classe = classe_escolhida
        else:
            messagebox.showwarning("NOME", "Coloque um nome para o seu Personagem!")

    labelclasses = tk.Label(janeladasclasses, text=textodasclasses, justify="center", bg="black", fg="white", font=("Comic Sans MS", 12, "normal"), padx=10, pady=10)
    labelclasses.pack()

    # Espaço para escrever o nome
    digitar_nome = tk.Entry(janeladasclasses, font=("Comic Sans MS", 12, "normal"), bg="darkgray")
    digitar_nome.pack()

    # Lista das classes
    listaclasses = tk.Listbox(janeladasclasses, font=("Comic Sans MS", 12, "normal"), bg="black", fg="white")
    listaclasses.pack(pady=10)

    for nome_classe in classes.keys():
        listaclasses.insert(tk.END, nome_classe)

    # Botão para confirmar o nome e a classe escolhidas
    botaoaceitar = tk.Button(janeladasclasses,text="Confirmar" ,font=("Comic Sans MS", 12, "normal"), bg="darkgreen", fg="white", command=confirmar_info)
    botaoaceitar.pack(pady=10)

def janeladificuldade():
    janeladasdificuldades = tk.Toplevel()
    janeladasdificuldades.title("Dificuldade de Jogo")
    janeladasdificuldades.geometry("720x480")
    janeladasdificuldades.config(bg="black")
    textodificuldade = """
    Qual dificuldade você quer escolher?
    """
    
    labeldificuldade = tk.Label(janeladasdificuldades, text=textodificuldade, justify="center", bg="black", fg="white", font=("Comic Sans MS", 12, "normal"), padx=10, pady=10)
    labeldificuldade.pack()

    def confirmar_dificuldade():
        global Dificuldade
        selecao = listadificuldades.curselection()
        indice = selecao[0]
        dificuldadeescolhida = listadificuldades.get(indice)
        if dificuldadeescolhida != "":
            messagebox.showinfo("Sucesso", "Dificuldade escolhida com sucesso!")
            Dificuldade = dificuldadeescolhida
            janeladasdificuldades.destroy()
        else:
            messagebox.showwarning("Dificuldade", "Escolha uma dificuldade!")

    # Lista para escolher uma dificuldade
    listadificuldades = tk.Listbox(janeladasdificuldades, font=("Comic Sans MS", 12, "normal"), bg="black", fg="white", height=6)
    listadificuldades.pack()
    for item in Dificuldades:
        listadificuldades.insert(tk.END, item)

    # Botão para confirmar a dificuldade escolhida
    botaoconfirmar = tk.Button(janeladasdificuldades, text="Confirmar", font=("Comic Sans MS", 12, "normal"), bg="green", fg="black", command=confirmar_dificuldade)
    botaoconfirmar.pack(pady=50)

def janelajogar():
    #Identifica se colocou todos os dados do personagem
    if nomee != "" and classe != "" and Dificuldade != "":

        # Cria a janela do jogo em tela cheia e tira a janela inicial principal, se tornando a nova janela principal
        jogo = tk.Toplevel()
        jogo.title("RPG")
        jogo.config(bg="black")
        jogo.attributes("-fullscreen", True)
        janelaprincipal.withdraw()

        # Cria um Frame central para ficar a foto e a legenda
        framejogoinicial = tk.Frame(jogo, bg="black")
        framejogoinicial.pack(expand=True)

        legendasuperiorfoto = tk.Label(framejogoinicial, text="Você:", font=("Comic Sans MS", 17, "normal"), bg="black", fg="white")
        legendasuperiorfoto.pack()

        caminhofoto = classes[classe]["fotonormal"]
        img = Image.open(caminhofoto)
        img = img.resize((250, 250))
        foto = ImageTk.PhotoImage(img)  
        labelfoto = tk.Label(framejogoinicial, image=foto, bg="black")
        labelfoto.image = foto
        labelfoto.pack(pady=(40, 5))

        textolegenda = (f"""
Nome: {nomee}
Vida: {classes[classe]["Vida"]}
Força: {classes[classe]["Força"]}
Habilidade Especial: {classes[classe]["Habilidade Especial"]}
Força da Habilidade Especial: {classes[classe]["Força da Habilidade"]}
Efeito da Habilidade Especial: {classes[classe]["Efeito da Habilidade"]}
        """)
        legendafoto = tk.Label(framejogoinicial, text=textolegenda, font=("Comic Sans MS", 12, "normal"), bg="black", fg="white")
        legendafoto.pack(pady=(0, 5))

        def jogar():
            # Campo de batalha do jogo
            global framejogoverinimigo, vidainimigo, botdesviou, jogadordesviou, forcainimigo, forhabinimigo, vidajogador, forcajogador, forhabjogador, jogador_usou_especial, bot_usou_especial, jogadorvaierrar, inimigovaierrar, fotojogador, ftjg, vezjogador
            framejogoverinimigo.destroy()
            vidainimigo = classes[personagembot]["Vida"]
            forcainimigo = classes[personagembot]["Força"]
            forhabinimigo = classes[personagembot]["Força da Habilidade"]
            inimigovaierrar = False
            vidajogador = classes[classe]["Vida"]
            forcajogador = classes[classe]["Força"]
            forhabjogador = classes[classe]["Força da Habilidade"]
            jogadorvaierrar = False
            jogador_usou_especial = False
            bot_usou_especial = False
            jogadordesviou = False
            botdesviou = False
            vezjogador = True

            frametd = tk.Frame(jogo, bg="black")
            frametd.pack(expand=True)
            
            # Parte do jogador
            framejogador = tk.Frame(frametd, bg="black")
            framejogador.pack(side="left", padx=50)

            legsupjg = tk.Label(framejogador, text="Você:", bg="black", fg="white", font=("Comic Sans MS", 17, "normal"))
            legsupjg.pack()
            
            caminhojog = classes[classe]["fotonormal"]
            imgjg = Image.open(caminhojog)
            imgjg = imgjg.resize((250, 250))
            ftjg = ImageTk.PhotoImage(imgjg)
            fotojogador = tk.Label(framejogador, image=ftjg, bg="black")
            fotojogador.image = ftjg
            fotojogador.pack()

            def attjogador():
                legendajg = (f"""
Nome: {nomee}
Vida: {vidajogador}
Força: {forcajogador}
Habilidade: {classes[classe]["Habilidade Especial"]}
Força da Habilidade: {forhabjogador}
Efeito da habilidade: {classes[classe]["Efeito da Habilidade"]}
""")
                legftjg.config(text=legendajg)
            legftjg = tk.Label(framejogador, font=("Comic Sans MS", 12, "normal"), fg="white", bg="black")
            attjogador()
            legftjg.pack()

            # Parte do bot
            framebot = tk.Frame(frametd, bg="black")
            framebot.pack(side="left", padx=50)

            legsupini = tk.Label(framebot, text="Inimigo:", bg="black", fg="white", font=("Comic Sans MS", 17, "normal"))
            legsupini.pack()

            caminhoini = classes[personagembot]["fotonormal"]
            imgini = Image.open(caminhoini)
            imgini = imgini.resize((250, 250))
            ftini = ImageTk.PhotoImage(imgini)
            fotoinimigo = tk.Label(framebot, image=ftini, bg="black")
            fotoinimigo.image = ftini
            fotoinimigo.pack()

            def attinimigo():
                texto = (f"""
Nome: {personagembot}
Vida: {vidainimigo}
Força: {forcainimigo}
Habilidade: {classes[personagembot]["Habilidade Especial"]}
Força Habilidade: {forhabinimigo}
Efeito Habilidade: {classes[personagembot]["Efeito da Habilidade"]}
""")
                legftini.config(text=texto)
            legftini = tk.Label(framebot, font=("Comic Sans MS", 12, "normal"), fg="white", bg="black")
            attinimigo()
            legftini.pack()

            # Parte do frame que tem as seleções
            frameacoesjogador = tk.Frame(jogo, bg="black")
            frameacoesjogador.pack(padx=10, expand=True)

            def ataquenormal():
                global vidainimigo, forcajogador, jogadorvaierrar, botdesviou, vezjogador
                if vezjogador == True:
                    if not botdesviou:
                        if not jogadorvaierrar:
                            vidainimigo -= forcajogador
                            forcajogador = classes[classe]["Força"]
                            attinimigo()
                            vezjogador = False
                            turnos()
                        else:
                            jogadorvaierrar = False
                            info = tk.Label(frameacoesjogador, text="Jogador errou o Ataque!", font=("Comic Sans MS", 12, "normal"), fg="red", bg="black")
                            info.pack()
                            jogo.after(2000, info.destroy)
                            vezjogador = False
                            turnos()
                    else:
                        jogadorvaierrar = False
                        info = tk.Label(frameacoesjogador, text="Inimigo desviou!", font=("Comic Sans MS", 12, "normal"), fg="red", bg="black")
                        info.pack()
                        jogo.after(2000, info.destroy)
                        vezjogador = False
                        turnos()
                        botdesviou = False
                else:
                    info = tk.Label(frameacoesjogador, text="Não é a sua vez!", font=("Comic Sans MS", 12, "normal"), fg="red", bg="black")
                    info.pack
                    jogo.after(2000, info.destroy)

            def ataqueespecial():
                global jogador_usou_especial, jogadorvaierrar, botdesviou, vezjogador
                if vezjogador == True:
                    if not botdesviou:
                        if not jogador_usou_especial and not jogadorvaierrar:
                            som = pygame.mixer.Sound(classes[classe]["Som Habilidade"])
                            som.play()
                            caminhofthab = classes[classe]["fotohabilidade"]
                            imagem = Image.open(caminhofthab).resize((250, 250))
                            fthab = ImageTk.PhotoImage(imagem)
                            fotojogador.config(image=fthab)
                            fotojogador.image = fthab
                            habilidade = classes[classe]["funcao habilidade"]
                            habilidade()
                            attinimigo()
                            def voltarimg():
                                fotojogador.config(image=ftjg)
                                fotojogador.image = ftjg
                            jogo.after(2000, voltarimg)
                            jogador_usou_especial = True
                            vezjogador = False
                            turnos()
                        elif jogador_usou_especial == True and jogadorvaierrar == False:
                            info = tk.Label(frameacoesjogador, text="Você já usou a habilidade!", font=("Comic Sans MS", 12, "normal"), fg="red", bg="black")
                            info.pack()
                            jogo.after(2000, info.destroy)
                        else:
                            info = tk.Label(frameacoesjogador, text="Você errou a habilidade, mas ainda pode usá-la!", font=("Comic Sans MS", 12, "normal"), fg="red", bg="black")
                            info.pack()
                            jogo.after(2000, info.destroy)
                            vezjogador = False
                            turnos()
                    else:
                        botdesviou = False
                else:
                    info = tk.Label(frameacoesjogador, text="Não é a sua vez!", font=("Comic Sans MS", 12, "normal"), fg="red", bg="black")
                    info.pack()
                    jogo.after(2000, info.destroy)
            
            def ataquenormalbot():
                global vidajogador, forcainimigo, inimigovaierrar, jogadordesviou
                if not jogadordesviou:
                    if not inimigovaierrar:
                        vidajogador -= forcainimigo
                        forcainimigo = classes[personagembot]["Força"]
                        attjogador()
                    else:
                        inimigovaierrar = False
                        info = tk.Label(frameacoesjogador, text="Inimigo Errou o Ataque!", font=("Comic Sans MS", 12, "normal"), fg="green", bg="black")
                        info.pack()
                        jogo.after(2000, info.destroy)
                else:
                    jogadordesviou = False
            
            def ataqueespecialbot():
                global bot_usou_especial, inimigovaierrar, jogadordesviou
                if not jogadordesviou:
                    if not bot_usou_especial and not inimigovaierrar:
                        som = pygame.mixer.Sound(classes[personagembot]["Som Habilidade"])
                        som.play()
                        caminhofthb = classes[personagembot]["fotohabilidade"]
                        imagemhb = Image.open(caminhofthb).resize((250, 250))
                        ftinis = ImageTk.PhotoImage(imagemhb)
                        fotoinimigo.config(image=ftinis)
                        fotoinimigo.image = ftinis
                        habini = habilidade_bot[personagembot]
                        habini()
                        attjogador()
                        def voltarimag():
                            fotoinimigo.config(image=ftini)
                            fotoinimigo.image = ftini
                        jogo.after(2000, voltarimag)
                        bot_usou_especial = True
                    else:
                        info = tk.Label(frameacoesjogador, text="Inimigo errou a habilidade, mas ainda pode usar!", font=("Comic Sans MS", 12, "normal"), fg="green", bg="black")
                        info.pack()
                        jogo.after(2000, info.destroy)
            
            botaoataquenormal = tk.Button(frameacoesjogador, text="Ataque Normal", font=("Comic Sans MS", 12, "normal"), fg="black", bg="lightgreen", command=ataquenormal)
            botaoataquenormal.pack(pady=10)

            botaoataquehabilidade = tk.Button(frameacoesjogador, text="Habilidade Especial (1 uso)", font=("Comic Sans MS", 12, "normal"), fg="black", bg="red", command=ataqueespecial)
            botaoataquehabilidade.pack(pady=10)

            def turnos():
                global vezjogador, jogadordesviou
                if vidajogador > 0 and vidainimigo > 0:
                    if not vezjogador:
                        if bot_usou_especial == True:
                            ataquenormalbot()
                            if vidajogador > 0 and vidainimigo > 0:
                                vezjogador = True
                            elif vidainimigo < 0:
                                jogadordesviou = False
                                botaoataquehabilidade.destroy()
                                botaoataquenormal.destroy()
                                info = tk.Label(frameacoesjogador, text="Você venceu!", font=("Comic Sans MS", 20, "normal"), fg="green", bg="black")
                                info.pack()
                                jogo.after(2000, janelaprincipal.destroy)
                            else:
                                jogadordesviou = False
                                botaoataquehabilidade.destroy()
                                botaoataquenormal.destroy()
                                info = tk.Label(frameacoesjogador, text="Você Perdeu!", font=("Comic Sans MS", 20, "normal"), fg="red", bg="black")
                                info.pack()
                                jogo.after(2000, janelaprincipal.destroy)
                        else:
                            ataqueespecialbot()
                            if vidajogador > 0 and vidainimigo > 0:
                                vezjogador = True
                            elif vidainimigo < 0:
                                jogadordesviou = False
                                botaoataquehabilidade.destroy()
                                botaoataquenormal.destroy()
                                info = tk.Label(frameacoesjogador, text="Você venceu!", font=("Comic Sans MS", 20, "normal"), fg="green", bg="black")
                                info.pack()
                                jogo.after(2000, janelaprincipal.destroy)
                            else:
                                jogadordesviou = False
                                botaoataquehabilidade.destroy()
                                botaoataquenormal.destroy()
                                info = tk.Label(frameacoesjogador, text="Você Perdeu!", font=("Comic Sans MS", 20, "normal"), fg="red", bg="black")
                                info.pack()
                                jogo.after(2000, janelaprincipal.destroy)
                elif vidainimigo < 0:
                    jogadordesviou = False
                    botaoataquehabilidade.destroy()
                    botaoataquenormal.destroy()
                    info = tk.Label(frameacoesjogador, text="Você venceu!", font=("Comic Sans MS", 20, "normal"), fg="green", bg="black")
                    info.pack()
                    jogo.after(2000, janelaprincipal.destroy)
                else:
                    jogadordesviou = False
                    botaoataquehabilidade.destroy()
                    botaoataquenormal.destroy()
                    info = tk.Label(frameacoesjogador, text="Você Perdeu!", font=("Comic Sans MS", 20, "normal"), fg="red", bg="black")
                    info.pack()
                    jogo.after(2000, janelaprincipal.destroy)

        def verinimigo():
            # Função para ver as estatísticas do inimigo (bot)
            global framejogoverinimigo, personagembot
            personagembot = Dificuldades[Dificuldade]["Personagem"]
            framejogoinicial.destroy()

            framejogoverinimigo = tk.Frame(jogo, bg="black")
            framejogoverinimigo.pack(expand=True)

            legendasuperiorinimigo = tk.Label(framejogoverinimigo, text="Inimigo:", bg="black", fg="white", font=("Comic Sans MS", 17, "normal"))
            legendasuperiorinimigo.pack()

            caminhofotoinimigo = classes[personagembot]["fotonormal"]
            imageminimigo = Image.open(caminhofotoinimigo)
            imageminimigo = imageminimigo.resize((250, 250))
            fotoinimigo = ImageTk.PhotoImage(imageminimigo)
            labelfotoinimigo = tk.Label(framejogoverinimigo, image=fotoinimigo, bg="black")
            labelfotoinimigo.image = fotoinimigo
            labelfotoinimigo.pack()

            textolegendainimigo = (f"""
Nome: {personagembot}
Vida: {classes[personagembot]["Vida"]}
Força: {classes[personagembot]["Força"]}
Habilidade Especial: {classes[personagembot]["Habilidade Especial"]}
Força da Habilidade Especial: {classes[personagembot]["Força da Habilidade"]}
Efeito da Habilidade Especial: {classes[personagembot]["Efeito da Habilidade"]}
""")
            descricaoinimigo = tk.Label(framejogoverinimigo, text=textolegendainimigo, font=("Comic Sans MS", 12, "normal"), bg="black", fg="white")
            descricaoinimigo.pack()

            botaojogarfinal = tk.Button(framejogoverinimigo, text="Jogar!", font=("Comic Sans MS", 12, "normal"), bg="lightgreen", fg="black", command=jogar)
            botaojogarfinal.pack(pady=10)

        botaocontinuar = tk.Button(framejogoinicial, text="Continuar", font=("Comic Sans MS", 12, "normal"), bg="lightgreen", fg="black", command=verinimigo)
        botaocontinuar.pack(pady=10)

    else:
        messagebox.showerror("Erro", "Preencha todos os dados e selecione a dificuldade!")

# Janela inicial principal
janelaprincipal = tk.Tk()
janelaprincipal.title("RPG")
janelaprincipal.geometry("720x500")
janelaprincipal.config(bg="black")
textoprincipal = """
BEM VINDO AO COIN MASTE RPG!

Você ainda não tem um personagem!
Crie um agora, IMEDIATAMENTE!
"""

Labelprincipal = tk.Label(janelaprincipal, text=textoprincipal, justify="center", bg="black", fg="white", font=("Comic Sans MS", 12, "normal"), padx=10, pady=10)
Labelprincipal.pack()

# Botão para jogar
botaojogar = tk.Button(janelaprincipal, text="JOGAR", font=("Comic Sans MS", 12, "normal"), fg="black", bg="green", command=janelajogar)
botaojogar.pack(pady=10)

# Botão para escolher os nomes e classes
botaoclasses = tk.Button(janelaprincipal, text="Escolher Classe e Nome", font=("Comic Sans MS", 12, "normal"), fg="black", bg="lightblue", command=janelaclasses)
botaoclasses.pack(pady=10)

# Botão para escolher a dificuldade
botaodificuldade = tk.Button(janelaprincipal, text="Escolher Dificuldade", font=("Comic Sans MS", 12, "normal"), fg="black", bg="lightblue", command=janeladificuldade)
botaodificuldade.pack(pady=10)

# Botão para ver as regras
botaoregras = tk.Button(janelaprincipal, text="Ver regras", font=("Comic Sans MS", 12, "normal"), fg="black", bg="yellow", command=janelaregras)
botaoregras.pack(pady=10)

janelaprincipal.mainloop()
