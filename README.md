# docs

This repository is for the BSVX team's ongoing specification document.

### Figure Generation
Prerequisites:
- The [bsvxpy library](https://github.com/bsvx/bsvxpy) is cloned to your local machine in the parent directory of this repo
  - `pip install ..\bsvxpy\` on Windows
  - `pip install ../bsvxpy/` on Linux/OS X
- Python 3
- Python numpy package
  - `pip install --user numpy`
- Python matplotlib package
  - `pip install --user matplotlib`

All you have to do to generate all of BSVX's figures is run the script called "generate_figures.py".
This script is located in the "scripts" directory of this repository.
This can be accomplished through `python generate_figures.py`.
