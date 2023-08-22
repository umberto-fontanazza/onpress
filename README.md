# onPress
This app displays pressed keyboard keys on the screen to help record video tutorials.

## Environment
This project uses conda as package manager, after cloning use
`conda env create -f environment.yml`
to replicate the same environment on your machine.
To update the dependencies use
`conda env export --no-builds > environment.yml`

## Keys images
I borrowed key images from the following website:
https://www.wpclipart.com/computer/keyboard_keys/

## Todo
- add animations
- add platform specific keys support (cmd vs Windows key)
- add .png transparenct support
- keep onPress always as topmost window
- add icon
- add options menu