import os
import time

def wyczysc_ekran():
    # Czyszczenie ekranu w zależności od systemu operacyjnego
    if os.name == 'nt':
        os.system('cls')  # Windows
    else:
        os.system('clear')  # Unix/Linux/Mac


def przesun_tekst_w_pionie(tekst, wysokosc_okna, opoznienie=0.1):
    while True:
        # TODO: twój kod 
        pass


if __name__ == "__main__":
    tekst = "  Hello world!  "  # tekst do przesuwania
    wysokosc_okna = 20  # Wysokość "okna" terminala
    przesun_tekst_w_pionie(tekst, wysokosc_okna)
