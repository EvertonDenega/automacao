import pyautogui as p

def coordenadas():
    with open("coordenadas.txt", "w") as c:
        while True:
            x, y = p.position()
            posicao = "x="+str(x) + ", " + "y="+str(y)
            print(posicao)
            c.write(posicao + '\n')
            c.flush()
            p.sleep(3)

coordenadas()