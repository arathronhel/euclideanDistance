# Noktaların Tanımlanması:
points = [
    (1,3),  # Birinci nokta
    (3,7),  # İkinci nokta
    (7,9),  # Üçüncü nokta
    (7,3)   # Dördüncü nokta
]

# Öklid Mesafesi İçin Bir Fonksiyon Yazma:
def euclideanDistance(x1,y1,x2,y2):
    x_diff = (x2 - x1) ** 2  # X farkının karesi
    y_diff = (y2 - y1) ** 2  # Y farkının karesi
    distance = (x_diff + y_diff) ** 0.5  # Karekök alıyoruz
    return distance

# Mesafelerin Hesaplanması:

# Mesafeleri saklayacağımız boş bir liste
distances = []

# Bütün noktalara bakarak mesafeleri hesaplayalım
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        x1, y1 = points[i]
        x2, y2 = points[j]

        # Fonksiyonu kullanarak mesafeyi hesaplıyoruz
        distance = euclideanDistance(x1, y1, x2, y2)

        # Mesafeyi listeye ekliyoruz
        distances.append(distance)

# Minimum Mesafenin Bulunması:

# Şimdi minimum mesafeyi bulalım
min_distance = min(distances)  # Mesafelerin en küçüğünü bul

print("Minimum Mesafe:", min_distance)  # Ekrana yazdır
