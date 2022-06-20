from asyncore import read

from torch import sign
from PyQt5 import QtWidgets, uic
import sys
import subprocess
import signal

class Ui(QtWidgets.QMainWindow):

    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('./adam_gui_wtf/main.ui', self)
        self.btn_start.clicked.connect(self.start_click)
        self.btn_stop.clicked.connect(self.stop_click)
        self.show()

    def start_click(self): #Start button callback
        print('start clicked!!')
        #Getting input info
        if(self.radio_in_mic.isChecked()):
            in_type = 'microphone_reader'
            in_addional_args = '{"samplerate":16000.0, "blocksize":1024}'
            in_args = f'{{"additional_args":{in_addional_args}}}'
        elif(self.radio_in_file.isChecked()):
            in_type = 'file_reader'
            in_args = f'"path":"{self.text_in_path.toPlainText()}", "blocksize":4096, "sample_size":4'
        reader = f'"type":"{in_type}", "args":{in_args}'
        pipeline = '[{"type":"DCCRN_processor", "args":{"sample_size":4, "should_overlap":True, "ratio_power":1, "model_path":"./models/DCCRN_sr_16k_batch_16_correct_BN_stft_lookahead.pth"}},]'
        # Getting ouput info
        if(self.radio_out_file.isChecked()):
            path = self.text_out_path.toPlainText()
            writers = f'[{{"type":"file_writer", "args":{{"path":"{path}", "blocking_time":0.0001}}}},]'
        elif(self.radio_out_net.isChecked()):
            ip = self.text_out_ip.toPlainText()
            port = self.text_out_port.toPlainText()
            writers = f'[{{"type":"socket_writer", "args":{{"dest":["{ip}", {port}]}}}},]'
        config_text = f'{{\n    "reader": {{{reader}}},\n    "pipeline": {pipeline},\n    "writers": {writers},\n}}'
        with open('settings.yaml', 'w') as f:
            f.write(config_text)
        self.start_script = subprocess.Popen('./adam_gui_wtf/start.sh')
        return
    
    def stop_click(self): #Stop button callback
        print('stop clicked!!')
        try:
            self.start_script.send_signal(signal.SIGINT)
        except:
            pass
        return


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
