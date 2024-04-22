import sys, pytesseract, cv2

# Récupérer le nom de l'image depuis la ligne de commande
image_name = sys.argv[1]

# Charger l'image en utilisant cv2
image = cv2.imread(image_name)

# Convertir l'image en niveaux de gris
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Extraire le texte de l'image
text = pytesseract.image_to_string(gray)

# Exporter le texte extrait dans un fichier results.txt
with open('results.txt', 'w') as f:
  f.write(text)
