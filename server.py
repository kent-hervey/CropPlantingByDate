from flask import Flask, render_template, request, redirect, session, flash, url_for
from datetime import *
from getCatalogFrAPI import make_catalog
import pytz

app = Flask(__name__)

@app.route('/plancrop')
def dateEntry(): #renders the date entry html template
    print("beginning of plancrop route")
    return render_template("start.html")

 
@app.route('/plancrop/success', methods=['POST'])
def success():
    print("beginning of success route")
    today = datetime.now(pytz.timezone('US/Central'))
    returned_begin_date=request.form['returnedBeginDate']
    returned_begin_date_wTZ=str(returned_begin_date+'--0600')
    returned_begin_date_obj=datetime.strptime(returned_begin_date_wTZ, '%Y-%m-%d-%z')
    print(returned_begin_date_obj)
    #returned_begin_date_obj=datetime.strptime(returned_begin_date + '--1000', '%Y-%m-%d-%z')    
    days_to_returned_begin_date =(returned_begin_date_obj - today).days
    output_begin_string1 = "Earliest first harvest date:  " + returned_begin_date + "  which is  " + str(days_to_returned_begin_date) + " days from now"
    print(output_begin_string1)

    returned_end_date=request.form['returnedEndDate']
    returned_end_date_obj=datetime.strptime(str(returned_end_date+'--0600'), '%Y-%m-%d-%z')
    days_to_returned_end_date =(returned_end_date_obj - today).days
    output_begin_string2 = "Latest first harvest date:  " + returned_end_date + "  which is  " + str(days_to_returned_end_date) + " days from now"


    catalog_result=make_catalog(days_to_returned_begin_date,days_to_returned_end_date)
    return render_template("success.html", returned_crops=catalog_result, beginString=output_begin_string1, endString=output_begin_string2)
    #return output_begin_string


if __name__ == "__main__":
    app.run(debug=True)




