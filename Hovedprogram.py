import json
import requests
from Stasjon import Stasjon
from Status import Status

class Hovedprogram:
    def __init__(self):
        self.antall_feilmeldinger = 0;
        alle_stasjonene = self.opprett_stasjoner()
        for s in alle_stasjonene:
            print(s.get_stasjons_info())
        #print("Antall feil: " + str(self.antall_feilmeldinger))

    def funnet_feil(self):          #Legger til 1 i telleren for feilmeldinger
        self.antall_feilmeldinger +=  1

    def hent_JSON(self, url):       #returnerer JSON-data fra input URL
        try:
            response = requests.get(url)
            status_kode = (response.status_code) #200 = alt bra med get(url)
            obj = response.json()
            return obj
        except:
            funnet_feil()
            print("Kunne ikke hente data fra " + url + ". Statuskode: " + status_kode)

    def opprett_statuser(self):     #Oppretter status-objekter
        status_info_string = self.hent_JSON("https://gbfs.urbansharing.com/oslobysykkel.no/station_status.json")
        updated_at = status_info_string['last_updated']
        stations = status_info_string['data']['stations']
        if not stations:
            funnet_feil()
            print("Ingen stasjoner funnet. ")
            return
        alle_statuser = []
        for status in stations:
            try:
                Ny_status = Status(updated_at, status['station_id'], status['is_installed'],
                                    + status['is_renting'], status['num_bikes_available'],
                                    + status['num_docks_available'], status['last_reported'], status['is_returning'])
                alle_statuser.append(Ny_status)
            except:
                funnet_feil()
                print("Feil ved opprettelse av status. ")
        return alle_statuser

    def opprett_stasjoner(self):    #Oppretter stasjon-objekter
        alle_statuser = self.opprett_statuser()
        station_info_string = self.hent_JSON("https://gbfs.urbansharing.com/oslobysykkel.no/station_information.json")
        updated_at = station_info_string['last_updated']
        stations = station_info_string['data']['stations']
        if not stations:
            return
        alle_stasjoner = []
        for station in stations:
            for status in alle_statuser:
                if (status.get_status_id() == station['station_id']):
                    stasjons_status = status
            try:
                ny_stasjon = Stasjon(updated_at, station['station_id'], station['name'], station['address'], +
                                    station['lat'], station['lon'], station['capacity'], stasjons_status)
                alle_stasjoner.append(ny_stasjon)
            except:
                funnet_feil()
                "Feil ved opprettelse av stasjon. "
        return alle_stasjoner

Hovedprogram()
