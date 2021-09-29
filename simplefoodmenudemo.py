import streamlit as st
from binarysearchtree import foodMenu
import pandas as pd

if 'hasFood' not in st.session_state:
    st.session_state.hasFood = 0


st.header("Welcome to ABC Simple Food Menu Demo")

readme = st.checkbox("readme first")

if readme:

    st.write("""
        This is a simple binary search tree demo using [streamlit](https://streamlit.io/) library. It is hosted on [heroku](https://www.heroku.com/). You may get the codes via [github](https://github.com/richieyuyongpoh/binarySearchTreeDemo)
        """)

    st.write ("For more info, please contact:")

    st.write("<a href='https://www.linkedin.com/in/yong-poh-yu/'>Dr. Yong Poh Yu </a>", unsafe_allow_html=True)

st.write("Choose an option from the radio button on the side bar to continue.")


option = st.sidebar.selectbox(
    'Select an option',
     ['Add a food','Find a food','Get the sorted food list','Reset entire food menu system'])

if option == 'Add a food':
    foodName = st.text_input("Please enter the food name")
    foodPrice = st.text_input("Please enter the food price")
    submit = st.button('submit')

    if submit:

        if foodName != "" and foodPrice !="":

            if st.session_state.hasFood==1:

                st.session_state.RBAFoodMenu.addNode(foodName,foodPrice)
                st.write("[{} , RM {}] has been added to the food Menu.".format(foodName, foodPrice))
            
            else:
                st.session_state.RBAFoodMenu = foodMenu(foodName,foodPrice)
                st.write("[{} , RM {}] has been added to the food Menu.".format(foodName, foodPrice))
                st.session_state.hasFood = 1

        else:
            st.write("Please fill in the details first. ")


elif option == 'Find a food':
        

    if st.session_state.hasFood ==1:

        foodName = st.text_input("Please enter the food name that you want to search for")
        
        st.write("The food is in the Food Menu: {}".format(st.session_state.RBAFoodMenu.findNode(foodName)))
 

    else:
        st.write("Empty Food Menu.")


    
elif option == 'Get the sorted food list':

    if st.session_state.hasFood ==1:
        st.write("The list in the Food Menu:")
        st.write(pd.DataFrame(st.session_state.RBAFoodMenu.inOrderTraversal(),columns=["Food Name", "Price"]))

    else:
        st.write("Empty Food Menu.")

else:
    st.write("The food menu system has been reset.")

    st.session_state.hasFood = 0 
    st.session_state.RBAFoodMenu = []
