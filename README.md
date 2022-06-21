# denoiner_gui
You need to place "denoiner_gui" in the same directory as "real_time_speech_denoiser"
````
mkdir denoiser && cd denoiser
````
````
git clone https://github.com/WajdBoulos/real_time_speech_denoiser.git && git clone https://github.com/adamkatav/denoiner_gui.git
````
Download and extract pip virtual enrivonment
````
wget -qO- https://technionmail-my.sharepoint.com/:u:/g/personal/adamkatav_campus_technion_ac_il/EWclzVkdRyJIhjE9cNEMBEABqQwrO2-1NwKtlHrgxuYVhQ?download=1 | tar xvz
````
Activate env
````
source ./env/bin/activate
````
from the parent directory run:
````
python ./denoiner_gui/main.py
````
