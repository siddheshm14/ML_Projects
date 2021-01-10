import streamlit as st
from PIL import Image

import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
#from sklearn.cluster import KMeans

###Loading KMeans Clustering Model######
model1=pickle.load(open('Kmeans_cluster.pkl','rb'))







def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def remote_css(url):
    st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)

def icon(icon_name):
    st.markdown(f'<i class="material-icons">{icon_name}</i>', unsafe_allow_html=True)

local_css("style.css")
remote_css('https://fonts.googleapis.com/icon?family=Material+Icons')

side_image=Image.open('Home_depot_icon.JPG')
st.sidebar.image(side_image,use_column_width=True)

image=Image.open('home_depot.JPG')
st.image(image,use_column_width=True)
icon("search")
st.sidebar.info("Example search like :bulb, cutting tool , sink")
st.sidebar.info("This Application is developed by Siddhesh D. Munagekar for recommended search in order to maximize sales in Home Depot")

placeholder = st.empty()
placeholder.text("What can we help you find?")

searched_object = st.text_input("")


#Loading Dataset


joined_df= pd.read_csv('C:\\Users\\siddh\\PycharmProjects\\pythonProject\\Searchengine\\joined_prod_title_and_Prod_des.csv',
                       encoding= 'unicode_escape')
joined_df=joined_df.dropna()



def run():
    ##Loading cleaned corpus file
    corpus = []

    # open file and read the content in a list
    with open('corpus.txt', 'r') as filehandle:
        for line in filehandle:
            # remove linebreak which is the last character of the string
            currentPlace = line[:-1]

            # add item to the list
            corpus.append(currentPlace)

    #print(corpus)



    ####Feature extraction from Product Description usinng tfidf######
    vectorizer=TfidfVectorizer(stop_words='english',analyzer='word',max_features=500)

    X=vectorizer.fit_transform(corpus)




    ###Creating  a function to print clusters

    def print_cluster(i):
        cluster_list=[]

        print("Cluster %d:"% i)
        for ind in ordered_centroids[i,:10]:
            print(' %s' % terms[ind])
            cluster_list.append(terms[ind])

        #print('Cluster List',cluster_list)
        return cluster_list


    k_value=10
    print("Top 10 search per clusters :")
    ordered_centroids=model1.cluster_centers_.argsort()[:,::-1]
    #print('ordered_centroids',ordered_centroids.shape)
    terms=vectorizer.get_feature_names()

    for i in range(k_value):
        print_cluster(i)

########Selecting the the cluster from the group based on user search#######

    def selected_cluster(i):
        cluster = []
        cluster.clear()
        print("Cluster %d:" % i)
        for ind in ordered_centroids[i, :10]:
            print(' %s' % terms[ind])
            cluster.append(terms[ind])
        return cluster

    def show_recommendations(product):
        Y = vectorizer.transform([product])
        prediction = model1.predict(Y)
        cluster = selected_cluster(prediction[0])
        return cluster




    if st.checkbox("Search"):

        domain   = show_recommendations(searched_object)
        choice=st.radio("Select your preference",domain)


        if domain.index(choice)==0:
            new_df = joined_df[joined_df['product_title'].str.contains(choice, regex=False, case=False, na=False)]
            products = new_df['product_title'].unique()
            df = pd.DataFrame(products[:10])
            df.rename({0: "Featuring top 10 trending Products"}, axis=1, inplace=True)
            st.table(df)

        if domain.index(choice)==1:
            new_df = joined_df[joined_df['product_title'].str.contains(choice, regex=False, case=False, na=False)]
            products = new_df['product_title'].unique()
            df = pd.DataFrame(products[:10])
            df.rename({0: "Featuring top 10 trending Products"}, axis=1, inplace=True)
            st.table(df)

        if domain.index(choice)==2:
            new_df=joined_df[joined_df['product_title'].str.contains(choice,regex=False,case=False,na=False)]
            products=new_df['product_title'].unique()
            df = pd.DataFrame(products[:10])
            df.rename({0: "Featuring top 10 trending Products"}, axis=1, inplace=True)
            st.table(df)

        if domain.index(choice)==3:
            new_df=joined_df[joined_df['product_title'].str.contains(choice,regex=False,case=False,na=False)]
            products=new_df['product_title'].unique()
            df = pd.DataFrame(products[:10])
            df.rename({0: "Featuring top 10 trending Products"}, axis=1, inplace=True)
            st.table(df)

        if domain.index(choice)==4:
            new_df=joined_df[joined_df['product_title'].str.contains(choice,regex=False,case=False,na=False)]
            products=new_df['product_title'].unique()
            df = pd.DataFrame(products[:10])
            df.rename({0: "Featuring top 10 trending Products"}, axis=1, inplace=True)
            st.table(df)

        if domain.index(choice)==5:
            new_df=joined_df[joined_df['product_title'].str.contains(choice,regex=False,case=False,na=False)]
            products=new_df['product_title'].unique()
            df = pd.DataFrame(products[:10])
            df.rename({0: "Featuring top 10 trending Products"}, axis=1, inplace=True)
            st.table(df)

        if domain.index(choice)==6:
            new_df=joined_df[joined_df['product_title'].str.contains(choice,regex=False,case=False,na=False)]
            products=new_df['product_title'].unique()
            df = pd.DataFrame(products[:10])
            df.rename({0: "Featuring top 10 trending Products"}, axis=1, inplace=True)
            st.table(df)

        if domain.index(choice)==7:
            if choice =='lithiumion':
                new_df=joined_df[joined_df['product_title'].str.contains('lithium-ion',regex=False,case=False,na=False)]
                products=new_df['product_title'].unique()
                df = pd.DataFrame(products[:10])
                df.rename({0: "Featuring top 10 trending Products"}, axis=1, inplace=True)
                st.table(df)
            else:
                new_df = joined_df[joined_df['product_title'].str.contains(choice, regex=False, case=False, na=False)]
                products = new_df['product_title'].unique()
                df = pd.DataFrame(products[:10])
                df.rename({0: "Featuring top 10 trending Products"}, axis=1, inplace=True)
                st.table(df)


        if domain.index(choice)==8:
            new_df=joined_df[joined_df['product_title'].str.contains(choice,regex=False,case=False,na=False)]
            products=new_df['product_title'].unique()
            df = pd.DataFrame(products[:10])
            df.rename({0: "Featuring top 10 trending Products"}, axis=1, inplace=True)
            st.table(df)

        if domain.index(choice)==9:
            new_df=joined_df[joined_df['product_title'].str.contains(choice,regex=False,case=False,na=False)]
            products=new_df['product_title'].unique()
            df = pd.DataFrame(products[:10])
            df.rename({0: "Featuring top 10 trending Products"}, axis=1, inplace=True)
            st.table(df)







        placeholder.empty()
#
if __name__=='__main__':
    if not searched_object:
        st.write('Please type home improvement materials in the above text box')
    else:
        run()
