import streamlit as st
import plotly.express as px
import pandas as pd
wide_df = px.data.medals_wide(indexed=True)
st.set_page_config(layout="wide")

# Read Excel file
df = pd.read_excel("Analysis.xlsx")


#  Add Title Widget
st.title("Check Each RCs Sales Performance For 2023")

#  select the RCs from the Excel file
RC = df["RCs"].unique()
# place the selected items into the dropdown list
selected_Rc = st.selectbox("Select an RC", RC)

# select the months header from the Excel file
select_months = df.columns.to_list()
get_months = select_months[2:]
# Add  MONTH select widget
RC_month = st.selectbox("Select the Month", get_months)

# Check performing RCs
performing_RC = st.selectbox("Check the Top and least RC Performance",
                             ("Top 5 Performing RC", "Least 5 performing RC"), key="disabled")

# Add the range widget
month = st.slider("Performance By Months", min_value=1, max_value=6,
          help="Select the number of months performance")
st.subheader(f"RC Sales report for {month} months")


col1, col2 = st.columns([0.7, 0.3])

with col1:
    if month == 1:
        # get the values from the RC column and the month column
        get_data = df.loc[df["RCs"] == selected_Rc][RC_month].squeeze()


        months = [RC_month]
        performance = [get_data]
        figure = px.bar(x=months, y=performance, labels={"x":"Month", "Y":"Performance"}, text_auto = True)
        figure.update_traces(textfont_size=14, textangle=0, textposition="outside")
        st.plotly_chart(figure)

    elif month == 2:
        get_data = df.loc[df["RCs"] == selected_Rc][["Jan", "Feb"]].squeeze()
        dt = pd.DataFrame(dict(
            group = ["Jan", "Feb"],
            value = get_data
        ))
        # months = [["Jan", "Feb"]]
        # performance = [[get_data]]
        figure = px.bar(dt, x='group', y='value', text_auto = True)
        figure.update_traces(textfont_size=14, textangle=0, textposition="outside")
        st.plotly_chart(figure)

    elif month == 3:
        get_data = df.loc[df["RCs"] == selected_Rc][["Jan", "Feb", "Mar"]].squeeze()
        dt = pd.DataFrame(dict(
            group = ["Jan", "Feb", "Mar"],
            value = get_data
        ))
        # months = [["Jan", "Feb"]]
        # performance = [[get_data]]
        figure = px.bar(dt, x='group', y='value', text_auto = True)
        figure.update_traces(textfont_size=14, textangle=0, textposition="outside")
        st.plotly_chart(figure)

    elif month == 4:
        get_data = df.loc[df["RCs"] == selected_Rc][["Jan", "Feb", "Mar", "Apr"]].squeeze()
        dt = pd.DataFrame(dict(
            group = ["Jan", "Feb", "Mar", "Apr"],
            value = get_data
        ))
        # months = [["Jan", "Feb"]]
        # performance = [[get_data]]
        figure = px.bar(dt, x='group', y='value', text_auto = True)
        figure.update_traces(textfont_size=14, textangle=0, textposition="outside")
        st.plotly_chart(figure)

    elif month == 5:
        get_data = df.loc[df["RCs"] == selected_Rc][["Jan", "Feb", "Mar", "Apr", "May"]].squeeze()
        dt = pd.DataFrame(dict(
            group = ["Jan", "Feb", "Mar", "Apr", "May"],
            value = get_data
        ))
        # months = [["Jan", "Feb"]]
        # performance = [[get_data]]
        figure = px.bar(dt, x='group', y='value', text_auto = True)
        figure.update_traces(textfont_size=14, textangle=0, textposition="outside")
        st.plotly_chart(figure)

    elif month == 6:
        get_data = df.loc[df["RCs"] == selected_Rc][["Jan", "Feb", "Mar", "Apr", "May", "Jun"]].squeeze()
        dt = pd.DataFrame(dict(
            month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
            sales = get_data
        ))
        # months = [["Jan", "Feb"]]
        # performance = [[get_data]]
        figure = px.bar(dt, x='month', y='sales', text_auto = True)
        figure.update_traces(textfont_size=14, textangle=0, textposition="outside")
        st.plotly_chart(figure)

with col2:

   st.subheader(f"Total sales for {selected_Rc} in 6 months")
   get_data = df.loc[df["RCs"] == selected_Rc].eval('Sum = Jan + Feb + Mar + Apr + May + Jun')["Sum"].squeeze()
   result = ('{:,}'.format(get_data))
   st.subheader(result)
   # Get best performing RCs

   if performing_RC == "Top 5 Performing RC":
         st.subheader("Top Performing RCs")
         sum_data = df.eval('Sum = Jan + Feb + Mar + Apr + May + Jun')
         performing = sum_data.sort_values(by=['Sum'], ascending=False).head()
         check = performing["RCs"].to_list()
         for rc in check:
             st.info(rc)

   if performing_RC == "Least 5 performing RC":

       st.subheader("Least Performing RCs")
       sum_data = df.eval('Sum = Jan + Feb + Mar + Apr + May + Jun')
       performing = sum_data.sort_values(by=['Sum'], ascending=True).head()
       check = performing["RCs"].to_list()
       for rc in check:
           st.info(rc)
       # st.info(check)

bg = """ 
      <style>
            #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.css-z5fcl4.e1g8pov64 > div:nth-child(1) > div > div.css-ocqkz7.esravye3 > div.css-1bzkvni.esravye1 > div:nth-child(1) > div > div:nth-child(1) > div > div{
            background-color:red;
            }
            #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.css-z5fcl4.e1g8pov64 > div:nth-child(1) > div > div.css-ocqkz7.esravye3 > div.css-1bzkvni.esravye1 > div:nth-child(1) > div > div:nth-child(2){
            backround-color:red;
            }
      </style>
    """
st.markdown(bg, unsafe_allow_html=True)