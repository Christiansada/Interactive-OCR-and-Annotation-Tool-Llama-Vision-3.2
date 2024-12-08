import streamlit as st
import ollama
from PIL import Image
import time


# Set page config for better UX
st.set_page_config(
    page_title="🦙 Llama OCR+",
    page_icon="🦙",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Page Styling (using markdown for custom CSS)
st.markdown(
    """
    <style>
    body {
        font-family: 'Arial', sans-serif;
        background-color: #f4f7fa;
        color: #333;
    }
    .main {
        background-color: #ffffff;
        border-radius: 12px;
        padding: 25px;
        box-shadow: 0px 10px 20px rgba(0, 0, 0, 0.1);
    }
    h1 {
        color: #5d6d7e;
        font-size: 3rem;
        text-align: center;
    }
    .stButton button {
        background-color: #1d4ed8;
        color: white;
        border-radius: 8px;
        font-weight: bold;
        transition: background-color 0.3s ease;
    }
    .stButton button:hover {
        background-color: #2563eb;
    }
    .stFileUploader {
        background-color: #ffffff;
        border: 2px dashed #cbd5e1;
        border-radius: 8px;
        padding: 20px;
        text-align: center;
    }
    .stFileUploader:hover {
        background-color: #e4eff4;
    }
    .stTextArea {
        border-radius: 8px;
        box-shadow: inset 0px 2px 4px rgba(0, 0, 0, 0.1);
    }
    </style>
    """, unsafe_allow_html=True
)

# Header Section
st.markdown("<h1>🦙 Llama OCR+ with Annotations</h1>", unsafe_allow_html=True)
st.markdown(
    "Upload an image to extract structured text and annotations using Llama 3.2 Vision. "
    "You can then refine the text and export it to your preferred format.",
    unsafe_allow_html=True
)

# File Upload Section (interactive and styled)
st.sidebar.header("Upload Image")
uploaded_file = st.sidebar.file_uploader("Choose an image file (PNG, JPG, JPEG)", type=['png', 'jpg', 'jpeg'])

if uploaded_file is not None:
    # Display image
    image = Image.open(uploaded_file)
    st.sidebar.image(image, caption="Uploaded Image", use_container_width=True)


    # Interactive Button for OCR
    if st.sidebar.button("🔍 Extract Text"):
        # Measure time for debugging
        start_time = time.time()
        with st.spinner("Processing... please wait."):
            
            try:
                # Send image to Llama Vision Model for OCR
                response = ollama.chat(
                    model='llama3.2-vision',
                    messages=[{
                        'role': 'user',
                        'content': """Analyze the text in this image and generate structured Markdown with headings, 
                                      lists, and key highlights. Add suggested annotations for better readability.""",
                        'images': [uploaded_file.getvalue()]
                    }]
                )
                processing_time = time.time() - start_time
                st.info(f"Processing completed in {processing_time:.2f} seconds")
                # Store the result and display it
                extracted_text = response.message.content
                st.session_state['ocr_result'] = extracted_text

                # Display OCR result
                st.markdown("### Extracted Text and Annotations")
                st.markdown(extracted_text)
            except Exception as e:
                st.error(f"Error processing the image: {str(e)}")

else:
    st.info("Please upload an image to extract text.")

# Section for Downloading Results
if "ocr_result" in st.session_state:
    st.markdown("---")
    st.download_button(
        label="📥 Download as Markdown",
        data=st.session_state['ocr_result'],
        file_name="ocr_results.md",
        mime="text/markdown",
        use_container_width=True
    )

    # Allow the user to copy the raw markdown to clipboard
    st.markdown(
        "Or **copy the raw markdown** text for further use:",
        unsafe_allow_html=True
    )
    st.text_area("Raw Markdown", st.session_state['ocr_result'], height=200, disabled=True)

# Footer Section
st.markdown("---")
st.markdown(
    "Made with ❤️ by Christian Sada | Powered by [Llama 3.2 Vision](https://ollama.com)."
    " | [Report Issues](christiansada787@gmail.com)",
    unsafe_allow_html=True
)
