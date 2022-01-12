from nyxtools.robot import DensoOphydRobot
from nyxtools.governor import _make_governors
from mxtools.zebra import Zebra
from nyxtools.vector import VectorProgram
from nyxtools.pilatus import PilatusBase
from nyxtools.flyer import NYXFlyer

robot = DensoOphydRobot("XF:19IDC-ES{Rbt:1}", name="robot")
govs = _make_governors("XF:19IDC-ES", name="govs")
zebra = Zebra("XF:19IDC-ES{Zeb:1}:", name="zebra")
detector = PilatusBase("XF:19IDC-ES{Det:Pil6M}", name="detector")
vector = VectorProgram("XF:19IDC-ES{Gon:1-Vec}", name="vector")
flyer = NYXFlyer(vector=vector, zebra=zebra, detector=detector)


# NOTE: This is a sample `scan_params` dictionary, change as you need.
# scan_params = {
#    'angle_start': 0,
#    'exposure_period_per_image': 0.5,
#    'detector_dead_time': 0.01,
#    'scan_width': 1.0,
#    'img_width': 0.2,
#    'num_images': 5,
#    'x_start_um': 0,
#    'y_start_um': 0,
#    'z_start_um': 0,
#    'file_prefix': 'testjun',
#    # 'data_directory_name': '/nyx-data/test/bluesky-2021-12-01',
#    'data_directory_name': '/nyx-data/test/juntest',
#    'file_number_start': 1,
#    'x_beam': 1000,
#    'y_beam': 1200,
#    'wavelength': 0.9876,
#    'det_distance_m': 0.25,
#    }

# In [2]: hdr.start
# Out[2]:
# {'uid': '5d7b5855-382c-4043-aa67-a7e026392543',
#  'time': 1638912272.5825405,
#  'beamline_attenuators': {},
#  'optinal_comments': '',
#  'scan_id': 21,
#  'facility': 'NSLS-II',
#  'beamline_beamsize': 'low_divergence',
#  'beamline_name': 'NYX',
#  'beamline_sample_environement': 'in-vacuum',
#  'beamline_id': 'SST-1 RSoXS',
#  'plan_type': 'generator',
#  'plan_name': 'fly'}
