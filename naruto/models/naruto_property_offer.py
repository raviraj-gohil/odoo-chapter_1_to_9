from odoo import models, fields, api
from datetime import datetime, timedelta

class NarutoPropertyOffer(models.Model):
	_name = "naruto.property.offer"
	_description = "for testing naruto offer"

	price = fields.Float()
	status = fields.Selection(selection = [('accepted','Accepted'), ('refused','Refused')], copy=False)
	partner_id = fields.Many2one('res.partner', required=True)
	property_id = fields.Many2one('naruto.property', required=True)
	validity = fields.Integer(default=7)
	current_date = fields.Date(default=fields.Date.today())
	date_deadline = fields.Date(compute='_compute_date_deadline', inverse='_inverse_date_deadline')

	@api.depends('validity')
	def _compute_date_deadline(self):
		for rec in self:
			rec.date_deadline = False
			if rec.validity:
				rec.date_deadline = rec.current_date + timedelta(days=rec.validity)

	@api.depends('date_deadline')
	def _inverse_date_deadline(self):
		for rec in self:
			if rec.date_deadline:
				rec.validity = (rec.date_deadline - rec.current_date).days