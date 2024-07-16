import time
import io
from datetime import datetime

from utils.logger import Logger

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
import xlsxwriter


class UserInvestments(APIView):
	''' This API is used to fetch Investments details '''
	def get(self, request, format=None):
		API_PROCESSING_TIME = time.time()
		API_STATUS  = None
		API_MESSAGE = ''
		DATA = {}
		try:
			API_STATUS  = status.HTTP_200_OK
			API_MESSAGE = 'Investments data retrieved successfully!'
			DATA = dict(request.data)
		except Exception as exc:
			Logger._ref._logError(exc)
			API_MESSAGE = str(exc)
			API_STATUS = status.HTTP_500_INTERNAL_SERVER_ERROR
		# calculate the processing time in milliseconds
		API_PROCESSING_TIME = int((time.time() - API_PROCESSING_TIME) * 1000)
		# log the processing time, message, and status
		Logger._ref._logInfo(API_PROCESSING_TIME, API_MESSAGE, API_STATUS)
		return Response({
			'processingTime': API_PROCESSING_TIME,
			'status' : API_STATUS,
			'message': API_MESSAGE,
			'data'	 : DATA
		}, status=API_STATUS)


class UserSavings(APIView):
	''' This API is used to fetch savings details '''
	def get(self, request, format=None):
		API_PROCESSING_TIME = time.time()
		API_STATUS  = None
		API_MESSAGE = ''
		DATA = {}
		try:
			API_STATUS  = status.HTTP_200_OK
			API_MESSAGE = 'Savings data retrieved successfully!'
			DATA = dict(request.data)
		except Exception as exc:
			Logger._ref._logError(exc)
			API_MESSAGE = str(exc)
			API_STATUS = status.HTTP_500_INTERNAL_SERVER_ERROR
		# calculate the processing time in milliseconds
		API_PROCESSING_TIME = int((time.time() - API_PROCESSING_TIME) * 1000)
		# log the processing time, message, and status
		Logger._ref._logInfo(API_PROCESSING_TIME, API_MESSAGE, API_STATUS)
		return Response({
			'processingTime': API_PROCESSING_TIME,
			'status' : API_STATUS,
			'message': API_MESSAGE,
			'data'	 : DATA
		}, status=API_STATUS)


class UserExpences(APIView):
	''' This API is used to fetch expenses details '''
	def get(self, request, format=None):
		API_PROCESSING_TIME = time.time()
		API_STATUS  = None
		API_MESSAGE = ''
		DATA = {}
		try:
			API_STATUS  = status.HTTP_200_OK
			API_MESSAGE = 'Expences data retrieved successfully!'
			DATA = dict(request.data)
		except Exception as exc:
			Logger._ref._logError(exc)
			API_MESSAGE = str(exc)
			API_STATUS = status.HTTP_500_INTERNAL_SERVER_ERROR
		# calculate the processing time in milliseconds
		API_PROCESSING_TIME = int((time.time() - API_PROCESSING_TIME) * 1000)
		# log the processing time, message, and status
		Logger._ref._logInfo(API_PROCESSING_TIME, API_MESSAGE, API_STATUS)
		return Response({
			'processingTime': API_PROCESSING_TIME,
			'status' : API_STATUS,
			'message': API_MESSAGE,
			'data'	 : DATA
		}, status=API_STATUS)


class DownloadExcel(APIView):
	''' This API is used to download finance data '''
	def post(self, request, format=None):
		API_PROCESSING_TIME = time.time()
		API_STATUS  = None
		API_MESSAGE = ''
		DATA = {}
		try:
			API_STATUS  = status.HTTP_200_OK
			API_MESSAGE = 'Expences data retrieved successfully!'
			DATA = dict(request.data)
			excelFile = self.fetchExcelData(options={})
			return HttpResponse(excelFile, content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
		except Exception as exc:
			Logger._ref._logError(exc)
			API_MESSAGE = str(exc)
			API_STATUS = status.HTTP_500_INTERNAL_SERVER_ERROR
		# calculate the processing time in milliseconds
		API_PROCESSING_TIME = int((time.time() - API_PROCESSING_TIME) * 1000)
		# log the processing time, message, and status
		Logger._ref._logInfo(API_PROCESSING_TIME, API_MESSAGE, API_STATUS)
		return Response({
			'processingTime': API_PROCESSING_TIME,
			'status' : API_STATUS,
			'message': API_MESSAGE,
			'data'	 : DATA
		}, status=API_STATUS)
	
	def fetchExcelData(self, options):
		options = {
			'rawData': True,
			'graphData': True
		}
		excelFile = self.generateExcel(options)
		return excelFile
	
	def generateExcel(self, options):
		buffer = io.BytesIO()
		workbook = xlsxwriter.Workbook(buffer, {'in_memory': True})
		
		# Stylings
		headerStyle = workbook.add_format({
			'bold'	: True,
			'align' : 'center'
		})
		keyStyle = workbook.add_format({
			'bg_color' : '#f2efef'
		})
		valueStyle = workbook.add_format({
			'bold'	   : True,
			'bg_color' : '#f2efef',
			'align'	   : 'left',
			'text_wrap': True
		})
		errorMessage = workbook.add_format({
			'bold'	   : True,
			'bg_color' : '#f2efef',
			'align'	   : 'center',
			'border'   : True
		})

		# Raw data option
		if options['rawData']:
			# Raw data
			rawData = {
				'data': {},
				'mapping': {}
			}
		
			row = 1
			col = 1
			
			worksheetData = workbook.add_worksheet("Data")

			worksheetData.write(row, col, "Test", keyStyle)
			worksheetData.merge_range(row, col + 1, row, col+4, '{}'.format('x, y, z'), valueStyle)
			row += 1
			worksheetData.write(row, col, "Start", keyStyle)
			worksheetData.merge_range(row, col + 1, row, col+4, '{}'.format(datetime.fromtimestamp(17237894930023/1000).strftime("%Y/%m/%d %H:%M:%S")), valueStyle)
			row += 1
			worksheetData.write(row, col,"End",keyStyle)
			worksheetData.merge_range(row, col + 1, row, col+4, '{} {}'.format(datetime.fromtimestamp(17237894930023/1000).strftime("%Y/%m/%d %H:%M:%S")), valueStyle)
			row += 2
			
			worksheetData.set_column(0, 0, 2)
			
			if len(rawData['data']) > 0:
				worksheetData.set_column(row, col, 10)
				worksheetData.write(row, col, "x1", headerStyle)

				worksheetData.set_column(row, col+1, 20)
				worksheetData.write(row, col+1, "x2", headerStyle)

				worksheetData.set_column(row, col+2, 20)
				worksheetData.write(row, col+2, "x3", headerStyle)

				worksheetData.set_column(row, col+3, 20)
				worksheetData.write(row, col+3, "x4", headerStyle)

				worksheetData.set_column(row, col+4, 20)
				worksheetData.write(row, col+4, "x6", headerStyle)

				worksheetData.set_column(row, col+5, 20)
				worksheetData.write(row, col+5, "x7", headerStyle)

				worksheetData.set_column(row, col+6, 20)
				worksheetData.write(row, col+6, "x8", headerStyle)

				worksheetData.set_column(row, col+7, 30)
				worksheetData.write(row, col+7, "x9", headerStyle)
				row += 1

				for _colData in rawData['data']:
					worksheetData.write(row, col, _colData['y1'])
					worksheetData.write(row, col+1, _colData['y2'])
					worksheetData.write(row, col+2, rawData['mapping']['y1'][_colData['y2']]) 
					worksheetData.write(row, col+3, rawData['mapping']['y1'][_colData['y2']])
					row += 1
			else:
				worksheetData.set_column(row , col + 1, 30)
				worksheetData.merge_range(row, col, row, col + 2, 'No Data Available', errorMessage)
		
		# Graph Option
		if options['graphData']:
			# Chart data
			graphData = {
				'data': {}
			}

			# Create sheet Containing Graph DATA
			worksheetGraph = workbook.add_worksheet("Graph")

			if len(graphData['data']) > 0:
				# Intermediate chart data
				worksheetIntermediateData = workbook.add_worksheet("IntermediateSheet")

				# Intermediate data : chart1
				headings = ["a", "b", "c", "d"]
				worksheetIntermediateData.write_row("A1", headings, headerStyle)
				worksheetIntermediateData.write_column("A2", graphData['data']['chart1']['categories'])
				worksheetIntermediateData.write_column("B2", graphData['data']['chart1']['xy'])
				worksheetIntermediateData.write_column("C2", graphData['data']['chart1']['xy'])

				# Intermediate data : chart2
				headings = ["a", "b", "c"]
				worksheetIntermediateData.write_row("E1", headings, headerStyle)
				worksheetIntermediateData.write_column("E2", graphData['data']['chart2']['categories'])
				worksheetIntermediateData.write_column("F2", graphData['data']['chart2']['xy'])
				worksheetIntermediateData.write_column("G2", graphData['data']['chart2']['xy'])

				# Intermediate data : chart3
				headings = ["a", "b", "c", "d", "e"]
				worksheetIntermediateData.write_row("I1", headings, headerStyle)
				worksheetIntermediateData.write_column("I2", graphData['data']['chart3']['categories'])
				worksheetIntermediateData.write_column("J2", graphData['data']['chart3']['xy'])
				worksheetIntermediateData.write_column("K2", graphData['data']['chart3']['xy'])
				worksheetIntermediateData.write_column("L2", graphData['data']['chart3']['xy'])
				worksheetIntermediateData.write_column("M2", graphData['data']['chart3']['xy'])

				# Plot chart1
				chart1 = workbook.add_chart({"type": "column"})
				chart1.add_series({
					"name"		: "=IntermediateSheet!$B$1",
					"categories": "=IntermediateSheet!$A$2:$A${}".format(len(graphData['data']['chart1']['categories'])+1),
					"values"	: "=IntermediateSheet!$B$2:$B${}".format(len(graphData['data']['chart1']['xy'])+1),
					"fill"		: { "color": "#ffb366" }
				})
				chart1.add_series({
					"name"		: "=IntermediateSheet!$C$1",
					"categories": "=IntermediateSheet!$A$2:$A${}".format(len(graphData['data']['chart1']['categories'])+1),
					"values"	: "=IntermediateSheet!$C$2:$C${}".format(len(graphData['data']['chart1']['xy'])+1),
					"fill"		: { "color": "#a5c90f" }
				})
				chart1.set_title({
					"name"	   : "xyxyxy",
					"name_font": {
						"color": "#808080"
					}
				})
				chart1.set_y_axis({"name": "Count"})
				chart1.set_legend({"position": "bottom"})
				chart1.set_style(11)
				chart1.set_size({'width': 665, 'height': 380})

				# Plot chart2
				chart2 = workbook.add_chart({"type": "column"})
				chart2.add_series({
					"name"		: "=IntermediateSheet!$F$1",
					"categories": "=IntermediateSheet!$E$2:$E${}".format(len(graphData['data']['chart2']['categories'])+1),
					"values"	: "=IntermediateSheet!$F$2:$F${}".format(len(graphData['data']['chart2']['xy'])+1),
					"fill"		: { "color": "#ffb366" }
				})
				chart2.add_series({
					"name"		: "=IntermediateSheet!$G$1",
					"categories": "=IntermediateSheet!$E$2:$E${}".format(len(graphData['data']['chart2']['categories'])+1),
					"values"	: "=IntermediateSheet!$G$2:$G${}".format(len(graphData['data']['chart2']['xy'])+1),
					"fill"		: { "color": "#a5c90f" }
				})
				chart2.set_title({
					"name"	   : "xyxy",
					"name_font": {
						"color": "#808080"
					}
				})
				chart2.set_y_axis({"name": "Count"})
				chart2.set_legend({"position": "bottom"})
				chart2.set_style(11)
				chart2.set_size({'width': 665, 'height': 380})

				# Plot chart3
				chart3 = workbook.add_chart({"type": "column"})
				chart3.add_series({
					"name"		: "=IntermediateSheet!$J$1",
					"categories": "=IntermediateSheet!$I$2:$I${}".format(len(graphData['data']['chart3']['categories'])+1),
					"values"	: "=IntermediateSheet!$J$2:$J${}".format(len(graphData['data']['chart3']['xy'])+1),
					"fill"		: { "color": "#ffb366" }
				})
				chart3.add_series({
					"name"		: "=IntermediateSheet!$K$1",
					"categories": "=IntermediateSheet!$I$2:$I${}".format(len(graphData['data']['chart3']['categories'])+1),
					"values"	: "=IntermediateSheet!$K$2:$K${}".format(len(graphData['data']['chart3']['xy'])+1),
					"fill"		: { "color": "#a5c90f" }
				})
				lineChart = workbook.add_chart({"type": "line"})
				lineChart.add_series({
					"name"		: "=IntermediateSheet!$L$1",
					"categories": "=IntermediateSheet!$I$2:$I${}".format(len(graphData['data']['chart3']['categories'])+1),
					"values"	: "=IntermediateSheet!$L$2:$L${}".format(len(graphData['data']['chart3']['xy'])+1),
					"y2_axis"	: True,
					"line"		: { "color": "#ffb366" }
				})
				lineChart.add_series({
					"name"		: "=IntermediateSheet!$M$1",
					"categories": "=IntermediateSheet!$I$2:$I${}".format(len(graphData['data']['chart3']['categories'])+1),
					"values"	: "=IntermediateSheet!$M$2:$M${}".format(len(graphData['data']['chart3']['xy'])+1),
					"y2_axis"	: True,
					"line"		: { "color": "#a5c90f" }
				})
				lineChart.set_y2_axis({"name": "Pressure (psi)"})
				lineChart.set_legend({"position": "bottom"})

				chart3.combine(lineChart)
				chart3.set_title({
					"name"	   : "gdhhd",
					"name_font": {
						"color": "#808080"
					}
				})
				chart3.set_y_axis({"name": "Count"})
				chart3.set_legend({"position": "bottom"})
				chart3.set_style(11)
				chart3.set_size({'width': 1350, 'height': 380})

				# Insert charts into the worksheet
				worksheetGraph.insert_chart("B2", chart1, { "x_offset": 20, "y_offset": 10 })
				worksheetGraph.insert_chart("M2", chart2, { "x_offset": 20, "y_offset": 10 })
				worksheetGraph.insert_chart("B24", chart3, { "x_offset": 20, "y_offset": 10 })

				# Hide the IntermediateData sheet
				worksheetIntermediateData.hide()
			else:
				worksheetGraph.set_column(1 , 2, 30)
				worksheetGraph.merge_range(1, 1, 1, 3, 'No Data Available', errorMessage)
		
		workbook.close()
		buffer.seek(0)
		return buffer.read()

