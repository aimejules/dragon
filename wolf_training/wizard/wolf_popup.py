from odoo import fields, models, api


class WolfPopup(models.TransientModel):
    _name = 'wolf.popup'
    _rec_name = 'birth_date'

    birth_date = fields.Date(string='Bith date')

    def update_birth_date(self):
        WolfTeam = self.env['wolf.team']
        active_id = self.env.context.get('active_id')
        wolf_id = WolfTeam.browse(active_id)
        birth_date = self.birth_date
        #to do compute age from bithd_date
        wolf_id.age = 67
