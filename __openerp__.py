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
{
    'name' : 'LDAP Bug Fix',
    'version' : '1.0',
    'depends' : ['base', "auth_ldap"],
    'author' : 'Aquasys G.K',
    'description': """
    Bug Fix ldap binddn field restricted to 64 chars
    """,
    'website' : 'http://www.aquasys.co.jp/',
    'category' : 'Bug Fix',
    'data' : [
    ],
    'auto_install': False,
    'installable': True,
    'external_dependencies' : {
        'python' : ['ldap'],
    }
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

