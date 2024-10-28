from odoo import models, fields, api


class Supplier(models.Model):
    _name = 'supplier'
    _description = 'Supplier'
    _rec_name = 'supplier_name'

    supplier_code = fields.Char(string='Supplier Code', required=True)
    supplier_name = fields.Char(string='Supplier Name', required=True)
    supplier_phone = fields.Char(string='No Hp', required=True)
    supplier_wa = fields.Char(string='No WatsApp', required=True)
    supplier_npwp = fields.Char(string='NPWP', required=True)
    supplier_email = fields.Char(string='Email', required=True)
    supplier_web = fields.Char(string='Website')
    supplier_address = fields.Html(string='Address', required=True)
    supplier_img = fields.Image(string='Supplier Image', required=True)
    supplier_ids = fields.One2many(comodel_name='materials', inverse_name='supplier_id', string='')

    _sql_constraints = [
        ('supplier_code_unique', 'unique(supplier_code)', 'Supplier Code sudah digunakan.')
    ]
    
