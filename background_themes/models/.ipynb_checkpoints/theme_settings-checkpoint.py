# -*- coding: utf-8 -*-

from odoo import models, fields, api


class theme_settings(models.Model):
     _name = 'themes.settings'
     _description = 'Configuration du themes'
     nav_font_color = fields.Char()
     nav_background_color = fields.Char()
     background_color = fields.Char()
#    society = fields.many2one('patient.name', 'name')

