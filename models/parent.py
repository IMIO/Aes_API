# -*- coding: utf-8 -*-
##############################################################################
#
#    AES API
#    Copyright (C) 2018
#    Michael Colicchia - Imio (<http://www.imio.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import api, fields, models
from tools import tools
import json
import datetime


class parentApi(models.Model):
    _name = "aes_api.parent"

    @api.multi
    def is_email_parent_valid(self, email):
        if self.env['extraschool.parent'].search([('email', '=ilike', email.get('email'))]):
            return True
        return False

    # Todo: Be able to search in email separated by , ex: a@a.aa, b@b.bb
    @api.multi
    def get_parent_children(self, email):
        parent_id = self.env['extraschool.parent'].search([('email', '=ilike', email.get('email'))]).id
        children = self.env['extraschool.child'].search([('parentid', '=', parent_id)])
        children_list = []

        for child in children:
            children_list.append(
                {
                    'id': child.id,
                    'lastname':child.lastname,
                    'firstname': child.firstname,
                    'age': tools.calculate_age(datetime.datetime.strptime(child.birthdate, "%Y-%m-%d")),
                    'text': child.name,
                }
            )

        if children_list:
            print json.dumps({'data': children_list}, indent=4)
            return {'data': children_list}
        print "NONE"
        return None
