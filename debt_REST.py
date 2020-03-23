from keras.models import load_model
import numpy as np
def g(x):
        max=0
        value=0;
        for j in range(0,2):
            if(x[j]>max):
                max=x[j]
                value=j
                
        return (value)

'''
Contains REST API to call model by taking inputs from bot/form
'''
from flask import Flask
import flask_restful
from flask_restful import Resource, Api
from flask_restful import reqparse
from flaskext.mysql import MySQL
from  flask import request

app = Flask(__name__)
api = Api(app)



class CreateUser(Resource):
    def post(self):
        try:
            # Parse the arguments
            #Take arguments from the form. 
            parser = reqparse.RequestParser()
            parser.add_argument('customer_id', type=str, help='Customers unique id')
            parser.add_argument('personal_id', type=str, help='Pesonal id of the customer')
            parser.add_argument('amount',type=str, help='Aisey hi ')
            parser.add_argument('interest',type=str,help='Interest of the user viz. car,house,etc.')
            parser.add_argument('years',type=str,help='Kitnay saal kay liye')
            parser.add_argument('verification',type=str,help='Verified or not')
            parser.add_argument('purpose',type=str,help='Car lena gaadi lena?')
            args = parser.parse_args()
            customer_id=args['customer_id']
            personal_id=args['personal_id']
            amount=args['amount']
            amount=float(amount)
            print("lll" +str(amount))
            interest=args['interest']
            purpose=interest
            duration=args['years']
            #duration=36
            verification = args['verification']
            #Argument taking part done.
            print("till here-2")
            #MySQL connectivity and execute query. 
            mysql1=MySQL()
            app.config['MYSQL_DATABASE_USER']='root'
            app.config['MYSQL_DATABASE_PASSWORD'] = ''
            app.config['MYSQL_DATABASE_DB'] = 'techm_db'
            app.config['MYSQL_DATABASE_HOST'] = 'localhost'
            app.config['MYSQL_DATABASE_PORT'] = 3306
            mysql1.init_app(app)
            conn=mysql1.connect()
            cursor=conn.cursor()
            cursor.execute("Select * from cust_banking where ind={}".format(str(customer_id)))
            row1=cursor.fetchall()
            cursor.execute("Select * from cust_personal where ind={}".format(str(personal_id)))
            row2=cursor.fetchall()
            #MySQL connectivity and query done.
            print("till here-1")
            #Seperate the tuple returned from the query in required fields.All the names of variables are in accordance with csv
            dti=row1[0][1]
            delinq_2yrs=row1[0][2]
            inq_last_6mths=row1[0][3]
            open_acc=row1[0][4]
            total_acc=row1[0][5]
            revol_bal=row1[0][6]
            revol_util=row1[0][7]
            fico_range_high=row1[0][8]
            fico_range_low=row1[0][9]
            fico_average=row1[0][10]

            emp_length=row2[0][1]
            annual_inc=row2[0][2]
            pub_rec=row2[0][3]
            home_ownership=row2[0][4]
            
            #calculate remaining values
            print("till here0")
            
            installment = float(amount) / float(duration)
            print("till here1")
            emp_len = -1
            if emp_length=="< 1 year":
                emp_len = 0
            elif emp_length=="1 year":
                emp_len = 1
            elif emp_length=="2 years":
                emp_len = 2
            elif emp_length=="3 years":
                emp_len = 3
            elif emp_length=="4 years":
                emp_len = 4
            elif emp_length=="5 years":
                emp_len = 5
            elif emp_length=="6 years":
                emp_len = 6
            elif emp_length=="7 years":
                emp_len = 7
            elif emp_length=="8 years":
                emp_len = 8
            elif emp_length=="9 years":
                emp_len = 9
            elif emp_length=="10+ years":
                emp_len = 10
            else:
                emp_len = -1
              
            verification_1 = 0
            verification_2 = 0
            verification_3 = 0
            if verification == 1:
                verification_1 = 1
            elif verification == 2:
                verification_2 = 1
            elif verification == 3:
                verification_3 = 1
                
            
            purpose_1 = 0
            purpose_2 = 0
            purpose_3 = 0
            purpose_4 = 0
            purpose_5 = 0
            purpose_6 = 0
            purpose_7 = 0
            purpose_8 = 0
            purpose_9 = 0
            purpose_10 = 0
            purpose_11 = 0
            purpose_12 = 0
            purpose_13 = 0
            purpose_14 = 0
            if purpose=="1":
                purpose_1 = 1
            elif purpose=="2":
                purpose_2 = 1
            elif purpose=="3":
                purpose_3 = 1
            elif purpose=="4":
                purpose_4 = 1
            elif purpose=="5":
                purpose_5 = 1
            elif purpose=="6":
                purpose_6 = 1
            elif purpose=="7":
                purpose_7 = 1
            elif purpose=="8":
                purpose_8 = 1
            elif purpose=="9":
                purpose_9 = 1
            elif purpose=="10":
                purpose_10 = 1
            elif purpose=="11":
                purpose_11 = 1
            elif purpose=="12":
                purpose_12 = 1
            elif purpose=="13":
                purpose_13 = 1
            elif purpose=="14":
                purpose_14 = 1
            
            print("till here2")
            home_ownership_1 = 0
            home_ownership_2 = 0
            home_ownership_3 = 0
            home_ownership_4 = 0
            home_ownership_5 = 0
            if home_ownership == "MORTGAGE":
                home_ownership_1 = 1
            elif home_ownership == "NONE":
                home_ownership_2 = 1
            elif home_ownership == "OTHER":
                home_ownership_3 = 1
            elif home_ownership == "OWN":
                home_ownership_4 = 1
            elif home_ownership == "RENT":
                home_ownership_5 = 1
            
            
            
            
            duration_36 = 0
            duration_60 = 0
            if duration==36:
                duration_36 = 1
            else:
                duration_60 = 1
            
            revol_util=revol_util[:len(revol_util)-1]
            revol_util=float(revol_util)
            print(revol_util)
            print("till here3")
            model = load_model('my_model_loan.h5')
            x= np.vstack([[float(amount), float(installment), float(emp_len), float(annual_inc), float(dti), float(delinq_2yrs), float(inq_last_6mths), float(open_acc),float(pub_rec),
                           float(revol_bal), float(revol_util),float( total_acc),float(fico_average),float( home_ownership_1), float(home_ownership_2), 
                           float(home_ownership_3),float( home_ownership_4),float( home_ownership_5), float(verification_1), float(verification_2),
                           float(verification_3),float( purpose_1),float( purpose_2),float( purpose_3),float( purpose_4), float(purpose_5),float( purpose_6),float( purpose_7),
                           float(purpose_8), float(purpose_9), float(purpose_10), float(purpose_11), float(purpose_12), float(purpose_13), float(purpose_14), float(duration_36),
                           float(duration_60)]])
            #x=np.vstack([[7200.0, 233.65, 5, 80000.0, 8.96, 0.0, 2.0, 6.0, 0.0, 3565.0,70.0, 1ss8.0, 707.0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0,0,0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0]])
            y=model.predict(x)
            p=2
            for i in range(0,len(y)):
                p=g(y[i])
            msg=""
            if p==1:
                msg="Loan accepted Congratulations"
            else:
                msg="Rejected"
            #If you receive this message then everything worked well and you are good to go.
            return {'message':msg}

        except Exception as e:
            return {'error': str(e)}

api.add_resource(CreateUser, '/CreateUser')

if __name__ == '__main__':
    app.run(debug=False)
