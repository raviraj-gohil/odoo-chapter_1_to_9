from odoo import models, fields

class NarutoPropertyType(models.Model):
	_name = "naruto.property.type"
	_description = "for testing naruto type"

	name = fields.Char(required=True)
