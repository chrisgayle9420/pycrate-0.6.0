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
# * File Name : pycrate_csn1dir/dtm_handover_ps_radio_resources_3_ie.py
# * Created : 2018-11-21
# * Authors : Benoit Michau
# *--------------------------------------------------------
#*/
# specification: TS 44.060 - d60
# section: 12.64 DTM Handover PS Radio Resources 3
# top-level object: DTM Handover PS Radio Resources 3 IE

# external references
from pycrate_csn1dir.egprs_mode_2_ie import egprs_mode_2_ie
from pycrate_csn1dir.egprs_window_size_ie import egprs_window_size_ie
from pycrate_csn1dir.cell_identification_ie import cell_identification_ie
from pycrate_csn1dir.gprs_power_control_parameters_ie import gprs_power_control_parameters_ie
from pycrate_csn1dir.gprs_cell_options_ie import gprs_cell_options_ie

# code automatically generated by pycrate_csn1
# change object type with type=CSN1T_BSTR (default type is CSN1T_UINT) in init
# add dict for value interpretation with dic={...} in CSN1Bit init
# add dict for key interpretation with kdic={...} in CSN1Alt init

from pycrate_csn1.csnobj import *

spare_bit = CSN1Bit(name='spare_bit')
Spare_bit = spare_bit
Spare_Bit = spare_bit

additional_pfcs_struct = CSN1List(name='additional_pfcs_struct', list=[
  CSN1Bit(name='tfi', bit=5),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='npm_transfer_time', bit=5)])}),
  CSN1Bit(name='pfi', bit=7)])

rlc_entity_struct = CSN1List(name='rlc_entity_struct', list=[
  CSN1Bit(name='tfi', bit=5),
  CSN1Bit(name='rlc_mode'),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Ref(name='egprs_window_size', obj=egprs_window_size_ie)])}),
  CSN1Bit(name='pfi', bit=7)])

extension_information = CSN1List(name='extension_information', trunc=True, list=[
  CSN1List(list=[
    CSN1Alt(alt={
      '0': ('', [
      CSN1Bit(name='emst_nw_capability')]),
      '1': ('', [
      CSN1Alt(alt={
        '0': ('', []),
        '1': ('', [
        CSN1Ref(name='downlink_rlc_entity_2', obj=rlc_entity_struct),
        CSN1Alt(alt={
          '0': ('', []),
          '1': ('', [
          CSN1Ref(name='downlink_rlc_entity_3', obj=rlc_entity_struct)])})])}),
      CSN1Alt(alt={
        '0': ('', []),
        '1': ('', [
        CSN1Ref(name='uplink_rlc_entity_2', obj=rlc_entity_struct),
        CSN1Alt(alt={
          '0': ('', []),
          '1': ('', [
          CSN1Ref(name='uplink_rlc_entity_3', obj=rlc_entity_struct)])})])})])}),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='mtti_downlink_assignment_c1')])}),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='mtti_downlink_assignment_c2')])}),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='mtti_uplink_assignment_c1')])}),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='mtti_uplink_assignment_c2')])}),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1List(num=-1, list=[
        CSN1Val(name='', val='1'),
        CSN1Ref(name='emsr_additional_pfcs_1', obj=additional_pfcs_struct)]),
      CSN1Val(name='', val='0'),
      CSN1List(num=-1, list=[
        CSN1Val(name='', val='1'),
        CSN1Ref(name='emsr_additional_pfcs_2', obj=additional_pfcs_struct)]),
      CSN1Val(name='', val='0'),
      CSN1List(num=-1, list=[
        CSN1Val(name='', val='1'),
        CSN1Ref(name='emsr_additional_pfcs_3', obj=additional_pfcs_struct)]),
      CSN1Val(name='', val='0')])}),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1List(num=-1, list=[
        CSN1Val(name='', val='1'),
        CSN1Ref(name='emsr_additional_pfcs_1', obj=additional_pfcs_struct)]),
      CSN1Val(name='', val='0'),
      CSN1List(num=-1, list=[
        CSN1Val(name='', val='1'),
        CSN1Ref(name='emsr_additional_pfcs_2', obj=additional_pfcs_struct)]),
      CSN1Val(name='', val='0'),
      CSN1List(num=-1, list=[
        CSN1Val(name='', val='1'),
        CSN1Ref(name='emsr_additional_pfcs_3', obj=additional_pfcs_struct)]),
      CSN1Val(name='', val='0')])})]),
  CSN1Bit(name='egprs_packet_downlink_ack_nack_type_3_support'),
  CSN1List(list=[
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='primary_tsc_set'),
      CSN1Bit(name='primary_tsc_value', bit=3)])}),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='secondary_dl_tsc_set'),
      CSN1Bit(name='secondary_dl_tsc_value', bit=3)])})]),
  CSN1Ref(obj=spare_bit, num=-1)])

dtm_handover_ps_radio_resources_3_ie = CSN1List(name='dtm_handover_ps_radio_resources_3_ie', list=[
  CSN1Ref(name='cell_identification', obj=cell_identification_ie),
  CSN1Bit(name='max_lapdm', bit=3),
  CSN1Bit(name='gprs_ms_txpwr_max_cch', bit=5),
  CSN1Ref(name='gprs_cell_options', obj=gprs_cell_options_ie),
  CSN1Ref(name='gprs_power_control_parameters', obj=gprs_power_control_parameters_ie),
  CSN1Bit(name='rlc_reset'),
  CSN1List(list=[
    CSN1Val(name='', val='00'),
    CSN1Ref(name='egprs_mode', obj=egprs_mode_2_ie)]),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='extension_length', bit=8),
    CSN1Ref(obj=extension_information, lref=([1], lambda x: x + 1))])})])

