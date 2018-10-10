# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Faculty(models.Model):
    _name = 'syllabus_minister.faculty'
    _inherit = 'mail.thread'
    _description = 'Faculty'

    name = fields.Char(string='Name')
    introduction = fields.Html(string='Introduction')
    vision = fields.Html(string='Vision')
    mission = fields.Html(string='Mission')
    goals = fields.Html(string='Goals and Objectives')
    characteristics = fields.Html(string='Characterstics')
    program_ids = fields.One2many('syllabus_minister.program','faculty_id',string='Program')
    university_id = fields.Many2one('syllabus_minister.university',string='University')
    # school_ids = fields.One2many('syllabus_minister.school','faculty_id',string='School')
    # college_ids = fields.One2many('syllabus_minister.college','faculty_id',string='College')

