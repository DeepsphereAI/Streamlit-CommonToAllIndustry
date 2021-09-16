import streamlit as vAR_st
import streamlit.components.v1 as components
import pandas as pd
from IPython.display import HTML
from sklearn.linear_model import LogisticRegression 
import time
import base64 
timestr = time.strftime("%Y%m%d-%H%M%S")

#for Setting the page layout to wide
vAR_st.set_page_config(layout="wide")

#for having the logo and title in the same line we use vAR.st_beta_columns() and make the ratio accordingly 
vAR_logo, vAR_title = vAR_st.columns((6,50))
with vAR_logo:
  vAR_st.image('https://raw.githubusercontent.com/DeepsphereAI/Streamlit-CommonToAllIndustry/master/Web_app/logo.jpg', width = 90)
with vAR_title:
#setting font size and colour for the title 
  
#by this text-align: centre, we can align the title to the centre of the page
  vAR_st.markdown("<h1 style='text-align: center; color: green; font-size:29px;'>Industry Science - Data Science Applications for Enterprise</h1>", unsafe_allow_html=True)

  vAR_st.markdown("<h1 style='text-align: center; color: green; font-size:29px;'>Powered by Streamlit</h1>", unsafe_allow_html=True)

 #To customize the background colour of the submit button  
m = vAR_st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: rgb(47 236 106) ;
}
</style>""", unsafe_allow_html=True)


vAR_st.markdown("""
<style>
div.stButton > button:first-child { border: 1px solid; width: 55%; }
</style>""", unsafe_allow_html=True)


vAR_st.markdown("""
<hr style="width:100%;height:3px;background-color:gray;border-width:10">
""", unsafe_allow_html=True)


vAR_st.markdown("""<style>.css-17eq0hr {
    background-color: #4c85e4;
}
</style>""", unsafe_allow_html=True)


def training():

  #training data
  training_data = df_training 
  training_data_features = training_data[['Quantity','Price','Service Call','Service Failure Rate%','Customer Lifetime(Days)']]
            
  #feature selection for training
  training_data_features = training_data_features[['Customer Lifetime(Days)']]

  #Label for Training
  training_data_label = training_data[['Churn']]

  #model training 
  model = LogisticRegression()
  model_training = model.fit(training_data_features,training_data_label)


def testing():

  #training dataset
  training_data = df_training 
  training_data_features = training_data[['Quantity','Price','Service Call','Service Failure Rate%','Customer Lifetime(Days)']]
            
  #feature selection for training
  training_data_features = training_data_features[['Customer Lifetime(Days)']]

  #Label for Training
  training_data_label = training_data[['Churn']]

  #model training 
  model = LogisticRegression()
  model_training = model.fit(training_data_features,training_data_label)

  #Test Dataset
  test_data = df_testing

  #Feature Selection for Model Testing
  test_data_features = test_data[['Customer Lifetime(Days)']]
  test_data_features = training_data_features[['Customer Lifetime(Days)']]

  #Model Testing
  model_testing = model.predict(test_data_features)
  model_prediction = pd.DataFrame(model_testing)
  model_prediction = pd.DataFrame(model_testing,columns=['Churn Prediction'])

  prediction_result = test_data.merge(model_prediction,left_index=True,right_index=True)
  vAR_st.write('')

  #Getting the Probability of Churn
  prediction_result_probability_all_features = model.predict_proba(test_data_features)
  prediction_result_probability_all_features = pd.DataFrame(prediction_result_probability_all_features,
    columns=['Probability of Non Churn', 'Probability of Churn'])
  churn_probability = prediction_result.merge(prediction_result_probability_all_features,
    left_index=True,right_index=True)
  table_7 = HTML(churn_probability.to_html(col_space=None,max_rows=10,max_cols=6))
  vAR_st.write(table_7)
  vAR_st.write('')


def test_code():
  with vAR_st.echo():
    #training dataset
    training_data = df_training 
    training_data_features = training_data[['Quantity','Price','Service Call','Service Failure Rate%','Customer Lifetime(Days)']]
            
    #feature selection for training
    training_data_features = training_data_features[['Customer Lifetime(Days)']]

    #Label for Training
    training_data_label = training_data[['Churn']]

    #model training 
    model = LogisticRegression()
    model_training = model.fit(training_data_features,training_data_label)

    #Test Dataset
    test_data = df_testing

    #Feature Selection for Model Testing
    test_data_features = test_data[['Customer Lifetime(Days)']]
    test_data_features = training_data_features[['Customer Lifetime(Days)']]

    #Model Testing
    model_testing = model.predict(test_data_features)
    model_prediction = pd.DataFrame(model_testing)
    model_prediction = pd.DataFrame(model_testing,columns=['Churn Prediction'])

    prediction_result = test_data.merge(model_prediction,left_index=True,right_index=True)

    #Getting the Probability of Churn
    prediction_result_probability_all_features = model.predict_proba(test_data_features)
    prediction_result_probability_all_features = pd.DataFrame(prediction_result_probability_all_features,
      columns=['Probability of Non Churn', 'Probability of Churn'])
    churn_probability = prediction_result.merge(prediction_result_probability_all_features,
      left_index=True,right_index=True)
    table_7 = HTML(churn_probability.to_html(col_space=None,max_rows=10,max_cols=6))
    vAR_st.write(table_7)




def train_code():
  with vAR_st.echo():
    def training():

      #training data
      training_data = df_training 
      training_data_features = training_data[['Quantity','Price','Service Call','Service Failure Rate%','Customer Lifetime(Days)']]
            
      #feature selection for training
      training_data_features = training_data_features[['Customer Lifetime(Days)']]

      #Label for Training
      training_data_label = training_data[['Churn']]

      #model training 
      model = LogisticRegression()
      model_training = model.fit(training_data_features,training_data_label)

def download():

  #training dataset
  training_data = df_training 
  training_data_features = training_data[['Quantity','Price','Service Call','Service Failure Rate%','Customer Lifetime(Days)']]
            
  #feature selection for training
  training_data_features = training_data_features[['Customer Lifetime(Days)']]

  #Label for Training
  training_data_label = training_data[['Churn']]

  #model training 
  model = LogisticRegression()
  model_training = model.fit(training_data_features,training_data_label)

  #Test Dataset
  test_data = df_testing

  #Feature Selection for Model Testing
  test_data_features = test_data[['Customer Lifetime(Days)']]
  test_data_features = training_data_features[['Customer Lifetime(Days)']]

  #Model Testing
  model_testing = model.predict(test_data_features)
  model_prediction = pd.DataFrame(model_testing)
  model_prediction = pd.DataFrame(model_testing,columns=['Churn Prediction'])

  prediction_result = test_data.merge(model_prediction,left_index=True,right_index=True)
  vAR_st.write('')

  #Getting the Probability of Churn
  prediction_result_probability_all_features = model.predict_proba(test_data_features)
  prediction_result_probability_all_features = pd.DataFrame(prediction_result_probability_all_features,
    columns=['Probability of Non Churn', 'Probability of Churn'])
  churn_probability = prediction_result.merge(prediction_result_probability_all_features,
    left_index=True,right_index=True)

  csvfile = churn_probability.to_csv()
  b64 = base64.b64encode(csvfile.encode()).decode()
  vAR_filename = "new_text_file_{}_.csv".format(timestr)
  #vAR_st.markdown("#### Download File ###")
  href = f'<a href="data:file/csv;base64,{b64}" download="{vAR_filename}">Download File!!</a>'
  vAR_st.markdown(href,unsafe_allow_html=True)
  


def feature():
  for col in df_training.columns:
    vAR_st.write(col)

def feature_code():
  with vAR_st.echo():
    def feature():
      for col in df_training.columns:
        vAR_st.write(col) 



menu = ["Home","Model Validation","Download Model Outcome","Data visualization","Deploy the Model"]
choice = vAR_st.sidebar.selectbox("Menu",menu)
col1, col2, col3, col4, col5 = vAR_st.columns([0.25,1.5,2.75,0.25,1.75])
with col2:
    vAR_st.write('')
    vAR_st.write('')
    vAR_st.subheader("Problem Statement")
with col3:
    vAR_problem = vAR_st.selectbox('',('','Customer Churn: Who is going to churn?','Customer Churn: When will the churn occur?','Customer Churn: Why does the churn occurs?'),index=0)



col1, col2, col3, col4, col5 = vAR_st.columns([0.25,1.5,2.75,0.25,1.75])
with col2:
  if vAR_problem != '':
    vAR_st.write('')
    vAR_st.write('')
    vAR_st.subheader("Problem type")
with col3:
  if vAR_problem != '':
    vAR_type = vAR_st.selectbox('',('','Classification','Regression','Clustering','Continued Decision Making'),index=0)



col1, col2, col3, col4, col5 = vAR_st.columns([0.25,1.5,2.75,0.25,1.75])
with col2:
  if vAR_problem != '':
    if vAR_type != '':
      vAR_st.write('')
      vAR_st.write('')
      vAR_st.subheader("Model Selection")
with col3:
  if vAR_problem != '':
    if vAR_type != '':
      vAR_model = vAR_st.selectbox('',('','Decision Tree','Random Forest','Logistics Regression','Linear Regression','K Means Clustering'),index=0)
with col5:
  if vAR_problem != '':
    if vAR_type != '':
      vAR_st.write('')
      vAR_st.write('')
      model_selection_source_code = vAR_st.button('source code',key='13')



vAR_st.write('')
col1, col2, col3, col4, col5 = vAR_st.columns([0.25,1.5,2.75,0.25,1.75])
with col2:
  if vAR_problem != '':
    if vAR_type != '':
      if vAR_model != '':
        vAR_st.write('')
        vAR_st.write('')
        vAR_st.subheader("Training Dataset")
with col3:
  if vAR_problem != '':
    if vAR_type != '':
      if vAR_model != '':
        vAR_training_data = vAR_st.file_uploader("Upload CSV file")
with col5:
  if vAR_problem != '':
    if vAR_type != '':
      if vAR_model != '':
        if vAR_training_data is not None:
          if vAR_training_data.type == 'application/vnd.ms-excel':
            df_training = pd.read_csv(vAR_training_data, encoding = 'unicode_escape',error_bad_lines=False)
            vAR_st.markdown('#')
            vAR_st.write('')
            preview_training = vAR_st.button('Preview', key="1")
          elif vAR_training_data.type == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
            df_training = pd.read_excel(vAR_training_data)
            vAR_st.markdown('#')
            vAR_st.write('')
            preview_training = vAR_st.button('Preview', key="1")
          else:
            vAR_st.markdown('#')
            vAR_st.write('Upload CSV file you uploaded',vAR_training_data.type)



col1, col2, col3, col4, col5 = vAR_st.columns([0.25,1.5,2.75,0.25,1.75])
with col3:
  if vAR_problem != '':
    if vAR_type != '':
      if vAR_model != '':
        if vAR_training_data is not None:
          if vAR_training_data.type == 'application/vnd.ms-excel' or 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
            full_table_1 = vAR_st.button('Click for all Set of rows')



if vAR_problem != '':
  if vAR_type != '':
    if vAR_model != '':
      if vAR_training_data is not None:
        if vAR_training_data.type == 'application/vnd.ms-excel' or 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
          if preview_training:
            table_1 = HTML(df_training.to_html(col_space=None,max_rows=7,max_cols=6))
            vAR_st.write(table_1)
          vAR_st.write('')  
          if full_table_1:
            table_2 = HTML(df_training.to_html(col_space=None))
            vAR_st.write(table_2)           



col1, col2, col3, col4, col5 = vAR_st.columns([0.25,1.5,2.75,0.25,1.75])
with col2:
  if vAR_problem != '':
    if vAR_type != '':
      if vAR_model != '':
        if vAR_training_data:
          vAR_st.subheader("Feature Engineering")
with col3:
  if vAR_problem != '':
    if vAR_type != '':
      if vAR_model != '':
        if vAR_training_data:
          vAR_st.write('')
          button_feature = vAR_st.button('Extract Feature')
          vAR_st.write('')
with col5:
  if vAR_problem != '':
    if vAR_type != '':
      if vAR_model != '':
        if vAR_training_data:
          vAR_st.write('')
          feature_source_code = vAR_st.button('source code',key='12')



col1, col2, col3, col4, col5= vAR_st.columns([0.25,2,2,2,1.75])
with col3:
  if vAR_problem != '':
    if vAR_type != '':
      if vAR_model != '':
        if vAR_training_data:
          if button_feature:
            for i in range(len(df_training.columns)):
              vAR_st.write('Feature ',i+1)    
with col4:
  if vAR_problem != '':
    if vAR_type != '':
      if vAR_model != '':
        if vAR_training_data:
          if button_feature:
            feature()

if vAR_problem != '':
  if vAR_type != '':
    if vAR_model != '':
      if vAR_training_data:
        if feature_source_code:
          feature_code()



vAR_st.write('') 
col1, col2, col3, col4, col5 = vAR_st.columns([0.25,1.5,2.75,0.25,1.75])
with col2:
  if vAR_problem != '':
    if vAR_type != '':
      if vAR_model != '':
        if vAR_training_data:

          vAR_st.subheader("Model Engineering")
with col3:
  if vAR_problem != '':
    if vAR_type != '':
      if vAR_model != '':
        if vAR_training_data:
          vAR_st.write('')
          button_train = vAR_st.button('Train the Model')
          if button_train:
            vAR_st.image('https://i.gifer.com/IPNp.gif',width = 200)
            training()
            vAR_success = vAR_st.success('Model training completed')
with col5:
  if vAR_problem != '':
    if vAR_type != '':
      if vAR_model != '':
        if vAR_training_data:
          vAR_st.write('')
          train_source_code = vAR_st.button('source code',key="10")



#to display traning code
if vAR_problem != '':
  if vAR_type != '':
    if vAR_model != '':
      if vAR_training_data:
        if train_source_code:
          train_code()



vAR_st.write('')
col1, col2, col3, col4, col5 = vAR_st.columns([0.25,1.5,2.75,0.25,1.75])
with col2:
  if vAR_problem != '':
    if vAR_type != '':
      if vAR_model != '':
        if vAR_training_data:
          #time.sleep(10)
          vAR_st.write('')
          vAR_st.write('')
          vAR_st.markdown('#')
          vAR_st.subheader('Model Engineering')
with col3:
  if vAR_problem != '':
    if vAR_type != '':
      if vAR_model != '':
        if vAR_training_data:
          vAR_st.subheader('Test the Model')
          vAR_testing_data = vAR_st.file_uploader("upload CSV file")
with col5:
  if vAR_problem != '':
    if vAR_type != '':
      if vAR_model != '':
        if vAR_training_data:
          if vAR_testing_data is not None:
            if vAR_testing_data.type == 'application/vnd.ms-excel':
              df_testing = pd.read_csv(vAR_testing_data, encoding = 'unicode_escape',error_bad_lines=False)
              vAR_st.markdown('#')
              vAR_st.markdown('#')
              vAR_st.write('')
              preview_testing = vAR_st.button('Preview', key="2")
            elif vAR_training_data.type == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
              df_testing = pd.read_excel(vAR_testing_data)
              vAR_st.markdown('#')
              vAR_st.markdown('#')
              vAR_st.write('')
              preview_testing = vAR_st.button('Preview', key="2")
            else:
              vAR_st.markdown('#')
              vAR_st.write('Upload CSV file you uploaded',vAR_testing_data.type)



col1, col2, col3, col4, col5 = vAR_st.columns([0.25,1.5,2.75,0.25,1.75])
with col3:
  if vAR_problem != '':
    if vAR_type != '':
      if vAR_model != '':
        if vAR_training_data:
          if vAR_testing_data is not None:
            if vAR_testing_data.type == 'application/vnd.ms-excel' or 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet': 
              vAR_st.write('')
              full_table_2 = vAR_st.button('Click for all Set of Rows')



if vAR_problem != '':
  if vAR_type != '':
    if vAR_model != '':
      if vAR_training_data:
        if vAR_testing_data is not None:
          if vAR_testing_data.type == 'application/vnd.ms-excel' or 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
            if preview_testing:
              table_3 = HTML(df_testing.to_html(col_space=None,max_rows=7,max_cols=6))
              vAR_st.write(table_3)
            vAR_st.write('')  
            if full_table_2:
              table_4 = HTML(df_testing.to_html(col_space=None))
              vAR_st.write(table_4)
            vAR_st.write('')



col1, col2, col3, col4, col5 = vAR_st.columns([0.25,1.5,2.75,0.25,1.75])
with col3:
  if vAR_problem != '':
    if vAR_type != '':
      if vAR_model != '':
        if vAR_training_data:
          if vAR_testing_data is not None:
            if vAR_testing_data.type == 'application/vnd.ms-excel' or 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet': 
              button_test = vAR_st.button('Test the Model')
              if button_test:
                vAR_st.image('https://i.gifer.com/IPNp.gif',width = 200)
                vAR_success_1 = vAR_st.success('Model testing completed')
with col5:
  if vAR_problem != '':
    if vAR_type != '':
      if vAR_model != '':
        if vAR_training_data:
          if vAR_testing_data is not None:
            if vAR_testing_data.type == 'application/vnd.ms-excel' or 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':             
              test_source_code = vAR_st.button('source code',key="11")



#to display test code
if vAR_problem != '':
  if vAR_type != '':
    if vAR_model != '':
      if vAR_training_data:
        if vAR_testing_data is not None:
          if vAR_testing_data.type == 'application/vnd.ms-excel' or 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
            if test_source_code:
              test_code()



col1, col2, col4 = vAR_st.columns([0.5,4,0.5])
with col2:
  if vAR_problem != '':
    if vAR_type != '':
      if vAR_model != '':
        if vAR_training_data:
          if vAR_testing_data is not None:
            if vAR_testing_data.type == 'application/vnd.ms-excel' or 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
              if button_test:
                testing()
vAR_st.markdown('#')
vAR_st.markdown("""
<hr style="width:100%;height:3px;background-color:gray">
""", unsafe_allow_html=True)


#vAR_st.markdown("""---""")
if choice == "Home":
  vAR_st.subheader("Go to the Menu")

if choice == "Model Validation":
  vAR_st.subheader("Model Validation")
  col1, col2, col4 = vAR_st.columns([2,4,4])
  with col1:
    vAR_st.button("Click here", key="6")

if choice == "Download Model Outcome":
  vAR_st.subheader("To Download the Model Outcome")
  col1, col2, col4 = vAR_st.columns([3,4,4])
  with col1:
    if vAR_problem != '':
      if vAR_type != '':
        if vAR_model != '':
          if vAR_training_data:
            if vAR_testing_data is not None:
              if vAR_testing_data.type == 'application/vnd.ms-excel' or 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
                button_download = vAR_st.button("Click here", key="9")
                if button_download:
                  download()
                

if choice == "Data visualization":
  vAR_st.subheader("Data visualization")
  col1, col2, col4 = vAR_st.columns([2,4,4])
  with col1:
    vAR_st.button("Click here", key="8")

if choice == "Deploy the Model":
  vAR_st.subheader("To Deploy the Model")



library = ["Library Used","Streamlit","Pandas","IPython.display","sklearn.linear_model"]
lib = vAR_st.sidebar.selectbox(" ",library)


services = ["GCP Services Used","VM Instance","Compute Engine"]
gcp = vAR_st.sidebar.selectbox(" ",services)


from bokeh.models.widgets import Div
if vAR_st.sidebar.button('Clear/Refresh'):
  js = "window.location.herf = 'http://localhost:8501/'"
  html = '<img src onerror="{}">'.format(js)
  div = Div(text=html)
  vAR_st.bokeh_chart(div)      
