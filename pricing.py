########
# Code voor prijsbepaling gebaseerd op:
# - waardeverhoging voor grote tuinen
# - bouwjaar invloed voor een lagere prijs voor oudere panded
# - prijzenmodel voor een gevectoriseerde vraagrpijs
########

import numpy as np 
from config import *

def tuin_waardeverhoging(opp_tuin, opp_woning):
    ratio = np.maximum(opp_tuin / np.maximum(opp_woning, 1), 0)
    bonus = np.where(ratio > 1, ratio -1 * TUIN_INVLOED["extra_factor_per_verdubbeling"], 0)

    if TUIN_INVLOED["schaaltype"] == "sqrt":
        verhoging = TUIN_INVLOED["basis_factor"] * np.sqrt(ratio)
    else:  # lineaire groei
        verhoging = TUIN_INVLOED["basis_factor"] * ratio

    verhoging += bonus
    verhoging = np.minimum(verhoging, TUIN_INVLOED['max_factor'])

    factor = 1+verhoging
    return factor

def bouwjaar_invloed(bouwjaar):
    huidig_jaar = 2025
    leeftijd = huidig_jaar - bouwjaar

    factor = 1.0 - BOUWJAAR_INVLOED["ouderdom_korting_per_jaar"] * leeftijd
    return factor


def prijzen_model(stijl, oppervlakte, tuin, bouwjaar, level):
    
    #basisprijs
    basis_ppm =np.array([PPM2_KERN[s] for s in stijl], dtype=float)
    vraagprijs = basis_ppm * oppervlakte

    #prijsverhoging tuin
    vraagprijs *= tuin_waardeverhoging(tuin, oppervlakte)
    
    #kwaliteit modifier
    vraagprijs *= np.array([KWALITEIT['modifier'][k-1] for k in level], dtype=float)

    #invloed bouwjaar
    vraagprijs *= bouwjaar_invloed(bouwjaar)

    #afwijking voor realisme 
    afwijking = RNG.normal(loc=1, scale=0.1, size=len(vraagprijs))
    afwijking = np.clip(afwijking, 0.8, 1.2)
    vraagprijs *= afwijking

    # verkoopprijs
    verkoopprijs = vraagprijs.copy()
    is_verkocht = RNG.random(len(verkoopprijs)) < VERKOCHT_KANS

    #korting toepassen op verkochte huizen
    korting = RNG.normal(KORTING['gemiddeld'], KORTING['standaardafwijking'], len(stijl))
    korting = np.clip(korting, 0, KORTING["max"])
    verkoopprijs[is_verkocht] *= (1 - korting[is_verkocht])
    verkoopprijs[~is_verkocht] = np.nan


    return vraagprijs.round(-3).astype(int), verkoopprijs.round(-3)
