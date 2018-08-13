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
import json
from datetime import datetime


class activityApi(models.Model):
    
    _inherit = 'extraschool.activity'

    portal_available = fields.Boolean(
        default=False,
        string="Is available for a parent on his portail"
    )

    @api.multi
    def get_activity_detail(self, data):
        """

        :param data:
        :return:
        """
        school_id = self.env['extraschool.child'].search([('id', '=', data.get('child_id'))]).schoolimplantation
        place_id = self.env['extraschool.place'].search([('schoolimplantation_ids', '=', school_id.id)])

        occurrence_ids = self.env['extraschool.activityoccurrence'].search([
            ('activityid', '=', int(data.get('activity'))),
            ('date_start', '>=', datetime.strptime(str(data.get('begining_date_search')), '%Y%m%dT%H:%M:%S').strftime("%Y-%m-%d")),
            ('date_stop', '<=', datetime.strptime(str(data.get('ending_date_search')), '%Y%m%dT%H:%M:%S').strftime("%Y-%m-%d")),
            ('place_id', '=', place_id.id)
        ])

        occurence_list = []
        for occurrence in occurrence_ids:
            occurence_list.append(
                {
                    'id': occurrence.id,
                    'activity_id': data.get('activity'),
                    'text': occurrence.occurrence_date,
                }
            )

        if occurence_list:
            print json.dumps({'data': occurence_list}, indent=4)
            return {'data': occurence_list}

        return None
