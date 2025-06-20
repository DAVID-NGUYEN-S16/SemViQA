#!/usr/bin/env bash
nvidia-smi
source ~/.bashrc

# Log GPU utilization in background
while true; do nvidia-smi > gpu_status.txt; sleep 5; done &

export PYTHONPATH="/kaggle/working/SemViQA:$PYTHONPATH"
cd /kaggle/working/SemViQA
# ---------------------------
# Training parameters
# ---------------------------
BS=6            # Effective per-device batch size
EPOCHS=16        # Number of training epochs
LR=2e-6          # Learning rate
MODEL_NAME="microsoft/infoxlm-large"  # Base model (change if desired)
OUTPUT_DIR="./output_deepspeed"
DS_CONFIG="./semviqa/ser/ds_zero2.json"

# Launch training with 🤗 Accelerate + DeepSpeed (Stage-2)
accelerate launch \\
    --multi_gpu \\
    --num_processes $(nvidia-smi -L | wc -l) \\
    ./semviqa/ser/main_ds.py \\
        --model_name "microsoft/infoxlm-large" \\
        --output_dir "$OUTPUT_DIR" \\
        --train_batch_size $BS \\
        --num_train_epochs $EPOCHS \\
        --learning_rate $LR \\
        --train_data "/kaggle/input/semviqa-data/data/evi/viwiki_train.csv" \\
        --eval_data "/kaggle/input/semviqa-data/data/evi/viwiki_test.csv" \\
        --patience 5 \\
        --is_pretrained 0 \\
        --ds_config "$DS_CONFIG"

echo "DeepSpeed QATC training completed!"
