# Copyright (c) 2020, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt


import frappe
from frappe import _
from frappe.query_builder.functions import Concat_ws, Date


def execute(filters=None):
	columns, data = get_columns(), get_data(filters)
	return columns, data


def get_columns():
	columns = [
		{
			"label": _("Opportunity"),
			"fieldname": "name",
			"fieldtype": "Link",
			"options": "Opportunity",
			"width": 150,
		},
         {"fieldname": "naming_series", "label": _("Series"), "fieldtype": "Data", "width": 100},
		 {"fieldname": "sales_engineer", "label": _("Sales Engineer"), "fieldtype": "Data", "width": 100},
        {"fieldname": "in_date", "label": _("Opportunity In DateOpportunity In Date"), "fieldtype": "Date", "width": 100},
        {"fieldname": "status", "label": _("Status"), "fieldtype": "Data", "width": 100},
       
        {"fieldname": "customer", "label": _("Customer"), "fieldtype": "Data", "width": 100},
        {"fieldname": "project", "label": _("Project Cost Center"), "fieldtype": "Data", "width": 100},
		{"fieldname": "project_catogary", "label": _("Project Category"), "fieldtype": "Data", "width": 100},
        {"fieldname": "is_lcipl_approved", "label": _("Is LCIPL Approved"), "fieldtype": "Data", "width": 100},
        {"fieldname": "list_of_competitors", "label": _("List of Competitors"), "fieldtype": "Data", "width": 100},
         {"fieldname": "initial_quote_submitted_values", "label": _("Initial Quote Submitted Value"), "fieldtype": "Currency", "width": 100},
		 {"fieldname": "initial_quote_submitted_factor", "label": _("Initial Quote Submitted Factor"), "fieldtype": "Float", "width": 100},
         {"fieldname": "initial_quote_submitted_by", "label": _("Initial Quote Submitted By"), "fieldtype": "Data", "width": 100},
		{"fieldname": "opportunity_amount", "label": _("Opportunity Amount"), "fieldtype": "Currency", "width": 100},
        {"fieldname": "currency", "label": _("Currency"), "fieldtype": "Currency", "width": 100},
		
		{
			"label": _("Company"),
			"fieldname": "company",
			"fieldtype": "Link",
			"options": "Company",
			"width": 120,
		},
		
	]
	return columns


def get_data(filters):
	lead = frappe.qb.DocType("Opportunity")
	address = frappe.qb.DocType("Address")
	dynamic_link = frappe.qb.DocType("Dynamic Link")

	query = (
		frappe.qb.from_(lead)
		.left_join(dynamic_link)
		.on((lead.name == dynamic_link.link_name) & (dynamic_link.parenttype == "Address"))
		.left_join(address)
		.on(address.name == dynamic_link.parent)
		.select(
			lead.name,
			lead.naming_series,
            lead.sales_engineer,
            lead.in_date,
			lead.status,
            lead.customer_name,
            lead.project,
			lead.project_catogary,
            lead.is_lcipl_approved,
            lead.list_of_competitors,
            lead.initial_quote_submitted_values,
            lead.initial_quote_submitted_factor,
            lead.initial_quote_submitted_by,
            lead.opportunity_amount,
            lead.currency,    
			lead.company,
			
		)
		.where(lead.company == filters.company)
		.where(Date(lead.creation).between(filters.from_date, filters.to_date))
	)

	if filters.get("status"):
		query = query.where(lead.status == filters.get("status"))
	if filters.get("sales_engineer"):
		query = query.where(lead.sales_engineer == filters.get("sales_engineer"))
	if filters.get("initial_quote_submitted_by"):
		query = query.where(lead.initial_quote_submitted_by == filters.get("initial_quote_submitted_by"))
	if filters.get("naming_series"):
		query = query.where(lead.naming_series == filters.get("naming_series"))
	if filters.get("project_catogary"):
		query = query.where(lead.project_catogary == filters.get("project_catogary"))

	return query.run(as_dict=1)