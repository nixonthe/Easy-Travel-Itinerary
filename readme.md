# Travel Itinerary Recommendation System

## Overview

This project showcases an advanced **Travel Itinerary Recommendation System**, designed to intelligently recommend personalized travel plans using state-of-the-art language models. The system integrates a Retrieval-Augmented Generation (RAG) pipeline with ChatGPT, powerful language models, to generate recommendations based on user queries and a database of curated travel data.

---

## Features

1. **Data-Driven Recommendations**:
   - The system uses a curated CSV dataset containing travel information to provide personalized suggestions.

2. **RAG Pipeline Integration**:
   - Combines retrieval-based search with generative responses to ensure recommendations are both accurate and contextually relevant.

3. **State-of-the-Art Language Model**:
   - Used by Chat-GPT 4o mini for high-quality, natural language responses.

4. **User Interface**:
   - Includes a user-friendly interface for querying travel plans using **Streamlit** framework.

5. **Scalable Vector Search**:
   - Uses FAISS (Facebook AI Similarity Search) for fast and efficient similarity searches on the dataset.

---

## Project Workflow

1. **Dataset Preparation**:
   - Load and preprocess a dataset containing travel-related information.
   - Split data into smaller chunks for effective retrieval using FAISS.

2. **Model Loading**:
   - Leverage Chat-GPT for generative responses.

3. **Pipeline Creation**:
   - Build a Retrieval-Augmented Generation pipeline with LangChain, combining retrieval and generation seamlessly.

4. **User Interaction**:
   - Users can input queries about destinations or activities.
   - The system retrieves relevant information and generates personalized responses.

---

## Key Technologies

- **Python**: Core programming language for implementation.
- **LangChain**: Framework for building RAG pipelines.
- **Open AI API**: For integrating with Chat-GPT model zoo and embedding models.
- **FAISS**: High-performance vector search library.
- **Streamlit**: For building the user interface.
- **Pandas**: Data manipulation and preprocessing.

---

## Installation

1. Clone the repository:

   ```bash
   git clone <repository-link>
   cd easy-travel-itinerary
   
2. Install dependencies:

   ```bash
    pip install -r requirements.txt

3. Create .env file and use your own API key. You are free to use a different model, even though quality may be worse.

4. Run the application:

   ```bash
    streamlit run app.py

---

## User Interface

![demo.jpg](assets%2Fdemo.jpg)

---

## Future Enhancements

- Expand the dataset to include more destinations and details (e.g. restaurants, travel time between destinations).
- Enhance the application's security (e.g. minimize unnecessary user prompts and ensure the database is inaccessible to unauthorized users)
- Add support for multi-language queries and responses.
- More examples for users to showcase of app's capabilities.
- And more...

---

## Why This Project?
This project is a testament to my ability to design and implement an end-to-end AI system that combines cutting-edge machine learning models with practical applications. It reflects my passion for artificial intelligence and its potential to solve real-world problems, since I am quite experienced traveler, who know how to come up with interesting and concentrated travel plan. 

This initiative underscores my skills in:

- Programming and problem-solving.
- Machine learning and NLP.
- Integrating AI with user-friendly interfaces.
- I believe this project demonstrates the depth and breadth of my technical expertise, making it a perfect idea for my future startup.