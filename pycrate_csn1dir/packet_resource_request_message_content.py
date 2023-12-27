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
# * File Name : pycrate_csn1dir/packet_resource_request_message_content.py
# * Created : 2018-11-21
# * Authors : Benoit Michau
# *--------------------------------------------------------
#*/
# specification: TS 44.060 - d60
# section: 11.2.16 Packet Resource Request
# top-level object: Packet Resource Request message content

# external references
from pycrate_csn1dir.padding_bits import padding_bits
from pycrate_csn1dir.channel_request_description_ie import channel_request_description_ie
from pycrate_csn1dir.egprs_timeslot_link_quality_measurements_ie import egprs_timeslot_link_quality_measurements_ie
from pycrate_csn1dir.tlli_g_rnti_ie import tlli_g_rnti_ie
from pycrate_csn1dir.egprs_bep_link_quality_measurements_type_2_ie import egprs_bep_link_quality_measurements_type_2_ie
from pycrate_csn1dir.iu_mode_channel_request_description_ie import extended_channel_request_description_ie
from pycrate_csn1dir.global_tfi_ie import global_tfi_ie
from pycrate_csn1dir.egprs_timeslot_link_quality_measurements_type_2_ie import egprs_timeslot_link_quality_measurements_type_2_ie
from pycrate_csn1dir.ms_radio_access_capability_2_ie import ms_radio_access_capability_2_ie
from pycrate_csn1dir.egprs_bep_link_quality_measurements_ie import egprs_bep_link_quality_measurements_ie
from pycrate_csn1dir.iu_mode_channel_request_description_ie import iu_mode_channel_request_description_ie

# code automatically generated by pycrate_csn1
# change object type with type=CSN1T_BSTR (default type is CSN1T_UINT) in init
# add dict for value interpretation with dic={...} in CSN1Bit init
# add dict for key interpretation with kdic={...} in CSN1Alt init

from pycrate_csn1.csnobj import *

packet_resource_request_message_content = CSN1List(name='packet_resource_request_message_content', list=[
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='access_type', bit=2)])}),
  CSN1Alt(alt={
    '0': ('', [
    CSN1Ref(name='global_tfi', obj=global_tfi_ie)]),
    '1': ('', [
    CSN1Ref(name='tlli_g_rnti', obj=tlli_g_rnti_ie)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Ref(name='ms_radio_access_capability_2', obj=ms_radio_access_capability_2_ie)])}),
  CSN1Ref(name='channel_request_description', obj=channel_request_description_ie),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='change_mark', bit=2)])}),
  CSN1Bit(name='c_value', bit=6),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='sign_var', bit=6)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='i_level_tn0', bit=4)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='i_level_tn1', bit=4)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='i_level_tn2', bit=4)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='i_level_tn3', bit=4)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='i_level_tn4', bit=4)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='i_level_tn5', bit=4)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='i_level_tn6', bit=4)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='i_level_tn7', bit=4)])}),
  CSN1Alt(alt={
    '0': ('', [
    CSN1Bit(bit=-1)]),
    '1': ('', [
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Ref(name='egprs_bep_link_quality_measurements', obj=egprs_bep_link_quality_measurements_ie)])}),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Ref(name='egprs_timeslot_link_quality_measurements', obj=egprs_timeslot_link_quality_measurements_ie)])}),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='pfi', bit=7)])}),
    CSN1Bit(name='additional_ms_rac_information_available'),
    CSN1Bit(name='retransmission_of_prr'),
    CSN1Alt(alt={
      '0': ('', [
      CSN1Bit(bit=-1)]),
      '1': ('', [
      CSN1Alt(alt={
        '0': ('', []),
        '1': ('', [
        CSN1Alt(alt={
          '0': ('', []),
          '1': ('', [
          CSN1Bit(name='g_rnti_extension', bit=4)])}),
        CSN1Ref(name='iu_mode_channel_request_description', obj=iu_mode_channel_request_description_ie)])}),
      CSN1Alt(alt={
        '0': ('', []),
        '1': ('', [
        CSN1Bit(name='hfn_lsb')])}),
      CSN1Alt(alt={
        '0': ('', [
        CSN1Bit(bit=-1)]),
        '1': ('', [
        CSN1Alt(alt={
          '0': ('', []),
          '1': ('', [
          CSN1Ref(name='extended_channel_request_description', obj=extended_channel_request_description_ie)])}),
        CSN1Alt(alt={
          '0': ('', [
          CSN1Bit(bit=-1)]),
          '1': ('', [
          CSN1Bit(name='early_tbf_establishment'),
          CSN1Alt(alt={
            '0': ('', []),
            '1': ('', [
            CSN1Ref(name='egprs_bep_link_quality_measurements_type_2', obj=egprs_bep_link_quality_measurements_type_2_ie)])}),
          CSN1Alt(alt={
            '0': ('', []),
            '1': ('', [
            CSN1Ref(name='egprs_timeslot_link_quality_measurements_type_2', obj=egprs_timeslot_link_quality_measurements_type_2_ie)])}),
          CSN1Alt(alt={
            '0': ('', [
            CSN1Bit(bit=-1)]),
            '1': ('', [
            CSN1Bit(name='low_access_priority_signalling'),
            CSN1Alt(alt={
              '0': ('', [
              CSN1Bit(bit=-1)]),
              '1': ('', [
              CSN1Alt(alt={
                '0': ('', []),
                '1': ('', [
                CSN1Bit(name='downlink_etfi', bit=3)])}),
              CSN1Ref(obj=padding_bits)]),
              None: ('', [])})]),
            None: ('', [])})]),
          None: ('', [])})]),
        None: ('', [])})]),
      None: ('', [])})]),
    None: ('', [])})])

