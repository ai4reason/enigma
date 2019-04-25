# **ENIGMA** #

Inference guiding machine for saturation-based Automated Theorem Provers.

## User Install

This is enough if you plan to use Enigma.

   $ pip install git+https://github.com/ai4reason/enigma --process-dependency-links --user

## Developers

You need this only if you plan to update the source codes.

1. Install `atpy`:

   $ git clone https://github.com/ai4reason/atpy.git
   $ cd atpy
   $ pip install -e . --user

2. Install `enigma`:

   $ git clone https://github.com/ai4reason/enigma.git
   $ cd enigma
   $ pip install -e . --user

After this, the `git pull` command issued in both `atpy` and `enigma`
directories will automatically update both Python packages to their latest
development versions from GitHub.

## Credits

Development of this software prototype was supported by: 

+ ERC Consolidator grant no. 649043 *AI4REASON*
+ ERC Starting grant no. 714034 *SMART*
+ FWF grant P26201
+ Cost Action CA15123 *EUTypes*

