#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/1/2 上午11:36
# @Author  : herbiel8800@gmail.com
# @Site    : 
# @File    : excel.py
# @Software: PyCharm
import xadmin
from xadmin.views import BaseAdminPlugin, ListAdminView
from django.template import loader
from xadmin.plugins.utils import get_context_dict


# excel 导入
class ListImportExcelPlugin(BaseAdminPlugin):
    import_excel = False

    def init_request(self, *args, **kwargs):
        return bool(self.import_excel)

    def block_top_toolbar(self, context, nodes):
       context = get_context_dict(context or {})
       nodes.append(loader.render_to_string('xadmin/excel/model_list.top_toolbar.import.html',context=context))


xadmin.site.register_plugin(ListImportExcelPlugin, ListAdminView)
