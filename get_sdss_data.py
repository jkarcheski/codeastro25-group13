from astroquery.sdss import SDSS
from astropy import coordinates as coords
from astropy.table import Table
import numpy as np
import os

query = """
        SELECT TOP 10
            p.objid, p.ra, p.dec,
            s.specobjid, s.z, s.class, s.subclass,
            s.plate, s.mjd, s.fiberid
        FROM
            PhotoObjAll p JOIN SpecObjAll s ON p.objid = s.bestobjid
        WHERE
            s.class = 'GALAXY' AND s.subclass LIKE '%AGN%'
        """
results = SDSS.query_sql(query)
print(results)

if results is not None:
    spectra_dir = "spectra"
    os.makedirs(spectra_dir, exist_ok=True)

    for filename in os.listdir(spectra_dir):
        file_path = os.path.join(spectra_dir, filename)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)  # Delete the file if it exists already
        except Exception as e:
            print(f"Could not delete {file_path}: {e}")

    for i in range(len(results)):
        try:
            plate = int(results['plate'][i])
            mjd = int(results['mjd'][i])
            fiberid = int(results['fiberid'][i])
            spec = SDSS.get_spectra(plate=plate, mjd=mjd, fiberID=fiberid)

            if spec:
                # filename = f"spectra/spec_{plate}_{mjd}_{fiberid}.fits"
                filename = os.path.join(spectra_dir, f"spec_{plate}_{mjd}_{fiberid}.fits")
                spec[0].writeto(filename, overwrite=True)
                print(f"Saved: {filename}")
            else:
                print(f"No spectrum for plate={plate}, mjd={mjd}, fiber={fiberid}")
        except Exception as e:
            print(f"Error for plate={plate}, mjd={mjd}, fiber={fiberid}: {e}")
else:
    print("No results found.")
