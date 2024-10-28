# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class MaterialController(http.Controller):

    @http.route('/materials', auth='user', website=True)
    def material_list(self, **kw):
        materials = request.env['materials'].sudo().search([])
        return request.render('backend_odoo_test.materials_template', {
            'materials': materials
        })


#     @http.route('/backend_odoo_test/backend_odoo_test/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('backend_odoo_test.listing', {
#             'root': '/backend_odoo_test/backend_odoo_test',
#             'objects': http.request.env['backend_odoo_test.backend_odoo_test'].search([]),
#         })

#     @http.route('/backend_odoo_test/backend_odoo_test/objects/<model("backend_odoo_test.backend_odoo_test"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('backend_odoo_test.object', {
#             'object': obj
#         })
