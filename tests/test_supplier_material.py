from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError

class TestSupplierMaterial(TransactionCase):

    def setUp(self):
        super(TestSupplierMaterial, self).setUp()
        # Creating a supplier record for testing
        self.supplier = self.env['supplier'].create({
            'supplier_code': 'SUPP001',
            'supplier_name': 'Supplier Test',
            'supplier_phone': '08123456789',
            'supplier_wa': '08123456789',
            'supplier_npwp': '1234567890',
            'supplier_email': 'test@supplier.com',
            'supplier_web': 'http://www.supplier.com',
            'supplier_address': '<p>123 Test Street</p>',
            'supplier_img': False,
        })

    def test_create_material(self):
        """Test material creation and validation"""
        material = self.env['materials'].create({
            'material_code': 'MAT001',
            'material_name': 'Test Material',
            'material_type': 'cotton',
            'material_buy_price': 150.0,
            'supplier_id': self.supplier.id,
        })
        self.assertEqual(material.material_code, 'MAT001', "Material code should be 'MAT001'")
        self.assertEqual(material.material_buy_price, 150.0, "Material price should be 150.0")

    def test_material_buy_price_validation(self):
        """Test that ValidationError is raised when material price is below 100"""
        with self.assertRaises(ValidationError):
            self.env['materials'].create({
                'material_code': 'MAT002',
                'material_name': 'Cheap Material',
                'material_type': 'fabric',
                'material_buy_price': 50.0,  # Below 100, should raise ValidationError
                'supplier_id': self.supplier.id,
            })

    def test_supplier_code_unique(self):
        """Test that the supplier code is unique"""
        with self.assertRaises(ValidationError):
            self.env['supplier'].create({
                'supplier_code': 'SUPP001',  # Duplicate supplier code
                'supplier_name': 'Duplicate Supplier',
                'supplier_phone': '08123456780',
                'supplier_wa': '08123456780',
                'supplier_npwp': '9876543210',
                'supplier_email': 'duplicate@supplier.com',
                'supplier_web': 'http://www.duplicatesupplier.com',
                'supplier_address': '<p>456 Duplicate Street</p>',
                'supplier_img': False,
            })

