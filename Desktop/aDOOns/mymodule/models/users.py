# -*- coding: utf-8 -*-
from odoo import fields, models, api, exceptions

class Users(models.Model):
    
    _inherit = 'res.users'
    
    is_pupil = fields.Boolean("Pupil",default=False)
    is_teacher = fields.Boolean("Teacher",default=False)

    pupils_activities = fields.One2many('pupilsop.activity', 'pupil_activity', string="Activities")
    my_fctpartner = fields.Many2one('res.partner',ondelete='set null',string="FCT Partner")
    
    my_teacher = fields.Many2one('res.users',ondelete='set null',string="Teacher")
    my_pupils = fields.One2many('res.users','my_teacher',string="Pupils")
    
    @api.constrains('is_pupil','is_teacher')
    def _verify_is_not_both(self):
        for r in self:
            if r.is_pupil and r.is_teacher:
                raise exceptions.ValidationError("Can't have both profiles at the same time")