#!/bin/bash

# Any beamline-specific operations that may be needed before running IPython startup files.
#!/bin/bash

export AZURE_TESTING=1

pip install -vv git+https://github.com/mskinner5278/nyxtools@pilatus_detector
pip install -vv git+https://github.com/NSLS-II-AMX/mxtools@main
