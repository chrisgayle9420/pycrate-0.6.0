# -*- coding: UTF-8 -*-
#/**
# * Software Name : pycrate
# * Version : 0.4
# *
# * Copyright 2018. Benoit Michau. ANSSI. P1sec.
# *
# * This library is free software; you can redistribute it and/or
# * modify it under the terms of the GNU Lesser General Public
# * License as published by the Free Software Foundation; either
# * version 2.1 of the License, or (at your option) any later version.
# *
# * This library is distributed in the hope that it will be useful,
# * but WITHOUT ANY WARRANTY; without even the implied warranty of
# * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# * Lesser General Public License for more details.
# *
# * You should have received a copy of the GNU Lesser General Public
# * License along with this library; if not, write to the Free Software
# * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, 
# * MA 02110-1301  USA
# *
# *--------------------------------------------------------
# * File Name : pycrate_csn1dir/ec_packet_channel_description_type_1.py
# * Created : 2018-11-21
# * Authors : Benoit Michau
# *--------------------------------------------------------
#*/
# specification: TS 44.018 - d80
# section: 10.5.2.84 EC Packet Channel Description Type 1
# top-level object: EC Packet Channel Description Type 1



# code automatically generated by pycrate_csn1
# change object type with type=CSN1T_BSTR (default type is CSN1T_UINT) in init
# add dict for value interpretation with dic={...} in CSN1Bit init
# add dict for key interpretation with kdic={...} in CSN1Alt init

from pycrate_csn1.csnobj import *

ec_packet_channel_description_type_1 = CSN1List(name='ec_packet_channel_description_type_1', list=[
  CSN1Bit(name='quarter_hyperframe_indicator', bit=2),
  CSN1Bit(name='dl_coverage_class', bit=2),
  CSN1Bit(name='ul_coverage_class', bit=2),
  CSN1Bit(name='tsc_set'),
  CSN1Bit(name='tsc', bit=3),
  CSN1Bit(name='ec_ma_number', bit=5),
  CSN1Bit(name='spare_bit')])

