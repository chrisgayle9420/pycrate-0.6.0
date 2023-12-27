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
# * File Name : pycrate_csn1dir/psi16_message_content.py
# * Created : 2018-11-21
# * Authors : Benoit Michau
# *--------------------------------------------------------
#*/
# specification: TS 44.060 - d60
# section: 11.2.25c Packet System Information Type 16
# top-level object: PSI16 message content

# external references
from pycrate_csn1dir.padding_bits import padding_bits

# code automatically generated by pycrate_csn1
# change object type with type=CSN1T_BSTR (default type is CSN1T_UINT) in init
# add dict for value interpretation with dic={...} in CSN1Bit init
# add dict for key interpretation with kdic={...} in CSN1Alt init

from pycrate_csn1.csnobj import *

cn_domain_identity_ie = CSN1Bit(name='cn_domain_identity_ie', bit=2)

gra_id_struct = CSN1List(name='gra_id_struct', list=[
  CSN1Bit(name='number_of_gra_ids', bit=3),
  CSN1Bit(name='gra_id', bit=16, num=([0], lambda x: x + 1))])

cn_domain_specific_drx_cycle_length_coefficient_ie = CSN1Bit(name='cn_domain_specific_drx_cycle_length_coefficient_ie', bit=4)

psi16_message_content = CSN1List(name='psi16_message_content', list=[
  CSN1Bit(name='page_mode', bit=2),
  CSN1Bit(name='psi16_change_mark', bit=2),
  CSN1Bit(name='psi16_index', bit=3),
  CSN1Bit(name='psi16_count', bit=3),
  CSN1Ref(name='gra_id_list', obj=gra_id_struct),
  CSN1Bit(name='iu_mode_nmo_support'),
  CSN1Bit(name='cn_domain_list', bit=2),
  CSN1List(num=([6], lambda x: x + 1), list=[
    CSN1Ref(name='cn_domain_identity', obj=cn_domain_identity_ie),
    CSN1Ref(name='cn_domain_specific_drx_cycle_length_coefficient', obj=cn_domain_specific_drx_cycle_length_coefficient_ie)]),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='_3g_lac', bit=16)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='_3g_rac', bit=8)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='gra_and_cell_update_timer', bit=3)])}),
  CSN1Ref(obj=padding_bits)])
