import streamlit as st
import pickle
import numpy as np
model = pickle.load(open('model.pkl','rb'))


def predict_Score(a,b,c,d,e,f,g,h,i,j,k,l):
    input=np.array([[a,b,c,d,e,f,g,h,i,j,k,l]]).astype(np.float64)
    prediction=model.predict(input)
    return prediction

def main():
    st.title("Credit Score Classifier")
    html_temp = """
    <div style="background-color:#025246 ;padding:10px">
    <h2 style="color:black;text-align:center;">Credit Score classification ML app </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    a = st.text_input("Annual Income","Type Here In $")
    b = st.text_input("Monthly Inhand Salary","Type Here In $")
    c = st.text_input("Number of Bank Accounts","Type Here")
    d = st.text_input("Number of Credit cards","Type Here")
    e = st.text_input("Interest rate on the credit card","Type Here In %")
    f = st.text_input("Number of Loans","Type Here")
    g = st.text_input("Average number of days delayed by the person","Type Here")
    h = st.text_input("Number of delayed payments","Type Here")
    i = st.text_input("Credit Mix (Bad: 0, Standard: 1, Good: 3)","Type Here")
    j = st.text_input("Outstanding Debt","Type Here In $")
    k = st.text_input("Credit History Age","Type Here")
    l = st.text_input("Monthly Balance at the end of the month","Type Here In $")
    good_html="""  
      <div style="background-color:#9CF080;padding:10px >
       <h2 style="color:black;text-align:center;"> Good Credit Score</h2>
       </div>
    """
    standard_html="""  
      <div style="background-color:#F4D03F;padding:10px >
       <h2 style="color:black;text-align:center;"> Standard Credit Score</h2>
       </div>
    """
    poor_html="""  
      <div style="background-color:#F08080;padding:10px >
       <h2 style="color:black ;text-align:center;"> poor Credit Score</h2>
       </div>
    """

    if st.button("Predict"):
        output=predict_Score(a,b,c,d,e,f,g,h,i,j,k,l)
        st.success('Predicted Credit Score = '+output)

        if output == ['Good']:
            st.markdown(good_html,unsafe_allow_html=True)
        elif output == ['Standard']:
            st.markdown(standard_html,unsafe_allow_html=True)
        else:
            st.markdown(poor_html,unsafe_allow_html=True)

if __name__=='__main__':
    main()