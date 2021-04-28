import unittest

class FirstTest(charts.createData):

    def test_createData(mode):
        if mode == 1:
            pass
        else
            raise ValueError("Fail")


    
class SecondTest(charts.validate):

    def test_validate(date_info):
        if re.search(dateRegex, date_info):
            pass
        else
            raise ValueError("Fail")
        

class ThirdTest(charts.makeGraph):

    def test_makeGraph(data, chartType, chartTimeSeries, chartStartDate, chartEndDate):
         if chartStartDate == chartEndDate:
            pass
        else
            raise ValueError("Fail")
        

class FourthTest(charts.getJsonPage):

    def test_getJsonPage(info):
        if 'Invalid API call' not in req.text:
            pass
        else
            raise ValueError("Fail")
        

class FithTest(routes.stocks):

    def test_stocks():
        if request.method == 'POST':
            pass
        else
            raise ValueError("Fail") 


    
if _name_ == "_main_":
    unittest.main()

