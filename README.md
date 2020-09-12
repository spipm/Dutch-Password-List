# Dutch cracking list repo

Spip's custom Dutch wordlists! It includes:

* Dutch wordlists! Massive lists scraped from Wikipedia, dictionaries, twitter, the bible, and then some
* A collection of best cracking rules and masks for hashcat


### Sources

| Thing        | Link           |
| ------------- |-------------|
| Twitter | See script |
| Wikipedia | https://wiki.kiwix.org/wiki/Content_in_all_languages |
| First names | http://www.naamkunde.net/?page_id=293 |
| Last names | https://github.com/digitalheir/family-names-in-the-netherlands |
| Dutch bible | https://oje.home.xs4all.nl/txt/bijbel/Het-Boek.txt |
| Wordlists | https://www.weakpass.com |
| Masks | https://blog.netspi.com/wp-content/uploads/2016/01/2015-Top40.hcmask |
| | https://raw.githubusercontent.com/trustedsec/hate_crack/master/masks/pathwell.hcmask |
| | https://raw.githubusercontent.com/hashcat/hashcat/master/masks/8char-1l-1u-1d-1s-compliant.hcmask |
| | https://raw.githubusercontent.com/hashcat/hashcat/master/masks/8char-1l-1u-1d-1s-noncompliant.hcmask |
| | https://github.com/hashcat/hashcat/blob/master/masks/rockyou-7-2592000.hcmask |
| | https://github.com/hashcat/hashcat/blob/master/masks/hashcat-default.hcmask |
| Rules | https://github.com/praetorian-code/Hob0Rules |
| | https://github.com/NSAKEY/nsa-rules |
| | https://github.com/hashcat/hashcat/tree/master/rules |
| | |


### Commands

#### Dump Wikipedia content
`./zimdump dump --dir=wikidump ~/Downloads/wikipedia_nl_all_nopic_2020-07.zim`

#### Password complexity regex
`grep -Poa "((?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@<=>~{|}^_\`?@\[\\]*+,-./:;&'\(\) \!\"#$%]).{8,})"`

From https://stackoverflow.com/questions/23699919/regular-expression-for-password-complexity


### Todo

* Create more/better markov chains for passphrases
* Make list of populair sentences (quotes, etc)

| Thing        | Link           |
| ------------- |-------------|
| Populaire citaten | http://www.citaten.nl/populaireauteurs.php |
| Spreekwoorden | https://nl.wikipedia.org/wiki/Lijst_van_Nederlandse_spreekwoorden_A-E |
| Gezegden | https://nl.wikipedia.org/wiki/Lijst_van_uitdrukkingen_en_gezegden_A-E |
| Straatnamen | https://www.kadaster.nl/zakelijk/producten/adressen-en-gebouwen/bag-compact |
