#!/bin/bash
# Depends on https://github.com/ashima/pdf-table-extract and curl

. ./html_template.sh

export PDF_FILE_NAME="vertretungsplan.pdf"
export HTML_FILE_NAME="vertretungsplan-table.html"

# extract table from pdf
pdf-table-extract -i $PDF_FILE_NAME -t table_html -p 2 -o $HTML_FILE_NAME

# Replace some strings to be easier to understand
sed -i s/"VLehrer Kürzel"/"Vertretungslehrer (Kürzel)"/g $HTML_FILE_NAME
sed -i s/"Pos"/"Stunde"/g $HTML_FILE_NAME

# Correct spelling misstakes
sed -i s/"Fällt"/"fällt"/g $HTML_FILE_NAME

# Vertretungsplan
export HTML=$(cat $HTML_FILE_NAME)
export GENTIME=$(TZ='Europe/Berlin' date)
export TITLE=Vertretungsplan
export TARGET=vertretungsplan.html
export SOURCE=https://gho.berlin/wp-content/frei_stunden/VPS.pdf
gen_from_html_template

rm $HTML_FILE_NAME
