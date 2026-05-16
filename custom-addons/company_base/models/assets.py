from odoo import models, fields

class CompanyAsset(models.Model):
    _name = 'company.asset'
    _description = 'Company Asset'

    name = fields.Char(string='Asset Name', required=True)
    serial_number = fields.Char(string='Serial Number')
