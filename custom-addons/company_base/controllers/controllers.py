# -*- coding: utf-8 -*-
# from odoo import http


# class CompanyBase(http.Controller):
#     @http.route('/company_base/company_base', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/company_base/company_base/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('company_base.listing', {
#             'root': '/company_base/company_base',
#             'objects': http.request.env['company_base.company_base'].search([]),
#         })

#     @http.route('/company_base/company_base/objects/<model("company_base.company_base"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('company_base.object', {
#             'object': obj
#         })

