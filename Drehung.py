#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

# GPIO-Bezeichnung BCM stezen
GPIO.setmode(GPIO.BCM)

# GPIO-Pins Encoder (gemeinsamer Encoder-Pin auf GND)
in_a = 17
in_b = 27

# Merker fuer Encoder-Zustand (global)
old_a = 1
old_b = 1

# Pullup-Widerstand einschalten
GPIO.setup(in_a, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(in_b, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def get_encoder():
  # liest den Encoder aus. Falls die Werte der Eingangspins
  # alten Wert abweichen, Richtung detektieren.
  # Rueckgabewert: -1, 0, +1
  global old_a, old_b
  result = 0

  # GPIO-Pins einlesen
  new_a = GPIO.input(in_a)
  new_b = GPIO.input(in_b)

  # Falls sich etwas geaendert hat, Richtung feststellen
  if (new_a != old_a or new_b != old_b):
    if (old_a == 0 and new_a == 1):
      result = (old_b * 2 - 1)
    elif (old_b == 0 and new_b == 1):
      result = -(old_a * 2 - 1)
  old_a = new_a
  old_b = new_b
  # entprellen
  time.sleep(0.02)
  return result


# Testprogramm
x = 0
while True:
  change = get_encoder()
  if change != 0:
    x = x + change
    print(x)
