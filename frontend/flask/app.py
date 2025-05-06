from flask import Flask, render_template, request, session, redirect, url_for
import requests

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for session management

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        session['prediction'] = None
        session['error'] = None

        if 'file' not in request.files:
            session['error'] = "No image file selected."
        else:
            image_file = request.files['file']
            if image_file:
                files = {'file': image_file}
                try:
                    response = requests.post("http://127.0.0.1:8000/api/v1/predict", files=files)
                    if response.status_code == 200:
                        data = response.json()
                        confidence_value = float(data['predictions']['confidence'])  # Ensure confidence is a float
                        if 0 <= confidence_value <= 1:  # Handle confidence as a fraction (e.g., 0.6829)
                            confidence_percentage = confidence_value * 100
                        else:  # Handle confidence already in percentage format (e.g., 68.29)
                            confidence_percentage = confidence_value

                        session['prediction'] = {
                            "class_name": data["predictions"]["class_name"],
                            "confidence": f"{confidence_percentage:.2f}%",  # Correctly format confidence
                            "inference_time": f"{data['inference_time']} ms",  # Ensure "ms" is not duplicated
                            "image_path": data.get("image_path")
                        }
                    else:
                        session['error'] = f"Prediction failed with status {response.status_code}"
                except Exception as e:
                    session['error'] = f"Request failed: {str(e)}"
        return redirect(url_for('index'))

    prediction = session.pop('prediction', None)
    error = session.pop('error', None)
    return render_template('index.html', prediction=prediction, error=error)

if __name__ == '__main__':
    app.run(debug=True)
