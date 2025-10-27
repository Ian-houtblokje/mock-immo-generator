# realistic_immo

### Kleinschalige aapasbare generator voor fictieve vastgoeddata (Nederlands).

## Snelstart
1. Installeer afhankelijkheden:
   pip install numpy pandas

2. Run generator:
   python main.py
   Outputbestand: immokantoor.csv (of Documents/immokantoor.csv bij schrijfprobleem)

## Belangrijkste onderdelen
- main.py         — startpunt; genereert dataset en schrijft CSV
- generator.py    — genereer_panden: bouwt rijen met kenmerken
- distriebuties.py— functies: genereer_oppervlakte, genereer_tuin, genereer_kwaliteit, genereer_bouwjaar
- pricing.py      — prijzen_model, tuin_waardeverhoging, bouwjaar_invloed
- config.py       — alle instelbare parameters (prijzen per m², verdelingen, RNG, enz.)

## Config aanpassen
- N_ROWS, CSV_PATH, RNG_SEED
- PPM2_KERN: basisprijs per m² per stijl
- STIJL_KANS: kansverdeling per stijl
- TUIN_INVLOED: parameters voor tuinaanpassing (basis_factor, extra_factor_per_verdubbeling, max_factor, schaaltype)
- BOUWJAAR_BUCKETS_KANS: buckets met kansverdeling voor bouwjaar
- OPPERVLAKTE_VERDELING en TUIN_VERDELING: gemiddelden, std, min, max per stijl
- KWALITEIT: levels, kansen en modifier
- SLAAPKAMERS: formule voor her toevoegen van meer slaapkamers op basis van grootte van het pand en het type
- VERDIEPINGEN: kans dat een stijl een aantal verdiepingen heeft

## Belangrijke implementatiepunten / tips
- Tuinfactor: factor = 1 + min(base + extra, max_factor). Bij sqrt-schaal wordt basis berekend met sqrt(ratio).
- Bouwjaar: invloed vermindert prijs lineair met leeftijd volgens BOUWJAAR_INVLOED.
- - Als verkoopprijs of tuin extreem hoge waarden toont: controleer TUIN_VERDELING / OPPERVLAKTE_VERDELING en TUIN_INVLOED parameters.

## Debuggen
- Print samples: main.py toont eerste 10 rijen.
- Om specifieke stappen te inspecteren: log tussenresultaten in prijzen_model (bijv. basis_ppm, tuin_factor, bouwjaar_factor).
- Voor consistente resultaten: wijzig RNG_SEED in config.py.

## Licentie / bijdrage
- Pas code direct aan in de Python-bestanden.
- Houd consistentie in config-namen en -structuren bij wijzigingen.

## Auteur 
Ian H. 
