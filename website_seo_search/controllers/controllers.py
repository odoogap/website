# -*- coding: utf-8 -*-
from odoo import http

# class MultiTitleMetaDescription/(http.Controller):
#     @http.route('/multi_title_meta_description//multi_title_meta_description//', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/multi_title_meta_description//multi_title_meta_description//objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('multi_title_meta_description/.listing', {
#             'root': '/multi_title_meta_description//multi_title_meta_description/',
#             'objects': http.request.env['multi_title_meta_description/.multi_title_meta_description/'].search([]),
#         })

#     @http.route('/multi_title_meta_description//multi_title_meta_description//objects/<model("multi_title_meta_description/.multi_title_meta_description/"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('multi_title_meta_description/.object', {
#             'object': obj
#         })