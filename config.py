###
# Config bestand met alle aanpasbare waarden bruikbaar in de generator
# Aanpasbaar voor andere data 
###

import numpy as np

RNG_SEED = 25 
RNG = np.random.default_rng(RNG_SEED)

N_ROWS = 250
CSV_PATH = "immo_mock"

VERKOCHT_KANS = 0.85

# standaardprijs per m² voor elk type 
PPM2_KERN = {
    "appartement": 2930,  
    "rijhuis":     2550,  
    "halfopen":    2600,  
    "open":        2650,  
    "villa":       2800,  
    "landelijk":   2300,  
    "hoeve":       2350,  
}

# kans dat een stijl voorkomt (som = 1!)
STIJL_KANS = {
    "appartement": 0.15,
    "rijhuis":     0.15,
    "halfopen":    0.15,
    "open":        0.15,
    "villa":       0.15,
    "landelijk":   0.15,
    "hoeve":       0.10
}

# instellingen van de kwaliteit
KWALITEIT = {
    "levels": [1, 2, 3, 4, 5],
    "labels": {1: "eenvoudig", 2: "standaard", 3: "comfortable", 4: "modern", 5: "luxe"},
    "kans": [0.15, 0.35, 0.25, 0.18, 0.07], # som moet 1 zijn!
    "modifier": [0.8, 1, 1.05, 1.15, 1.3]

}

# invloed van het bouwjaar op de prijs
BOUWJAAR_INVLOED = {
    "ouderdom_korting_per_jaar": 0.001,
    "ouderdom_modifier_min": 0.8,
    "ouderdom_modifier_max": 1.05
}

TUIN_INVLOED = {
    "basis_factor": 0.10,
    "extra_factor_per_verdubbeling": 0.05,           
    "max_factor": 0.35,             
    "schaaltype": "sqrt" # 'sqrt' of 'linear'
}

# kans dat een pand van een bepaald jaar voorkomt 
# opbouw: startjaar - eindjaar - kans (som moet 1 zijn)
BOUWJAAR_BUCKETS_KANS = [
    (1850, 1899, 0.10), 
    (1900, 1919, 0.10),
    (1920, 1939, 0.10),
    (1940, 1959, 0.10),
    (1960, 1979, 0.10),
    (1980, 1999, 0.10),
    (2000, 2009, 0.10),
    (2010, 2015, 0.10),
    (2016, 2020, 0.10),
    (2021, 2025, 0.10),
]

# statistische waarde kortingen
KORTING = {
    "gemiddeld": 0.07,
    "standaardafwijking": 0.03,
    "max": 0.15
}

# Oppervlakteverdeling per woningstijl
OPPERVLAKTE_VERDELING = {
    "appartement": {"mean": 105, "std": 25, "min": 40, "max": 220},
    "rijhuis":     {"mean": 150, "std": 40, "min": 70, "max": 300},
    "halfopen":    {"mean": 150, "std": 40, "min": 70, "max": 300},
    "open":        {"mean": 200, "std": 70, "min": 90, "max": 500},
    "villa":       {"mean": 200, "std": 70, "min": 90, "max": 500},
    "landelijk":   {"mean": 200, "std": 70, "min": 90, "max": 500},
    "hoeve":       {"mean": 200, "std": 70, "min": 90, "max": 500}
}

# Tuinverdeling per woningstijl
TUIN_VERDELING = {
    "appartement": {"mean": 15,   "std": 20,  "min": 0,   "max": 250},
    "rijhuis":     {"mean": 120,  "std": 80,  "min": 0,   "max": 800},
    "halfopen":    {"mean": 120,  "std": 80,  "min": 0,   "max": 800},
    "open":        {"mean": 350,  "std": 250, "min": 50,  "max": 1500},
    "villa":       {"mean": 800,  "std": 600, "min": 100, "max": 6000},
    "landelijk":   {"mean": 1500, "std": 1200,"min": 200, "max": 15000},
    "hoeve":       {"mean": 3000, "std": 2500,"min": 500, "max": 30000},
}

# Kans op aantal verdiepingen 1-2-3 (som moet 1 per stijl zijn)

VERDIEPINGEN = {
    "AANTAL":[1, 2, 3],
    "KANS":{
        "appartement": [0.90, 0.08, 0.02],  
        "rijhuis":     [0.07, 0.90, 0.03],
        "halfopen":    [0.05, 0.85, 0.10],
        "open":        [0.05, 0.85, 0.10],
        "villa":       [0.05, 0.50, 0.45],
        "landelijk":   [0.15, 0.70, 0.15],
        "hoeve":       [0.25, 0.65, 0.10]
    }
}

SLAAPKAMER_MODEL = {
    "appartement": {"base": 1.0, "rate": 0.012, "min": 1, "max": 3},   
    "rijhuis":     {"base": 2.0, "rate": 0.008, "min": 1, "max": 4},   
    "halfopen":    {"base": 2.0, "rate": 0.008, "min": 2, "max": 4},   
    "open":        {"base": 2.0, "rate": 0.007, "min": 2, "max": 5},   
    "villa":       {"base": 2.5, "rate": 0.009, "min": 3, "max": 6},   
    "landelijk":   {"base": 2.0, "rate": 0.007, "min": 2, "max": 5},   
    "hoeve":       {"base": 2.5, "rate": 0.008, "min": 3, "max": 6}    
}