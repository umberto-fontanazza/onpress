# onpress

This project uses conda as package manager, after cloning use
`conda env create -f environment.yml`
to replicate the same environment on your machine

## dependencies

This package ttps://github.com/boppreh/keyboard seems out of date, therefor I went for pynput

The second option I'm trying is https://github.com/moses-palmer/pynput
Before installing with pip make sure you are using pip installed inside the right conda env
Other versions of pynput give problems but 1.7.6 seems to work fine.
    pip install pynput==1.7.6

### finding images of keys
https://www.wpclipart.com/computer/keyboard_keys/

### todo
- elements must be added to the window with the proper size
- animate adding elements to the window and removal

### bugs
- images with unusual aspect ratio, cause blank spaces between shown keys to appear

### problems
- init of KeyDisplayer never finishes execution because of window.mainloop(), a separate start() method should be
created to avoid this problem