# super-duper-journey

Project / M3202C - Modélisations mathématiques @ IUT Aix-en-Provence

## Auteurs

* ACHACHE Sirine
* LEGRAND Benjamin
* MARTINEZ Nicolas
* TARFI Emma

## Dépendances

| **Paquet** |
|------------|
| sagemath   |
| ffmpeg     |

## Usage

```
λ  super-duper-journey master ✗ ./main.sage --help
usage: main.sage.py [-h] [--output OUTPUT] [--width WIDTH] [--height HEIGHT]
                    [--fps FPS] [--bpm BPM]

Generate an animation with SageMath based on beat timing. For better result,
BPM should be divisible by FPS.

optional arguments:
  -h, --help       show this help message and exit
  --output OUTPUT  Output filename (default: output/output.mp4)
  --width WIDTH    Frame width (default: 1280)
  --height HEIGHT  Frame height (default: 720)
  --fps FPS        Frame rate (default: 30)
  --bpm BPM        Beat-per-minute (default: 150)
```
