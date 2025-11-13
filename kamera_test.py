from ultralytics import YOLO
model = YOLO('yolov8n.pt') 
sciezka_do_klatek = r"C:\Users\olekp\Documents\VisDrone2019-VID-val\VisDrone2019-VID-val\sequences\uav0000086_00000_v" 
results = model(sciezka_do_klatek, save=True, show=False) 
print("Analiza zakończona")