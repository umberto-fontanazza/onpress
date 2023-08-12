# onpress

## dependencies

I tried https://github.com/boppreh/keyboard package at first to attach an handler to the keydown event but as well as this
package works on Windows, it crashed on mac OS (possibly due to lacking permissions)

The second option I'm trying is https://github.com/moses-palmer/pynput
Before installing with pip make sure you are using pip installed inside the right conda env
Other versions of pynput give problems but 1.7.6 seems to work fine.
    pip install pynput==1.7.6