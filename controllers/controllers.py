# -*- coding: utf-8 -*-
# from odoo import http


# class LoanModule(http.Controller):
#     @http.route('/loan_module/loan_module/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/loan_module/loan_module/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('loan_module.listing', {
#             'root': '/loan_module/loan_module',
#             'objects': http.request.env['loan_module.loan_module'].search([]),
#         })

#     @http.route('/loan_module/loan_module/objects/<model("loan_module.loan_module"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('loan_module.object', {
#             'object': obj
#         })
