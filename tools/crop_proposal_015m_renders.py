"""Crop native KiCad PDF rasterizations to review-scale connector images."""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
REPORTS = ROOT / ".kicad_agent" / "reports" / "proposal_015m"


def font(size: int, bold: bool = False) -> ImageFont.ImageFont:
    candidate = Path("C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf")
    if candidate.exists():
        return ImageFont.truetype(str(candidate), size)
    return ImageFont.load_default()


def crop_review(source: Path, destination: Path, *, allow_blank: bool = False) -> Image.Image:
    image = Image.open(source).convert("RGB")
    difference = ImageChops.difference(image, Image.new("RGB", image.size, "white"))
    box = difference.getbbox()
    if box is None:
        if not allow_blank:
            raise AssertionError(f"{source} contains no non-white review content")
        cropped = Image.new("RGB", (1200, 760), "white")
        draw = ImageDraw.Draw(cropped)
        draw.rectangle((4, 4, 1195, 755), outline="#777777", width=4)
        message = (
            "INTENTIONALLY BLANK NATIVE BOTTOM VIEW\n\n"
            "Top-side SMD footprint has no bottom-layer copper, mask, paste,\n"
            "silkscreen, fabrication, or courtyard features."
        )
        draw.multiline_text(
            (600, 380),
            message,
            fill="#333333",
            font=font(28, bold=True),
            anchor="mm",
            align="center",
            spacing=12,
        )
        cropped.save(destination)
        print(f"WROTE {destination} ({cropped.width} x {cropped.height}; blank disclosed)")
        return cropped
    padding = 24
    left = max(0, box[0] - padding)
    top = max(0, box[1] - padding)
    right = min(image.width, box[2] + padding)
    bottom = min(image.height, box[3] + padding)
    cropped = image.crop((left, top, right, bottom))
    scale = max(1, min(5, 1400 // max(cropped.width, cropped.height)))
    if scale > 1:
        cropped = cropped.resize(
            (cropped.width * scale, cropped.height * scale),
            Image.Resampling.LANCZOS,
        )
    cropped.save(destination)
    print(f"WROTE {destination} ({cropped.width} x {cropped.height})")
    return cropped


def fit(image: Image.Image, max_size: tuple[int, int]) -> Image.Image:
    fitted = image.copy()
    fitted.thumbnail(max_size, Image.Resampling.LANCZOS)
    return fitted


def composite(front: Image.Image, back: Image.Image) -> None:
    canvas = Image.new("RGB", (1800, 1500), "white")
    draw = ImageDraw.Draw(canvas)
    draw.text(
        (900, 45),
        "JST ZE BM06B-ZESS-TBT — native KiCad 2D review",
        fill="#111111",
        font=font(38, bold=True),
        anchor="ma",
    )
    panels = (("FRONT / TOP / COMPONENT SIDE", front), ("BACK / BOTTOM SIDE", back))
    y_positions = (110, 800)
    for (title, image), y in zip(panels, y_positions):
        draw.text((900, y), title, fill="#222222", font=font(30, bold=True), anchor="ma")
        panel = fit(image, (1660, 600))
        x = (canvas.width - panel.width) // 2
        canvas.paste(panel, (x, y + 45))
    note = (
        "Raw native exports are preserved beside this review image. "
        "The blank bottom view is an expected absence result, not missing render data."
    )
    draw.text((900, 1460), note, fill="#333333", font=font(21), anchor="mm")
    destination = REPORTS / "proposal_015m_jst_ze_front_back_review.png"
    canvas.save(destination)
    print(f"WROTE {destination} ({canvas.width} x {canvas.height})")


def main() -> None:
    front = crop_review(
        REPORTS / "proposal_015m_jst_ze_front_2d.png",
        REPORTS / "proposal_015m_jst_ze_front_2d_review.png",
    )
    back = crop_review(
        REPORTS / "proposal_015m_jst_ze_back_2d.png",
        REPORTS / "proposal_015m_jst_ze_back_2d_review.png",
        allow_blank=True,
    )
    composite(front, back)


if __name__ == "__main__":
    main()
