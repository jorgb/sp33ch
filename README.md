See: https://github.com/mozilla/DeepSpeech

## RUN
virtualenv -p python3 $HOME/tmp/deepspeech-venv/
source $HOME/tmp/deepspeech-venv/bin/activate

## INSTALL ONCE

# Install DeepSpeech
pip3 install deepspeech

# Download pre-trained English model and extract
curl -LO https://github.com/mozilla/DeepSpeech/releases/download/v0.5.1/deepspeech-0.5.1-models.tar.gz
tar xvf deepspeech-0.5.1-models.tar.gz

# Download example audio files
curl -LO https://github.com/mozilla/DeepSpeech/releases/download/v0.5.1/audio-0.5.1.tar.gz
tar xvf audio-0.5.1.tar.gz

# Transcribe an audio file
deepspeech --model deepspeech-0.5.1-models/output_graph.pbmm --lm deepspeech-0.5.1-models/lm.binary --trie deepspeech-0.5.1-models/trie --audio audio/2830-3980-0043.wav

## TESTING

# Upload audio
curl -F 'audio_file=@/home/jorgb/testdata/audio_file.wav' http://localhost:5000/upload
id returned: 1ddfa1b5-d0d4-433c-ab3a-2abdf7ad9893


# Execute deepspeech
curl http://localhost:5000/api/1ddfa1b5-d0d4-433c-ab3a-2abdf7ad9893/deepspeech
Response:
{
  "text": "b'and her look would them it as a pigment alma i did\\n'"
}

