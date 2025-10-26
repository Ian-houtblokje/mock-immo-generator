import numpy as np
from config import *
from distriebuties import *
from pricing import prijzen_model

def genereer_panden(n_rows=N_ROWS):
    stijlen = list(STIJL_KANS.keys())
    stijl_kans = list(STIJL_KANS.values())
    stijl_array = RNG.choice(stijlen, size=n_rows, p=stijl_kans)

    oppervlakte = np.array([genereer_oppervlakte(s, 1)[0] for s in stijl_array])

    tuin = np.array([genereer_tuin(s, 1)[0] for s in stijl_array])

    bouwjaar = genereer_bouwjaar(n_rows)

    kwaliteit = genereer_kwaliteit(n_rows)

    vraagprijs, verkoopprijs = prijzen_model(
        stijl_array, oppervlakte, tuin, bouwjaar, kwaliteit
    )

    dataframe = {
        "stijl": stijl_array,
        "oppervlakte": oppervlakte,
        "tuin": tuin,
        "bouwjaar": bouwjaar,
        "kwaliteit": kwaliteit,
        "vraagprijs": vraagprijs,
        "verkoopprijs": verkoopprijs
    }

    return dataframe