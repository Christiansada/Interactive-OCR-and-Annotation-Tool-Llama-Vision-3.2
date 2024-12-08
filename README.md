# Interactive OCR and Annotation Tool: Llama Vision 3.2

This repository hosts a Streamlit-based application that performs Optical Character Recognition (OCR) and annotation using **Llama 3.2 Vision**. Upload an image, extract structured text and annotations, and download the results in Markdown format—all within an interactive interface.

---

## Project Overview

The **Llama OCR+** tool leverages state-of-the-art computer vision and language models to extract text from images with added annotations. This tool is ideal for processing documents, flyers, or any visual content requiring structured text extraction and formatting.

---

## Features

1. **OCR with Annotations**:
   - Upload images in PNG, JPG, or JPEG formats.
   - Extract text with annotations in Markdown format.

2. **Interactive Interface**:
   - Built with **Streamlit** for a clean and responsive user experience.
   - Preview uploaded images and process them in seconds.

3. **Download and Export**:
   - Download extracted text as a Markdown file.
   - Copy raw Markdown for further use.

---

## Project Structure

- **Application**: `app.py`  
  Contains the Streamlit application code to handle image uploads, OCR processing, and Markdown export.

- **Dataset**: Not applicable (the tool processes user-uploaded images dynamically).

- **Requirements**: `requirement.txt`  
  Specifies the dependencies required to run the application.

---

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Llama-OCR-Annotation-Tool.git
   cd Llama-OCR-Annotation-Tool
2. Install the required Python packages:
    ```bash
    pip install -r requirement.txt
3. Run the Streamlit application:
   ```bash
   streamlit run app.py
4. Open your browser and navigate to:
   ```bash
   http://localhost:8501
5. Upload an image and extract text with annotations! 

