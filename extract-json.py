#!/usr/bin/python3
import json
import pdftableextract as pdf
import datetime

PDF_FILE_NAME = "vertretungsplan.pdf"

class JsonObject:
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True, indent=4)

def extractCellsFromPdf(fname):
    pages = ["2"]
    cells = [pdf.process_page(PDF_FILE_NAME, p) for p in pages]

    # flatten the cells structure
    cells = [item for sublist in cells for item in sublist]
    cells = pdf.table_to_list(cells, pages)[2]

    return cells

def convertCellsToJson(cellsList, dlTime):
    json = JsonObject()
    json.lastUpdated = dlTime.strftime("%Y-%m-%dT%H:%M")
    json.data = []

    for i in range(0, len(cellsList)):
        cell = cellsList[i]

        # ignore cell if has not enough fields
        #                is header
        #                all fields are empty
        if len(cell) < 7 or "Pos" in cell[0] or cell[1:] == cell[:-1]:
            continue

        jObj = JsonObject()
        jObj.lesson = cell[0]; jObj.course = cell[1]; jObj.subject = cell[2]
        jObj.room = cell[3]; jObj.teacher = cell[4]; jObj.note = cell[5]
        jObj.type = cell[6]

        json.data.append(jObj)

    return json.toJSON()

def main():
    # get current time needed later for 'lastUpdated' in JSON
    dlTime = datetime.datetime.now()
    # extract JSON from pdf table
    cells = extractCellsFromPdf(PDF_FILE_NAME)
    # build json
    json = convertCellsToJson(cells, dlTime)
    outfile = open("vertretungsplan.json", "w")
    outfile.write(json)
    outfile.close

main()
