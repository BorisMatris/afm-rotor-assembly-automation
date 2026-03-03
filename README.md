# AFM Rotor Assembly Automation

Avtomatizirana sestava rotorja za **Matris AFM motor** z industrijskim cobotom.

## Proces

```
Za vsak rotor (10 rotorjev v mreži 5×2):
  1. Epoxy dispenser   → 10 žepov (spodnja FR4 plošča)
  2. Magnet placement  → 10 magnetov iz sarže (N-S-N-S...)
  3. Epoxy dispenser   → na magnete (zgoraj)
  4. FR4 zgornja plošča → položi
  5. Aluminij jig      → položi
  6. Pnevmatično stiskanje → aktivira
  7. Premik → naslednji rotor
```

## Specifikacije

| Parameter | Vrednost |
|-----------|----------|
| Motor | Matris AFM 55kW |
| Magnet dimenzije | 70 × 50 × 6.5 mm |
| Magnet tip | NdFeB N42 |
| Magnetov na rotor | 10 (N-S-N-S-N-S-N-S-N-S) |
| Rotorjev v celici | 10 (5×2 mreža) |
| Pozicionirna toleranca | ±0.1 mm |
| Epoxy pot life | 30 min |
| Doziranje | Pnevmatski dispenser |
| Sarža magnetov | Predorientirani tulec |

## Struktura

```
afm-rotor-assembly-automation/
│
├── docs/
│   ├── process-description.md    # Detajlni opis procesa
│   ├── cell-layout.md            # Layout delovne celice
│   ├── cobot-selection.md        # Primerjava in izbira cobota
│   └── safety.md                 # Varnostne zahteve
│
├── cobot/
│   ├── programs/                 # Cobot programi (URScript / TP)
│   │   ├── main_cycle.urp        # Glavni cikel
│   │   ├── epoxy_dispense.urp    # Epoxy nanašanje
│   │   ├── magnet_pick.urp       # Pobiranje magneta iz sarže
│   │   └── place_fr4.urp         # Polaganje FR4 plošče
│   └── tool/
│       └── gripper-spec.md       # Specifikacije vakuumskega gripperja
│
├── cell-design/
│   ├── layout.md                 # 5×2 mreža, pozicije
│   └── fixtures.md               # Vpenjalni sistemi, jigi
│
├── process/
│   ├── cycle-time-analysis.md    # Analiza takt časa
│   └── epoxy-timing.md           # Epoxy pot life management
│
└── bom/
    └── equipment-bom.md          # Seznam opreme in dobaviteljev
```

## Ključni izzivi

1. **Magnetna sila** — gripper mora biti vakuumski (ne feromagnetni!)
2. **±0.1mm toleranca** — zahteva visoko repeatability cobota
3. **Pot life 30 min** — za 10 rotorjev × 10 magnetov = kritično timing
4. **Polarnost N-S** — sarža mora zagotavljati pravilno orientacijo

## Cobot kandidati

| Model | Repeatability | Payload | Doseg | Cena |
|-------|--------------|---------|-------|------|
| **UR5e** ⭐ | ±0.03mm | 5kg | 850mm | ~38k€ |
| UR10e | ±0.05mm | 10kg | 1300mm | ~45k€ |
| Fanuc CRX-10iA | ±0.02mm | 10kg | 1418mm | ~42k€ |

**Priporočilo: UR5e** — zadostna natančnost, odlična ekosistem podpora, URScript enostaven za programiranje epoxy path-ov.

## Kontakt

Matris d.o.o. | [matris.eu](https://matris.eu)
