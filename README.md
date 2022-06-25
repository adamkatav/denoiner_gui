# denoiner_gui
## Instuctions
````bash
mkdir denoiser && cd denoiser
````
````bash
git clone 'https://github.com/WajdBoulos/real_time_speech_denoiser.git' && git clone 'https://github.com/adamkatav/denoiner_gui.git'
````
Download and extract pip virtual enrivonment
````bash
wget -qO- 'https://technionmail-my.sharepoint.com/:u:/g/personal/adamkatav_campus_technion_ac_il/EWclzVkdRyJIhjE9cNEMBEABqQwrO2-1NwKtlHrgxuYVhQ?download=1' | tar xvz
````
Activate env
````bash
source ./env/bin/activate
````
from the parent directory run:
````bash
python ./denoiner_gui/main.py
````
### notes:
In order to run without terminal you may have to make main.py executable like so:
````bash
chmod +x ./denoiner_gui/main.py
````
Also, you may have to use the "fix_requirements_linux" branch in "real_time_speech_denioser" repo
````bash
cd real_time_speech_denoiser && git checkout fix_requirements_linux && cd ..
````
