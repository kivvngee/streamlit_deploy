import streamlit as st

# Set page layout to wide
st.set_page_config(layout="wide")

# st.title("Redirect Button Example")

# Streamlit Sidebar Menu
st.sidebar.title("메뉴")
menu = st.sidebar.radio("선택해주세요", ["추천드리고 싶은 곳들", "예약 링크들", "예약 내역"])


if menu == "추천드리고 싶은 곳들":
    st.title("어시스트립에서 당신께 추천드리고 싶은 곳들들")





elif menu == "예약 링크들":
    # st.title("예약 링크들")
    # Add a button
    # if st.button("Go to YouTube"):
    #     # Provide a direct clickable link
    #     st.write("[Click here to go to YouTube](https://www.youtube.com)")

    # st.link_button("Go to YouTube", "https://www.youtube.com")



    

    # Create two columns for the split layout
    left_column, right_column = st.columns(2)



    # Left half of the page
    with left_column:
        st.markdown("<h1 style='text-align: center;'>항공권 예매</h1>", unsafe_allow_html=True)
        
        # Create 2x3 grid for buttons
        button_cols = st.columns(3)
        
        # Define button names and URLs
        left_buttons = [
            ("네이버 항공권", "https://flight.naver.com/"),
            ("구글 플라이트", "https://www.google.com/travel/flights?hl=ko"),
            ("스카이스캐너", "https://www.skyscanner.co.kr/"),
            ("트립닷컴", "https://kr.trip.com/flights/"),
            ("인터파크투어", "https://sky.interpark.com/"),
            ("익스피디아", "https://www.expedia.co.kr/air")
        ]
        
        # Create buttons in a 2x3 grid
        for i, (name, url) in enumerate(left_buttons):
            with button_cols[i % 3]:
                st.link_button(name, url)

    # Right half of the page
    with right_column:
        st.markdown("<h1 style='text-align: center;'>숙박 예약</h1>", unsafe_allow_html=True)
        
        # Create 2x3 grid for buttons
        button_cols = st.columns(3)
        
        # Define button names and URLs (same as left side)
        right_buttons = [
            ("아고다", "https://www.agoda.com"),
            ("트립닷컴", "https://kr.trip.com/hotels/"),
            ("호텔스 컴바인", "https://www.hotelscombined.co.kr/"),
            ("에어비앤비", "https://www.airbnb.co.kr/"),
            ("호텔스닷컴", "https://kr.hotels.com/"),
            ("야놀자", "https://www.yanolja.com/")
        ]
        
        
        # Create buttons in a 2x3 grid
        for i, (name, url) in enumerate(right_buttons):
            with button_cols[i % 3]:
                st.link_button(name, url)


    







    



elif menu == "예약 내역":
    st.title("예약 내역")

    


