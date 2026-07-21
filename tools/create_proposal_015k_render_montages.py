#!/usr/bin/env python3
"""Create review montages from native KiCad Proposal 015K renders."""

from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
RENDER_ROOT = (
    ROOT
    / ".kicad_agent"
    / "reports"
    / "proposal_015k_breakout_closure"
    / "renders"
)
NAMES = ("CN7", "CN8", "CN11", "CN12")


def crop_white_margin(image: Image.Image, margin: int = 30) -> Image.Image:
    rgb = image.convert("RGB")
    # KiCad/PDF renderers may emit either a white or a light theme-colored
    # page.  Use the actual corner color as the page background so the review
    # montage crops to the board instead of preserving a nearly blank sheet.
    page_background = Image.new("RGB", rgb.size, rgb.getpixel((0, 0)))
    white_background = Image.new("RGB", rgb.size, "white")
    corner_difference = ImageChops.difference(rgb, page_background).convert("L")
    white_difference = ImageChops.difference(rgb, white_background).convert("L")
    # Treat both the outer renderer background and the inner white PDF page as
    # margin.  Only pixels that differ from both are review content.
    difference = ImageChops.darker(corner_difference, white_difference)
    mask = difference.point(lambda value: 255 if value > 5 else 0)
    box = mask.getbbox()
    if box is None:
        return rgb
    left = max(0, box[0] - margin)
    top = max(0, box[1] - margin)
    right = min(rgb.width, box[2] + margin)
    bottom = min(rgb.height, box[3] + margin)
    return rgb.crop((left, top, right, bottom))


def fit_inside(image: Image.Image, width: int, height: int) -> Image.Image:
    scale = min(width / image.width, height / image.height)
    target = (
        max(1, round(image.width * scale)),
        max(1, round(image.height * scale)),
    )
    return image.resize(target, Image.Resampling.LANCZOS)


def make_schematic_montage() -> None:
    source = RENDER_ROOT / "schematic_png"
    cell_width = 1500
    cell_height = 1060
    label_height = 52
    canvas = Image.new(
        "RGB",
        (cell_width * 2, (cell_height + label_height) * 2),
        "#eeeeea",
    )
    draw = ImageDraw.Draw(canvas)
    font = ImageFont.load_default(size=28)

    for index, name in enumerate(NAMES):
        image = Image.open(source / f"{name}_schematic.png").convert("RGB")
        cropped = crop_white_margin(image, margin=50)
        fitted = fit_inside(cropped, cell_width - 24, cell_height - 24)
        column = index % 2
        row = index // 2
        x0 = column * cell_width
        y0 = row * (cell_height + label_height)
        x = x0 + (cell_width - fitted.width) // 2
        y = y0 + label_height + (cell_height - fitted.height) // 2
        draw.rectangle(
            (x0, y0, x0 + cell_width - 1, y0 + label_height - 1),
            fill="#1f2937",
        )
        draw.text(
            (x0 + 18, y0 + 10),
            f"{name} - native KiCad schematic render",
            font=font,
            fill="white",
        )
        canvas.paste(fitted, (x, y))

    canvas.save(
        RENDER_ROOT / "proposal_015k_schematic_overview.png",
        optimize=True,
    )


def make_pcb_montage() -> None:
    source = RENDER_ROOT / "pcb_png"
    cell_width = 900
    cell_height = 1040
    label_height = 52
    canvas = Image.new(
        "RGB",
        (cell_width * 2, (cell_height + label_height) * 4),
        "#eeeeea",
    )
    draw = ImageDraw.Draw(canvas)
    font = ImageFont.load_default(size=26)

    for row, name in enumerate(NAMES):
        for column, side in enumerate(("front", "back")):
            image = Image.open(source / f"{name}_{side}_review.png")
            cropped = crop_white_margin(image)
            cropped.save(
                source / f"{name}_{side}_review_cropped.png",
                optimize=True,
            )
            fitted = fit_inside(
                cropped,
                cell_width - 36,
                cell_height - 36,
            )
            x0 = column * cell_width
            y0 = row * (cell_height + label_height)
            x = x0 + (cell_width - fitted.width) // 2
            y = y0 + label_height + (cell_height - fitted.height) // 2
            draw.rectangle(
                (x0, y0, x0 + cell_width - 1, y0 + label_height - 1),
                fill="#1f2937",
            )
            draw.text(
                (x0 + 18, y0 + 10),
                f"{name} - {side} review plot",
                font=font,
                fill="white",
            )
            canvas.paste(fitted, (x, y))

    canvas.save(
        RENDER_ROOT / "proposal_015k_pcb_front_back_overview.png",
        optimize=True,
    )


if __name__ == "__main__":
    make_schematic_montage()
    make_pcb_montage()
