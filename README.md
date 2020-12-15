
# Oslo Bysykkel Sanntidsdata #

## Om programmet ##
Programmet henter sanntidsdata om Oslo Bysykkels sykkelstativer og viser ledige sykler og låser på alle Bysykkel-stasjoner. Det er også mulig å modere for å søke etter stativ-navn og kun få opp relevante stativer.

## Biblioteker ##
Programmet bruker bibliotekene *json* og *requests*.

## Kjøring ##
Programmet er skrevet i Python versjon 3.7.4.
Start programmet ved å kjøre **Hovedprogram.py**.
I windows terminal:
```bash
py Hovedprogram.py
```

## Feilmeldinger ##
Hovedprogrammet teller antall feil under kjøring i *antall_feilmeldinger*.
Kjør programmet uten å printe stasjonsinfo for å kun få feilmeldinger som vist under:

``` bash
def __init__(self):
      self.antall_feilmeldinger = 0;
      alle_stasjonene = self.opprett_stasjoner()
      print("Antall feil: " + str(self.antall_feilmeldinger))

```

## Søk på stativer ##

Bytt ut *self.print_alle_stativer(alle_stasjoner)* med *sok_paa_stativer(alle_stasjoner)* i *__init__* i Hovedprogram for å kun søke på stativer som vist under:

``` bash
def __init__(self):
      self.antall_feilmeldinger = 0;
      alle_stasjoner = self.opprett_stasjoner()
      self.sok_paa_stativer(alle_stasjoner)
```


## API ##
Sanntidsdataen er hentet fra [oslobysykkel.no](https://oslobysykkel.no/apne-data/sanntid).


---
Laget av Alpha Marie Storvik
