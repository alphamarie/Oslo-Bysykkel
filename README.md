
# Oslo Bysykkel Sanntidsdata #

## Kjøring ##
Programmet er skrevet i Python versjon 3.7.4.
Kjør programmet med ved å kjøre **Hovedprogram.py**. 
I windows terminal:
```bash
py Hovedprogram.py
```

## Feilmeldinger ##
Hovedprogrammet teller antall feil under kjøring i *antall_feilmeldinger*.
Kjør programmet uten å printe stasjonsinfo for å kun få feilmeldinger:

``` bash
def __init__(self):
      self.antall_feilmeldinger = 0;
      alle_stasjonene = self.opprett_stasjoner()
      print("Antall feil: " + str(self.antall_feilmeldinger))

```

## API ##
Sanntidsdataen er hentet fra [oslobysykkel.no](https://oslobysykkel.no/apne-data/sanntid).


---
Laget av Alpha Marie Storvik
