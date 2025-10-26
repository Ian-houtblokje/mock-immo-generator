########
# Code voor de distributies van oppervlaktes, tuinen, verdiepingen, kamers. kwaliteit en bouw jaar
# Prijs wordt hiet NIET berekend
########

import numpy as np
from config import *

# Oppervlakte 
def genereer_oppervlakte(stijl, aantal):
    config = OPPERVLAKTE_VERDELING[stijl]
    opp = np.clip(RNG.normal(config['mean'], config['std'], aantal), config['min'], config['max']) #normale distributie
    return opp.round()

# Tuin
def genereer_tuin(stijl, aantal):
    config = TUIN_VERDELING[stijl]
    tuin = np.clip(RNG.normal(config['mean'], config['std'], aantal), config['min'], config['max']) #normale distributie
    return tuin.round()

# Kwaliteit 
def genereer_kwaliteit(aantal):
    levels = KWALITEIT['levels']
    kans = KWALITEIT['kans']
    return RNG.choice(levels, size=aantal, p=kans)

# Bouwjaar
def genereer_bouwjaar(aantal):
    jaren = []
    kansen = []

    for start, einde, kans in BOUWJAAR_BUCKETS_KANS:

        jaar_range = list(range(start, einde +1))
        jaren.extend(jaar_range)

        kans_per_jaar = kans / len(jaar_range)
        kansen.extend([kans_per_jaar] * len(jaar_range))

    return RNG.choice(jaren, size=aantal, p=kansen)