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
# * File Name : pycrate_csn1dir/si_18_rest_octets.py
# * Created : 2018-11-21
# * Authors : Benoit Michau
# *--------------------------------------------------------
#*/
# specification: TS 44.018 - d80
# section: 10.5.2.37h SI 18 Rest Octets
# top-level object: SI 18 Rest Octets



# code automatically generated by pycrate_csn1
# change object type with type=CSN1T_BSTR (default type is CSN1T_UINT) in init
# add dict for value interpretation with dic={...} in CSN1Bit init
# add dict for key interpretation with kdic={...} in CSN1Alt init

from pycrate_csn1.csnobj import *

spare_bit = CSN1Bit(name='spare_bit')
Spare_bit = spare_bit
Spare_Bit = spare_bit

spare_padding = CSN1Val(name='spare_padding', val='L', num=-1)
Spare_padding = spare_padding
Spare_Padding = spare_padding 

non_gsm_message_struct = CSN1List(name='non_gsm_message_struct', list=[
  CSN1Bit(name='non_gsm_protocol_discriminator', bit=3),
  CSN1Bit(name='nr_of_container_octets', bit=5),
  CSN1Bit(name='container', bit=8, num=([1], lambda x: x))])

si_18_rest_octets = CSN1List(name='si_18_rest_octets', list=[
  CSN1Bit(name='si18_change_mark', bit=2),
  CSN1Bit(name='si18_index', bit=3),
  CSN1Bit(name='si18_last'),
  CSN1Ref(obj=spare_bit, num=2),
  CSN1Ref(name='non_gsm_message', obj=non_gsm_message_struct, num=-1),
  CSN1Ref(obj=spare_padding)])

