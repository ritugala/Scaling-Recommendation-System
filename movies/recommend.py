from movies import app
from flask import render_template
import pickle
from movies.model_selection import *
import pandas as pd
import numpy as np
import os
from surprise import dump

# resource_path = os.path.join(app.root_path, 'meow_tmp.csv')
# ratings_df = pd.read_csv(resource_path)
ratings_df = data_load()
#model_evaluation(ratings_df)
_, algo_SVD = dump.load(app.root_path+"/models/latest_model/SVDmodel")
_, algo_NMF = dump.load(app.root_path+"/models/latest_model/NMFmodel")

@app.route('/')
def home():
    return 'Hello! This is the main page'


@app.route('/recommend/<userid>')
def recommend(userid):
    #return str(userid)
    try:
        print("userid is",userid,"\n\n\n")
        uid = int(userid)
        if (uid >= 0 and uid <= 1000000):
            if uid%2==0:
                movie_recom = get_recommendations_for_users_new(ratings_df,uid,algo=algo_SVD, n=10)
            else:
                movie_recom = get_recommendations_for_users_new(ratings_df,uid, algo=algo_NMF, n=10)
            # print(movie_recom)
            recom_list = ','.join(movie_recom)
            #recom_list = ','.join(map(str, movie_recom))
            return recom_list
        else:
            return "UserId exceeded range"
    except ValueError:
        print("userid is",userid)
        return "Incorrect userid provided!"
