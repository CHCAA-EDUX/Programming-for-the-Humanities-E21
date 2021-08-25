# Programming for the Humanities E21 #

This repository contains all of the code and data related to the Fall 2021 (E21) course _Programming for the Humanities_ which is an [internationalisation elective](https://kursuskatalog.au.dk/da/course/106983/Programming-for-the-Humanities) at [Aarhus University](https://international.au.dk/), [Faculty of Arts](https://arts.au.dk/en/). The course is taught by [Center for Humanities Computing Aarhus](https://chcaa.io/#/), any inquiries can be addressed to [CHCAA](mailto:chcaa@cas.au.dk?subject=[PftHe21]%20Student%20Inquiry)

This repository is in active development, with new material being pushed on a weekly basis. 
## Technicalities

For the sake of convenience, I recommend using our own [JupyterHub server](https://worker02.chcaa.au.dk/jupyter/hub/login) for development purposes. The first time you use the server, you'll need to create your own version of the repo and install relevant dependencies in a virtual environment:

```bash
git clone https://github.com/CDS-AU-DK/cds-visual.git
cd cds-visual
bash create_vision_venv.sh
```

From then on, every time you use the server, make sure you update the repo and install any new dependencies:

```bash
cd lang101
git pull origin main
bash create_vision_venv.sh
```

## Repo structure

This repository has the following directory structure:

| Column | Description|
|--------|:-----------|
```data```| A folder to be used for sample datasets that we use in class.
```notebooks``` | This is where you should save all exploratory and experimental notebooks.
```src``` | Python scripts to be used in class.
```utils``` | Utility functions that are written by me, and which we'll use in class.


## Class times

This class takes place on Monday Mornings 0800-1200.

## Course overview and readings

## Contact details

