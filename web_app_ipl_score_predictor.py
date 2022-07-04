import streamlit as st
import numpy as np
import joblib


loaded_model = joblib.load('Trained_IPL_model_ridge_regression.sav')


def prediction(input_data):
    input_data_as_numpy_array=np.asarray(input_data)
    input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)
    predictions=loaded_model.predict(input_data_reshaped)
    return int(predictions[0])

def main():
    st.title('IPL score predictor')
    st.subheader('made by Keshava Krishna Srinivasan')

    teams=['Chennai Super Kings',
       'Delhi Capitals', 'Punjab Kings',
       'Kolkata Knight Riders', 'Mumbai Indians',
       'Rajasthan Royals', 'Royal Challengers Bangalore',
       'Sunrisers Hyderabad']

    batting_team=st.radio('Batting Team',teams)
    batting_vector=[]
    for i in teams:
        if i==batting_team:
            batting_vector.append(1)
        else:
            batting_vector.append(0)
    bowling_team=st.radio('Bowling Team',teams)
    bowling_vector=[]
    for i in teams:
        if i==bowling_team:
            bowling_vector.append(1)
        else:
            bowling_vector.append(0)


    all_stadiums=['Brabourne Stadium', 'Dubai International Cricket Stadium',
       'Eden Gardens', 'Feroz Shah Kotla',
       'Himachal Pradesh Cricket Association Stadium', 'Kingsmead',
       'M Chinnaswamy Stadium', 'MA Chidambaram Stadium, Chepauk',
       'Punjab Cricket Association IS Bindra Stadium, Mohali',
       'Punjab Cricket Association Stadium, Mohali',
       'Rajiv Gandhi International Stadium, Uppal',
       'Sardar Patel Stadium, Motera', 'Sawai Mansingh Stadium',
       'Sheikh Zayed Stadium', 'SuperSport Park',
       'Wankhede Stadium']
    stadium=st.radio('Specify the venue',all_stadiums)
    stadium_vector=[]

    for i in all_stadiums:
        if i==stadium:
            stadium_vector.append(1)
        else:
            stadium_vector.append(0)
    overs=st.slider('Number of overs that has been completed',min_value=5,max_value=19)
    runs=st.text_input('Runs scored')
    wickets=st.slider('Wickets lost',min_value=0,max_value=9)
    runs_5=st.text_input('Runs scored in the last 5 overs')
    wickets_5=st.slider('Wickets lost in the last 5 overs',min_value=0,max_value=9)
    scoreboard=[runs,wickets,overs,runs_5,wickets_5]

    data=scoreboard+stadium_vector+batting_vector+bowling_vector

    ans=''
    if st.button('Predict Score'):
        predict=prediction(data)
        ans='The predicted score at the end of 20 overs is: '+str(predict)


    st.success(ans)


if __name__=='__main__':
    main()
