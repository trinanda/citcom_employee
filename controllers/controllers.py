# -*- coding: utf-8 -*-
# from odoo import http


# class CitcomEmployee(http.Controller):
#     @http.route('/citcom_employee/citcom_employee/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/citcom_employee/citcom_employee/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('citcom_employee.listing', {
#             'root': '/citcom_employee/citcom_employee',
#             'objects': http.request.env['citcom_employee.citcom_employee'].search([]),
#         })

#     @http.route('/citcom_employee/citcom_employee/objects/<model("citcom_employee.citcom_employee"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('citcom_employee.object', {
#             'object': obj
#         })
