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

from openerp import api, models
import json


class childApi(models.Model):
    _name = "aes_api.child"

    # Todo: affinate the search
    @api.multi
    def get_child_activities(self, child_id):
        school_ids = self.env['extraschool.child'].search([('id', '=', child_id.get('id'))]).schoolimplantation
        print school_ids

        activities = self.env['extraschool.activity'].search([('portal_available', '=', True)])

        activities_list = []

        for activity in activities:
            activities_list.append(
                {
                    'id': activity.id,
                    'text': activity.name,
                }
            )

        if activities_list:
            print json.dumps({'data': activities_list}, indent=4)
            return {'data': activities_list}

        return None
