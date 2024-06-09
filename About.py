import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
from torchvision import transforms
import torch 
from model.frontend import Frontend
from model.plastic_pred import PlasticPredict 
import google.generativeai as genai
import time
from dotenv import load_dotenv
import os 
def config():
    load_dotenv()
config()
API_KEY = os.getenv('KEY')


ui = Frontend()
st.set_page_config(page_title=None, page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items=None)

selected = option_menu(None, ["About", 'Micro Plastic Prediction'], 
    icons=['house', 'gear'], menu_icon="cast", default_index=1,orientation="horizontal" , styles = {"container": {"padding" : "0"}})
selected

plastic_dic = {
  0: "Low-Density Polyethylene (LDPE) with dust",
  1: "Polyethylene (PE)",  
  2: "Polyethylene (PE) with dust",  
  3: "Polyhydroxyalkanoate (PHA)",  
  4: "Polyhydroxyalkanoate (PHA) with dust",
  5: "Polystyrene (PS)",
  6: "Polystyrene (PS) with dust",
  7: "Mixed Plastic (combination of different types)",
  8: "None"
}
# ------------------------------------------------------Main Features ----------------------------------------------------
if selected == "Micro Plastic Prediction":
    st.markdown(ui.plastic_css_front(), unsafe_allow_html=True)
    st.markdown(ui.plastic_html_front(), unsafe_allow_html=True)
    transform  = transforms.Compose([transforms.Resize((255, 255)) , transforms.ToTensor()])
    device = "cuda" if torch.cuda.is_available() else "cpu"
    img = st.file_uploader("Choose an image...", type=['jpg', 'jpeg', 'png'], )
    if img:
        user_image = Image.open(img)
        user_image = user_image.resize((255,255))
        st.image(user_image.resize((255,255)))
        user_image = user_image.convert('RGB')
        input_tensor = transform(user_image).to(device)
        plstic = PlasticPredict(input_tensor)
        ans = plstic.pred()
        st.markdown("<h3><u>Predicted Plastic Type:</u></h3>",unsafe_allow_html=True)
        st.markdown(f"\t ###### {plastic_dic[ans]}")
        genai.configure(api_key=API_KEY)
        model = genai.GenerativeModel("gemini-pro")
        if ans != 8:
            with st.spinner('Processing  .........'):
                st.markdown("<hr>",unsafe_allow_html=True)
                st.markdown(f"<h2> About {plastic_dic[ans]} and How {plastic_dic[ans]} is affecting world Ocean",unsafe_allow_html=True)
                if "_LOREM_IPSUM" not in st.session_state:
                    with st.spinner('Processing  .........'):
                        res = model.generate_content(f"How {plastic_dic[ans]} is affecting world Ocean ?")
                        st.session_state["_LOREM_IPSUM"] = res.text 
            def stream_data(sentecnce :str ):
                for word in sentecnce.split(" "):
                    yield word + " "
                    time.sleep(0.05)
            st.write_stream(stream_data(st.session_state._LOREM_IPSUM))
            st.markdown(f"<hr><h2> How {plastic_dic[ans]} could be treated ?",unsafe_allow_html=True)
            if "point_two" not in st.session_state:
                res = model.generate_content(f"How {plastic_dic[ans]} could be treated ?")
                st.session_state["point_two"] = res.text

            st.write_stream(stream_data(st.session_state.point_two))

# =--------------------------------------------------------------------------------------------------------------------------------
elif selected == "About" :
    
    def main():
        st.markdown(ui.about_css_front(), unsafe_allow_html=True)

        st.markdown(ui.about_html_front(), unsafe_allow_html=True)
        
    if __name__ == "__main__":
        main()
