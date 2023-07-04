from odoo import models, fields, api
from datetime import datetime
from dateutil.relativedelta import relativedelta

class NarutoProperty(models.Model):
	_name = "naruto.property"
	_description = "for testing naruto"

	name = fields.Char(string="Title", required=True, default="unknown")
	description = fields.Text()
	postcode = fields.Char()
	date_availability = fields.Date(string="Available From", default=lambda self: fields.Datetime.now() + relativedelta(months=3))
	expected_price = fields.Float(copy=False)
	selling_price = fields.Float(readonly=True, default=1200)
	bedrooms = fields.Integer(default=2)
	living_area = fields.Integer()
	facades = fields.Integer()
	garage = fields.Boolean()
	garden = fields.Boolean()
	active = fields.Boolean(default=True)
	garden_area = fields.Integer()
	state = fields.Selection(selection = [('new', 'New'), ('received', 'Received'), ('accepted', 'Accepted'), ('sold', 'Sold'), ('canceled', 'Canceled')], default="new", copy=False, required=True)
	garden_orientation = fields.Selection(selection = [('n', 'North'), ('s', 'South')])

	property_type_id = fields.Many2one("naruto.property.type", string="Property Type")
	buyer_id = fields.Many2one("res.partner", string="Buyer")
	seller_id = fields.Many2one("res.partner", string="SalesMan")
	tag_ids = fields.Many2many('naruto.property.tags', string='Tags')
	offer_ids = fields.One2many('naruto.property.offer', 'property_id')

	total_area = fields.Integer(compute="_compute_total_area")

	best_price = fields.Float(compute="_compute_best_price")

	@api.depends('living_area', 'garden_area')
	def _compute_total_area(self):
		for rec in self:
			rec.total_area = rec.living_area + rec.garden_area

	@api.depends('offer_ids')
	def _compute_best_price(self):
		for rec in self:
			rec.best_price = max(rec.offer_ids.mapped('price'), default=0)

	@api.onchange("garden")
	def _onchange_garden(self):
		for rec in self:
			if rec.garden == True:
				rec.garden_area = 10
				rec.garden_orientation = 'n'
			else:
				rec.garden_area = ""
				rec.garden_orientation = ""


