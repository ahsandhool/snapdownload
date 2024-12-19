from flask import Flask, request, send_file, jsonify
import requests
from io import BytesIO

app = Flask(__name__)

@app.route('/download', methods=['POST'])
def download_video():
    data = request.get_json()
    video_url = data.get('url')

    if not video_url:
        return jsonify({'error': 'No URL provided'}), 400

    try:
        # Replace this logic with actual Snapchat video URL processing if needed.
        response = requests.get(video_url, stream=True)

        if response.status_code == 200:
            # Stream the video as a response
            return send_file(
                BytesIO(response.content),
                as_attachment=True,
                download_name='snapchat_video.mp4',
                mimetype='video/mp4'
            )
        else:
            return jsonify({'error': 'Failed to fetch the video'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
