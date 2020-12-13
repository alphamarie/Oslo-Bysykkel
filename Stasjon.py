
class Stasjon:
    def __init__(self, last_updated, tation_id, name, adress, lat, lon, capactiy, status):
        self._last_updated = last_updated  #format:integer POSIX timestamp
        self._station_id = tation_id
        self._name = name
        self._adress = adress
        self._lat = lat
        self._lon = lon
        self._capactiy = capactiy
        self._status = status

    def get_stasjons_info(self):
        tekst = "\n Stativ: " + self._name + self._status.get_stasjon_info() +"\n"
        return tekst

    def get_last_updated(self):
        return self._last_updated

    def set_last_updated(self, x):
        self._last_updated = x

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
