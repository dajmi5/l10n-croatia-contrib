{
    "name": """Account reference: Poziv na broj""",
    "summary": """Add reference type: Poziv na broj""",
    "category": "Accounting",
    "images": [],
    "version": "16.0.1.0.0",
    "application": False,
    "author": "Ecodica ltd, Daj Mi 5",
    "licence": "AGPL-3",
    "depends": ["l10n_hr_account_base"],
    "data": [
        "views/account_journal_view.xml",
        "data/pnbr_default_property.xml",
        "views/report_invoice.xml",
    ],
    "demo": [],
    # "post_load": None,
    # "pre_init_hook": None,
    # "post_init_hook": None,
    "auto_install": False,
    "installable": True,
}