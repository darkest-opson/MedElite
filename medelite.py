import streamlit as st

def main():
    st.set_page_config(page_title="MedElite Online Coaching", page_icon="📚", layout="wide")

    col1, col2,col2 = st.columns([1,1,100])
    with col2:
        st.markdown("<h1 style='color: red;'>MedElite</h1>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([1,2])
    with col2:
        st.markdown("##### <span style='color: red;'>🚀 New Batches will start from june 2024🚀 Scroll Down to Demo Classes.</span>", unsafe_allow_html=True)
        st.write("Welcome to MedElite, an online coaching platform, your premiere destination for mastering biology in the 11th and 12th grades, paving the way for future doctors. At MedElite, we take pride in our dedicated team of educators and our meticulously crafted curriculum designed to provide personalized attention to each student. Our mission is to make the journey into life sciences exciting and enriching, fostering a deep understanding that lays the foundation for medical excellence.")
        # st.markdown("###### Meet our founder: PRABHAT TRIPATHI")
        st.markdown("###### <span style='color: red;'>Meet Our Founder: PRABHAT TRIPATHI</span>", unsafe_allow_html=True)

        st.write("Prabhat Tripathi, the visionary behind MedElite, is a distinguished Research Scholar at SysBio Lab, Bioinformatic Centre, Indian Institute of Information Technology Allahabad, Prayagraj. With a profound passion for advancing knowledge in the field, Prabhat brings a wealth of expertise to the world of biology education. His commitment to excellence is reflected in every aspect of MedElite's mission to shape the future generation of doctors.")
        st.write("Join us at MedElite, where academic excellence and personalized guidance converge to create a unique learning experience. Your journey to medical mastery begins here!")
    
    # Teacher Photo and Qualification
    with col1:
        st.image("./pictures/Snapchat-1082235770~2.jpg", caption="Mentor : Prabhat Tripathi", width=250 )
        st.write("B.Tech.(Biotech.) | M.Tech(Bioinformatics) and PhD")
        st.write("Research Scholar @Department of Applied sciences, Indian Institute of information Technology Allahabad, Prayagraj")

    
    col1, col2 = st.columns([1,1])
    with col1:
        # Get Started
        st.markdown("<h1 style='color: red;'>Get Started</h1>", unsafe_allow_html=True)
        st.markdown("[Click here to Experience a demo class!](https://chat.whatsapp.com/BGHy9jeYpPTJ6dixTmhjYm)")
        st.markdown("Ready to enroll? [Pay your course fees here](https://forms.gle/RzRzXQEqjEdo715u7)")

        # Student Reviews
        st.markdown("<h1 style='color: red;'>Student Reviews</h1>", unsafe_allow_html=True)
        st.write("Have you attended our classes? [Share your feedback](https://forms.gle/PKQUiFFETL56nmcb8)")

    with col2:
        # Contact Us
        st.markdown("<h1 style='color: red;'>Contact Us</h1>", unsafe_allow_html=True)
        st.write("For any queries, feel free to reach out:")
        st.write("- Phone: [+91 6388124238](tel:+916388124238)")
        st.write("- Email: [medelite.biology@gmail.com](mailto:medelite.biology@gmail.com)")


    # Footer
    st.markdown("2024 MedElite | Follow us on [YouTube](https://www.youtube.com/channel/UCfZQZj7EkCx6dzsKXGh1IKA)", unsafe_allow_html=True)


if __name__ == "__main__":
    main()
