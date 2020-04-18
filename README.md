# mmkk

In `.config/fish/config.fish`:
```
alias kk="source /path/to/kkmm/kk.sh"
set PATH /path/to/kkmm  $PATH
```

In the directory `mmkk`, create a file named `path.txt` containing
only the path to the directory `mmkk`.
Since `kk` is going to be sourced, I do not know how to make him know its
own working directory.
