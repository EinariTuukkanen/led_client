
# Setup

## Socket Server (Led Controller)
Raspberry Pi (tested with version 3B) which acts as dummy socket server with only minimal features.
Needs separate configuration for
- Led pin (default 18)
- Led count (default 100, incorrect value number will not work!)
- Led color mode i.e. R, G, B, (W) order

Takes in protobuf packet with two arguments:
- `offset`, no need to update all leds at once; offset tells from which index to start and update until colors run out
- `colors`, list of colors as list, e.g.

```
# RGB
[[255, 0, 0], [0, 255, 0], [0, 0, 255]]

# RGBW
[[255, 0, 0, 255], [0, 255, 0, 255], [0, 0, 255, 255]]
```

