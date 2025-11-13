def ispisi(ploca):
    for i in range(3):
        print(ploca[i][0], "|", ploca[i][1], "|", ploca[i][2])
        if i < 2:
            print("---------")

def ima_pobjednika(ploca, znak):
    for i in range(3):
        if ploca[i][0] == ploca[i][1] == ploca[i][2] == znak:
            return True
        if ploca[0][i] == ploca[1][i] == ploca[2][i] == znak:
            return True
    if ploca[0][0] == ploca[1][1] == ploca[2][2] == znak:
        return True
    if ploca[0][2] == ploca[1][1] == ploca[2][0] == znak:
        return True
    return False

def puna(ploca):
    for i in range(3):
        for j in range(3):
            if ploca[i][j] == " ":
                return False
    return True

def minimax(ploca, racunar):
    if ima_pobjednika(ploca, "O"):
        return 1
    if ima_pobjednika(ploca, "X"):
        return -1
    if puna(ploca):
        return 0
    if racunar:
        najbolja = -999
        for i in range(3):
            for j in range(3):
                if ploca[i][j] == " ":
                    ploca[i][j] = "O"
                    vrijednost = minimax(ploca, False)
                    ploca[i][j] = " "
                    if vrijednost > najbolja:
                        najbolja = vrijednost
        return najbolja
    else:
        najbolja = 999
        for i in range(3):
            for j in range(3):
                if ploca[i][j] == " ":
                    ploca[i][j] = "X"
                    vrijednost = minimax(ploca, True)
                    ploca[i][j] = " "
                    if vrijednost < najbolja:
                        najbolja = vrijednost
        return najbolja

def najbolji_potez(ploca):
    najbolja = -999
    potez = (0, 0)
    for i in range(3):
        for j in range(3):
            if ploca[i][j] == " ":
                ploca[i][j] = "O"
                vrijednost = minimax(ploca, False)
                ploca[i][j] = " "
                if vrijednost > najbolja:
                    najbolja = vrijednost
                    potez = (i, j)
    return potez

def igra():
    ploca = [[" " for _ in range(3)] for _ in range(3)]
    print("Igra Križić-Kružić (Ti = X, Računalo = O)")
    ispisi(ploca)
    while True:
        potez = input("Unesi potez (red,stupac) npr. 1,3: ")
        try:
            r, s = map(int, potez.split(","))
            r -= 1
            s -= 1
            if ploca[r][s] == " ":
                ploca[r][s] = "X"
            else:
                print("To polje je zauzeto!")
                continue
        except:
            print("Pogrešan unos!")
            continue
        ispisi(ploca)
        if ima_pobjednika(ploca, "X"):
            print("Pobijedio si!")
            break
        if puna(ploca):
            print("Neriješeno!")
            break
        print("Računalo razmišlja...")
        i, j = najbolji_potez(ploca)
        ploca[i][j] = "O"
        ispisi(ploca)
        if ima_pobjednika(ploca, "O"):
            print("Računalo je pobijedilo!")
            break
        if puna(ploca):
            print("Neriješeno!")
            break


