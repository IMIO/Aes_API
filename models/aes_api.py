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
from parent import parentApi
from child import childApi
from activity import activityApi
import logging, json
_logger = logging.getLogger(__name__)

class aesApi(models.Model):
    _name = 'aes_api.aes_api'

    @staticmethod
    def test(cr, uid, context=None):
        _logger.info("Hello world was requested. Hi there !")
        return "Hello World (an u)"

    @staticmethod
    def get_activity_details(cr, uid, data, context=None):
        """
        :param cr, uid, context needed for a static method
        :param smartphone_id: Id of the smartphone that contact us.
        :return: Dictionnary of children {id: , nom: , prenom:, tagid:}
        """
        # Declare new Environment.
        env = api.Environment(cr, uid, context={})

        return activityApi.get_activity_detail(env['extraschool.activity'], data)

    @staticmethod
    def is_registered_parent(cr, uid, info, context=None):
        """
        :param cr, uid, context needed for a static method
        :param info: email of parents
        :return: True if the email already exists, False if it doesn't.
        """
        # Declare new Environment.
        env = api.Environment(cr, uid, context={})
        _logger.info(json.dumps(info, indent=4))

        return parentApi.is_email_parent_valid(env['aes_api.parent'], info)

    @staticmethod
    def get_children(cr, uid, email, context=None):
        """
        :param cr, uid, context needed for a static method
        :param email: email of parents
        :return: True if the email already exists, False if it doesn't.
        """
        # Declare new Environment.
        env = api.Environment(cr, uid, context={})
        print json.dumps(email, indent=4)

        return parentApi.get_parent_children(env['aes_api.parent'], email)

    @staticmethod
    def get_activities(cr, uid, child_id, context=None):
        """
        :param cr, uid, context needed for a static method
        :param smartphone_id: Id of the smartphone that contact us.
        :return: Dictionnary of children {id: , nom: , prenom:, tagid:}
        """
        # Declare new Environment.
        env = api.Environment(cr, uid, context={})

        return childApi.get_child_activities(env['aes_api.child'], child_id)

    @staticmethod
    def add_registration_child(cr, uid, data, context=None):
        """
        :param cr, uid, context needed for a static method
        :param smartphone_id: Id of the smartphone that contact us.
        :return: Dictionnary of children {id: , nom: , prenom:, tagid:}
        """
        # Declare new Environment.
        env = api.Environment(cr, uid, context={})

        return childApi.get_child_activities(env['aes_api.child'], data)
