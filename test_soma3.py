#!/usr/bin/env python3

import soma3

dining = soma3.SomaBlind("E4:A1:D6:1D:B6:6D")
print(dining.get_position())
print(dining.get_battery())
print(dining.set_position(5))
