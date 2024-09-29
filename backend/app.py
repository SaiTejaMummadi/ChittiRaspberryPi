from flask import Flask, render_template, request, jsonify
import os
from datetime import datetime
from pydub import AudioSegment
import openai
from openai import OpenAI
from dotenv import load_dotenv

app = Flask(__name__)

# Load environment variables from .env file
load_dotenv()
client = OpenAI()

# Set your OpenAI API key securely
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')  # Loaded from .env file
if not OPENAI_API_KEY:
    raise ValueError("OpenAI API key not found. Please set the 'OPENAI_API_KEY' environment variable in the .env file.")
openai.api_key = OPENAI_API_KEY



# Ensure the recordings and transcriptions directories exist
RECORDINGS_DIR = os.path.join(os.getcwd(), 'recordings')
TRANSCRIPTIONS_DIR = os.path.join(RECORDINGS_DIR, 'transcriptions')
os.makedirs(RECORDINGS_DIR, exist_ok=True)
os.makedirs(TRANSCRIPTIONS_DIR, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_audio', methods=['POST'])
def process_audio():
    if 'audio_data' not in request.files:
        return jsonify({'status': 'error', 'message': 'No audio data received.'}), 400

    audio_file = request.files['audio_data']
    if audio_file.filename == '':
        return jsonify({'status': 'error', 'message': 'No selected file.'}), 400

    try:
        # Save the uploaded WebM file temporarily
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        temp_webm_filename = f'audio_{timestamp}.webm'
        temp_webm_path = os.path.join(RECORDINGS_DIR, temp_webm_filename)
        audio_file.save(temp_webm_path)

        # Convert WebM to MP3 using pydub
        mp3_filename = f'audio_{timestamp}.mp3'
        mp3_path = os.path.join(RECORDINGS_DIR, mp3_filename)

        # Load the WebM file
        audio = AudioSegment.from_file(temp_webm_path, format="webm")

        # Export as MP3
        audio.export(mp3_path, format="mp3")

        # Remove the temporary WebM file
        os.remove(temp_webm_path)

        return jsonify({'status': 'success', 'message': f'Audio saved as {mp3_filename}.', 'filename': mp3_filename}), 200

    except Exception as e:
        # In case of any error, ensure no zero-byte files are left
        if os.path.exists(temp_webm_path):
            os.remove(temp_webm_path)
        return jsonify({'status': 'error', 'message': f'Error processing audio: {e}'}), 500

@app.route('/convert_stt', methods=['POST'])
def convert_stt():
    data = request.get_json()
    if not data or 'filename' not in data:
        return jsonify({'status': 'error', 'message': 'No filename provided.'}), 400

    filename = data['filename']
    audio_path = os.path.join(RECORDINGS_DIR, filename)

    # Check if the MP3 file exists
    if not os.path.exists(audio_path):
        return jsonify({'status': 'error', 'message': 'Audio file not found.'}), 404

    try:
        # Open the audio file in binary read mode
        with open(audio_path, 'rb') as audio_file_stream:
            # Use OpenAI's Whisper API for transcription
            transcription = client.audio.transcriptions.create(model="whisper-1", file=audio_file_stream)

        # Extract the transcribed text
        print(transcription)
        transcribed_text = transcription.text

        # Save the transcription to a .txt file with _stt suffix in transcriptions folder
        base_filename = os.path.splitext(filename)[0]
        txt_filename = f'{base_filename}_stt.txt'
        txt_path = os.path.join(TRANSCRIPTIONS_DIR, txt_filename)
        with open(txt_path, 'w', encoding='utf-8') as txt_file:
            txt_file.write(transcribed_text)

        return jsonify({'status': 'success', 'message': f'Transcription saved as {txt_filename}.', 'transcription': transcribed_text}), 200

    except Exception as e:
        return jsonify({'status': 'error', 'message': f'Error during transcription: {e}'}), 500

if __name__ == '__main__':
    app.run(debug=True)