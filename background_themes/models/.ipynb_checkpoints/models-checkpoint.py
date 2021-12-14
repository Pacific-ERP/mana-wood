# -*- coding: utf-8 -*-

from odoo import models, fields, api


class background_themes(models.Model):
     _name = 'background_themes.background_themes'
     _description = 'background_themes.background_themes'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
