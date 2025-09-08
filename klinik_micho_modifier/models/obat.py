from odoo import api,fields,models



class KlinikObat(models.Model):
    _name = 'klinik.obat'
    _description = 'Klinik Obat'
    _rec_name = 'nama_obat'

    kode_obat = fields.Char(string='')
    nama_obat = fields.Char(string='')
    jenis_obat = fields.Selection([
        ('tablet', 'Tablet'),
        ('sirup', 'Sirup'),
        ('kapsul', 'Kapsul'),
        ('injeksi', 'Injeksi'),
        ('salep', 'Salep'),
    ], string='Jenis Obat', required=True)
    stok_obat = fields.Integer(string='')
    harga_obat = fields.Float(string='')
    updated_at = fields.Datetime('')
    
    