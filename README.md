# **ENIGMA** #

Inference guiding machine for saturation-based Automated Theorem Provers.

## User Install

This is enough if you plan to use Enigma.  There is no need to clone this
repo manually.

```console
pip install git+https://github.com/ai4reason/enigma --process-dependency-links --user
```

This installs:

* Python packages `atpy` and `enigma` from GitHub
* other Python dependencies (`xgboost`, `numpy`, ...)
* statically compiled binaries for `eprover` with Enigma support, Enigma
  feature extractor `enigma-features`, and LIBLINEAR training and prediction
  binaries `train` and `predict`.

## Developers

You need this only if you plan to update the source codes.

1. Install `atpy`:

   ```console
   $ git clone https://github.com/ai4reason/atpy.git
   $ cd atpy
   $ pip install -e . --user
   ```

2. Install `enigma`:

   ```console
   $ git clone https://github.com/ai4reason/enigma.git
   $ cd enigma
   $ pip install -e . --user
   ```

After this, the `git pull` command issued in both `atpy` and `enigma`
directories will automatically update both Python packages to their latest
development versions from GitHub.

## Credits

Development of this software prototype was supported by: 

+ ERC Consolidator grant no. 649043 *AI4REASON*
+ ERC Starting grant no. 714034 *SMART*
+ FWF grant P26201
+ Cost Action CA15123 *EUTypes*

