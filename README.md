# onpress

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
- removing elements from the image buffer when deleting
- handle keys which are not squared, the images must be loaded with different dimensions and
the window must resize accordingly