# Delovna celica — Layout

## Tloris

```
+----------------------------------------------------------+
|                    VARNOSTNA OGRAJA                       |
|                                                          |
|   [SARŽA]    [COBOT UR5e]    [EPOXY]                    |
|   magnetov      🦾            dispenser                  |
|                                                          |
|     [R1] [R2]    [R3] [R4]    [R5]                      |
|     [R6] [R7]    [R8] [R9]    [R10]                     |
|                                                          |
|          DELOVNA MIZA (5×2 mreža)                       |
|                                                          |
|   [OPERATOR]  ←  vstopna točka                          |
+----------------------------------------------------------+
```

## Dimenzije

| Element | Pozicija | Opombe |
|---------|----------|--------|
| Cobot baza | Center celice | Doseg UR5e 850mm pokriva vse rotorje |
| Delovna miza | 800×600mm | 5×2 mreža rotorjev |
| Sarža magnetov | Desno od cobota | Znotraj dosega |
| Epoxy dispenser | Levo od cobota | Fiksna postaja |
| FR4 zaloga | Zadaj | Operator polni med cikli |
| Al jigi | Ob mizi | 10 kosov pripravljenih |

## Razdalje (cobot TCP)

| Od cobota do | Razdalja | Znotraj dosega? |
|-------------|----------|-----------------|
| Rotor R1 (levo spredaj) | ~400mm | ✅ |
| Rotor R10 (desno zadaj) | ~750mm | ✅ |
| Sarža magnetov | ~300mm | ✅ |
| Epoxy postaja | ~250mm | ✅ |

## Pozicije rotorjev (koordinate)

Izhodišče = baza cobota

| Rotor | X [mm] | Y [mm] | Vrstica |
|-------|--------|--------|---------|
| R1 | -300 | +200 | 1 |
| R2 | -150 | +200 | 1 |
| R3 | 0 | +200 | 1 |
| R4 | +150 | +200 | 1 |
| R5 | +300 | +200 | 1 |
| R6 | -300 | +350 | 2 |
| R7 | -150 | +350 | 2 |
| R8 | 0 | +350 | 2 |
| R9 | +150 | +350 | 2 |
| R10 | +300 | +350 | 2 |

> Točne koordinate se določijo med kalibracijo cobota na dejanskem mestu.

## FR4 Rotor plošča — dimenzije (iz risbe SP2025-0063-0048)

| Parameter | Vrednost |
|-----------|----------|
| Zunanja dimenzija | Φ 260 mm |
| Debelina | 5 mm |
| Material | FR4 (neferomagnetna ✅) |
| Število žepov | 10 |
| Radij žepov (notranji) | R 89.55 mm |
| Radij žepov (zunanji) | R 122.95 mm |
| Toleranca žepov | ±0.03 mm |
| Montažne izvrtine | 6× Φ 6.4 mm skoznje |
| Masa | 294.88 g |

### Magnet pozicioniranje
- Žep širina: ~75mm (±1.00mm)
- Globina žepa: 6.5mm (debelina magneta)
- Cobot mora polagati magnet v žep s **±0.03mm** toleranco → vakuumski gripper + počasno spuščanje

## Varnost

- CE skladna varnostna ograja z varnostnimi vrati
- Safety PLC — cobot se ustavi pri odprtju vrat
- Operator vstopa samo med menjavo plošč (med cikli)
- Cobot deluje v "collaborative mode" — omejena hitrost in sila
