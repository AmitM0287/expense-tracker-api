import xlsxwriter
import io


def generateExcel(self, rawData):
		output = io.BytesIO()
		workbook = xlsxwriter.Workbook(output, {'in_memory': True})
		# Formattings / Stylings
		headerStyle = workbook.add_format({
			'bold'	: True,
			'align' : 'center'
		})
		infoKeyStyle = workbook.add_format({
			'bg_color' : '#f2efef'
		})
		infoValueStyle = workbook.add_format({
			'bold'	   : True,
			'bg_color' : '#f2efef',
			'align'	   : 'left',
			'text_wrap': True
		})
		# infoValueStyle.set_text_wrap()
		errorMessage = workbook.add_format({
			'bold'	   : True,
			'bg_color' : '#f2efef',
			'align'	   : 'center',
			'border'   : True
		})

		row = 1
		col = 1
		
		# Create sheet Containing RAW DATA
		worksheetData = workbook.add_worksheet("Data")

		# Creating Parameter Info Conatiner
		worksheetData.write(row, col, "Sites", infoKeyStyle)
		worksheetData.merge_range(row, col + 1, row, col + 4, str(["Site 1", "Site 1", "Site 1", "Site 1"]), infoValueStyle)
		row += 1
		worksheetData.write(row, col, "Start Time", infoKeyStyle)
		worksheetData.merge_range(row, col + 1, row, col + 4, "08-07-2024 (CT)", infoValueStyle)
		row += 1
		worksheetData.write(row, col,"End Time",infoKeyStyle)
		worksheetData.merge_range(row, col + 1, row, col + 4, "15-07-2024 (CT)", infoValueStyle)
		row += 2

		worksheetData.set_column(0, 0, 2)
		
		if len(rawData['data']) > 0:
			worksheetData.set_column(row, col, 22)
			worksheetData.write(row, col, "Sl No", headerStyle)

			worksheetData.set_column(row, col+1, 15)
			worksheetData.write(row, col+1, "Date", headerStyle)

			worksheetData.set_column(row, col+2, 60)
			worksheetData.write(row, col+2, "Activity", headerStyle)

			worksheetData.set_column(row, col+3, 28)
			worksheetData.write(row, col+3, "Site Name", headerStyle)

			worksheetData.set_column(row, col+4, 30)
			worksheetData.write(row, col+4, "Operator Name", headerStyle)

			worksheetData.set_column(row, col+5, 20)
			worksheetData.write(row, col+5, "Pressure", headerStyle)

			worksheetData.set_column(row, col+6, 20)
			worksheetData.write(row, col+6, "Pig Type", headerStyle)

			worksheetData.set_column(row, col+7, 20)
			worksheetData.write(row, col+7, "Abnormal Condition Present", headerStyle)
			row += 1

			for _colData in rawData['data']:
				worksheetData.write(row, col+1, _colData['sno'])
				worksheetData.write(row, col+2, _colData['dt'])
				worksheetData.write(row, col+3, _colData['act'])
				worksheetData.write(row, col+4, _colData['st'])
				worksheetData.write(row, col+5, _colData['on'])
				worksheetData.write(row, col+6, _colData['psi'])
				worksheetData.write(row, col+7, _colData['pt'])
				worksheetData.write(row, col+8, _colData['doa'])
				row += 1
		else:
			worksheetData.set_column(row , col + 1, 30)
			worksheetData.merge_range(row, col, row, col + 2, 'No Data Available', errorMessage)
		workbook.close()
		output.seek(0)
		return output.read()
