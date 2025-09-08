from odoo import api,fields,models



class KlinikDokter(models.Model):
    _name = 'klinik.dokter'
    _description = 'Klinik Dokter'
    _rec_name = 'nama_dokter'

    kode_dokter = fields.Char(string='')
    nama_dokter = fields.Char(string='')
    spesialis = fields.Selection([
        ('jantung', 'Jantung'),
        ('penyakit_dalam', "Penyakit Dalam"),
        ('anak', "Anak"),
        ('bedah', "Bedah"),
        ('saraf', "Saraf"),
        ('kulit', "Kulit"),
        ('tht', "THT"),
    ], string='Spesialis',required=True)
    nomor_hp = fields.Char(string='')
    updated_at = fields.Datetime('')
    

    
