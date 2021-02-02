# -*- coding: utf-8 -*-

from odoo import models, fields

class PmoOverall (models.Model):
    _name = 'pmo.overall'
    _description = 'Overall Record'

    overall_year = fields.Char(string='Year', required=True)


    overall_id = fields.One2many('overalltable.overalltable', 'overalltable_id', string='Overall Planning')

class Overalltable(models.Model):
   _name = 'overalltable.overalltable'
   name = fields.Char(string='Project')

   overalltable_id = fields.Char(string='Jan')

   feb = fields.Char(string='Feb')
   mrz = fields.Char(string='Mrz')
   apr = fields.Char(string='Apr')
   mai = fields.Char(string='Mai')
   jun = fields.Char(string='Jun')
   jul = fields.Char(string='Jul')
   aug = fields.Char(string='Aug')
   sep = fields.Char(string='Sep')
   okt = fields.Char(string='Okt')
   nov = fields.Char(string='Nov')
   dec = fields.Char(string='Dec')



