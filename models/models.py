# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Employee(models.Model):
    _inherit = 'hr.employee'

    family_ids = fields.One2many(comodel_name='citcom.family', inverse_name='employee_id', string='Family')
    skill_ids = fields.Many2many(comodel_name='citcom.skill', string='Skills')


class Family(models.Model):
    _name = 'citcom.family'

    employee_id = fields.Many2one(comodel_name='hr.employee', string='Employee')
    name = fields.Char(string='Name')
    relation = fields.Selection(string='Relation', selection=[
        ('mother', 'Mother'),
        ('father', 'Father'),
        ('brother', 'Brother'),
        ('sister', 'Sister'),
    ])

class Skill(models.Model):
    _name = 'citcom.skill'
    _description = 'Skills'

    name = fields.Char(string='Skill Name')
