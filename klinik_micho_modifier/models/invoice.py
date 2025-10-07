from odoo import api,fields,models
from odoo.exceptions import UserError



class KlinikiInvoice(models.Model):
    _name = 'klinik.invoice'
    _description = 'Klinik Invoice'
    _rec_name = 'kode_invoice'

    kode_invoice = fields.Char(default='New', copy=False, readonly=True)
    tanggal = fields.Date(string='')
    pasien_id = fields.Many2one(comodel_name='klinik.pasien', string='')
    dokter_id = fields.Many2one(comodel_name='klinik.dokter', string='')
    administrasi_id = fields.Many2one(comodel_name='klinik.administrasi', string='')
    biaya_layanan = fields.Float(string='')
    resep_id = fields.Many2one(comodel_name='klinik.resep', string='')
    total = fields.Float(string='', compute="_compute_total", store=True)
    klinik_line_ids = fields.One2many(comodel_name='klinik.invoice.line', inverse_name='invoice_id', string='')
    status = fields.Selection(string='', selection=[('draft', 'Draft'), ('posted', 'Posted'), ('cancel', 'Cancel')], default="draft")


    def action_post(self):
        for rec in self:
            if self.user_has_groups('account.group_account_manager'):
                if rec.kode_invoice == "New":
                    rec.kode_invoice = self.env['ir.sequence'].next_by_code('sequence.klinik.invoice')
                if rec.status == 'draft':
                    for line in rec.klinik_line_ids:
                        if line.obat_id.stok_obat < line.qty:
                            raise UserError(f"Stok Obat tidak mencukupi, stok obat {line.obat_id.nama_obat} saat ini adalah {line.obat_id.stok_obat}")
                        else:
                            line.obat_id.stok_obat = line.obat_id.stok_obat - line.qty
                            rec.status = 'posted'
            else :
                raise UserError("Hanya Klinik Manager yang dapat memposting ini, silahkan izin ke Klinik Manager terlebih dahulu")

    def action_cancel(self):
        for rec in self:
            if rec.status == 'posted':
                rec.status = 'cancel'

    def action_draft(self):
        for rec in self:
            if rec.status == 'cancel':
                rec.status = 'draft'
    


    @api.onchange('administrasi_id')
    def _onchange_administrasi_id(self):
        for rec in self:
            if rec.administrasi_id:
                if rec.administrasi_id.dokter_id:
                    rec.dokter_id = rec.administrasi_id.dokter_id
                if rec.administrasi_id.pasien_id:
                    rec.pasien_id = rec.administrasi_id.pasien_id
                if rec.administrasi_id.resep_id:
                    rec.resep_id = rec.administrasi_id.resep_id
                if rec.administrasi_id.biaya:
                    rec.biaya_layanan = rec.administrasi_id.biaya

    @api.onchange('resep_id')
    def _compute_klinik_line_ids(self):
        for rec in self:
            if rec.resep_id:
                lines = []
                for line in rec.resep_id.obat_ids:
                    vals = {
                        'obat_id': line.id,
                    }
                    lines.append((0, 0, vals))
                rec.klinik_line_ids = lines
            else:
                rec.klinik_line_ids = [(5, 0, 0)]  # kosongkan kalau tidak ada resep


    @api.depends('klinik_line_ids.sub_total', 'biaya_layanan')
    def _compute_total(self):
        for rec in self:
            if rec.klinik_line_ids and rec.biaya_layanan:
                total = sum(rec.klinik_line_ids.mapped('sub_total'))
                rec.total = rec.biaya_layanan + total
            #     total = 0
            #     for line in rec.klinik_line_ids:
            #         total += line.sub_total
            #         # total = total + line.sub_total
            #     rec.total = rec.biaya_layanan + total
            else:
                rec.total = 0

        
                
    



class KlinikInvoiceLine(models.Model):
    _name = 'klinik.invoice.line'
    _description = 'Klinik Invoice Line'

    obat_id = fields.Many2one(comodel_name='klinik.obat', string='')
    harga_obat = fields.Float(string='Harga Obat', related='obat_id.harga_obat', store=True)
    qty = fields.Integer(string='Quantity')
    sub_total = fields.Float(string='', compute='_compute_sub_total', store=True)
    invoice_id = fields.Many2one(comodel_name='klinik.invoice', string='')
    
    
    
    @api.depends('harga_obat', 'qty')
    def _compute_sub_total(self):
        for rec in self:
            if rec.harga_obat and rec.qty:
                rec.sub_total = rec.qty * rec.harga_obat
            else:
                rec.sub_total = 0 