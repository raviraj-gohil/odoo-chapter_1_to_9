from odoo import models, fields

class NarutoPropertyTags(models.Model):
	_name = "naruto.property.tags"
	_description = "for testing naruto tags"

	name = fields.Char(required=True)