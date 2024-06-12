{ 
"name" : "Sanbe - Training",
"description" : "Latihan Teknik Odoo",
"author" : "Sanbe, PT. Arkana Solusi Digital",
"version" : "17.0.1.0.0",
"category" : "Others",
"license" : "OPL-1",
"depends" : [
             "base",
             "mail",
             "hr",
            ],
"data" : [
         "security/ir.model.access.csv",
         "views/planning_role_view.xml",
],
"auto_install" : False,
"installable" : True,
"application" : True,
"external_dependencies" : {"python" : []}
}