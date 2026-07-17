#!/usr/bin/env python3
"""Export README preview GIFs directly from the installed Linwan v2 atlas."""

from pathlib import Path
from PIL import Image

ATLAS = Path("assets/linwan/spritesheet.webp")
OUTPUT = Path("previews/linwan")
STATES = [
    "idle", "running-right", "running-left", "waving", "jumping",
    "failed", "waiting", "running", "review",
]
DURATIONS = {
    "idle": [160] * 8,
    "running-right": [120, 120, 120, 120, 120, 120, 120, 220],
    "running-left": [120, 120, 120, 120, 120, 120, 120, 220],
    "waving": [120] * 8,
    "jumping": [120] * 8,
    "failed": [120] * 8,
    "waiting": [160] * 8,
    "running": [140] * 8,
    "review": [120] * 8,
}
CELL_W, CELL_H = 192, 208


def main() -> None:
    atlas = Image.open(ATLAS).convert("RGBA")
    if atlas.size != (CELL_W * 8, CELL_H * 11):
        raise SystemExit(f"unexpected atlas size: {atlas.size}")
    OUTPUT.mkdir(parents=True, exist_ok=True)
    for row, state in enumerate(STATES):
        frames = [
            atlas.crop((col * CELL_W, row * CELL_H, (col + 1) * CELL_W, (row + 1) * CELL_H))
            for col in range(8)
        ]
        frames[0].save(
            OUTPUT / f"{state}.gif",
            save_all=True,
            append_images=frames[1:],
            duration=DURATIONS[state],
            loop=0,
            disposal=2,
            transparency=0,
            optimize=False,
        )


if __name__ == "__main__":
    main()
