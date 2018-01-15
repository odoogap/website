# -*- coding: utf-8 -*-
# Copyright 2017 OdooGap - PromptEQUATION - Diogo Duarte
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo import api, models, fields


class ProductPublicCategory(models.Model):
    _inherit = "product.public.category"

    website_ids = fields.Many2many(
        'website', string='Show in the following websites only', default=lambda self: self.env['website'].search(
            [('id', '=', self.env.ref('website.default_website').id)]))
