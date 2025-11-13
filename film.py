import cv2
import os
import glob
import re

folder_z_klatkami = r"C:\Users\olekp\runs\detect\predict4"
nazwa_filmu_wyjsciowego = "result.mp4"
fps = 30
def natural_sort_key(s):
    return [int(text) if text.isdigit() else text.lower()
            for text in re.split(r'(\d+)', s)]
sciezki_do_klatek = glob.glob(os.path.join(folder_z_klatkami, "*.jpg"))
sciezki_do_klatek.extend(glob.glob(os.path.join(folder_z_klatkami, "*.png")))
sciezki_do_klatek.sort(key=natural_sort_key)
if not sciezki_do_klatek:
    print(f"Nie znaleziono klatek w: {folder_z_klatkami}")
    exit()
pierwsza_klatka = cv2.imread(sciezki_do_klatek[0])
if pierwsza_klatka is None:
    print(f"Błąd odczytu pierwszej klatki: {sciezki_do_klatek[0]}")
    exit()
wysokosc, szerokosc, kanaly = pierwsza_klatka.shape
rozmiar = (szerokosc, wysokosc)
print(f"Rozmiar: {szerokosc}x{wysokosc}, FPS: {fps}, Klatki: {len(sciezki_do_klatek)}")
fourcc = cv2.VideoWriter_fourcc(*'mp4v') 
out = cv2.VideoWriter(nazwa_filmu_wyjsciowego, fourcc, fps, rozmiar)
print(f"Rozpoczynam tworzenie filmu...")

for sciezka in sciezki_do_klatek:
    klatka = cv2.imread(sciezka)
    if klatka is not None:
        out.write(klatka) 
out.release()
print(f"\nGotowe! Film zapisany jako '{nazwa_filmu_wyjsciowego}'")