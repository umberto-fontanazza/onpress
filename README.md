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
- window must resize if elements are added or removed
- elements must be added to the window with the proper size
- animate adding elements to the window and removal
- removing elements from the image buffer when deleting