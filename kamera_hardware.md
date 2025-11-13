# Uruchamianie Modeli AI na Luxonis OAK-D Pro

## Kluczowe Informacje

Poniżej znajdują się kluczowe punkty na temat wgrywania modeli AI na kamerę OAK-D Pro.

### 1. Architektura RVC2
* Kamera jest zbudowana na układzie (SoC) **RVC2 (Robotics Vision Core 2)**.
* To ten układ jest odpowiedzialny za całe przetwarzanie AI bezpośrednio na urządzeniu.

### 2. Konieczność Konwersji Modelu
* To jest najważniejszy wymóg: **Modele AI muszą zostać przekonwertowane**.
* Nie można wgrać na kamerę surowego modelu w popularnych formatach (np. TensorFlow, PyTorch, Caffe).

### 3. Wymagany Format 
* Model musi zostać najpierw przekonwertowany do specjalnego formatu **.blob**, który jest zrozumiały dla procesora RVC2.
* Szczegółowe informacje na temat procesu konwersji modeli z oficjalnej dokumentacji: **[Proces Konwersji Modeli AI (Luxonis Docs)](https://docs.luxonis.com/software/ai-inference/conversion)**.

### 4. Uruchamianie na Urządzeniu 
* Więcej informacji na ten temat: **[Programowanie na urządzeniu (Luxonis Docs)](https://docs.luxonis.com/software-v3/depthai/tutorials/on-device-programming/)**
