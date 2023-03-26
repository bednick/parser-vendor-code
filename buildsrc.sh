#!/bin/sh
pyuic5 ui/directories.ui         -o parser_vendor_code/ui/ui_directories.py
pyuic5 ui/directory_update.ui    -o parser_vendor_code/ui/ui_directory_update.py
pyuic5 ui/main_window.ui         -o parser_vendor_code/ui/ui_main_window.py
pyuic5 ui/new_directory.ui       -o parser_vendor_code/ui/ui_new_directory.py
pyuic5 ui/new_directory_value.ui -o parser_vendor_code/ui/new_directory_value.py
pyuic5 ui/template.ui            -o parser_vendor_code/ui/ui_template.py
pyuic5 ui/template_item.ui       -o parser_vendor_code/ui/ui_template_item.py
pyuic5 ui/templates.ui           -o parser_vendor_code/ui/ui_templates.py
