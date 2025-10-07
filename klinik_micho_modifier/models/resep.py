from odoo import api,fields,models



class KlinikResep(models.Model):
    _name = 'klinik.resep'
    _description = 'Klinik Resep'
    _rec_name = 'kode_resep'

    kode_resep = fields.Char(string='')
    obat_ids = fields.Many2many(comodel_name='klinik.obat', string='')
    tanggal = fields.Date(string='')
    keterangan = fields.Text('Keterangan')
    pasien_id = fields.Many2one(comodel_name='klinik.pasien')
    dokter_id = fields.Many2one(comodel_name='klinik.dokter')
    
    