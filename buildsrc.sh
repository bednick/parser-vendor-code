#!/bin/sh
pyuic5 ui/main_window.ui   -o parser_vendor_code/ui/ui_main_window.py
pyuic5 ui/template.ui      -o parser_vendor_code/ui/ui_template.py
pyuic5 ui/template_item.ui -o parser_vendor_code/ui/ui_template_item.py
pyuic5 ui/templates.ui     -o parser_vendor_code/ui/ui_templates.py
