# Analiza takt časa — AFM Rotor Assembly

## Predpostavke
- 10 rotorjev v celici (5×2)
- 10 magnetov na rotor
- Pot life epoxy: 30 min
- Cobot: UR5e (max hitrost 1.5 m/s, tipična 0.5-0.8 m/s pri natančnih operacijah)

## Operacije na enem rotorju

| Operacija | Čas (ocena) | Opombe |
|-----------|-------------|--------|
| Premik na rotor | 3 s | med rotorji |
| Epoxy 10 žepov | 45 s | 4.5s/žep: premik + doziranje |
| Poberi magnet #1-10 | 60 s | 6s/magnet: iz sarže + position + place |
| Epoxy na magnete | 30 s | 3s/magnet, samo prelaz |
| Položi FR4 zgoraj | 8 s | |
| Položi aluminij jig | 8 s | |
| Aktiviraj pnevmatiko | 2 s | I/O signal |
| **Skupaj na rotor** | **~156 s** | **~2.6 min** ✅ |

## Skupaj za 10 rotorjev
- 10 × 2.6 min = **26 minut**
- Pot life 30 min → **4 minute rezerve** ⚠️

## Kritična pot — epoxy timing

```
t=0:00  Začetek prvega rotorja — nanaša epoxy
t=0:45  Začetek polaganja magnetov (rotor 1)
t=2:36  Konec rotorja 1, začetek rotorja 2
...
t=26:00 Konec rotorja 10
t=30:00 Pot life epoxy poteče
```

**Rezerva: 4 minute** — to je TESNO. Priporočila:
1. Epoxy dispenser mora biti hiter in zanesljiv
2. Cobot hitrost optimizirati na max za premike (ne za pozicioniranje)
3. Razmisliti o doziranju v skupinah (5 rotorjev → stiskanje → naslednjih 5)

## Alternativni pristop: 2 seriji po 5

```
Serija A (rotorji 1-5):
  t=0:00  Epoxy + magneti + FR4 → rotorji 1-5 (~13 min)
  t=13:00 Stiskanje aktivirano za vse 5 hkrati

Serija B (rotorji 6-10):
  t=13:00 Epoxy + magneti + FR4 → rotorji 6-10 (~13 min)
  t=26:00 Stiskanje aktivirano
```

→ **17 minut rezerve** za vsako serijo ✅ Priporočeno!

## Throughput

| Scenarij | Čas/cikel | Rotorjev/h |
|----------|-----------|------------|
| 1 serija (10) | ~30 min | 20/h |
| 2 seriji (5+5) | ~28 min | 21/h |
| Z menjavo plošč | +5 min | 17/h |
