from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Send Money & TT"),
			"items": [
				{
					"type": "doctype",
					"name": "Send Money",
					"description": _("Send Money."),
				},
				{
					"type": "doctype",
					"name": "Send TT",
					"description": _("Send TT."),
				},
			]
		},
		{
			"label": _("Received Money & TT"),
			"items": [
				{
					"type": "doctype",
					"name": "Received Money",
					"description": _("Received Money."),
				},
				{
					"type": "doctype",
					"name": "Received TT",
					"description": _("Received TT."),
				},
			]
		},
		{
			"label": _("Tellers"),
			"items": [
				{
					"type": "doctype",
					"name": "Teller Transfer",
					"description": _("Teller Transfer."),
				},
				{
					"type": "doctype",
					"name": "Transfer to Vault",
					"description": _("Transfer to Vault."),
				},
				{
					"type": "doctype",
					"name": "Transfer from Vault",
					"description": _("Transfer from Vault."),
				},
			]
		},
		{
			"label": _("Setup"),
			"items": [
				{
					"type": "doctype",
					"name": "Agents",
					"description": _("Agents."),
				},
				{
					"type": "doctype",
					"name": "Location",
					"description": _("Location."),
				},
				{
					"type": "doctype",
					"name": "Transfer from Bank to Vault",
					"description": _("Transfer from Bank to Vault."),
				},
			]
		},
		{
			"label": _("Reports"),
			"items": [
				{
					"type": "report",
					"is_query_report": True,
					"name": "Tellers Report",
					"doctype": "Send Money"
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Tellers Details Report",
					"doctype": "Send Money"
				},
			]
		},
		{
			"label": _("End of Day"),
			"items": [
				{
					"type": "doctype",
					"name": "EOD",
					"description": _("EOD."),
				},
			]
		},
	]
