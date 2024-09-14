import pathlib
from PIL import Image, ImageOps
import numpy as np

ORIGINAL_PATH = r""
EDITED_PATH = r""
DST_PATH = r""

for orig in pathlib.Path(ORIGINAL_PATH).iterdir():
    if orig.is_file():
        orig_image = np.array(ImageOps.exif_transpose(Image.open(str(orig)))).astype(np.int16)
        edited_image = np.array(ImageOps.exif_transpose(Image.open(str(pathlib.Path(EDITED_PATH).joinpath(orig.name))))).astype(np.int16)
        mask = orig_image - edited_image
        np.save(str(pathlib.Path(DST_PATH).joinpath(orig.name).with_suffix(".npy")), mask)