import librosa
import torch
from transformers import pipeline, Wav2Vec2Tokenizer, Wav2Vec2ForCTC

def load_model():
    # load pre-trained model and tokenizer
    tokenizer = Wav2Vec2Tokenizer.from_pretrained("facebook/wav2vec2-base-960h")
    model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")
    return tokenizer, model

def load_audio(audio):
    tokenizer, model = load_model()
    # load any audio file of your choice
    speech, rate = librosa.load(audio, sr=16000)
    input_values = tokenizer(speech, return_tensors='pt').input_values
    # Store logits (non-normalized predictions)
    logits = model(input_values).logits
    # Store predicted id's
    predicted_ids = torch.argmax(logits, dim=-1)
    # decode the audio to generate text
    transcriptions = tokenizer.decode(predicted_ids[0])
    print(transcriptions) 
