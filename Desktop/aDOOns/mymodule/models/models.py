# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions

class Activity (models.Model):
    
    _name = 'pupilsop.activity'
    
    name = fields.Char(string="Title", required=True)
    description = fields.Text()
    remarks = fields.Text()
    hours = fields.Float(string="Duration of the activity")
    
    pupil_activity = fields.Many2one('res.users',default=lambda self: self.env.user, ondelete='set null', string="Pupil", required=True)
    
    @api.constrains('hours')
    def _verify_hours(self):
        for record in self:
            if record.hours > 8:
                raise exceptions.ValidationError("An activity can't have more than 8 hours")
                
    
    #@api.constrains('is_pupil','is_teacher')
    #def _verify_is_not_both(self):
    #    for r in self:
    #        if r.is_pupil and r.is_teacher:
    #            raise exceptions.ValidationError("Can't have both profiles at the same time")