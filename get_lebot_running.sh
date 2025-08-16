sudo apt-get update
sudo apt-get install -y python3-dev pkg-config libavformat-dev libavcodec-dev libavdevice-dev libavfilter-dev libavutil-dev libswscale-dev libswresample-dev

git clone https://github.com/huggingface/lerobot.git
cd lerobot

#pip install av --no-binary av
#pip install -e ".[pusht]"
pip install -e .

#pip install 'lerobot[all]'          # All available features
#pip install 'lerobot[aloha,pusht]'  # Specific features (Aloha & Pusht)
#pip install 'lerobot[feetech]'      # Feetech motor support