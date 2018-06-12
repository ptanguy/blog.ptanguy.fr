Title: RTL-SDR Installation
Date: 2017-06-15
Authors: ptanguy
slug: rtl-sdr-install
Summary: Installation des outils pour utiliser une clé USB RTL2832U
Status: published

Pour l'installation du logiciel j'ai suivi le guide disponible à l'adresse suivant https://ranous.files.wordpress.com/2016/03/rtl-sdr4linux_quickstartv10-16.pdf .

En résumé cela donne ça:

    $ git clone git://git.osmocom.org/rtl-sdr.git
    $ cd rtl-sdr/
    $ mkdir build
    $ cd build
    $ cmake ../ -DINSTALL_UDEV_RULES=ON
    $ make
    $ sudo make install
    $ sudo ldconfig
    $ sudo cp ../rtl-sdr.rules /etc/udev/rules.d/

Il ne faut pas charger le driver de la clé usb qui charger par défaut en éditant le fichier:

    $ sudo vim /etc/modprobe.d/blacklist-rtl.conf

et en ajoutant la ligne suivante: blacklist dvb_usb_rtl28xxu


On vérifie ensuite l'installation:
```
    $ rtl_test -t
    Found 1 device(s):
      0:  Generic, RTL2832U, SN: 77771111153705700

      Using device 0: Generic RTL2832U
      Found Rafael Micro R820T tuner
      Supported gain values (29): 0.0 0.9 1.4 2.7 3.7 7.7 8.7 12.5 14.4 15.7 16.6 19.7 20.7 22.9 25.4 28.0 29.7 32.8 33.8 36.4 37.2 38.6 40.2 42.1 43.4 43.9 44.5 48.0 49.6 
      [R82XX] PLL not locked!
      Sampling at 2048000 S/s.
      No E4000 tuner found, aborting.
```

Et enfin, on fait un petit test du démodulateur FM pour écouter une radio:

    $ rtl_fm -f 93.5M -s 192000 -r 48000 - | aplay -r 48k -f S16_LE -t raw -c 1
    
Le wiki officiel est évidemment aussi une bonne source d'information: http://osmocom.org/projects/sdr/wiki/rtl-sdr
