from django.shortcuts import render
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.tree import DecisionTreeClassifier

def index(request):
    return render(request, 'Home.html')

def Views(request):
    if request.method == 'POST':
        # Assuming the form field name is 'news_text'
        news_text = request.POST.get('news_text', '')

        # Read the CSV file
        df = pd.read_csv("train.csv")

        # Assuming 'text' column contains text data and 'label' column contains labels
        x = df['text']
        y = df['label']

        # Vectorize the text data
        vectorizer = CountVectorizer()
        x_vectorized = vectorizer.fit_transform(x)

        # Initialize and train the model
        model = DecisionTreeClassifier()
        model.fit(x_vectorized, y)

        # Vectorize the user input
        user_input_vectorized = vectorizer.transform([news_text])

        # Perform prediction
        prediction = model.predict(user_input_vectorized)

        # Display the result on the Views.html page
        result_text = "reliable" if prediction[0] == 1 else "unreliable"
        return render(request, 'Views.html', {'result': result_text, 'user_input': news_text})
    else:
        # Render the initial Views.html page (GET request)
        return render(request, 'Views.html')
