from odoo import api,fields,models



class KlinikAdministrasi(models.Model):
    _name = 'klinik.administrasi'
    _description = 'Klinik Administrasi'
    _rec_name = 'kode_administrasi'

    kode_administrasi = fields.Char(string='')
    tanggal = fields.Date(string='')
    pasien_id = fields.Many2one(comodel_name='klinik.pasien', string='')
    dokter_id = fields.Many2one(comodel_name='klinik.dokter', string='')
    biaya = fields.Float(string='')
    
    
    
    
    
