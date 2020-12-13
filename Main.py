import json
import requests

class Hovedprogram:
    main()

    def __main__():
        response = requests.get(" https://gbfs.urbansharing.com/oslobysykkel.no/station_information.json")
        print(response.status_code)
