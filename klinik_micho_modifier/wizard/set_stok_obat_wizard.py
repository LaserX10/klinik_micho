from odoo import api,fields,models



class SetStokObatWizard(models.TransientModel):
    _name = 'set.stok.obat.wizard'
    _description = 'Set Stok Obat Wizard'

    obat_id = fields.Many2one(comodel_name='klinik.obat', string='', required=True)
    stok_obat = fields.Integer(string='', required=True)

    def action_confirm(self):
        for rec in self:
            if rec.obat_id and rec.stok_obat:
                rec.obat_id.stok_obat = rec.obat_id.stok_obat + rec.stok_obat
        

    
