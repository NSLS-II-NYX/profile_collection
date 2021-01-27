from pathlib import Path

import appdirs
import nslsii
from bluesky.utils import PersistentDict
from IPython import get_ipython

# Base configuration
#  pbar=False disables progress bar (undesirable in Jupyter)
#  bec=False disables Best Effort Callback (seems to be causing issues)
nslsii.configure_base(get_ipython().user_ns, "nyx", pbar=False, bec=False)

runengine_metadata_dir = appdirs.user_data_dir(appname="bluesky") / Path(
    "runengine-metadata"
)

# PersistentDict will create the directory if it does not exist
RE.md = PersistentDict(runengine_metadata_dir)

RE.md["beamline_name"] = "NYX"
RE.md["facility"] = "NSLS-II"
