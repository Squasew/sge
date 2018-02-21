# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions
from datetime import datetime

class Activity (models.Model):
    
    _name = 'pupilsop.activity'
    
    name = fields.Char(string="Title", required=True)
    date = fields.Date(string="Date", default=datetime.today())
    description = fields.Text()
    remarks = fields.Text()
    hours = fields.Float(string="Duration of the activity")
    
    pupil_activity = fields.Many2one('res.users',default=lambda self: self.env.user, ondelete='set null', string="Pupil", required=True)
    
    @api.constrains('hours')
    def _verify_hours(self):
        for record in self:
            if record.hours > 8:
                raise exceptions.ValidationError("An activity can't have more than 8 hours")
                
    
#    @api.constrains('hours','date')
#    def _verify_hours_day(self):
#        hoursDate = fields.Float()
#            for record in self:
##            if record.date = date:
##                hoursDate = hoursDate + record.hours
##        if hoursDate > 8:
##                raise exceptions.ValidationError("Adding activity the day has more than 8 hours in activities")