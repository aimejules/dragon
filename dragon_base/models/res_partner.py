# -*- coding: utf-8 -*-

from odoo import models, fields

class ResParnter(models.Model):
    _inherit = 'res.partner'

    nif = fields.Char(string='NIF')
    stat = fields.Char(string='STAT')
    rcs = fields.Char(string='RCS')
