#!/bin/bash

# Default log directory
LOGDIR="${1:-./logs}"

# Default port
PORT="${2:-6006}"

# Start TensorBoard
tensorboard --logdir "$LOGDIR" --port "$PORT" &

# Wait a moment for TensorBoard to start
sleep 2

# Open TensorBoard in the default browser
"$BROWSER" "http://localhost:$PORT"