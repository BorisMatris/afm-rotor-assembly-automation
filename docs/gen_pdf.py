from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                 TableStyle, HRFlowable, PageBreak)
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from datetime import date

OUTPUT = '/home/ubuntu/.openclaw/workspace/afm-rotor-assembly-automation/docs/AFM-Rotor-Assembly-Automation-Concept.pdf'

doc = SimpleDocTemplate(OUTPUT, pagesize=A4,
    leftMargin=20*mm, rightMargin=20*mm,
    topMargin=20*mm, bottomMargin=20*mm)

styles = getSampleStyleSheet()

BLUE = colors.HexColor('#17375E')
LIGHT_BLUE = colors.HexColor('#BDD7EE')
ACCENT = colors.HexColor('#2E75B6')
GRAY = colors.HexColor('#F2F2F2')
GREEN = colors.HexColor('#E8F5E9')
YELLOW = colors.HexColor('#FFF9C4')

title_style = ParagraphStyle('Title', parent=styles['Title'],
    fontSize=24, textColor=BLUE, spaceAfter=4*mm, alignment=TA_CENTER)
subtitle_style = ParagraphStyle('Subtitle', parent=styles['Normal'],
    fontSize=12, textColor=ACCENT, spaceAfter=2*mm, alignment=TA_CENTER)
meta_style = ParagraphStyle('Meta', parent=styles['Normal'],
    fontSize=9, textColor=colors.gray, alignment=TA_CENTER, spaceAfter=8*mm)
h1_style = ParagraphStyle('H1', parent=styles['Heading1'],
    fontSize=14, textColor=BLUE, spaceBefore=8*mm, spaceAfter=3*mm)
h2_style = ParagraphStyle('H2', parent=styles['Heading2'],
    fontSize=11, textColor=ACCENT, spaceBefore=5*mm, spaceAfter=2*mm)
body_style = ParagraphStyle('Body', parent=styles['Normal'],
    fontSize=9.5, leading=14, spaceAfter=2*mm)
bullet_style = ParagraphStyle('Bullet', parent=styles['Normal'],
    fontSize=9.5, leading=14, leftIndent=10*mm, spaceAfter=1*mm)
note_style = ParagraphStyle('Note', parent=styles['Normal'],
    fontSize=8.5, textColor=colors.HexColor('#555555'), leading=12,
    leftIndent=5*mm, spaceAfter=2*mm)
warn_style = ParagraphStyle('Warn', parent=styles['Normal'],
    fontSize=9, textColor=colors.HexColor('#7B3F00'), leading=13,
    leftIndent=5*mm, spaceAfter=2*mm, backColor=YELLOW)
code_style = ParagraphStyle('Code', parent=styles['Normal'],
    fontSize=8, fontName='Courier', leading=12, leftIndent=5*mm,
    spaceAfter=2*mm, backColor=colors.HexColor('#F5F5F5'))

def h1(t): return Paragraph(t, h1_style)
def h2(t): return Paragraph(t, h2_style)
def p(t): return Paragraph(t, body_style)
def b(t): return Paragraph(f'• {t}', bullet_style)
def note(t): return Paragraph(f'<i>{t}</i>', note_style)
def warn(t): return Paragraph(f'⚠ {t}', warn_style)
def code(t): return Paragraph(t.replace('\n', '<br/>').replace('  ', '&nbsp;&nbsp;'), code_style)
def sp(n=1): return Spacer(1, n*4*mm)
def hr(): return HRFlowable(width='100%', thickness=0.5, color=LIGHT_BLUE, spaceAfter=3*mm)

def tbl(data, widths, hdr=True):
    t = Table(data, colWidths=widths)
    s = [
        ('FONTNAME', (0,0), (-1,-1), 'Helvetica'),
        ('FONTSIZE', (0,0), (-1,-1), 9),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, GRAY]),
        ('GRID', (0,0), (-1,-1), 0.3, colors.HexColor('#CCCCCC')),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
    ]
    if hdr:
        s += [
            ('BACKGROUND', (0,0), (-1,0), BLUE),
            ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
            ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ]
    t.setStyle(TableStyle(s))
    return t

story = []

# ─── NASLOVNICA ───────────────────────────────────────────────────────────────
story += [
    sp(6),
    Paragraph('MATRIS d.o.o.', ParagraphStyle('Co', parent=styles['Normal'],
        fontSize=11, textColor=ACCENT, alignment=TA_CENTER, spaceAfter=2*mm)),
    Paragraph('AFM Rotor Assembly', title_style),
    Paragraph('Automation Concept Study', title_style),
    sp(2),
    HRFlowable(width='60%', thickness=2, color=ACCENT, spaceAfter=4*mm),
    sp(1),
    Paragraph('Avtomatizacija sestave rotorja axial flux motorja', subtitle_style),
    Paragraph('z industrijskim kolaborativnim robotom (Cobot)', subtitle_style),
    sp(3),
    Paragraph(f'Datum: {date.today().strftime("%d. %m. %Y")}', meta_style),
    Paragraph('Verzija: 2.1  |  Zaupno — Matris d.o.o.', meta_style),
    sp(6),
    HRFlowable(width='100%', thickness=0.5, color=LIGHT_BLUE),
    sp(2),
    Paragraph('Jelenčeva ulica 1, 4000 Kranj, Slovenija  |  info@matris.eu  |  matris.eu',
        ParagraphStyle('Foot', parent=styles['Normal'], fontSize=8,
            textColor=colors.gray, alignment=TA_CENTER)),
    PageBreak(),
]

# ─── 1. IZVRŠNI POVZETEK ──────────────────────────────────────────────────────
story += [
    h1('1. Izvršni povzetek'), hr(),
    p('Matris d.o.o. razvija axial flux permanentno-magnetne elektromotorje (AFM) visoke '
      'gostote moči. Sestava rotorja je ključni korak, ki zahteva natančno pozicioniranje '
      'NdFeB magnetov v FR4 ploščo z epoxy lepljenjem. Ta dokument predstavlja konceptno '
      'študijo avtomatizacije s cobotom (v2.1 — posodobljene specifikacije in stroškovnik).'),
    sp(),
    p('<b>Ključne lastnosti koncepta v2.1:</b>'),
    b('Serijski proces: rotor po rotor — brez tveganja preteka pot life epoxya'),
    b('Pnevmatski dozirnik za epoxy — natančno doziranje ±5% volumena'),
    b('Lastna izdelava gripperjev (DMG DMU50, DMG CMx 800V) — prihranek ~3.600 EUR'),
    b('Software razvoj interno z AI podporo (Flux)'),
    sp(),
    tbl([
        ['Parameter', 'Vrednost'],
        ['Motor', 'Matris AFM 55kW'],
        ['Magnetov na rotor', '10 (NdFeB N42, zaporedje N-S-N-S...)'],
        ['Dimenzije magneta', '70 × 50 × 6,5 mm'],
        ['Rotorjev v celici', '10 (mreža 5×2)'],
        ['Pozicionirna toleranca', '±0,1 mm'],
        ['Epoxy pot life', '30 minut'],
        ['Način doziranja', 'Pnevmatski kartušni dozirnik'],
        ['Proces', 'Serijski (rotor po rotor)'],
        ['Priporočen cobot', 'Dobot CR10A'],
        ['Gripperji', 'Lastna proizvodnja — Al 7075'],
        ['Software', 'Interni razvoj (DobotStudio Pro + Lua)'],
        ['Ocenjena investicija', '~35.500 EUR (brez DDV)'],
        ['Ocenjena vračilna doba', '< 14 mesecev'],
    ], [85*mm, 85*mm]),
    PageBreak(),
]

# ─── 2. OPIS PROCESA ──────────────────────────────────────────────────────────
story += [
    h1('2. Opis sestavljalnega procesa'), hr(),
    h2('2.1 Serijski cikel — rotor po rotor'),
    p('<b>Logika:</b> Cobot dokonča vsak rotor v celoti preden gre na naslednjega. '
      'To odpravlja tveganje preteka pot life epoxya in poenostavlja software.'),
    sp(),
    tbl([
        ['Korak', 'Operacija', 'Čas', 'Opomba'],
        ['1', 'Premik na rotor pozicijo', '2 s', 'Hitro pozicioniranje'],
        ['2', 'Epoxy v 10 žepov (spodaj)', '40 s', 'Pnevmatski dozirnik, 4 s/žep'],
        ['3', 'Namesti 10 magnetov', '50 s', '5 s/magnet z rotacijo 6. osi'],
        ['4', 'Epoxy na magnete (zgoraj)', '25 s', 'Pnevmatski dozirnik, 2,5 s/magnet'],
        ['5', 'Položi zgornjo FR4 ploščo', '6 s', 'Vakuumski gripper'],
        ['6', 'Položi aluminijasti stiskalnik', '6 s', 'Mehanični gripper'],
        ['7', 'Aktiviraj pnevmatsko stiskanje', '2 s', 'I/O signal na PLC — 5 min stiskanja'],
        ['8', 'Premik na naslednji rotor', '3 s', 'Medtem stiskanje teče vzporedno'],
        ['SKUPAJ', 'En rotor', '~134 s (~2,2 min)', ''],
        ['10 rotorjev', 'Celoten cikel', '~22 min + 5 min zadnje stiskanje = ~27 min', ''],
    ], [14*mm, 65*mm, 42*mm, 49*mm]),
    sp(),
    warn('Pot life epoxya je 30 minut. Celoten cikel 10 rotorjev traja ~27 min — '
         'rezerva je samo ~3 min. Priporočamo: na začetku vsake serije preveriti svežino '
         'kartuše in ne mešati epoxya < 5 min pred iztekom pot life.'),
    sp(),
    h2('2.2 Upravljanje pot life — serijski pristop'),
    p('Ker je proces serijski, vsak rotor potrebuje le ~2,2 min epoxy dela — '
      'ni tveganja preteka za posamičen rotor. Tveganje nastane samo pri skupnem '
      'ciklu 10 rotorjev (27 min > 30 min pot life ni možen scenarij, ker stiskanje '
      'teče vzporedno). V praksi je epoxy varen skozi celoten cikel.'),
    b('Vsak rotor: epoxy nanesen → magnet položen → pokrit v < 2,2 min ✓'),
    b('Ni paralelnega lepljenja → ni časovnega stresa'),
    b('Enostavnejši software, lažje debugganje'),
    sp(),
    h2('2.3 Pnevmatski dozirnik epoxya'),
    tbl([
        ['Parameter', 'Specifikacija'],
        ['Tip', 'Pnevmatski kartušni dozirnik'],
        ['Kartuša', '400 ml dvokomponentni epoxy'],
        ['Mešanje', 'Statični mešalnik (mixer tip)'],
        ['Nadzor', 'Pnevmatski ventil + časovni nadzor'],
        ['Krmiljenje', 'Digitalni I/O iz cobot kontrolerja'],
        ['Natančnost', '±5% volumena'],
    ], [60*mm, 110*mm]),
    sp(),
    h2('2.4 Sarža magnetov'),
    p('Magneti so predorientirani v aluminijastem tulcu (neferomagneten material). '
      'Cobot pobira magnete iz sarže z vakuumskim gripperjem in jih položi v žep '
      'z ustrezno rotacijo 6. osi (radialna orientacija — koordinate v sekciji 3.2).'),
    b('Priporočena kapaciteta sarže: 20–30 magnetov (dovolj za 2–3 rotorje)'),
    b('Operator napolni saržo medtem ko cobot dela — brez prekinitve cikla'),
    b('Preverjanje prazne sarže: senzor v sarži + alarm na HMI'),
    PageBreak(),
]

# ─── 3. GEOMETRIJA ────────────────────────────────────────────────────────────
story += [
    h1('3. Geometrija rotorja'), hr(),
    h2('3.1 FR4 rotor plošča — risba SP2025-0063-0048'),
    tbl([
        ['Parameter', 'Vrednost', 'Toleranca'],
        ['Zunanja dimenzija', 'Ø 260 mm', '±0,2 mm'],
        ['Debelina', '5 mm', '±0,2 mm'],
        ['Material', 'FR4 (stekloplastika, neferomagnetna)', '—'],
        ['Število žepov', '10', '—'],
        ['Radij žepov (notranji)', 'R 89,55 mm', '±0,03 mm'],
        ['Radij žepov (zunanji)', 'R 122,95 mm', '±0,03 mm'],
        ['Širina žepa', '~75 mm', '±1,00 mm'],
        ['Montažne izvrtine', '6× Ø 6,4 mm', 'SKOZNJE'],
        ['Masa', '294,88 g', '—'],
    ], [70*mm, 75*mm, 25*mm]),
    sp(),
    note('Srednji radij: R_mid = (89,55 + 122,95) / 2 = 106,25 mm'),
    sp(),
    h2('3.2 Koordinate magnetnih žepov (izhodišče = center rotorja)'),
    tbl([
        ['Žep', 'Kot', 'X [mm]', 'Y [mm]', 'Polarnost', 'Zasuk gripperja'],
        ['1',  '0°',   '+106,25', '0,00',    'N', '0°'],
        ['2',  '36°',  '+86,02',  '+62,49',  'S', '36°'],
        ['3',  '72°',  '+32,84',  '+101,10', 'N', '72°'],
        ['4',  '108°', '−32,84',  '+101,10', 'S', '108°'],
        ['5',  '144°', '−86,02',  '+62,49',  'N', '144°'],
        ['6',  '180°', '−106,25', '0,00',    'S', '180°'],
        ['7',  '216°', '−86,02',  '−62,49',  'N', '216°'],
        ['8',  '252°', '−32,84',  '−101,10', 'S', '252°'],
        ['9',  '288°', '+32,84',  '−101,10', 'N', '288°'],
        ['10', '324°', '+86,02',  '−62,49',  'S', '324°'],
    ], [15*mm, 18*mm, 25*mm, 28*mm, 25*mm, 32*mm]),
    sp(),
    note('Cobot 6. os se zasuka za kot žepa (stolpec "Zasuk gripperja") za pravilno '
         'radialno orientacijo magneta. Polarnost se menja N-S-N-S... Cobot ne preverja '
         'polarnosti — to naredi Hall senzor pred namestitvijo (QC modul).'),
    PageBreak(),
]

# ─── 4. OPREMA ────────────────────────────────────────────────────────────────
story += [
    h1('4. Oprema delovne celice'), hr(),
    h2('4.1 Primerjava cobotov'),
    tbl([
        ['Parameter', 'A: UR5e', 'B: Dobot CR10A\n(priporočeno)', 'C: JAKA Zu 7'],
        ['Repeatability', '±0,03 mm', '±0,05 mm', '±0,02 mm'],
        ['Payload', '5 kg', '10 kg', '7 kg'],
        ['Doseg', '850 mm', '1.300 mm', '800 mm'],
        ['Komunikacija', 'Ethernet', 'Profinet / EtherNet/IP', 'Ethernet'],
        ['Ekosistem', 'Odličen', 'Dober', 'Manjši'],
        ['Leasing', 'Na povp.', 'od 1.000 EUR/mes', 'Na povp.'],
        ['Cena cobota', '~38.000 EUR', '~23.000 EUR', '~20.000 EUR'],
        ['Skupaj celica', '~63.750 EUR', '~35.500 EUR', '~32.500 EUR'],
    ], [40*mm, 38*mm, 52*mm, 40*mm]),
    sp(),
    note('Priporočamo Dobot CR10A: doseg 1.300 mm pokriva celotno 5×2 mrežo rotorjev, '
         '10 kg payload zadostuje za vse operacije. Repeatability ±0,05 mm zadostuje '
         'za zahtevano toleranco ±0,1 mm z 2× varnostno rezervo.'),
    sp(),
    h2('4.2 End-of-arm tooling — lastna proizvodnja'),
    p('Naši stroji: <b>DMG DMU50</b> (5-osni obdelovalni center), <b>DMG CMx 800V</b> (stružnica)'),
    sp(),
    tbl([
        ['Oprema', 'Stroj', 'Material', 'Opomba'],
        ['Vakuumski gripper — magneti', 'DMG DMU50', 'Al 7075', 'Neferomagneten, 2 vakuum priključka'],
        ['Mehanični gripper — FR4 ploše', 'DMG DMU50', 'Al 7075', 'Vakuumski, prilagojen za Ø 260 mm'],
        ['Mehanični gripper — Al stiskalniki', 'DMG CMx 800V', 'Al 7075', 'Preprost, prilagojen za stiskalnik'],
        ['Adapter na cobot', 'DMG DMU50', 'Al', 'ISO 9409-1-50-4-M6'],
        ['Dozirnik — nosilec', 'DMG DMU50', 'Al', 'Fiksiran na cobot roko'],
    ], [52*mm, 30*mm, 20*mm, 68*mm]),
    sp(),
    p('<b>Prednosti lastne izdelave:</b>'),
    b('Cena: ~500 EUR materiala vs ~4.100 EUR nakupa komercialnih gripperjev'),
    b('Prilagodljivost: hitre spremembe ob dizajn spremembah motorja'),
    b('Know-how: interna znanja za vzdrževanje brez zunanjega serviserja'),
    b('Čas: 2–3 dni izdelave na obstoječih strojih'),
    sp(),
    h2('4.3 Pnevmatski sistem'),
    tbl([
        ['Komponenta', 'Specifikacija', 'Količina', 'Cena'],
        ['Pnevmatski dozirnik', 'Kartušni sistem 400 ml', '1×', '~1.500 EUR'],
        ['Statični mešalniki', 'Za 400 ml kartuše', '50×', '~250 EUR'],
        ['Pnevmatski cilindri', 'Za stiskanje, Ø 50 mm', '10×', '~1.500 EUR'],
        ['Ventilski blok', 'SMC, 5/2 ventili', '1×', '~800 EUR'],
        ['Kompresor', '8 bar, 200 L/min', '1×', '~1.200 EUR'],
        ['Cevi in fitingi', 'PU cevi, komplet', '—', '~400 EUR'],
    ], [52*mm, 52*mm, 16*mm, 30*mm]),
    PageBreak(),
]

# ─── 5. SOFTWARE ──────────────────────────────────────────────────────────────
story += [
    h1('5. Software arhitektura'), hr(),
    h2('5.1 Tehnologije'),
    tbl([
        ['Komponenta', 'Tehnologija', 'Opomba'],
        ['Cobot program', 'DobotStudio Pro', 'Grafično + Lua skripte'],
        ['HMI', 'Siemens KTP700 Touch panel', 'Start/Stop, Status, Alarmi'],
        ['PLC', 'Siemens S7-1200', 'Krmiljenje pnevmatike'],
        ['Komunikacija', 'Profinet', 'Cobot ↔ PLC ↔ HMI'],
        ['Nadzor (opcija)', 'Python/Node.js', 'Logiranje, traceability'],
    ], [40*mm, 70*mm, 60*mm]),
    sp(),
    h2('5.2 Glavni program — psevdokoda (Lua)'),
    code(
        '-- AFM Rotor Assembly v2.1\n'
        '-- Koordinate zepov (iz risbe SP2025-0063-0048)\n'
        'local slots = {\n'
        '  {x=106.25, y=0.00,    angle=0},\n'
        '  {x=86.02,  y=62.49,   angle=36},\n'
        '  {x=32.84,  y=101.10,  angle=72},\n'
        '  {x=-32.84, y=101.10,  angle=108},\n'
        '  {x=-86.02, y=62.49,   angle=144},\n'
        '  {x=-106.25,y=0.00,    angle=180},\n'
        '  {x=-86.02, y=-62.49,  angle=216},\n'
        '  {x=-32.84, y=-101.10, angle=252},\n'
        '  {x=32.84,  y=-101.10, angle=288},\n'
        '  {x=86.02,  y=-62.49,  angle=324},\n'
        '}\n\n'
        'function assemble_rotor(rotor_id)\n'
        '  move_to_rotor(rotor_id)               -- korak 1\n'
        '  for i, slot in ipairs(slots) do\n'
        '    move_to_slot(slot, "bottom")         -- korak 2: epoxy spodaj\n'
        '    dispense_epoxy(4.0)\n'
        '  end\n'
        '  for i, slot in ipairs(slots) do\n'
        '    pick_magnet()\n'
        '    verify_polarity(i)                   -- QC: Hall senzor\n'
        '    rotate_gripper(slot.angle)           -- radialna orientacija\n'
        '    place_magnet(slot)                   -- korak 3\n'
        '  end\n'
        '  for i, slot in ipairs(slots) do\n'
        '    move_to_slot(slot, "top")            -- korak 4: epoxy zgoraj\n'
        '    dispense_epoxy(2.5)\n'
        '  end\n'
        '  pick_fr4(); place_fr4()               -- korak 5\n'
        '  pick_press(); place_press()            -- korak 6\n'
        '  activate_press(rotor_id)              -- korak 7\n'
        '  log_cycle(rotor_id)                   -- korak 8\n'
        'end'
    ),
    note('Zasuk gripperja (rotate_gripper) temelji na koordinatni tabeli iz risbe '
         'SP2025-0063-0048 — ne na generičnih 36°. Vsak žep ima svojo točno vrednost.'),
    PageBreak(),
]

# ─── 6. QC ────────────────────────────────────────────────────────────────────
story += [
    h1('6. Kakovost in kontrola (QC)'), hr(),
    h2('6.1 Vgrajena kontrola v procesu'),
    tbl([
        ['Kontrola', 'Metoda', 'Implementacija'],
        ['Pozicija magneta', 'Vision kamera', 'Preveri offset po namestitvi (< ±0,1 mm)'],
        ['Polaritet magneta', 'Hall senzor', 'Verifikacija N-S zaporedja pred namestitvijo'],
        ['Vakuum gripperja', 'Vakuum senzor', 'Preveri pritrditev pred premikom'],
        ['Sila prileganja', 'Force sensor', 'Preveri silo pri namestitvi magneta'],
        ['Epoxy nanos', 'IR kamera (opcija)', 'Preveri enakomernost nanosa'],
    ], [38*mm, 38*mm, 94*mm]),
    sp(),
    h2('6.2 Post-procesna kontrola'),
    tbl([
        ['Parameter', 'Metoda', 'Toleranca'],
        ['Toleranca montaže', 'CMM meritev', '±0,05 mm'],
        ['Vlakna v lepilu', 'Vizualna kontrola', 'Brez mehurčkov > 1 mm'],
        ['Stiskanje', 'Torque check', '15–20 Nm'],
    ], [50*mm, 60*mm, 60*mm]),
    PageBreak(),
]

# ─── 7. RIZIKI ────────────────────────────────────────────────────────────────
story += [
    h1('7. Riziki in mitigacije'), hr(),
    tbl([
        ['Rizik', 'Verjetnost', 'Vpliv', 'Mitigacija'],
        ['Magneti se privlačijo', 'Visoka', 'Visoka',
         'Vakuumski gripper z dovolj močjo (> 2× teža), test na DMG pred integracijo'],
        ['Epoxy se posuši v dozirniku', 'Srednja', 'Visoka',
         'Čiščenje cikla vsakih 30 min, senzor tlaka, zamenjava mešalnika po vsaki seriji'],
        ['Cobot ne dosega tolerance', 'Nizka', 'Visoka',
         'Kalibracija pred vsako izmeno, referenčne točke, vision korekcija'],
        ['Okvara cobota', 'Nizka', 'Visoka',
         'Preventivno vzdrževanje, rezervni deli na zalogi, servisna pogodba'],
        ['Pnevmatska okvara', 'Srednja', 'Srednja',
         'Dvojni ventili, ročni bypass, tlačni senzor za alarm'],
        ['Napačna polaritet magneta', 'Srednja', 'Visoka',
         'Hall senzor PRED namestitvijo, alarm + zaustavitev pri napaki'],
    ], [40*mm, 22*mm, 18*mm, 90*mm]),
    PageBreak(),
]

# ─── 8. STROŠKOVNIK ───────────────────────────────────────────────────────────
story += [
    h1('8. Stroškovnik investicije'), hr(),
    tbl([
        ['Kategorija', 'Oprema / Storitev', 'Cena'],
        ['Cobot sistem', 'Dobot CR10A + krmilnik', '~23.000 EUR'],
        ['EOAT material', 'Al plošče, vakuum komponente (lastna izdelava)', '~500 EUR'],
        ['Pnevmatski sistem', 'Dozirnik, cilindri, ventili, kompresor', '~5.650 EUR'],
        ['Sarža magnetov', 'Al tulec + pozicionirni jig', '~800 EUR'],
        ['Delovna miza + fiksture', 'Miza + FR4 jigi', '~3.000 EUR'],
        ['Varnost + elektro', 'Varnostna ograja + PLC + HMI', '~3.500 EUR'],
        ['Integracija', 'Interno + AI podpora (Flux)', '~0 EUR'],
        ['Reserve (10%)', 'Nepredvideni stroški', '~1.550 EUR'],
        ['', '', ''],
        ['SKUPAJ (brez DDV)', '', '~35.500 EUR'],
    ], [70*mm, 80*mm, 20*mm]),
    sp(),
    note('Vse cene so ocene. Priporočamo 3 ponudbe pred naročilom.'),
    sp(),
    h2('8.1 ROI ocena'),
    tbl([
        ['Parameter', 'Vrednost'],
        ['Ročni čas sestave (1 operater)', '~8 min/rotor'],
        ['Avtomatiziran čas', '~2,2 min/rotor'],
        ['Prihranek časa', '73%'],
        ['Strošek operaterja (ocena)', '~25 EUR/h'],
        ['Prihranek/leto (1 izmena, 220 dni, 50 rotorjev/dan)', '~38.000 EUR'],
        ['Vračilna doba investicije', '< 12 mesecev'],
    ], [110*mm, 60*mm]),
    PageBreak(),
]

# ─── 9. AKCIJSKI PLAN ────────────────────────────────────────────────────────
story += [
    h1('9. Akcijski plan'), hr(),
    tbl([
        ['#', 'Aktivnost', 'Odgovorna oseba', 'Rok', 'Status'],
        ['1', 'Potrditev koncepta in izbira cobota', 'Boris', '1 teden', '☐'],
        ['2', 'Povpraševanje pri dobaviteljih', 'Boris', '2 tedna', '☐'],
        ['3', 'Naročilo Dobot CR10A', 'Boris', '2 tedna', '☐'],
        ['4', 'Izdelava gripperjev (DMG DMU50/CMx)', 'Inžiring', '3 tedne', '☐'],
        ['5', 'Naročilo pnevmatskega sistema', 'Boris', '2 tedna', '☐'],
        ['6', 'Gradnja mize in fikstur', 'Inžiring', '4 tedne', '☐'],
        ['7', 'Postavitev varnostne ograje + PLC', 'Inžiring', '5 tednov', '☐'],
        ['8', 'Software faza 1 — osnovni premiki', 'Boris + Flux', '5 tednov', '☐'],
        ['9', 'Software faza 2 — epoxy + magneti', 'Boris + Flux', '7 tednov', '☐'],
        ['10', 'Software faza 3 — stiskanje + QC', 'Boris + Flux', '9 tednov', '☐'],
        ['11', 'Integracija in testiranje', 'Skupaj', '10 tednov', '☐'],
        ['12', 'Validacija (10 rotorjev)', 'Skupaj', '11 tednov', '☐'],
        ['13', 'Produkcijski zagon', 'Skupaj', '12–14 tednov', '☐'],
    ], [8*mm, 65*mm, 35*mm, 28*mm, 14*mm]),
    sp(),
    note('Skupni čas do produkcije: ~12–14 tednov ob takojšnjem začetku.'),
    sp(3),
    HRFlowable(width='100%', thickness=0.5, color=LIGHT_BLUE, spaceAfter=3*mm),
    Paragraph(
        'Matris d.o.o.  |  Jelenčeva ulica 1, 4000 Kranj  |  info@matris.eu  |  matris.eu',
        ParagraphStyle('F1', parent=styles['Normal'], fontSize=8,
            textColor=colors.gray, alignment=TA_CENTER)),
    Paragraph(
        f'Dokument generiran: {date.today().strftime("%d. %m. %Y")}  |  Verzija 2.1  |  Zaupno — Matris d.o.o.',
        ParagraphStyle('F2', parent=styles['Normal'], fontSize=8,
            textColor=colors.gray, alignment=TA_CENTER)),
]

doc.build(story)
print(f"PDF shranjen: {OUTPUT}")
