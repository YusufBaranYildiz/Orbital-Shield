def calculate_hazard(diameter_m, distance_km, velocity_kms):
    """
    4. Gün: Deterministik risk hesaplama.
    Çap > 100m VE mesafe < 7.5 milyon km ise YÜKSEK risk.
    """
    if diameter_m > 100 and distance_km < 7_500_000:
        return "YÜKSEK"
    elif diameter_m > 50 and distance_km < 10_000_000:
        return "ORTA"
    else:
        return "DÜŞÜK"
