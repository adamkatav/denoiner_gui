# denoiner_gui
You need to place "denoiner_gui" in the same directory as "real_time_speech_denoiser"

Please use this repo requirements.txt in virtual env.
````
mkdir denoiser && cd denoiser
````
````
git clone https://github.com/WajdBoulos/real_time_speech_denoiser.git && git clone https://github.com/adamkatav/denoiner_gui.git
````
Extract pip virtual enrivonment
````
tar -xzvf env.tar.gz
````
Activate env
````
source ./env/bin/activate
````
from the parent directory run:
````
python ./denoiner_gui/main.py
````
