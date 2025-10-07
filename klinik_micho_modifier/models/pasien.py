from odoo import api,fields,models



class KlinikPasien(models.Model):
    _name = 'klinik.pasien'
    _description = 'Klinik Pasien'
    _rec_name = 'nama_pasien'

    kode_pasien = fields.Char(string='')
    nama_pasien = fields.Char(string='')
    jenis_kelamin = fields.Selection([
        ('laki_laki', 'Laki-laki'),
        ('perempuan', 'Perempuan'),
    ], string='Jenis Kelamin', required=True)
    usia = fields.Integer(string='')
    
    status = fields.Selection([
        ('belum_menikah', 'Belum Menikah'),
        ('sudah_menikah', 'Sudah Menikah'),
        ('duda', 'Duda'),
        ('janda', 'Janda'),
    ], string='Status', required=True)
    alamat = fields.Char(string='')
    updated_at = fields.Datetime('')
    