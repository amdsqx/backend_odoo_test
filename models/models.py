# -*- coding: utf-8 -*-

from odoo import models, fields


class POSConfig(models.Model):
    _inherit = 'pos.config'

    visible_price_btn = fields.Boolean(string='Visible price button')
    
# class PosSession (models.Model):
#     _inherit = "pos.session"

#     def _pos_data_process (self, loaded_data):
#         super().pos_data_process(loaded_data);
#         loaded_data['visible_price_btn'] = self.config_id.visible_price_btn