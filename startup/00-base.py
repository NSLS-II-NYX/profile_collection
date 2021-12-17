try:
    ###############################################################################
    # TODO: remove this block once https://github.com/bluesky/ophyd/pull/959 is
    # merged/released.
    from datetime import datetime
    from ophyd.signal import EpicsSignalBase, EpicsSignal, DEFAULT_CONNECTION_TIMEOUT

    def print_now():
        return datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S.%f')

    def wait_for_connection_base(self, timeout=DEFAULT_CONNECTION_TIMEOUT):
        '''Wait for the underlying signals to initialize or connect'''
        if timeout is DEFAULT_CONNECTION_TIMEOUT:
            timeout = self.connection_timeout
        # print(f'{print_now()}: waiting for {self.name} to connect within {timeout:.4f} s...')
        start = time.time()
        try:
            self._ensure_connected(self._read_pv, timeout=timeout)
            # print(f'{print_now()}: waited for {self.name} to connect for {time.time() - start:.4f} s.')
        except TimeoutError:
            if self._destroyed:
                raise DestroyedError('Signal has been destroyed')
            raise

    def wait_for_connection(self, timeout=DEFAULT_CONNECTION_TIMEOUT):
        '''Wait for the underlying signals to initialize or connect'''
        if timeout is DEFAULT_CONNECTION_TIMEOUT:
            timeout = self.connection_timeout
        # print(f'{print_now()}: waiting for {self.name} to connect within {timeout:.4f} s...')
        start = time.time()
        self._ensure_connected(self._read_pv, self._write_pv, timeout=timeout)
        # print(f'{print_now()}: waited for {self.name} to connect for {time.time() - start:.4f} s.')

    EpicsSignalBase.wait_for_connection = wait_for_connection_base
    EpicsSignal.wait_for_connection = wait_for_connection
    ###############################################################################

    from ophyd.signal import EpicsSignalBase
    # EpicsSignalBase.set_default_timeout(timeout=10, connection_timeout=10)  # old style
    EpicsSignalBase.set_defaults(timeout=10, connection_timeout=10)  # new style
except ImportError:
    print('EpicsSignalBase does not exist in ophyd')

from pathlib import Path

import appdirs
import nslsii
from IPython import get_ipython

# Base configuration
#  pbar=False disables progress bar (undesirable in Jupyter)
#  bec=False disables Best Effort Callback (seems to be causing issues)
nslsii.configure_base(get_ipython().user_ns, "nyx", pbar=False, bec=True)

try:
    from bluesky.utils import PersistentDict
    runengine_metadata_dir = appdirs.user_data_dir(appname="bluesky") / Path(
        "runengine-metadata"
    )
    # PersistentDict will create the directory if it does not exist
    RE.md = PersistentDict(runengine_metadata_dir)
except ImportError:
    print('Older bluesky did not have PersistentDict, moving on.')

RE.md["beamline_name"] = "NYX"
RE.md["facility"] = "NSLS-II"

# TODO: comment out when in production.
from bluesky.utils import ts_msg_hook
RE.msg_hook = ts_msg_hook
print(f"\n\t{__file__}: Using 'ts_msg_hook'...\n")


# Temp workaround to register the handler (does not work via entrypoints in
# setup.py for some reason...)

from nyxtools.handlers import PilatusHandlerMX
db.reg.register_handler("AD_PILATUS_MX", PilatusHandlerMX)
