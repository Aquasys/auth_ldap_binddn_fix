# -*- coding: utf-8 -*-
##########################################################################
# Aquasys G.K.

# Copyright (C) 20012-2013.

#

# This program is free software: you can redistribute it and/or modify

# it under the terms of the GNU Affero General Public License as

# published by the Free Software Foundation, either version 3 of the

# License, or (at your option) any later version.

#

# This program is distributed in the hope that it will be useful,

# but WITHOUT ANY WARRANTY; without even the implied warranty of

# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the

# GNU Affero General Public License for more details.

#

# You should have received a copy of the GNU Affero General Public License

# along with this program. If not, see <http://www.gnu.org/licenses/>.
#########################################################################

from osv import osv
from osv import fields

class res_company_ldap(osv.osv):
    _inherit = 'res.company.ldap'

    _columns = {
        'ldap_binddn': fields.char('LDAP binddn', size=256,
            help=("The user account on the LDAP server that is used to query "
                  "the directory. Leave empty to connect anonymously.")),

    }

res_company_ldap()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
