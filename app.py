import streamlit as st
from PIL import Image

st.set_page_config(layout="wide")

def main():
    
    
    st.title('Treasure Hunt Game')
    
    hints = ["","Hint 1", "Hint 2", "Hint 3", "Hint 4", "Hint 5"]
    select = st.sidebar.selectbox("Choisis un hint", hints)
    
    if select == "":
        st.title('Joyeux Anniversaire ma Zoubaaaa!!')
        st.write("Comme promis une petite chasse au trésor! <3")
        st.write("T'es prêtes?")
        if st.button("Non..."):
            st.text("Ok, encore joyeux anniversaire et à l'année prochaine!")
        if st.button("Oui! =)"):
            st.header("Ok, alors il faudra les trouver ;)")
            st.write("Chaque 'Hint' t'indiquera un objet/lieu où tu trouveras un code à 4 digit")
            st.write("Un code correctement trouvé devoilera des lettres qui te permettront de trouver le trésor!")
        
    elif select == "Hint 1":
        
        st.subheader('Hint 1:')
        st.text("'Un jour je serai le roi des pirates!'")
        c1 = st.text_input("Code 1", '')
    
    
        if st.button("submit code 1"):
            if c1 == '4567':
                st.write("Bravo!")
                st.subheader("Les lettres à noter:")
                st.write("I, M, E, F")
            else:
                st.text("FAUX!")
    
    elif select == "Hint 2":
        
        st.subheader('Hint 2:')
        st.text("'Elementaire, mon cher Watson.'")
        
        A_ = Image.open('A_.png')
        P_ = Image.open('P_.png')
        E_ = Image.open('E_.png')
        R_ = Image.open('R_.png')
        O_ = Image.open('O_.png')
        L_ = Image.open('L_.png')
    
        col1, col2, col3, col4, col5, col6 = st.beta_columns(6)
        col1.image(A_, use_column_width=True)
        col2.image(P_, use_column_width=True)
        col3.image(E_, use_column_width=True)
        col4.image(R_, use_column_width=True)
        col5.image(O_, use_column_width=True)
        col6.image(L_, use_column_width=True)
        c2 = st.text_input("Code 2", '')
    
    
        if st.button("submit code 2"):
            if c2 == '9134':
                st.write("Bravo!")
                st.subheader("Les lettres à noter:")
                st.write("J, E")
            else:
                st.text("FAUX!")
                
    elif select == "Hint 3":
        
        st.subheader('Hint 3:')
        st.text("45.150631725, -0.733851552")
        c3 = st.text_input("Code 3", '')
    
    
        if st.button("submit code 3"):
            if c3 == '1290':
                st.write("Bravo!")
                st.subheader("Les lettres à noter:")
                st.write("T, A")
            else:
                st.text("FAUX!")
    
    elif select == "Hint 4":
        
        st.subheader('Hint 4:')
        st.text("D'un côté je suis apprécie dans le monde entier et d'un autre je ressens un ras-le-bol pour m'accepter")
                
        c4 = st.text_input("Code 4", '')
    
    
        if st.button("submit code 4"):
            if c4 == '8378':
                st.write("Bravo!")
                st.subheader("Les lettres à noter:")
                st.write("O, R, T")
            else:
                st.text("FAUX!")
                
    elif select == "Hint 5":
        
        st.subheader('Hint 5:')
        st.text("DEUX TROIS UN QUATRE")

if __name__ == "__main__":
    main()