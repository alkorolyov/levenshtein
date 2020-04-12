# Straight forward realization of dameralu-levenshtein distance on Cython. #

In order to compile you need Cython installed.

Change one line in build.cmd:

call "D:\Soft\anaconda3\Scripts\activate.bat" "D:\Soft\anaconda3"
to
call "YourAnaconda3Path\Scripts\activate.bat" "YourAnaconda3Path"

Save your cython code in "yournewmodule.pyx" then run "build yournewmodule.pyx". This would compile your cython module and install it as a package in current anaconda env. To use it in other python files:

from yournewmodule import *
# python code here
