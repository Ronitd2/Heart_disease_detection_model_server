import json
import pickle
import numpy as np
__data_columns=None
__model=None
__modelb=None

def get_disease_output(data):
    global __modelb
    with open("./artifacts/prediction_model.pickle",'rb') as f:
        __modelb=pickle.load(f)
        resultb= __modelb.predict([data])
        return resultb[0]
def get_disease_result(data):
    global __model
    with open("./artifacts/Detect_model.pickle",'rb') as f:
        __model=pickle.load(f)
        result= __model.predict([data])
        return result[0]
def get_col_names():
    global __data_columns
    global __model
    with open("./artifacts/columns.json",'r') as f:
        __data_columns=json.load(f)['data_columns']
        print(__data_columns)
    # with open("./artifacts/Detection_model.pickle",'rb') as f:
    #     __model=pickle.load(f)
if __name__=="__main__":
    print("Your Prediction is loading.....")
    # get_col_names()
    # data=np.zeros(len(__data_columns))
    # data[0]=56
    # data[1]=1
    # data[2]=3
    # data[3]=130
    # data[4]=400
    # data[5]=1
    # data[6]=2
    # data[7]=148
    # data[8]=0
    # data[9]=2.1
    # data[10]=2
    # data[11]=1
    # data[12]=7
    # print(get_disease_result(data))