#!/usr/bin/env python3
"""
Cheeky Donut Gremlin Simulator
Run this for a dose of sugar-fueled chaos and questionable wisdom.
"""

import random
import time

PUNS = [
    "I'm on a roll!",
    "You donut know how happy I am.",
    "Glazed and confused? Natural state.",
    "Sprinkle a little chaos on your day!",
    "I'm just here for the hole-y experience.",
    "Donut worry, be happy.",
    "Powered by sugar and bad decisions."
]

ACTIONS = [
    "rearranged your donut box into a smiley face",
    "taste-tested every donut (all approved)",
    "left a sassy sticky note on the fridge",
    "stole one donut but left two squished ones instead",
    "reorganized the sprinkles then ate the evidence",
    "whispered 'just one more' until you caved",
    "turned your coffee into an accidental espresso",
    "hid the last cronut and is giggling somewhere"
]

GREETINGS = [
    "Heehee... did someone say donuts?",
    "Oh hi! I definitely didn't eat anything.",
    "Psst... the box looks a little empty. Coincidence?",
    "I come in peace... and powdered sugar."
]

def summon_gremlin():
    print("\n🍩 === CHEEKY DONUT GREMLIN ACTIVATED === 🍩")
    time.sleep(0.5)
    print(random.choice(GREETINGS))
    time.sleep(0.8)
    print(f"\nToday the gremlin has: {random.choice(ACTIONS)}.")
    time.sleep(0.6)
    print(f"\nIts wisdom: \"{random.choice(PUNS)}\"")
    time.sleep(0.5)
    print("\n🔥 One more donut never hurt... probably.")
    print("(Run again for fresh chaos!)\n")

if __name__ == "__main__":
    summon_gremlin()