import streamlit as st
import requests

st.set_page_config(page_title='Customer Segmentation System', page_icon='🛍️', layout='wide')

DEFAULTS={'gender':'Male','age':30,'income':60,'spending':50}
for k,v in DEFAULTS.items():
    st.session_state.setdefault(k,v)

def reset():
    for k,v in DEFAULTS.items():
        st.session_state[k]=v
    st.rerun()

st.title('🛍️ Customer Segmentation System')
st.divider()

left,center,right=st.columns([1,1.7,1])

with left:
    st.subheader('👤 Customer Inputs')
    st.selectbox('Gender',['Male','Female'],key='gender')
    st.slider('Age',18,70,key='age')
    st.number_input('Annual Income (k$)',10,150,key='income')
    st.slider('Spending Score (1-100)',1,100,key='spending')
    c1,c2=st.columns(2)
    predict=c1.button('🔍 Predict',use_container_width=True)
    c2.button('🔄 Reset',use_container_width=True,on_click=reset)

with right:
    st.subheader('📊 Model Info')
    st.info('''Algorithm: K-Means Clustering

Clusters: 5

Silhouette Score: 0.55''')

with center:
    st.subheader('🎯 Prediction Result')
    if predict:
        payload={
            'Gender':st.session_state.gender,
            'Age':st.session_state.age,
            'Annual Income (k$)':st.session_state.income,
            'Spending Score (1-100)':st.session_state.spending
        }
        try:
            r=requests.post('http://127.0.0.1:5000/predict',json=payload,timeout=10)
            if r.status_code==200:
                res=r.json()
                st.success('Prediction completed successfully!')
                st.markdown(f"## ⭐ {res['segment']} — **Cluster No:** {res['cluster']}")
                # st.markdown(f"## ⭐ {res['segment']}")
                # st.markdown(f"Cluster No : {res['cluster']}")

                # a,b=st.columns(2)
                # a.metric('Cluster No',res['cluster'])
                # b.metric("Customer Type", res["segment"])
                st.info(f"### {res['description']}")
                st.warning(f"### {res['marketing_action']}")
            else:
                st.error(r.text)
        except Exception as e:
            st.error(f'Connection Error: {e}')
    else:
        st.info('Enter inputs and click Predict.')

st.divider()
st.caption('Developed using Streamlit • Flask • Scikit-learn • K-Means')
