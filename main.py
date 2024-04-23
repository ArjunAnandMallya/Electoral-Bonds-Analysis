from flask import Flask, redirect, url_for, request, Response, render_template,jsonify,json
from flask_mysqldb import MySQL
import plotly.graph_objects as go
print("HELLO WORLD")

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'tiger'
app.config['MYSQL_DB'] = 'elecbonds'

mysql = MySQL(app)

@app.route('/', methods = ["POST", "GET"])
def main_page():
    return render_template("index.html")


@app.route('/search', methods = ["POST", "GET"])
def searchmainpage():
    
    return render_template("search.html")
@app.route('/search/result',methods=["GET", "POST"])
def search():

        selected_column = request.form['search_column']
        search_term = request.form['search_term']
        if request.method == "POST":

            if selected_column and search_term:
                print(selected_column)
                cursor = mysql.connection.cursor()
                print(selected_column=="purchased.IssueBranchCode")
                if selected_column =="purchased.ReferenceNo" or  selected_column =="purchased.JournalDate"or selected_column == "purchased.DateofPurchase"or selected_column =="purchased.DateofExpiry" or selected_column =="purchased.NameofthePurchaser" or selected_column =="purchased.Prefix" or selected_column =="purchased.BondNumber"or selected_column =="purchased.Denominations"or selected_column =="purchased.IssueBranchCode" or selected_column =="purchased.IssueTeller":
                    cursor.execute(f"SELECT * FROM purchased WHERE {selected_column} = %s", (search_term,))
       

                    search_results = cursor.fetchall()
                    cursor.close()
                else:

                    cursor.execute(f"SELECT * FROM encashed WHERE {selected_column} = %s", (search_term,))
                    search_results = cursor.fetchall()
                    cursor.close()
                return render_template("search.html", search_results=search_results, selected_column=selected_column)
            
            
@app.route('/analyze')
def analyzemain():

                
    return render_template('analyze.html')

@app.route('/analyze/result', methods=['POST','GET'])
def analyze():
    political_party = request.form['political_party']

    if request.method == "POST":
        if political_party:
            cursor = mysql.connection.cursor()
            cursor.execute("SELECT YEAR(dateofencashment) AS year, COUNT(*) AS num_bonds, SUM(denominations) AS total_value FROM encashed WHERE nameofthepoliticalparty =%s GROUP BY YEAR(dateofencashment)", (political_party,))
            data = cursor.fetchall()
            cursor.close()

            years = []
            num_bonds = []
            total_value = []
            print("YO")
            print(data)

            for row in data:
                years.append(row[0])
                num_bonds.append(row[1])
                total_value.append(row[2])
            

            return render_template('analyze.html', years=years, num_bonds=num_bonds, total_value=total_value)
        else:

            return render_template('analyze.html')
@app.route('/company')
def analyzemain2():

                
    return render_template('company.html')


@app.route('/company/result', methods=['POST','GET'])
def analyzecompany():
    company = request.form['company']


    if request.method == "POST":
        if company:
            cursor = mysql.connection.cursor()
            cursor.execute("SELECT YEAR(dateofpurchase) AS year, COUNT(*) AS num_bonds, SUM(denominations) AS total_value FROM purchased WHERE nameofthepurchaser =%s GROUP BY YEAR(dateofpurchase)", (company,))
            data = cursor.fetchall()
            cursor.close()

            years = []
            num_bonds = []
            total_value = []
            print("YO")
            print(data)

            for row in data:
                years.append(row[0])
                num_bonds.append(row[1])
                total_value.append(row[2])
            

            return render_template('company.html', years=years, num_bonds=num_bonds, total_value=total_value)
    else:

        
        return render_template('company.html')

@app.route('/pi')
def pichart():

    cursor = mysql.connection.cursor()
    cursor.execute("SELECT nameofthepoliticalparty, sum(denominations) FROM encashed GROUP BY nameofthepoliticalparty")
    data = cursor.fetchall()
    cursor.close()

    political_parties = []
    denominations = []
    print(data)
    for row in data:
        political_parties.append(row[0])
        denominations.append(row[1])

    return render_template('pi.html', political_parties=political_parties, denominations=denominations)

@app.route('/alluvialparty')
def alluvialparty():
    return render_template("alluvialparty.html")
@app.route('/alluvialparty/result', methods=['POST','GET'])
def alluvialpartychart():
    alluvialpartydata = request.form['alluvialparty']
    if request.method == "POST":
        if alluvialpartydata:
            cursor = mysql.connection.cursor()
            cursor.execute("Select encashed.nameofthepoliticalparty, purchased.NameofthePurchaser, SUM(encashed.denominations) as total FROM encashed JOIN purchased ON encashed.Prefix = purchased.Prefix AND encashed.BondNumber = purchased.BondNumber where NameofthePoliticalParty = %s GROUP BY purchased.NameofthePurchaser", (alluvialpartydata,))
            query_data = cursor.fetchall()
            print(query_data)
            cursor.close()


            data = []
            
            for row in query_data:

                data.append({"from": row[0  ], "to": row[2], "value": row[1]})
            print(data)


            return render_template('alluvialparty.html', chart_data=json.dumps(data),query_data=query_data)


    else:
        return render_template('alluvialparty.html', data=None)

@app.route('/alluvialcompany')
def alluvialcompany():
    return render_template("alluvialcompany.html")
@app.route('/alluvialcompany/result', methods=['POST','GET'])
def alluvialcompanychart():
    alluvialcompanydata = request.form['alluvialcompany']
    if request.method == "POST":
        if alluvialcompanydata:
            cursor = mysql.connection.cursor()
            cursor.execute("SELECT nameofthepurchaser, NameofthePoliticalparty , SUM(purchased.denominations) as total FROM purchased JOIN encashed ON encashed.Prefix = purchased.Prefix AND encashed.BondNumber = purchased.BondNumber where nameofthepurchaser = %s GROUP BY NameofthePoliticalparty", (alluvialcompanydata,))
            query_data = cursor.fetchall()
            cursor.close()



            return render_template('alluvialcompany.html', chart_data=query_data,query_data=query_data)


    else:
        return render_template('alluvialcompany.html', data=None)



@app.route('/line-chart')
def line_chart():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT nameofthepurchaser, SUM(denominations) FROM purchased GROUP BY nameofthepurchaser;")
    data = cursor.fetchall()
    cursor.close()


    political_parties = [row[0] for row in data]
    total_denominations = [row[1] for row in data]


    chart_data = {
        "labels": political_parties,  
        "datasets": [{
            "label": "Total Denominations",
            "data": total_denominations,  
            "backgroundColor": "rgba(75, 192, 192, 0.2)",  
            "borderColor": "rgba(75, 192, 192, 1)",  
            "borderWidth": 1
        }]
    }


    return render_template('line_chart.html', chart_data=json.dumps(chart_data))


    

if __name__ == '__main__':
   app.run(host="0.0.0.0", port="80", debug = True) 
