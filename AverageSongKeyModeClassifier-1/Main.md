

# AverageSongModeClassifier-1
Classify average mode (major or minor) by extracting features from a song.

## Metadata
- Name: Average Song Mode Classifier (1)
- Description: Classify average mode (major or minor) by extracting features from a song.
- Author: NP-chaonay (Nuttapong Punpipat)
- Version: V.1.0.0_alpha
- Version Note: 
  - Major version: indicates of very significant changes or changes that break compatibility on some system/platforms.
  - Minor version: indicates of significant changes or features adding.
  - Micro version: indicates of small changes or bug patches, or even typo revising.
- Revised Date: 2020-0- : (UTC)
- License: MIT License
- Programming Language: Python
- CUI/GUI Language: English

## Definition/Glossary
> Wait for adding...

- **Pre-processed format**: Audio array consists of 1 channel 16-bit 44100Hz PCM, with specific-regions-cropped and necessary-filters applied.
- **specific-regions-cropped**: *`Waiting for adding...`*
- **Number in label**:
  - 0 : Song in major mode
  - 1 : Song in minor mode

## Abstract
> Wait for adding...

## Data gathering
> Wait for adding...

- (Recommended) n randomly-selected songs from searching on Youtube by yourself
  - Audio array from downloading Youtube video)
  - You should flag the target by yourself.
- n randomly-selected songs from MillionSongDataset
  - Audio array from downloading Youtube video)
  - Use "mode_confidence" dataset property as sample weight)
### User-specific datasets
- Institutional songs from "Bodindecha (Sing Singhaseni) 2 School"
  - Target=[ 0, 1, 1,  0, 1,  0,  0,  0,  0,  0,  0,  0, 1, 1]

## Data Processing Procedure
> Wait for adding...

1. Load the audio data in pre-processed format
    - From local stroage
    - From Youtube
    - From system audio input
2. 
3. Extract features using FFT-related
4. Cleaning the data by

## Project Requirements
> Wait for adding...

## Initialization Code
> Wait for adding...

See on *InitCode.py*

## Recommended Further Projects/Implementations
> Wait for adding...

- Song key classification
- Singing/Speaking classification
- English or Thai voice tone classification
