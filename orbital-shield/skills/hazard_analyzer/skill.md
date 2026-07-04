---
name: hazard-analyzer
description: Gök cismi çap, mesafe ve hızını kullanarak tehlike skoru hesaplar.
triggers:
  - keyword: "tehlike analizi"
---

# Tehlike Analizi Prosedürü
1. Gök cisminin maksimum tahmini çapını (metre) al.
2. İlk yakın geçiş mesafesini (km) al.
3. Bağıl hızını (km/s) al.
4. hazard_calculator aracını kullanarak tehlike skoru hesapla.
5. Sonuçları JSON formatında döndür.
