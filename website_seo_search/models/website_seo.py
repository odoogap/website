# -*- coding: utf-8 -*-

from odoo import models
from odoo.http import request
from odoo import http


class Website(models.Model):
    _inherit = 'website'

    def get_meta_tags(self, active_tags=False, pager=False, main_object=False):
        tag_names = ""
        tags = []
        meta_tags = {'title': '', 'meta_description': ''}
        active_url = http.request.httprequest.url
        title = ""
        print('passei aqui')
        print(active_tags)
        print(active_url)
        if active_tags:
            tags = self.env['blog.tag'].browse(active_tags)

        if '/tag/' in active_url:
            url_tags = active_url.split('tag/')[1].split(',')
            if not url_tags[0].isdigit():
                tags = url_tags

        if len(tags) > 0:
            for tag in tags:
                if not isinstance(tag, str):
                    tag_names += tag.name + ' '
                else:
                    tag_names += tag + ' '
        print(tag_names)
        if main_object and 'website_meta_title' in main_object:
            title = main_object.website_meta_title
            meta_tags['title'] = main_object.website_meta_title
            if pager and isinstance(main_object.website_meta_title, str):
                title = main_object.website_meta_title.split('|')
                print(title)
                if len(title) > 1:
                    title = '%s %s Page %s |%s' % (title[0], tag_names, pager['page']['num'], title[
                        1]) if main_object._name != 'blog.post' else '%s %s |%s' % (title[0], tag_names, title[1])
                    print(title)
                else:
                    title = '%s %s Page %s' % (title[0], tag_names, pager['page'][
                        'num']) if main_object._name != 'blog.post' else '%s %s' % (title[0], tag_names)

            elif pager and not isinstance(main_object.website_meta_title, str):
                title = 'OdoogapBlog %s Page %s | www.odoogap.com' % (tag_names, pager['page'][
                        'num']) if main_object._name != 'blog.post' else 'OdoogapBlog %s' % (tag_names)

            meta_tags['title'] = title


        if main_object and main_object.website_meta_description:
            meta_tags['meta_description'] = main_object.website_meta_description
            if pager and isinstance(main_object.website_meta_description, str):
                meta_description = '%s %s | Page %s' % (main_object.website_meta_description, tag_names, pager['page'][
                    'num']) if main_object._name != 'blog.post' else '%s %s' % (
                    main_object.website_meta_description, tag_names)
                meta_tags['meta_description'] = meta_description
        return meta_tags

    def active_tags_header(self, active_tags=False):
        tag_title = ""
        if active_tags:
            tags = self.env['blog.tag'].browse(active_tags)
            for tag in tags:
                tag_title += tag.name + ', '
            tag_title = self.last_occurence_rep(tag_title[:-2], ',', ' & ')
        return tag_title

    def last_occurence_rep(self, string, old, new):
        return (string[::-1].replace(old[::-1], new[::-1], 1))[::-1]
