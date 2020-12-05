from ophyd import Device, Component as Cpt, EpicsMotor


class XYMotor(Device):
    x = Cpt(EpicsMotor, '-Ax:X}Mtr')
    y = Cpt(EpicsMotor, '-Ax:Y}Mtr')


class Slits(Device):
    b     = Cpt(EpicsMotor, '-Ax:B}Mtr')
    i     = Cpt(EpicsMotor, '-Ax:I}Mtr')
    o     = Cpt(EpicsMotor, '-Ax:O}Mtr')
    t     = Cpt(EpicsMotor, '-Ax:T}Mtr')
    x_ctr = Cpt(EpicsMotor, '-Ax:XCtr}Mtr')
    x_gap = Cpt(EpicsMotor, '-Ax:XGap}Mtr')
    y_ctr = Cpt(EpicsMotor, '-Ax:YCtr}Mtr')
    y_gap = Cpt(EpicsMotor, '-Ax:YGap}Mtr')


class DCM(Device):
    # Virtual Motor
    energy  = Cpt(EpicsMotor, '-Ax:E}Mtr')

    # Real Motors
    bragg   = Cpt(EpicsMotor, '-Ax:B}Mtr')
    perp    = Cpt(EpicsMotor, '-Ax:Perp}Mtr')
    para    = Cpt(EpicsMotor, '-Ax:Para}Mtr')
    pitch   = Cpt(EpicsMotor, '-Ax:P}Mtr')
    roll    = Cpt(EpicsMotor, '-Ax:R}Mtr')
    yaw     = Cpt(EpicsMotor, '-Ax:Yaw}Mtr')
    c2_bnd1 = Cpt(EpicsMotor, '-Ax:Bnd1}Mtr')
    c2_bnd2 = Cpt(EpicsMotor, '-Ax:Bnd2}Mtr')
    c1_bnd  = Cpt(EpicsMotor, '-Ax:Bnd}Mtr')


class Mirror(Device):
    y    = Cpt(EpicsMotor, '-Ax:Y}Mtr')
    x    = Cpt(EpicsMotor, '-Ax:X}Mtr')
    p    = Cpt(EpicsMotor, '-Ax:P}Mtr')
    r    = Cpt(EpicsMotor, '-Ax:R}Mtr')
    bnd1 = Cpt(EpicsMotor, '-Ax:Bnd1}Mtr')
    bnd2 = Cpt(EpicsMotor, '-Ax:Bnd2}Mtr')


#######################################################
# NYX
#######################################################

# Beam Mask
beam_mask = XYMotor('XF:19IDC-OP{BM:1', name='beam_mask')

# BPMs
bpm1 = XYMotor('XF:19IDC-OP{BPM:1', name='bpm1')
bpm2 = XYMotor('XF:19IDC-OP{BPM:2', name='bpm2')
bpm3 = XYMotor('XF:19IDC-OP{BPM:3', name='bpm3')

# Slits
wb_slits = Slits('XF:19IDC-OP{Slt:WB', name='wb_slits')
mb_slits = Slits('XF:19IDC-OP{Slt:MB', name='mb_slits')

# Mono
dcm = DCM('XF:19IDC-OP{Mono:DCM', name='dcm')

# Mirror
mirror = Mirror('XF:19IDC-OP{Mir:1', name='mirror')
