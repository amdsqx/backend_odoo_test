from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Material(models.Model):
    _name = 'materials'
    _description = 'Material'
    _rec_name = 'material_name'

    material_code = fields.Char(string='Material Code', required=True)
    material_name = fields.Char(string='Material Name', required=True)
    material_type = fields.Selection([
        ('fabric', 'Fabric'),
        ('jeans', 'Jeans'),
        ('cotton', 'Cotton')], 
        string='Material Type', required=True)
    material_buy_price = fields.Float(string='Material Buy Price', required=True)
    supplier_id = fields.Many2one(comodel_name='supplier', string='Supplier Name', required=True)

    _sql_constraints = [
        ('material_code_unique', 'unique(material_code)', 'Material Code must be unique.')
    ]
    

    @api.constrains('material_buy_price')
    def _check_material_buy_price(self):
        if any(record.material_buy_price < 100 for record in self):
            raise ValidationError("Pembelian material minimal 100.")
