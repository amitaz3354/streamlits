import streamlit as st
import tradingeconomics as te
import pandas as pd
import matplotlib.pyplot as plt

# connecting to the api 

def main():

    st.title("demo data app")
    te.login()
    data = te.getIndicatorData(country=['united states', 'china'], output_type='df')
    df = pd.DataFrame(data)  
    is_usa = df['Country'] == "United States"
    new_df = df[is_usa]

    values = new_df['PreviousValue']
    values2 = new_df['Category']


    st.write(new_df)
    

    st.bar_chart(values)
    st.bar_chart(values2)
   

  



 

if __name__ == "__main__":
    main()
