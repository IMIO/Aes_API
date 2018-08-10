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

from openerp import models, api
from datetime import date, datetime
import urllib
import urlparse, random
import base64, hmac, hashlib, requests
import logging

class tools(models.Model):
    _name = "aes_api.tools"

    @staticmethod
    def calculate_age(date_of_birth):
        today = date.today()
        return today.year - date_of_birth.year - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))

##############################################################################
#
#    Portail Parent
#    Copyright (C) 2018
#    Colicchia Michaël - Imio (<http://www.imio.be>).
#
##############################################################################
    def sign_url(self, url, key, orig, algo='sha256', timestamp=None, nonce=None):
        parsed = urlparse.urlparse(url)
        new_query = self.sign_query(parsed.query, key, orig, algo, timestamp, nonce)
        return urlparse.urlunparse(parsed[:4] + (new_query,) + parsed[5:])

    def sign_query(self, query, key, orig, algo='sha256', timestamp=None, nonce=None):
        if timestamp is None:
            timestamp = datetime.datetime.utcnow()
        timestamp = timestamp.strftime('%Y-%m-%dT%H:%M:%SZ')
        if nonce is None:
            nonce = hex(random.getrandbits(128))[2:-1]
        new_query = query
        if new_query:
            new_query += '&'
        new_query += urllib.urlencode((
            ('algo', algo),
            ('orig', orig),
            ('timestamp', timestamp),
            ('nonce', nonce)))
        signature = base64.b64encode(self.sign_string(new_query, key, algo=algo))
        new_query += '&signature=' + urllib.quote(signature)
        return new_query

    def sign_string(self, s, key, algo='sha256', timedelta=30):
        digestmod = getattr(hashlib, algo)
        hash = hmac.HMAC(key, digestmod=digestmod, msg=s)
        return hash.digest()

    @api.multi
    def test_TS(self):
        key = "yPWNGX3c9PHyf2Huuuac97MvS58ArCb8f8wnTWgYEKa732x3eeEJjDxEA83Fp5PT"
        query_string = "https://demo-formulaires.guichet-citoyen.be/tests-et-bac-a-sable/demo-cb-aes/1/jump/trigger/validate"
        orig = "aes"
        query_full = self.sign_url(query_string, key, orig)
        logging.getLogger(__name__).info(requests.post(query_full))
