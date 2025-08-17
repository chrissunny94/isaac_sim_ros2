





# FOR lerobot

activate the miniconda environment first 

```
source ~/miniconda3/bin/activate
conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/r
conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/main
conda create -y -n lerobot python=3.10
conda activate lerobot
```

I have CUDA 11.4 and Nvidia driver 470 , quiet old !
```
pip install --force-reinstall torch==2.0.1+cu117 torchvision==0.15.2+cu117 torchaudio==2.0.2+cu117 \
    --index-url https://download.pytorch.org/whl/cu117

```


- https://youtu.be/INDGt76GARY 