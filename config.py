###
# Config bestand met alle aanpasbare waarden bruikbaar in de generator
# Aanpasbaar voor andere data 
###

import numpy as np

RNG_SEED = 75 
RNG = np.random.default_rng(RNG_SEED)

N_ROWS = 250
CSV_PATH = "immokantoor"

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
