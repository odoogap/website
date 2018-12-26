# -*- coding: utf-8 -*-
import re

from odoo import models, fields


class Website(models.Model):
    _inherit = 'website'

    def get_meta_tags(self, active_tags=False, pager=False, main_object=False, meta_type='t'):
        tag_names = ""
        if active_tags:
            tags = self.env['blog.tag'].browse(active_tags)
            for tag in tags:
                tag_names += tag.name

        if meta_type == 'title':
            if pager and main_object and 'website_meta_title' in main_object:
                if isinstance(main_object.website_meta_title, str):
                    title = main_object.website_meta_title.split('|')
                    if len(title) > 1:
                        title = '%s Page %s |%s' % (title[0], pager['page']['num'], title[1])
                    else:
                        title = '%s Page %s' % (title[0], pager['page']['num'])
                    return tag_names + title

        if meta_type == 'd':
            if isinstance(main_object.website_meta_description, str):
                if pager and main_object and main_object.website_meta_description:
                    meta_description = '%s | Page %s' % (main_object.website_meta_description, pager['page']['num'])
                    return tag_names + meta_description

        return False
