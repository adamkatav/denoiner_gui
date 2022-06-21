# denoiner_gui
You need to place "adam_gui_wtf" in the same directory as "real_time_speech_denoiser"

Please use this repo requirements.txt in virtual env.
````
mkdir denoiser && cd denoiser
````
````
git clone https://github.com/WajdBoulos/real_time_speech_denoiser.git && git clone https://github.com/adamkatav/denoiner_gui.git
````
Create and activate pip virtual environment
````
python -m venv env
````
````
source env/bin/activate
````
Install pip packages
````
pip install -r ./requirements.txt
````
from the parent directory run:
````
python ./adam_gui_wtf/main.py
````
