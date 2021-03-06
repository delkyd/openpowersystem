#------------------------------------------------------------------------------
# Copyright (C) 2009 Richard Lincoln
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU Affero General Public License as published by the Free
# Software Foundation; version 2 dated June, 1991.
#
# This software is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANDABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA
#------------------------------------------------------------------------------

""" A collection of equipment at one common system voltage forming a switchgear. The equipment typically consist of breakers, busbars, instrumentation, control, regulation and protection devices as well as assemblies of all these. 
"""

# <<< imports
# @generated
from cdpsm.iec61970.core.equipment_container import EquipmentContainer

from cdpsm.iec61970.core.base_voltage import BaseVoltage
from cdpsm.iec61970.core.substation import Substation

from cdpsm.iec61970.domain import Voltage

from google.appengine.ext import db
# >>> imports

class VoltageLevel(EquipmentContainer):
    """ A collection of equipment at one common system voltage forming a switchgear. The equipment typically consist of breakers, busbars, instrumentation, control, regulation and protection devices as well as assemblies of all these. 
    """
    # <<< voltage_level.attributes
    # @generated
    # The bus bar's low voltage limit 
    low_voltage_limit = Voltage

    # The bus bar's high voltage limit 
    high_voltage_limit = Voltage

    # >>> voltage_level.attributes

    # <<< voltage_level.references
    # @generated
    # The base voltage used for all equipment within the VoltageLevel. 
    base_voltage = db.ReferenceProperty(BaseVoltage,
        collection_name="voltage_level")

    # Virtual property. The association is used in the naming hierarchy.  
    pass # bays

    # The association is used in the naming hierarchy. 
    substation = db.ReferenceProperty(Substation,
        collection_name="voltage_levels")

    # >>> voltage_level.references

    # <<< voltage_level.operations
    # @generated
    # >>> voltage_level.operations

# EOF -------------------------------------------------------------------------
