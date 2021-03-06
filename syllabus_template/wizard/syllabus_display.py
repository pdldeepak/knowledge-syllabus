# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError


class SyllabusDisplay(models.TransientModel):
    _name = "syllabus.display"
    _description = "Syllabus display wizard"

    def _get_default_syllabus(self):
        return self.env['document.page'].browse(self._context.get('active_ids'))[0]

    def _get_temp_syllabus(self):
        return self.env['document.page'].browse(self._context.get('active_ids'))[0].temp_content

    syllabus_id = fields.Many2one("document.page", string="Syllabus", default=_get_default_syllabus)
    temp_syllabus = fields.Html(string="Temporary syllabus", default=_get_temp_syllabus)
    summary = fields.Text(String="Change Summary")
    major_change = fields.Boolean("Major Change?", default=False)
    major_version = fields.Char("Provide Version Convention")

    @api.multi
    def saveSyllabus(self):
        for record in self:
            record.syllabus_id.write({
                'content': record.temp_syllabus,
                'summary': record.summary,
                'major_change': record.major_change,
                'major_version': record.major_version
            })
        return {'type': 'ir.actions.act_window_close'}
