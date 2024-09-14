import pathlib
from PIL import Image, ImageOps
import numpy as np

ORIGINAL_PATH = r""
MASK_PATH = r""
DST_PATH = r""

for orig in pathlib.Path(ORIGINAL_PATH).iterdir():
    if orig.is_file():
        orig_image = np.array(ImageOps.exif_transpose(Image.open(str(orig)))).astype(np.int16)
        mask = np.load(str(pathlib.Path(MASK_PATH).joinpath(orig.name).with_suffix(".npy")))
        reconstructed_image = (orig_image - mask).astype(np.uint8)
        Image.fromarray(reconstructed_image).save(pathlib.Path(DST_PATH).joinpath(orig.name), quality=100)