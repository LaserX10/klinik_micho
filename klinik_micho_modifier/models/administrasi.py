from odoo import api,fields,models
from odoo.exceptions import ValidationError, UserError
from datetime import datetime



class KlinikAdministrasi(models.Model):
    _name = 'klinik.administrasi'
    _description = 'Klinik Administrasi'
    _rec_name = 'kode_administrasi'
    _sql_constraints = [
        ("kode_administrasi_unique", "unique(kode_administrasi)", "Kode Administrasi sudah tersedia"),
        ("biaya_limit", "check(biaya > 10000)", "Biaya tidak boleh lebih kecil daripada Rp 10.000" )
    ]

    kode_administrasi = fields.Char(string='')
    tanggal = fields.Date(string='')
    pasien_id = fields.Many2one(comodel_name='klinik.pasien', string='', required=True)
    usia = fields.Integer(string='')
    jenis_kelamin = fields.Selection(string='Jenis Kelamin', related='pasien_id.jenis_kelamin', store=True)
    dokter_id = fields.Many2one(comodel_name='klinik.dokter', string='')
    biaya = fields.Float(string='')
    resep_id = fields.Many2one(comodel_name='klinik.resep', compute='_compute_resep_id', store=True)
        
        
    @api.depends('tanggal', 'pasien_id', 'dokter_id')
    def _compute_resep_id(self):
        for rec in self:
            if rec.tanggal and rec.pasien_id and rec.dokter_id:
                resep = self.env['klinik.resep'].search([('tanggal','=',rec.tanggal),('pasien_id','=',rec.pasien_id.id),('dokter_id','=',rec.dokter_id.id)])
                if resep:
                    rec.resep_id = resep
                else:
                    rec.resep_id = False
            else:
                rec.resep_id = False
    
    @api.onchange('pasien_id')
    def _onchange_pasien_id(self):
        for rec in self:
            if rec.pasien_id and rec.pasien_id.usia:
                rec.usia = rec.pasien_id.usia
            else:
                rec.usia = False
    
    @api.constrains('tanggal')
    def _constrains_tanggal(self):
        for rec in self:
            if rec.tanggal:
                if rec.tanggal > fields.Date.today():
                    raise UserError("Tanggal tidak boleh lebih besar dari tanggal hari ini")
