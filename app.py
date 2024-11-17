from flask import Flask, request, jsonify
from convertor import generate_translation
from flask_cors import CORS
app = Flask(__name__)
CORS(app, origins=["http://localhost:3000"])


@app.route('/convert', methods=['POST'])
def convert():
    # Get JSON data from the request body
    data = request.get_json()
    
    # Ensure input is provided
    if not data or 'text' not in data:
        return jsonify({"error": "No text provided"}), 400

    input_text = data['text']
    
    # Call your conversion logic
    isl_output = generate_translation(input_text)
    
    # Return the output as a JSON response
    return jsonify({"input": input_text, "output": isl_output})

if __name__ == "__main__":
    # Run the Flask server on port 8080
    app.run(host='0.0.0.0', port=8080)