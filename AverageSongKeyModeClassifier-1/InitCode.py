# Remarks: This file is designed for copy-paste directly on Python interpreter shell.

# Configure project parameters here.
def apply_params():
	# Choose default function for this alias (Useful when using different platform).
	load_audio_from_system_input=load_audio_from_linux_system_input

## Initialization
### Python Import
import np_chaonay.main as npc_m
import scipy.io.wavfile as scp_io_wavfile

### Namespace declaration
gen_io=npc_m.Namespace('General I/O')
data_proc=npc_m.Namespace('Data Processing')

### Function defination (Unfinished)
# Function: Load audio from local storage.
def temp_fun():
	pass

gen_io.load_audio_from_storage=temp_fun

# Function: Load audio from system audio input (Linux).
def temp_fun():
	pass

gen_io.load_audio_from_linux_system_input=temp_fun

# Function: Load audio from Youtube.
def temp_fun():
	pass

gen_io.load_audio_from_Youtube=temp_fun
