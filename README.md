# MRAD (Maritime Reflection Analysis Dataset)

This is the repository for the datasets used in the BMVC RROW 2024 workshop paper **Impact of Surface Reflections in Maritime Obstacle Detection**.

The code in this repository is released under MIT license.

We do not own and therefore share the images in the dataset. Instead, we share URLs to the original sources.
We also share masks that you can use to reconstruct the inpainted versions of the images, along with the reconstruction code.

You can find the masks in: https://drive.google.com/file/d/1UTR_P3sQ8xCOO_uytw5bcmgYaGXsjUKA

# How to reconstruct
* Extract the masks in to a folder.
* Create another folder with the same structure and download the originals to that folder. This will be the source folder.
* Create third folder with the same structure. This will be the destination folder.
* Enter the paths in `reconstruct.py` and run.

# How to open the URLs quickly
* Download the `urls.txt` file.
* Enter the path to the file in `open_urls.py`.
* Run. It will open the original sources in the default browser.
  
# How to cite
You can use the below BibTeX entry to cite our research if you find it useful.

```
@misc{yalçın2024impactsurfacereflectionsmaritime,
    title={Impact of Surface Reflections in Maritime Obstacle Detection}, 
    author={Samed Yalçın and Hazım Kemal Ekenel},
    year={2024},
    eprint={2410.08713},
    archivePrefix={arXiv},
    primaryClass={cs.CV},
    url={https://arxiv.org/abs/2410.08713}, 
}
```
