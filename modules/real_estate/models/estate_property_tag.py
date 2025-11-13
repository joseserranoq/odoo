from odoo import models, fields

class EstatePropertyTag(models.Model):
    _name = 'estate.property.tag'
    _description = 'Real Estate Property Tag'
    name = fields.Char(string="Tag Name", required=True)
    # SQL constaints
    _sql_constraints = [
        ('name_unique', 'UNIQUE(name)', 'The tag name must be unique.')
    ]
