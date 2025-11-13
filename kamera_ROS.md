# Integracja Luxonis DepthAI z ROS 

## Kluczowe Informacje (na podstawie dokumentacji `depthai-ros`)

Plik podsumowuje kluczowe informacje dotyczące pakietu `depthai-ros`, który umożliwia integrację kamery Luxonis OAK-D Pro z ROS.

### 1. Główny Cel Pakietu `depthai-ros`

Pakiet `luxonis/depthai-ros` pozwala na:

* Używanie kamer OAK jako klasycznych czujników **RGBD** (obraz kolorowy + dane głębi) na potrzeby widzenia 3D w ROS.
* **Ładowanie Sieci Neuronowych (AI)** bezpośrednio na kamerę i odbieranie wyników inferencji (np. detekcji obiektów) prosto w ROS.

### 2. Wspierane Wersje ROS

* Noetic 
* Humble 
* Iron 
* powinno też działać na Jazzy 

### 3. Sposoby Użycia

Możesz rozwijać swoje aplikacje ROS na dwa główne sposoby:

1.  **Użycie `depthai_bridge`:** Wykorzystanie dostarczonych klas do zbudowania własnego, niestandardowego sterownika (drivera).
2.  **Użycie `depthai_ros_driver`:** Użycie gotowego pakietu sterownika (dostępnego dla ROS2 Humble i ROS Noetic), aby uzyskać standardową funkcjonalność "out-of-the-box".

### 4. Instalacja

* **Z binarów ROS (zalecane):**
    ```bash
    sudo apt install ros-<distro>-depthai-ros
    ```

### 5. Dodatkowe Funkcje (`depthai_filters`)

Pakiet zawiera zestaw przykładowych węzłów, które pokazują, jak pracować z danymi z kamery:

* **`Detection2DOverlay`**: Nakłada wyniki detekcji (bounding boxy) na surowy obraz z kamery.
* **`SegmentationOverlay`**: Nakłada wyniki segmentacji semantycznej na obraz.
* **`WLS filter`**: Filtr wygładzający obraz głębi w oparciu o dane dysparytetu.
* **`SpatialBB`**: Publikuje ramki graniczne obiektów jako znaczniki 3D w przestrzeni.
* **`FeatureTrackerOverlay`**: Wyświetla śledzone punkty kluczowe na obrazie.
* **`Features3D`**: Używa obrazu głębi, aby opublikować śledzone punkty kluczowe jako chmurę punktów 3D.

### 6. Niestandardowe Konwertery
Użytkownicy mogą pisać własne konwertery i podłączać je do bridge publishera, jeśli potrzebują publikować dane w niestandardowym formacie wiadomości ROS.
