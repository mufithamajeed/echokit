import whisper

def transcribe_video(video_path, model_size='base'):
    model = whisper.load_model(model_size)
    result = model.transcribe(video_path)
    return result['text'], result['segments']
