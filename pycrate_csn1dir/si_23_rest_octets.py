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
# * File Name : pycrate_csn1dir/si_23_rest_octets.py
# * Created : 2018-11-21
# * Authors : Benoit Michau
# *--------------------------------------------------------
#*/
# specification: TS 44.018 - d80
# section: 10.5.2.37o SI 23 Rest Octets
# top-level object: SI 23 Rest Octets

# external references
from pycrate_csn1dir.measurement_information import repeated_e_utran_not_allowed_cells_struct
from pycrate_csn1dir.enhanced_cell_reselection_parameters_ie import enhanced_cell_reselection_parameters_ie
from pycrate_csn1dir.si2quater_rest_octets import repeated_e_utran_pcid_to_ta_mapping_struct

# code automatically generated by pycrate_csn1
# change object type with type=CSN1T_BSTR (default type is CSN1T_UINT) in init
# add dict for value interpretation with dic={...} in CSN1Bit init
# add dict for key interpretation with kdic={...} in CSN1Alt init

from pycrate_csn1.csnobj import *

spare_padding = CSN1Val(name='spare_padding', val='L', num=-1)
Spare_padding = spare_padding
Spare_Padding = spare_padding 

repeated_e_utran_neighbour_frequency_and_priority_struct = CSN1List(name='repeated_e_utran_neighbour_frequency_and_priority_struct', list=[
  CSN1List(num=-1, list=[
    CSN1Val(name='', val='1'),
    CSN1Bit(name='earfcn_extended', bit=18),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='measurement_bandwidth', bit=3)])})]),
  CSN1Val(name='', val='0'),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='e_utran_priority', bit=3)])}),
  CSN1Bit(name='thresh_e_utran_high', bit=5),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='thresh_e_utran_low', bit=5)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='e_utran_qrxlevmin', bit=5)])})])

repeated_utran_fdd_tdd_neighbour_frequency_and_priority_struct = CSN1List(name='repeated_utran_fdd_tdd_neighbour_frequency_and_priority_struct', list=[
  CSN1List(num=-1, list=[
    CSN1Val(name='', val='1'),
    CSN1Bit(name='utran_arfcn', bit=14)]),
  CSN1Val(name='', val='0'),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='utran_priority', bit=3)])}),
  CSN1Bit(name='thresh_utran_high', bit=5),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='thresh_utran_low', bit=5)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='utran_qrxlevmin', bit=5)])})])

utran_fdd_tdd_description_struct = CSN1List(name='utran_fdd_tdd_description_struct', list=[
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='bandwidth', bit=3)])}),
  CSN1List(num=-1, list=[
    CSN1Val(name='', val='1'),
    CSN1Ref(name='repeated_utran_fdd_tdd_neighbour_frequency_and_priority', obj=repeated_utran_fdd_tdd_neighbour_frequency_and_priority_struct)]),
  CSN1Val(name='', val='0')])

priority_and_e_utran_parameters_description_struct = CSN1Alt(name='priority_and_e_utran_parameters_description_struct', alt={
  '0': ('', []),
  '1': ('', [
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='default_e_utran_priority', bit=3)])}),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='default_thresh_e_utran_low', bit=5)])}),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='default_e_utran_qrxlevmin', bit=5)])})])}),
  CSN1List(num=-1, list=[
    CSN1Val(name='', val='1'),
    CSN1Ref(name='repeated_e_utran_neighbour_frequency_and_priority', obj=repeated_e_utran_neighbour_frequency_and_priority_struct)]),
  CSN1Val(name='', val='0'),
  CSN1List(num=-1, list=[
    CSN1Val(name='', val='1'),
    CSN1Ref(name='repeated_e_utran_not_allowed_cells', obj=repeated_e_utran_not_allowed_cells_struct)]),
  CSN1Val(name='', val='0'),
  CSN1List(num=-1, list=[
    CSN1Val(name='', val='1'),
    CSN1Ref(name='repeated_e_utran_pcid_to_ta_mapping', obj=repeated_e_utran_pcid_to_ta_mapping_struct)]),
  CSN1Val(name='', val='0'),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Ref(name='enhanced_cell_reselection_parameters_description', obj=enhanced_cell_reselection_parameters_ie)])})])})

priority_and_utran_parameters_description_struct = CSN1Alt(name='priority_and_utran_parameters_description_struct', alt={
  '0': ('', []),
  '1': ('', [
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='default_utran_priority', bit=3)])}),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='default_thresh_utran_low', bit=5)])}),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='default_utran_qrxlevmin', bit=5)])})])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Ref(name='utran_fdd_tdd_description', obj=utran_fdd_tdd_description_struct)])})])})

irat_cell_reselection_information_struct = CSN1List(name='irat_cell_reselection_information_struct', list=[
  CSN1Ref(name='priority_and_utran_parameters_description_for_the_common_plmn', obj=priority_and_utran_parameters_description_struct),
  CSN1Ref(name='priority_and_e_utran_parameters_description_for_the_common_plmn', obj=priority_and_e_utran_parameters_description_struct),
  CSN1Bit(name='nb_additional_plmns', bit=2),
  CSN1List(num=([2], lambda x: x + 1), list=[
    CSN1Bit(name='plmn_index', bit=2),
    CSN1Ref(name='priority_and_utran_parameters_description', obj=priority_and_utran_parameters_description_struct),
    CSN1Ref(name='priority_and_e_utran_parameters_description', obj=priority_and_e_utran_parameters_description_struct)])])

si_23_rest_octets = CSN1List(name='si_23_rest_octets', list=[
  CSN1Bit(name='si_23_ba_ind'),
  CSN1Bit(name='si_23_change_mark', bit=2),
  CSN1Bit(name='si_23_index', bit=3),
  CSN1Bit(name='si_23_count', bit=3),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Ref(name='irat_cell_reselection_information', obj=irat_cell_reselection_information_struct)])}),
  CSN1Ref(obj=spare_padding)])
