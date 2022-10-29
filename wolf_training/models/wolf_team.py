# -*- coding: utf-8 -*-

from odoo import models, fields, api


class WolfTeam(models.Model):
    _name = 'wolf.team'
    _description = 'Wolf Team'

    name = fields.Char(string='Name')
    age = fields.Integer(string='Age')
    phone = fields.Char(string='Char')
    sexe = fields.Selection([('m', 'Male'), ('f', 'Female')], string='Sexe', default='m')
    # state = fields.Selection([('new','New'),('')])
