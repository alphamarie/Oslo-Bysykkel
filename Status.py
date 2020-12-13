
class Status:
    def __init__(self, sist_oppdatert, status_id, is_installed, is_renting, num_bikes_available, num_docks_available, last_reported, is_returning):
        self._sist_oppdatert = sist_oppdatert #i integer POSIX timestamp format
        self._status_id = status_id
        self._is_installed = is_installed
        self._is_renting = is_renting
        self._num_bikes_available = num_bikes_available
        self._num_docks_available = num_docks_available
        self._last_reported = last_reported
        self._is_returning = is_returning

    def get_stasjons_info(self):
        text = ("\n Ledige sykler: " + str(self._num_bikes_available) + "\n Ledige låser: " + str(self._num_docks_available))
        return text

    def get_sist_oppdatert(self):
        return self._sist_oppdatert

    def set_sist_oppdatert(self, x):
        self._sist_oppdatert = x

    def get_status_id(self):
        return self._status_id

    def set_status_id(self, x):
        self._status_id = x

    def get_is_installed(self):
        return self._is_installed

    def set_is_installed(self, x):
        self._is_installed = x

    def get_is_renting(self):
        return self._is_renting

    def set_is_renting(self, x):
        self._is_renting = x

    def get_num_bikes_available(self):
        return self._num_bikes_available

    def set_num_bikes_available(self, x):
        self._num_bikes_available = x

    def get_num_docks_available(self):
        return self._num_docks_available

    def set_num_docks_available(self, x):
        self._num_docks_available = x

    def _last_reported(self):
        return self._last_reported

    def set_last_reported(self, x):
        self._last_reported = x

    def get_is_returning(self):
        return self._is_returning

    def set_is_returning(self, x):
        self._is_returning = x
