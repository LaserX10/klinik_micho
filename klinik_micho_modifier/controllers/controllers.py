# -*- coding: utf-8 -*-
# from odoo import http


# class KlinikMichoModifier(http.Controller):
#     @http.route('/klinik_micho_modifier/klinik_micho_modifier/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/klinik_micho_modifier/klinik_micho_modifier/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('klinik_micho_modifier.listing', {
#             'root': '/klinik_micho_modifier/klinik_micho_modifier',
#             'objects': http.request.env['klinik_micho_modifier.klinik_micho_modifier'].search([]),
#         })

#     @http.route('/klinik_micho_modifier/klinik_micho_modifier/objects/<model("klinik_micho_modifier.klinik_micho_modifier"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('klinik_micho_modifier.object', {
#             'object': obj
#         })
