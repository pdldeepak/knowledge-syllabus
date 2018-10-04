# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Package(models.Model):
    _name = 'syllabus_package.package'
    _inherit = 'mail.thread'

    name = fields.Char(string='Name')
    syllabus_ids = fields.One2many('syllabus_minister.syllabus','package_id',string='Syllabus')