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

""" The parts of a power system that are physical devices, electronic or mechanical 
"""

# <<< imports
# @generated
from cdpsm.iec61970.core.power_system_resource import PowerSystemResource

from cdpsm.iec61970.core.equipment_container import EquipmentContainer


from google.appengine.ext import db
# >>> imports

class Equipment(PowerSystemResource):
    """ The parts of a power system that are physical devices, electronic or mechanical 
    """
    # <<< equipment.attributes
    # @generated
    # The equipment is normally in service. 
    norma_ily_in_service = db.BooleanProperty()

    # >>> equipment.attributes

    # <<< equipment.references
    # @generated
    # The association is used in the naming hierarchy. 
    equipment_container = db.ReferenceProperty(EquipmentContainer,
        collection_name="equipments")

    # >>> equipment.references

    # <<< equipment.operations
    # @generated
    # >>> equipment.operations

# EOF -------------------------------------------------------------------------
