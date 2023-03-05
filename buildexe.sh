#!/bin/sh
pyinstaller --onefile --windowed  --name "ParserVendorCode" --add-data "sqlite;sqlite" --noconsole -y ParserVendorCode.py
