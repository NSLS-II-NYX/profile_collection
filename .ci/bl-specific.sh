#!/bin/bash

# Any beamline-specific operations that may be needed before running IPython startup files.
#!/bin/bash

export AZURE_TESTING=1

conda install mxtools -c conda-forge
conda install nyxtools -c conda-forge
