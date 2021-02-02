# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

#Goal is a report to record production batches in system (first no stock impacts)
class PmoSprint(models.Model):
    _name = 'pmo.sprint'
    _description = 'sprint Record'

    #chatter and notes frame
    _inherit = ['mail.thread', 'mail.activity.mixin']

    #general info
    name = fields.Char(string="Sprint Name")
    planning_date = fields.Date(string="Planning Date")
    start = fields.Char(string="Sprint Start")
    end = fields.Char(string="Sprint End")
    attendants = fields.Char(string='Attendants')

    #notes
    notes = fields.Html(string='Notes')

    #release question
    releaseq = fields.Selection([('a', 'Yes'), ('b', 'No')], string="Everyone fine?")

    #review
    review_well = fields.Html(string="What went well?")
    improvements = fields.Html(string="What to improve for next month/ in general?")


    #statusbar
    state = fields.Selection([
            ('planning', 'planning'),
            ('ongoing', 'ongoing'),
            ('review', 'review'),
        ], string='Status', readonly=True, default='planning')

    #sequence field
    sprint_sequence = fields.Char(string="Sequence", required=True, copy=False, readonly=True,
                                    index=True, default=lambda self: _('New'))

    #record name sprint/SPR001
    _rec_name = 'sprint_sequence'

    #sprint sequence
    @api.model
    def create(self, vals):
        if vals.get('sprint_sequence', _('New')) == _('New'):
            vals['sprint_sequence'] = self.env['ir.sequence'].next_by_code('pmo.sprint.sequence') or _('New')
        result = super(PmoSprint, self).create(vals)
        return result


    #change status button
    status = fields.Selection([('new', 'New'), ('planning', 'planning'), ('ongoing', 'ongoing'), ('review','review')], string='Status', default='new')

    def set_sprint_to_new(self):
        self.status = 'new'

    def set_sprint_to_planning(self):
        self.status = 'planning'

    def set_sprint_to_ongoing(self):
        self.status = 'ongoing'

    def set_sprint_to_review(self):
        self.status = 'review'






    # capacity table
    capacity_id = fields.One2many('capacity.capacity', 'capacity_id', string='Capacity Planning')

class Capacity(models.Model):
   _name = 'capacity.capacity'
   name = fields.Char(string='Project')

   capacity_id = fields.Char(string='Planned Capacity')
   iscapacity_id = fields.Char(string='Actual Used Capacity')
   note_id = fields.Char(string='Note')
