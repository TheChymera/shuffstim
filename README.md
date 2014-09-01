#Shuffsim

This is a script suite allowing you to simulate (at present only deterministic) card shuffles.

We currently include code to simulate the Australian and Tasmanian shuffles (see [this paper for reference](http://www.scirp.org/journal/PaperInformation.aspx?PaperID=24163#.U-gXe_Ztgck)).

##Dependencies

* **[NumPy](https://en.wikipedia.org/wiki/Numpy)** - in [Portage](http://en.wikipedia.org/wiki/Portage_(software)) as **app-text/texlive**

##Usage
From the containing folder:
```
python shuffsim_cli.py [-h] [-d DECK_SIZE] [-t TASMANIAN_DOWN_NUMBER] [-f]
                       shuffle
```

Example (doing an Australian shuffle on a 50-card deck):
```
python shuffsim_cli.py -d 50 australian
```

##Arguments

```
positional arguments:
  shuffle               Shuffle type to use, we currently support the
                        following types of shuffles: australian, tasmanian,
                        texas.

optional arguments:
  -h, --help            show this help message and exit
  -d DECK_SIZE, --deck-size DECK_SIZE
                        Specify the number of files in the deck.
  -t TASMANIAN_DOWN_NUMBER, --tasmanian-down-number TASMANIAN_DOWN_NUMBER
                        Specify the number of files in the deck.
  -f, --force-simulation
                        Do NOT use formulaic solutions (even when they are
                        present), force actual simulation.
```

Released under the GPLv3 license.
Project led by Horea Christian (address all e-mail correspondence to: h.chr@mail.ru)
