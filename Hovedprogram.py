import json
import requests
from Stasjon import Stasjon
from Status import Status

class Hovedprogram:
    def __init__(self):
        self.antall_feilmeldinger = 0;
        alle_stasjoner = self.opprett_stasjoner()
        self.print_alle_stativer(alle_stasjoner)
        #self.sok_paa_stativer(alle_stasjoner)
        print("Antall feil: " + str(self.antall_feilmeldinger))

    def print_alle_stativer(self, alle_stasjoner):
        if not alle_stasjoner:
            return
        for s in alle_stasjoner:
            print(s.get_stasjons_info())

    def funnet_feil(self, feilmelding):          #Legger til 1 i telleren for feilmeldinger
        print("Feilmelding: " + feilmelding + "\n")
        self.antall_feilmeldinger +=  1

    def hent_JSON(self, url):       #returnerer JSON-data fra input URL
        try:
            respons = requests.get(url)
            status_kode = (respons.status_code) #skal være 200 hvis alt bra med get(url)
            data = respons.json()
            return data
        except:
            self.funnet_feil("Kunne ikke hente data fra " + url + ". ")

    def opprett_statuser(self):     #Oppretter status-objekter
        try:
            status_info_string = self.hent_JSON("https://gbfs.urbansharing.com/oslobysykkel.no/station_status.json")
            updated_at = status_info_string['last_updated']
            statuser = status_info_string['data']['stations']
        except:
            self.funnet_feil("Kunne ikke opprette statuser. ")
            return
        if not statuser:
            funnet_feil("Ingen stasjoner funnet. ")
            return
        alle_statuser = []
        for status in statuser:
            try:
                ny_status = Status(updated_at, status['station_id'], status['is_installed'],
                                    + status['is_renting'], status['num_bikes_available'],
                                    + status['num_docks_available'], status['last_reported'], status['is_returning'])
                alle_statuser.append(ny_status)
            except:
                self.funnet_feil("Feil ved opprettelse av status. ")
        return alle_statuser

    def opprett_stasjoner(self):    #Oppretter stasjon-objekter
        try:
            alle_statuser = self.opprett_statuser()
            station_info_string = self.hent_JSON("https://gbfs.urbansharing.com/oslobysykkel.no/station_information.json")
            updated_at = station_info_string['last_updated']
            stasjoner = station_info_string['data']['stations']
        except:
            self.funnet_feil("Kunne ikke opprette stasjoner. ")
            return
        if not stasjoner:
            return
        alle_stasjoner = []
        for station in stasjoner:
            for status in alle_statuser:
                if (status.get_status_id() == station['station_id']):
                    stasjons_status = status
            try:
                ny_stasjon = Stasjon(updated_at, station['station_id'], station['name'], station['address'], +
                                    station['lat'], station['lon'], station['capacity'], stasjons_status)
                alle_stasjoner.append(ny_stasjon)
            except:
                self.funnet_feil("Feil ved opprettelse av stasjon. ")
        return alle_stasjoner


    def sok_paa_stativer(self, alle_stasjoner):   #Oppgir informasjon om alle stativer der stativ-navnet
        soke_ord = input("\n Søk på stativ: ")  #inneholder søkeord oppgitt av bruker
        stativer_med_treff_paa_soke_ord = []
        for s in alle_stasjoner:
            if soke_ord in s.get_name():
                stativer_med_treff_paa_soke_ord.append(s)
        for t in stativer_med_treff_paa_soke_ord:
            print(t.get_stasjons_info())


Hovedprogram()
