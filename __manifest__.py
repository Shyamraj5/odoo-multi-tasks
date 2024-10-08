{
    'name': 'AIO',
    'version': '17.0.1.0',
    # 'summary': 'Automatically generate delivery orders and invoices on sale order confirmation',
    'author': 'shyamraj',
    'website': 'https://github.com/Shyamraj5',
    'category': 'Sales',
    'depends': ['sale','stock','base'],
    'data': [
             "security/ir.model.access.csv",
             "report/daily_sales_report_views.xml",
             "report/daily_sales_report.xml",
             "report/sale_report_header.xml",
             "data/email_scheduler.xml",
             "data/email_template.xml",
             "data/res_group.xml",
             'wizard/sale_report_wizard.xml',
             "views/sale_order.xml",
             "views/res_partner.xml",
             "views/res_config.xml",
             "views/menu.xml",
             ],
    'installable': True,
    'auto_install': False,
}
