#!/bin/bash
# Depends on https://github.com/ashima/pdf-table-extract and curl

. ./html_template.sh

export PDF_FILE_NAME="vertretungsplan.pdf"

# extract table from pdf
pdf-table-extract -i vertretungsplan.pdf -t table_html -p 2 -o vertretungsplan-table.html

# Replace some strings to be easier to understand
sed -i s/"VLehrer Kürzel"/"Vertretungslehrer (Kürzel)"/g vertretungsplan-table.html
sed -i s/"Pos"/"Stunde"/g vertretungsplan-table.html

# Correct spelling misstakes
sed -i s/"Fällt"/"fällt"/g vertretungsplan-table.html

# Vertretungsplan
export HTML=$(cat vertretungsplan-table.html)
export GENTIME=$(TZ='Europe/Berlin' date)
export TITLE=Vertretungsplan
export TARGET=vertretungsplan.html
export SOURCE=https://gho.berlin/wp-content/frei_stunden/VPS.pdf
gen_from_html_template

rm vertretungsplan-table.html
