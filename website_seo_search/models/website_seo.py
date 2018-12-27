# -*- coding: utf-8 -*-

from odoo import models


class Website(models.Model):
    _inherit = 'website'

    def get_meta_tags(self, active_tags=False, pager=False, main_object=False):
        tag_names = ""
        meta_tags = {'title': '', 'meta_description': ''}
        if active_tags:
            tags = self.env['blog.tag'].browse(active_tags)
            for tag in tags:
                tag_names += tag.name + ' '
        if main_object and 'website_meta_title' in main_object:
            meta_tags['title'] = main_object.website_meta_title
            if pager and isinstance(main_object.website_meta_title, str):
                title = main_object.website_meta_title.split('|')
                if len(title) > 1:
                    title = '%s %s Page %s |%s' % (title[0], tag_names, pager['page']['num'], title[1])
                else:
                    title = '%s %s Page %s' % (title[0], tag_names, pager['page']['num'])
                meta_tags['title'] = title
        if main_object and main_object.website_meta_description:
            meta_tags['meta_description'] = main_object.website_meta_description
            if pager and isinstance(main_object.website_meta_description, str):
                meta_description = '%s %s | Page %s' % (main_object.website_meta_description,
                                                        tag_names,
                                                        pager['page']['num'])
                meta_tags['meta_description'] = meta_description
        return meta_tags

    def active_tags_header(self, active_tags=False):
        tag_title = ""
        if active_tags:
            tags = self.env['blog.tag'].browse(active_tags)
            for tag in tags:
                tag_title += tag.name + ','
            tag_title = tag_title[:-1]
        return tag_title
