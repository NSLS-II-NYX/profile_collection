from nyxtools.robot import DensoOphydRobot
from nyxtools.governor import _make_governors
from mxtools.zebra import Zebra
from nyxtools.vector import VectorProgram
from nyxtools.flyer import NYXFlyer

robot = DensoOphydRobot("XF:19IDC-ES{Rbt:1}", name="robot")
govs = _make_governors("XF:19IDC-ES", name="govs")
zebra = Zebra("XF:19IDC-ES{Zeb:1}:", name="zebra")
vector = VectorProgram("XF:19IDC-ES{Gon:1-Vec}", name="vector")
flyer = NYXFlyer(vector=vector, zebra=zebra)
