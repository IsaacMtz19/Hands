import cv2
import keras
import numpy as np

# Cargar el modelo
Clasificador = keras.models.load_model("Mymodel (3).h5")

# Iniciar la captura de video
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    imgOrig = frame.copy()  # Copia para mostrar el texto
    frame = cv2.resize(frame, (150, 150))  # Redimensionar al tamaño esperado
    frame = frame / 255.0  # Normalizar valores de píxeles
    frame = frame.reshape((1, 150, 150, 3))  # Cambiar las dimensiones para el modelo
    
    pred = Clasificador.predict(frame)
    clase_idx = np.argmax(pred)  # Obtener el índice de la clase con mayor probabilidad
    
    # Mapear el índice a las clases
    if clase_idx == 0:
        clase = "una mano"
    elif clase_idx == 1:
        clase = "dos manos"
    else:
        clase = "sin manos"
    
    # Mostrar el resultado en la imagen
    imgOrig = cv2.putText(imgOrig, clase, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 
                          1, (255, 0, 0), 2, cv2.LINE_AA)
    
    # Mostrar la imagen
    cv2.imshow('Camara', imgOrig)
    if cv2.waitKey(1) == ord('q'):  # Presiona 'q' para salir
        break

cap.release()
cv2.destroyAllWindows()
