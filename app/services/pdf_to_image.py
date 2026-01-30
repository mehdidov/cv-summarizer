from pathlib import Path
from pdf2image import convert_from_path

IMAGES_DIR = Path("uploads/images")
IMAGES_DIR.mkdir(parents=True, exist_ok=True)

def pdf_to_images(pdf_path: Path, cv_id: str) -> list[Path]:
    output_dir = IMAGES_DIR / cv_id
    output_dir.mkdir(parents=True, exist_ok=True)

    images = convert_from_path(pdf_path)

    image_paths = []
    for i, image in enumerate(images):
        img_path = output_dir / f"page_{i+1}.png"
        image.save(img_path, "PNG")
        image_paths.append(img_path)

    return image_paths
