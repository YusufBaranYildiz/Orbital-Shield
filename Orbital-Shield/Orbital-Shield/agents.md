# Orbital Shield – Gezegen Savunma Ağı

## Amaç
NASA'nın NeoWs API'sini kullanarak Dünya'ya yaklaşan gök cisimlerini tarayan, risk analizi yapan ve yüksek riskli cisimler için uyarı üreten otonom bir çok ajanlı sistem.

## Koşum Takımı (Harness)
- Model: Gemini Flash (hafif kararlar için)
- Orkestratör: Görev dağıtıcı
- MCP Araçları: NASA API istemcisi, risk hesaplama motoru
- Beceriler: hazard_analyzer (tehlike skoru hesaplama)
- Güvenlik: API yanıt doğrulama, rate limiting
- A2UI: Dinamik risk panosu

## İş Akışı
1. Kullanıcı "bugün", "bu hafta" gibi bir zaman aralığı verir.
2. Orkestratör, Gözlemci Ajan'ı tetikler.
3. Gözlemci, NASA API MCP aracını kullanarak veriyi çeker.
4. Analist Ajan, hazard_analyzer becerisini yükleyerek risk skoru hesaplar.
5. Haberci Ajan, yüksek riskli cisimleri A2UI panosunda listeler.
6. Yörünge değerlendirmesi yapılır.
