# -*- coding: utf-8 -*-
from odoo import fields, models 

class Partner(models.Model):
    
    _inherit = 'res.partner'
    
    is_fctpartner = fields.Boolean("Is FCT Partner",default=False)
    
    my_fctpupils = fields.One2many('res.users','my_fctpartner',string="Pupils")