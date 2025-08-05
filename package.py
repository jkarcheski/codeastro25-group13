import numpy as np
import matplotlib.pyplot as plt
from astroquery.sdss import SDSS
from astropy import coordinates as coords
from astropy.table import Table, unique, hstack  # type: ignore
from astropy.io import fits, ascii  # type: ignore
import os
import mplcursors
