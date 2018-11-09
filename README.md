# super-duper-journey

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/5b78a1524ac64e8eb275ff96d4caf404)](https://www.codacy.com?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Xartrick/super-duper-journey&amp;utm_campaign=Badge_Grade)

Projet / M3202C - Modélisations mathématiques @ IUT Aix-en-Provence

## Auteurs

* ACHACHE Sirine
* LE-GRAND Benjamin
* MARTINEZ Nicolas
* TARFI Emma

## Dépendances

* sagemath
* ffmpeg

### Arch Linux

```
$ sudo pacman -S sagemath ffmpeg
```

### Ubuntu

```
$ sudo apt-get install sagemath ffmpeg
```

## Installation des modules Python2

```
$ pip2 install -r requirements.txt --user
```

## Usage

```
$ ./main.sage --help
usage: main.sage.py [-h] [--output OUTPUT] [--audio AUDIO] [--width WIDTH]
                    [--height HEIGHT] [--fps FPS] [--bpm BPM] [-a]

Generate an animation with SageMath based on beat timing. For better result,
BPM should be divisible by FPS.

optional arguments:
  -h, --help       show this help message and exit
  --output OUTPUT  Output filename (default: output/output.mp4)
  --audio AUDIO    Audio filename (default: output/audio.mp3)
  --width WIDTH    Frame width (default: 1280)
  --height HEIGHT  Frame height (default: 720)
  --fps FPS        Frame rate (default: 30)
  --bpm BPM        Beat-per-minute (default: 150)
  -a               Add audio to final file (default: False)
```

Commande utilisé pour le rendu final :

```
$ ./main.sage --fps 60 -a
```

*Remarque 1 : le fichier `output/audio.mp3` doit être présent pour qu'il soit ajouté.*
*Remarque 2 : ne pas utiliser `-a` si on ne veut pas ajouter le son.*
*Remarque 3 : ne pas utiliser `--fps` pour être en 30 FPS (pour un rendu plus rapide).*

## Références

* http://doc.sagemath.org/html/en/reference/plot3d/sage/plot/plot3d/tachyon.html
* http://web.mit.edu/sage/export/tachyon-0.98~beta.dfsg/docs/tachyon.pdf
* https://fr.wikipedia.org/wiki/Matrice_de_rotation#Rotations_en_deux_et_trois_dimensions
* https://fr.wikipedia.org/wiki/Bruit_de_Perlin
* https://fr.wikipedia.org/wiki/Fractale
* https://fr.wikipedia.org/wiki/Flocon_de_Koch
