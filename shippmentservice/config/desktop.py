# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"module_name": "ShippmentService-PGL",
			"category":"Modules",
			"color": "#1abc9c",
			"icon": "octicon octicon-tag",
			"type": "module",
			"label": _("ShippmentService_PGL"),
			"description":"Peace Global Logistic Service."
		},

		{
			"module_name": "testModule",
			"category":"Modules",
			"color": "#1abc9c",
			"icon": "octicon octicon-tag",
			"type": "module",
			"label": _("testModule"),
			"description":"desk top icons test run."
		}


	]
