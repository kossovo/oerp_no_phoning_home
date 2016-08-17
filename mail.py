# -*- coding: utf-8 -*-
#/#############################################################################
#
#    BizzAppDev
#    Copyright (C) 2004-TODAY bizzappdev(<http://www.bizzappdev.com>).
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
#/#############################################################################

import logging
from openerp.tools.config import config
config['publisher_warranty_url'] = ''
_logger = logging.getLogger(__name__)
from openerp.models import AbstractModel
from openerp import api

from openerp.tools import config

config['publisher_warranty_url'] = ''


class publisher_warranty_contract(AbstractModel):
    _inherit = "publisher_warranty.contract"

    @api.model
    def _get_message():
        return {}

    @api.model
    def _get_sys_logs():
        return

    @api.multi
    def update_notification(ids, cron_mode=True):

        _logger.info("NO More Spying Stuff")
        return True

publisher_warranty_contract()
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
