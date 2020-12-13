
class Stasjon:
    def __init__(self, oppdatert, stasjonsID, navn, adresse, lati, long, cap, stat):
        self._sist_oppdatert = oppdatert #i integer POSIX timestamp format
        self._station_id = stasjonsID
        self._name = navn
        self._adress = adresse
        self._lat = lati
        self._lon = long
        self._capactiy = cap
        self._status = stat

    def print_stasjons_info(self):
        print("Sykkel-stasjon: " + self._name)
        self._status.print_status_info()
        print(" ")

    def get_sist_oppdatert(self):
        return self._sist_oppdatert

    def set_sist_oppdatert(self, x):
        self._sist_oppdatert = x

    def get_station_id(self):
        return self._station_id

    def set_station_id(self, x):
        self._station_id = x

    def get_name(self):
        return self._name

    def set_name(self, x):
        self._name = x

    def get_adress(self):
        return self._adress

    def set_adress(self, x):
        self._adress = x

    def get_lat(self):
        return self._lat

    def set_lat(self, x):
        self._lat = x

    def get_lon(self):
        return self._lon

    def set_lon(self, x):
        self._lon = x

    def get_capactiy(self):
        return self._capactiy

    def set_capactiy(self, x):
        self._capactiy = x

    def get_status(self):
        return self._status

    def set_status(self, x):
        self._status = x
