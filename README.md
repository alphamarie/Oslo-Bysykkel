
#Bysykkel informasjon

##Kjøring
Kjør programmet med ved å kjøre Hovedprogram.py
```bash
py Hovedprogram.py
```

##Feilmeldinger
Hovedprogrammet teller antall feil under kjøring i *antall_feilmeldinger*.
Kjør programmet uten å printe stasjonsinfo for å kun få feilmeldinger:

``` bash
def __init__(self):
      self.antall_feilmeldinger = 0;
      alle_stasjonene = self.opprett_stasjoner()
      print("Antall feil: " + str(self.antall_feilmeldinger))

```

##API
Sanntidsdataen er hentet fra [oslobysykkel.no](https://oslobysykkel.no/apne-data/sanntid).


---
Laget av Alpha Marie Storvik
