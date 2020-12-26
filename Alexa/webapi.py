from pycaret.classification import  load_model,predict_model
import streamlit as st
import pandas as pd
import plotly.express as px

import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings("ignore")




#Loading Model ,model is placed in my local directory where the code file is
model=load_model('final_model')

def predict(model ,input_df):
    predictions_df=predict_model(estimator=model,data=input_df)
    predictions=predictions_df['Label'][0]
    return predictions

def run_app():
    from PIL import Image
    image=Image.open('diabetes_img.JPG')
    st.image(image,use_column_width=True)
    add_selectbox=st.sidebar.selectbox("How would you like to predict diabetes?",("In Person","Batch"))

    st.sidebar.info('This application is developed by Siddhesh D. Munagekar to predict diabetes')


    if add_selectbox=='In Person':
        pregnancies=st.number_input('Pregnancies',min_value=0,max_value=17,value=5)
        glucose=st.number_input('glucose',min_value=0,max_value=200,value=100)
        blood_pressure=st.number_input('blood_pressure',min_value=0,max_value=122,value=25)
        skin_thickness=st.number_input('skin_thickness',min_value=0,max_value=110,value=60)
        insulin=st.number_input('insulin',min_value=0,max_value=744,value=500)
        bmi=st.number_input('bmi',min_value=0.0,max_value=90.0,value=15.5)
        db_pedigree_fun=st.number_input('pedigree_value',min_value=0.000,max_value=2.420,value=1.000)
        age=st.number_input('Age',min_value=1,max_value=100,value=25)



        input_dict={'Pregnancies':pregnancies,'Glucose':glucose,'BloodPressure':blood_pressure,
                    'SkinThickness':skin_thickness,'Insulin':insulin,'BMI':bmi ,'DiabetesPedigreeFunction':db_pedigree_fun,'Age':age }

        ##pass dictionary in the form of list to DataFrame function.
        input_df=pd.DataFrame([input_dict])





        if st.button("Predict Diabetes"):
            output=int(predict(model=model,input_df=input_df))

            if output==0:
                st.success("Congratulations !! you don't have Diabetes :)")

            else:
                st.warning('You are diabetic .Please take care')






    if add_selectbox == 'Batch':
        file_uploader=st.file_uploader("Upload diabetes .csv file for prediction",type=["csv"])
        st.info("If you don't have file ,please download it from this link:https://www.kaggle.com/johndasilva/diabetes")

        if file_uploader is not None:
            data=pd.read_csv(file_uploader)

            predictions=predict_model(estimator=model,data=data)
            st.write(predictions)

            if st.checkbox('Visualize data'):
                visual=st.selectbox('Please select the visual from the dropdown',['Count Plot','Correlation Matrix','Glucose vs Diabetes','Custom Plot',
                                                                                  'Feature Distribution'])
                data=pd.DataFrame(data)


                if visual =='Glucose vs Diabetes':
                    fig=plt.figure()
                    barplot = sns.barplot(data['Outcome'], data['Glucose'], ci=None,edgecolor='Black')
                    barplot.set(xlabel='Diabetes', ylabel='Glucose')
                    for p in barplot.patches:
                        barplot.annotate(format(p.get_height(), '.2f'),
                                       (p.get_x() + p.get_width() / 2., p.get_height()),
                                       ha='center', va='center', xytext=(0,-15), textcoords='offset points')
                    plt.title("Average glucose level between Diabetic and Non Diabetic patients")
                    st.pyplot(fig)

                if visual =='Count Plot':
                    fig = plt.figure()
                    pie_plot = data['Outcome'].value_counts().plot.pie(explode=[0, 0.1],autopct="%1.1f%%",shadow=True)
                    plt.title('Count of Diabetic (1) and Non Diabetics (0) in a file')
                    st.write(pie_plot)
                    st.pyplot(fig)

                if visual=='Correlation Matrix':
                    fig = plt.figure()
                    corrMatrix=data.corr()
                    sns.heatmap(corrMatrix,annot=True)
                    st.pyplot(fig)

                if visual=='Feature Distribution':
                    fig, ax = plt.subplots(4, 2, figsize=(17, 17))
                    sns.distplot(data.Age, bins=20, ax=ax[0, 0], color='r', kde=True)
                    sns.distplot(data.Pregnancies, bins=20, ax=ax[0, 1], color='b')
                    sns.distplot(data.Glucose, bins=20, ax=ax[1, 0], color='g')
                    sns.distplot(data.BloodPressure, bins=20, ax=ax[1, 1], color='y')
                    sns.distplot(data.SkinThickness, bins=20, ax=ax[2, 0], color='pink')
                    sns.distplot(data.Insulin, bins=20, ax=ax[2, 1], color='orange')
                    sns.distplot(data.DiabetesPedigreeFunction, bins=20, ax=ax[3, 0], color='violet')
                    sns.distplot(data.BMI, bins=20, ax=ax[3, 1], color='black')
                    st.pyplot(fig)

                if visual=='Custom Plot':
                    column_list=data.columns
                    x=st.selectbox("Select x variable",column_list)
                    y=st.selectbox("Select y variable",column_list)
                    if x !=y:
                        fig=px.scatter(data,x=x,y=y, trendline="ols",title="Relationship of "+x + "with"+y,color='Outcome')
                        st.plotly_chart(fig)
                    else:
                        st.info("To find relationship x and y should not be same. Please select different features in X and Y")



if __name__=='__main__':
    run_app()


