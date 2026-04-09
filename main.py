import streamlit as st

# st.title('welcome to wscube tech ')
# st.header('python')
# st.subheader('java')
# st.markdown('i love python')
# st.code('''for i in range(1,5,1'):
#               print('hello")
#        ''')
# create datasetcheck
#import pandas as pd
#
# dataset = pd.read_csv('heart.csv')
# st.dataframe(dataset)


#    create a form
name = st.text_input('Enter Your Name:-')
fname = st.text_input('Enter Your Father Name:-')
adr = st.text_area('Enter YOUR Text :')
classdata=st.selectbox('Enter Your Class:-',(1,2,3,4,5,6))

button=st.button('SAVE')
if button:
    st.markdown(f"""
    Name:{name}
    Father Name:{fname}
    address:{adr}
    class:{classdata}
""")