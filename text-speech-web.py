# server.py
from flask import Flask, request, jsonify
import pytesseract
import cv2
import numpy as np
import base64

app = Flask(__name__)

# Route pour l'analyse de l'image
@app.route('/analyze_image', methods=['POST'])
def analyze_image():
    # Récupérer les données binaires de l'image depuis la requête POST
    image_data = request.files['image'].read()
    
    # Convertir les données binaires en tableau NumPy
    nparr = np.frombuffer(image_data, np.uint8)
    
    # Décoder le tableau NumPy en image
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    # Convertir l'image en niveaux de gris
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Extraire le texte de l'image
    text = pytesseract.image_to_string(gray)
    
    return jsonify({'text': text})

if __name__ == '__main__':
    app.run(debug=True)
