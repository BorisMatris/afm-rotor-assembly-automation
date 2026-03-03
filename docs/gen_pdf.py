
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

def h1(t): return Paragraph(t, h1_style)
def h2(t): return Paragraph(t, h2_style)
def p(t): return Paragraph(t, body_style)
def b(t): return Paragraph(f'• {t}', bullet_style)
def note(t): return Paragraph(f'<i>{t}</i>', note_style)
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

# NASLOVNICA
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
    Paragraph('Verzija: 1.0  |  Zaupno — Matris d.o.o.', meta_style),
    sp(6),
    HRFlowable(width='100%', thickness=0.5, color=LIGHT_BLUE),
    sp(2),
    Paragraph('Jelenčeva ulica 1, 4000 Kranj, Slovenija  |  info@matris.eu  |  matris.eu',
        ParagraphStyle('Foot', parent=styles['Normal'], fontSize=8,
            textColor=colors.gray, alignment=TA_CENTER)),
    PageBreak(),
]

# 1. POVZETEK
story += [
    h1('1. Izvršni povzetek'), hr(),
    p('Matris d.o.o. razvija axial flux permanentno-magnetne elektromotorje (AFM) visoke '
      'gostote moči. Sestava rotorja je ključni korak, ki zahteva natančno pozicioniranje '
      'NdFeB magnetov v FR4 ploščo z epoxy lepljenjem. Ta dokument predstavlja konceptno '
      'študijo avtomatizacije s cobotom.'),
    sp(),
    tbl([
        ['Parameter', 'Vrednost'],
        ['Motor', 'Matris AFM 55kW'],
        ['Magnetov na rotor', '10 (NdFeB N42, zaporedje N-S-N-S...)'],
        ['Dimenzije magneta', '70 x 50 x 6.5 mm'],
        ['Rotorjev v celici', '10 (mreza 5x2)'],
        ['Pozicionirna toleranca', '+/- 0.1 mm'],
        ['Epoxy pot life', '30 minut'],
        ['Priporocen cobot', 'Dobot CR10A'],
        ['Ocenjena investicija', '~48.750 EUR (Opcija B)'],
        ['Ocenjena vracilna doba', '< 18 mesecev'],
    ], [80*mm, 90*mm]),
    PageBreak(),
]

# 2. PROCES
story += [
    h1('2. Opis sestavljalnega procesa'), hr(),
    h2('2.1 Korak po korak — avtomatizirani cikel'),
    tbl([
        ['Korak', 'Operacija', 'Cas', 'Opomba'],
        ['1', 'Premik cobota na rotor', '3 s', 'Med rotorji v mrezi'],
        ['2', 'Epoxy v 10 zepov (spodaj)', '45 s', '4.5 s/zep: premik + doziranje'],
        ['3', 'Poberi in polozi 10 magnetov', '60 s', '6 s/magnet iz sarze'],
        ['4', 'Epoxy na magnete (zgoraj)', '30 s', 'Prelaz po magnetih'],
        ['5', 'Polozi zgornja FR4 plosca', '8 s', 'Vakuumski gripper'],
        ['6', 'Polozi aluminijasti stiskalnik', '8 s', ''],
        ['7', 'Aktiviraj pnevmaticno stiskanje', '2 s', 'I/O signal na PLC'],
        ['SKUPAJ', 'En rotor', '~156 s', '~2.6 min na rotor'],
        ['10 rotorjev', 'Celoten cikel', '~26 min', 'Rezerva 4 min za pot life'],
    ], [15*mm, 70*mm, 20*mm, 65*mm]),
    sp(),
    h2('2.2 Upravljanje pot life epoxya (30 min)'),
    p('Priporocamo <b>dve seriji po 5 rotorjev</b> za vecjo varnostno rezervo:'),
    b('Serija A (rotorji 1-5): ~13 min sestave → stiskanje aktivirano → 17 min rezerve'),
    b('Serija B (rotorji 6-10): ~13 min sestave → stiskanje aktivirano → 17 min rezerve'),
    sp(),
    h2('2.3 Sarza magnetov'),
    p('Magneti so predorientirani v aluminijastem tulcu (neferomagneten material). '
      'Cobot pobira magnete iz sarze z vakuumskim gripperjem in jih polozi v zep '
      'z ustrezno rotacijo 6. osi (radialna orientacija).'),
    b('Priporocena kapaciteta sarze: 20-50 magnetov (dovolj za 2-5 rotorjev)'),
    b('Operator napolni sarzо med menjavo serij — brez prekinitve cikla'),
    PageBreak(),
]

# 3. GEOMETRIJA
story += [
    h1('3. Geometrija rotorja'), hr(),
    h2('3.1 FR4 rotor plosca — risba SP2025-0063-0048'),
    tbl([
        ['Parameter', 'Vrednost', 'Toleranca'],
        ['Zunanja dimenzija', 'Phi 260 mm', '+/- 0.2 mm'],
        ['Debelina', '5 mm', '+/- 0.2 mm'],
        ['Material', 'FR4 (stekloplastika, neferomagnetna)', '—'],
        ['Stevilo zepov', '10', '—'],
        ['Radij zepov (notranji)', 'R 89.55 mm', '+/- 0.03 mm'],
        ['Radij zepov (zunanji)', 'R 122.95 mm', '+/- 0.03 mm'],
        ['Sirina zepa', '~75 mm', '+/- 1.00 mm'],
        ['Montazne izvrtine', '6x Phi 6.4 mm', 'SKOZNJE'],
        ['Masa', '294.88 g', '—'],
    ], [70*mm, 75*mm, 35*mm]),
    sp(),
    h2('3.2 Koordinate magnetnih zepov (izhodisce = center rotorja)'),
    tbl([
        ['Zep', 'Kot', 'X [mm]', 'Y [mm]', 'Polarnost', 'Zasuk gripperja'],
        ['1', '0 deg', '+106.25', '0.00', 'N', '0 deg'],
        ['2', '36 deg', '+86.02', '+62.49', 'S', '36 deg'],
        ['3', '72 deg', '+32.84', '+101.10', 'N', '72 deg'],
        ['4', '108 deg', '-32.84', '+101.10', 'S', '108 deg'],
        ['5', '144 deg', '-86.02', '+62.49', 'N', '144 deg'],
        ['6', '180 deg', '-106.25', '0.00', 'S', '180 deg'],
        ['7', '216 deg', '-86.02', '-62.49', 'N', '216 deg'],
        ['8', '252 deg', '-32.84', '-101.10', 'S', '252 deg'],
        ['9', '288 deg', '+32.84', '-101.10', 'N', '288 deg'],
        ['10', '324 deg', '+86.02', '-62.49', 'S', '324 deg'],
    ], [15*mm, 20*mm, 25*mm, 25*mm, 25*mm, 35*mm]),
    sp(),
    note('Srednji radij: R_mid = (89.55 + 122.95) / 2 = 106.25 mm. '
         'Cobot 6. os se zasuka za kot zepa za pravilno radialno orientacijo magneta.'),
    PageBreak(),
]

# 4. OPREMA
story += [
    h1('4. Oprema delovne celice'), hr(),
    h2('4.1 Primerjava cobotov'),
    tbl([
        ['Parameter', 'A: UR5e', 'B: Dobot CR10A (priporoceno)', 'C: JAKA Zu 7'],
        ['Repeatability', '+/- 0.03 mm', '+/- 0.03 mm', '+/- 0.02 mm'],
        ['Payload', '5 kg', '10 kg', '7 kg'],
        ['Doseg', '850 mm', '1300 mm', '800 mm'],
        ['Komunikacija', 'Ethernet', 'Profinet / EtherNet/IP', 'Ethernet'],
        ['Ekosistem', 'Odlicen', 'Dober', 'Manjsi'],
        ['Leasing', 'Na povp.', 'od 1.000 EUR/mes', 'Na povp.'],
        ['Cena cobota', '~38.000 EUR', '~23.000 EUR', '~20.000 EUR'],
        ['Skupaj celica', '~63.750 EUR', '~48.750 EUR', '~45.750 EUR'],
    ], [40*mm, 40*mm, 58*mm, 32*mm]),
    sp(),
    note('Priporocamo Dobot CR10A: doseg 1300mm pokriva celotno 5x2 mrezo rotorjev, '
         '10kg payload zadostuje za vse operacije, leasing moznost zmanjsa zacetno investicijo.'),
    sp(),
    h2('4.2 End-of-arm tooling'),
    p('<b>Pozor:</b> NdFeB magneti so mocno magnetni — gripper mora biti iz neferomagnetnega '
      'materiala (Al, plastika). Priporocamo vakuumski sistem.'),
    tbl([
        ['Oprema', 'Model', 'Namen', 'Cena'],
        ['Vakuumski gripper', 'Schmalz SGPN 70x50', 'Magneti in FR4 plosce', '~800 EUR'],
        ['Vakuumska crpalka', 'Schmalz ECBPi', 'Vakuum vir', '~1.200 EUR'],
        ['Tool changer', 'Schunk SWK', 'Menjava gripper/dispenser', '~1.500 EUR'],
        ['Epoxy dispenser tip', 'Nordson', 'Doziranje epoxya', '~600 EUR'],
    ], [45*mm, 45*mm, 50*mm, 30*mm]),
    sp(),
    h2('4.3 Pnevmatski stiskalni sistem'),
    tbl([
        ['Oprema', 'Kolicina', 'Cena'],
        ['Pnevmatski cilindri', '10x (en na rotor)', '~2.000 EUR'],
        ['Ventilski blok SMC', '1x', '~800 EUR'],
        ['Aluminijasti stiskalniki (jigi)', '10x', '~3.000 EUR'],
    ], [80*mm, 40*mm, 50*mm]),
    PageBreak(),
]

# 5. LAYOUT
story += [
    h1('5. Layout delovne celice'), hr(),
    h2('5.1 Tloris (shematski)'),
    Paragraph(
        '<font face="Courier" size="8.5">'
        '+--------------------------------------------------------+<br/>'
        '|                 VARNOSTNA OGRAJA (CE)                  |<br/>'
        '|                                                        |<br/>'
        '|  [SARZA magnetov]   [COBOT CR10A]   [EPOXY dispenser]  |<br/>'
        '|                          ARM                           |<br/>'
        '|                                                        |<br/>'
        '|    [R1]  [R2]    [R3]  [R4]    [R5]                   |<br/>'
        '|    [R6]  [R7]    [R8]  [R9]    [R10]                  |<br/>'
        '|                                                        |<br/>'
        '|            DELOVNA MIZA 5x2 (10 rotorjev)             |<br/>'
        '|                                                        |<br/>'
        '|  [OPERATOR vstop] -- nalaganje/raznalaganje ploc       |<br/>'
        '+--------------------------------------------------------+'
        '</font>', body_style),
    sp(),
    h2('5.2 Varnostne zahteve'),
    b('CE skladna varnostna ograja z varnostnimi vrati (safety interlock)'),
    b('Safety PLC — cobot se ustavi pri odprtju vrat'),
    b('Collaborative mode — omejena hitrost (1 m/s) in sila (150 N)'),
    b('Elektromagnetne zavore — zaustavitev v 18ms pri izpadu napajanja'),
    b('Operator vstopa samo med menjavo ploc (cobot v cakanju)'),
    PageBreak(),
]

# 6. STROSKOVNIK
story += [
    h1('6. Stroskovnik investicije'), hr(),
    tbl([
        ['Kategorija', 'Oprema / Storitev', 'Dobavitelj', 'Cena'],
        ['Cobot sistem', 'Dobot CR10A + krmilnik', 'Unchained Robotics', '~23.000 EUR'],
        ['EOAT', 'Vakuumski gripper + tool changer', 'Schmalz / Schunk', '~4.100 EUR'],
        ['Epoxy sistem', 'Nordson dispenser + SMC regulator', 'Nordson', '~2.150 EUR'],
        ['Sarza magnetov', 'Al tulec + pozicionirni jig', 'Lokalno', '~1.300 EUR'],
        ['Pnevmatika', '10x cilinder + ventili + Al jigi', 'SMC / lokalno', '~2.800 EUR'],
        ['Miza + fiksture', 'Delovna miza + FR4 jigi', 'Lokalno', '~4.000 EUR'],
        ['Varnost + elektro', 'Ograja + PLC + HMI', 'Siemens', '~2.900 EUR'],
        ['Integracija + prog.', 'Programiranje + testiranje', 'Integrator', '~8.000 EUR'],
        ['', '', 'SKUPAJ (brez DDV)', '~48.250 EUR'],
    ], [38*mm, 58*mm, 38*mm, 36*mm]),
    sp(),
    h2('6.1 ROI ocena'),
    tbl([
        ['Parameter', 'Vrednost'],
        ['Rocni cas sestave (1 operater)', '~8 min/rotor'],
        ['Avtomatiziran cas', '~2.6 min/rotor'],
        ['Prihranak casa', '67%'],
        ['Strosek operaterja (ocena)', '~25 EUR/h'],
        ['Prihranak/leto (1 izmena, 220 dni)', '~35.000 EUR'],
        ['Vracilna doba investicije', '< 18 mesecev'],
    ], [80*mm, 90*mm]),
    PageBreak(),
]

# 7. NASLEDNJI KORAKI
story += [
    h1('7. Naslednji koraki in odprta vprasanja'), hr(),
    h2('7.1 Akcijski plan'),
    tbl([
        ['Korak', 'Aktivnost', 'Rok'],
        ['1', 'Potrditev koncepta in izbira cobota (A/B/C)', '2 tedna'],
        ['2', 'Povprasevanje pri dobaviteljih (Dobot, Schmalz, Nordson)', '2 tedna'],
        ['3', 'Detajlni nacrt celice (CAD layout)', '4 tedne'],
        ['4', 'Narocilo cobota in opreme', '6 tednov'],
        ['5', 'Gradnja mize, fikstur, pnevmatike', '8 tednov'],
        ['6', 'Integracija in programiranje cobota', '10 tednov'],
        ['7', 'Testiranje in validacija (10 rotorjev)', '12 tednov'],
        ['8', 'Produkcijski zagon', '14 tednov'],
    ], [12*mm, 100*mm, 30*mm]),
    sp(),
    h2('7.2 Odprta vprasanja'),
    b('Izbira cobota: UR5e vs Dobot CR10A vs JAKA Zu 7'),
    b('Kapaciteta sarze: koliko magnetov v enem tulcu? (priporocamo 20-50)'),
    b('Menjava gripperja med ciklom ali multi-tool (epoxy + vakuum hkrati)?'),
    b('Interni programer ali zunanji integrator?'),
    b('CE certifikacija: interni varnostni inzenir ali zunanja agencija?'),
    sp(3),
    HRFlowable(width='100%', thickness=0.5, color=LIGHT_BLUE, spaceAfter=3*mm),
    Paragraph(
        'Matris d.o.o.  |  Jelenčeva ulica 1, 4000 Kranj  |  info@matris.eu  |  matris.eu',
        ParagraphStyle('F1', parent=styles['Normal'], fontSize=8,
            textColor=colors.gray, alignment=TA_CENTER)),
    Paragraph(
        f'Dokument generiran: {date.today().strftime("%d. %m. %Y")}  |  Verzija 1.0  |  Zaupno',
        ParagraphStyle('F2', parent=styles['Normal'], fontSize=8,
            textColor=colors.gray, alignment=TA_CENTER)),
]

doc.build(story)
print(f"Shranjeno: {OUTPUT}")
