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
		},{
			"fieldname":"sales_engineer",
			"label": __("Sales Engineer"),
			"fieldtype": "Select",
			options: [
				{ "value": "Sundharavel", "label": __("Sundharavel") },
				{ "value": "Akshay", "label": __("Akshay") },
				{ "value": "Pradeep", "label": __("Pradeep") },
				{ "value": "Ashok", "label": __("Ashok") },
				{ "value": "Others", "label": __("Others") },
				
			],
		},
		{
			"fieldname":"initial_quote_submitted_by",
			"label": __("Initial Quote Submitted By"),
			"fieldtype": "Select",
			options: [
				{ "value": "Melvin", "label": __("Melvin") },
				{ "value": "Kavin", "label": __("Kavin") },
				{ "value": "Vishal", "label": __("Vishal") },
				{ "value": "Niveditha", "label": __("Niveditha") },
				{ "value": "Pradeep", "label": __("Pradeep") },
				{ "value": "Akshay", "label": __("Akshay") },
				{ "value": "Sushma", "label": __("Sushma") },
				
			],
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
		},
		{
			"fieldname":"naming_series",
			"label": __("Series"),
			"fieldtype": "Select",
			options: [
				{ "value": "QTN/2324", "label": __("QTN/2324") },
				{ "value": "SQTN/2324", "label": __("SQTN/2324") },
				
				
			],
		},
		{
			"fieldname":"project_catogary",
			"label": __("Project Category"),
			"fieldtype": "Select",
			options: [
				{ "value": "A", "label": __("A") },
				{ "value": "B", "label": __("B") },
				{ "value": "C", "label": __("C") },
				{ "value": "Others", "label": __("Others") },
			
				
			],
		}
	]
};