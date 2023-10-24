frappe.query_reports["Enquiry Status Report"] = {
	"filters": [
		{
			"fieldname":"company",
			"label": __("Company"),
			"fieldtype": "Link",
			"options": "Company",
			"default": frappe.defaults.get_user_default("Company"),
			"reqd": 1
		},
		{
			"fieldname":"from_date",
			"label": __("From Date"),
			"fieldtype": "Date",
			"default": frappe.datetime.add_months(frappe.datetime.get_today(), -12),
			"reqd": 1
		},
		{
			"fieldname":"to_date",
			"label": __("To Date"),
			"fieldtype": "Date",
			"default": frappe.datetime.get_today(),
			"reqd": 1
		},
		{
			"fieldname":"status",
			"label": __("Status"),
			"fieldtype": "Select",
			options: [
				{ "value": "Regret", "label": __("Regret") },
				{ "value": "Under Hold", "label": __("Under Hold") },
				{ "value": "Won", "label": __("Won") },
				{ "value": "Qualification", "label": __("Qualification") },
				{ "value": "Qualified", "label": __("Qualified") },
				{ "value": "Quotation", "label": __("Quotation") },
				{ "value": "Closed", "label": __("Closed") },
				{ "value": "Lost", "label": __("Lost") },
				
			],
		}
	]
};