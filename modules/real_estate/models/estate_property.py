from odoo import models, fields

class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = 'Real Estate Property'

    name = fields.Char(string="Title",required=True, default="New Property")
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(string="Available From",copy=False, default=lambda self: fields.Date.add(fields.Date.today(), months=3))
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True, copy=False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer(string='Living Area (sqm)')
    facades = fields.Integer()
    garage = fields.Integer()
    garden = fields.Boolean()
    garden_area = fields.Integer(string='Garden Area (sqm)')
    active = fields.Boolean(default=False)
    state = fields.Selection(string='State',selection=[
        ('new', 'New'),
        ('offer_received', 'Offer Received'),
        ('offer_accepted', 'Offer Accepted'),
        ('sold', 'Sold'),
        ('canceled', 'Canceled')
    ], default='new', copy=False)
    garden_orientation = fields.Selection(string='Type',selection=[
        ('north', 'North'),
        ('south', 'South'),
        ('east', 'East'),
        ('west', 'West')
    ])
