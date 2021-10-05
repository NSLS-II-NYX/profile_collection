from nyxtools.robot import DensoOphydRobot
from nyxtools.governor import _make_governors

robot = DensoOphydRobot("XF:19IDC-ES{Rbt:1}", name="robot")
govs = _make_governors("XF:19IDC-ES", name="govs")
