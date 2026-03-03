# Pozicioniranje magnetov — izračun koordinat

## Rotor geometrija (iz risbe SP2025-0063-0048)

- Φ 260mm, 10 žepov enakomerno razporejenih
- Radij sredine žepa: R_mid = (89.55 + 122.95) / 2 = **106.25 mm**
- Kotni korak med žepi: 360° / 10 = **36°**

## Koordinate centrov žepov (izhodišče = center rotorja)

```python
import numpy as np

R_mid = 106.25  # mm
n_pockets = 10
angles = [i * 36 for i in range(n_pockets)]  # 0, 36, 72, ... 324°

pockets = []
for i, angle in enumerate(angles):
    x = R_mid * np.cos(np.radians(angle))
    y = R_mid * np.sin(np.radians(angle))
    polarity = "N" if i % 2 == 0 else "S"
    pockets.append((i+1, angle, round(x,2), round(y,2), polarity))
    print(f"Žep {i+1:2d} | {angle:3d}° | X={x:8.2f} | Y={y:8.2f} | {polarity}")
```

## Rezultat

| Žep | Kot | X [mm] | Y [mm] | Polarnost |
|-----|-----|--------|--------|-----------|
| 1  | 0°  | +106.25 | 0.00   | N |
| 2  | 36° | +86.02  | +62.49 | S |
| 3  | 72° | +32.84  | +101.10| N |
| 4  | 108°| -32.84  | +101.10| S |
| 5  | 144°| -86.02  | +62.49 | N |
| 6  | 180°| -106.25 | 0.00   | S |
| 7  | 216°| -86.02  | -62.49 | N |
| 8  | 252°| -32.84  | -101.10| S |
| 9  | 288°| +32.84  | -101.10| N |
| 10 | 324°| +86.02  | -62.49 | S |

## Cobot TCP path

Za vsak rotor cobot naredi:
1. Premik na center rotorja (kalibrirana referenčna točka)
2. Izračun pozicije žepa iz tabele zgoraj
3. Prilagoditev kota gripperja = kot žepa (magnet je orientiran radialno)
4. Spust z **0.05 m/s** za zadnjih 5mm (natančno polaganje)

## Orientacija gripperja

Vsak magnet je orientiran **radialno** — gripper se mora zasukati za kot žepa:
- Žep 1 (0°) → gripper zasuk 0°
- Žep 2 (36°) → gripper zasuk 36°
- itd.

Zahteva **rotacijsko os na gripperju** ali tool changer z rotacijo.
