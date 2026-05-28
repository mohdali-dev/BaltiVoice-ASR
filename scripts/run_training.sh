#!/bin/bash
# BaltiVoice ASR — One-command training script
# Usage: bash scripts/run_training.sh hf_yourtoken

TOKEN=$1

if [ -z "$TOKEN" ]; then
    echo "❌ Please provide your HuggingFace token"
    echo "   Usage: bash scripts/run_training.sh hf_yourtoken"
    exit 1
fi

echo "🚀 Starting BaltiVoice ASR training..."

pip install -r requirements.txt -q

python src/train.py \
    --model_name    openai/whisper-small \
    --output_dir    ./whisper-balti \
    --max_steps     1000 \
    --learning_rate 1e-5 \
    --token         $TOKEN \
    --push_to_hub

echo "✅ Training complete!"
