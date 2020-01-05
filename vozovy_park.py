class Vozidlo:
    def __init__(self, spz):
        self.spz = spz

class MercedesBenz(Vozidlo):
    kapacita = 42
    naklady_na_km = 30
    palivo = "nafta"

class Setra(Vozidlo):
    kapacita = 30
    naklady_na_km = 40
    palivo = "nafta"

class TeslaElectro(Vozidlo):
    kapacita = 42
    naklady_na_km = 20
    palivo = "elektro"
    dojezd = 200

class IsuzuHybrid(Vozidlo):
    kapacita = 40
    palivo = "hybrid"
    dojezd = 200
    naklady_na_km_elektro = 20 
    naklady_na_km_nafta = 40
    naklady_na_km = 0

class ZadneVozidlo:
    kapacita = 0
    naklady_na_km = 10000

# výpočet nákladů na km u hybridu
def naklady_na_km_hybridu(vuz, vzdalenost):
    if vuz.palivo == "hybrid":
        vzdalenost_pro_naftu = vzdalenost - vuz.dojezd
        if vzdalenost_pro_naftu > 0:
            vuz.naklady_na_km = (vzdalenost_pro_naftu * vuz.naklady_na_km_nafta + vuz.dojezd * vuz.naklady_na_km_elektro) / vzdalenost
        else:
            vuz.naklady_na_km = vuz.naklady_na_km_elektro
    return vuz.naklady_na_km


def najdi_auto(seznam_aut, minimalni_kapacita, vzdalenost):
    vyhovujici_auta = [ZadneVozidlo]
    optimalni_auto = [vyhovujici_auta[0]]
    # přepočte náklady na km, pokud je to hybrid
    for auto in seznam_aut:
        auto.naklady_na_km = naklady_na_km_hybridu(auto, vzdalenost)
    # vybere auta s vyhovující kapacitou a dojezdem   
    for auto in seznam_aut:
        if auto.kapacita >= minimalni_kapacita and (auto.palivo in ["nafta", "hybrid"] or (auto.palivo == "elektro" and auto.dojezd >= vzdalenost)):
            vyhovujici_auta.append(auto)
    # z kapacitně vyhovujících aut vybere auto s nejmenšími náklady
    for i in range(0, len(vyhovujici_auta)-1):
        if vyhovujici_auta[i+1].naklady_na_km < vyhovujici_auta[i].naklady_na_km:
            optimalni_auto = vyhovujici_auta[i+1]
    return optimalni_auto


bus_1 = MercedesBenz("3E3 2020")
bus_2 = TeslaElectro("AA 1111")
bus_3 = Setra("5J4 2222")
bus_4 = IsuzuHybrid("2E2 3333")

vozovy_park = [bus_1, bus_2, bus_3, bus_4]

print(najdi_auto(vozovy_park, 40, 250))
