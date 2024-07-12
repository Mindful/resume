# Resume
This repository holds my personal resume, and a simple script to build variations of it in multiple lengths/languages. 

## PII
Personally identifiable information is intentionally excluded from the repo and has to be added by creating a file that contains entries like this
```latex
\newcommand{\phonenumber}{xxx-yyy-zzzz}
\newcommand{\email}{email@domain.com}
\newcommand{\linkedin}{www.linkedin.com/in/linkedinid/}
\newcommand{\github}{https://github.com/githubid/}
```

## Requirements
Noto sans
```shell
# linux
apt install fonts-noto latex-cjk-al texlive-fonts-extra

# mac
brew tap homebrew/cask-fonts 
brew install font-noto-sans
brew install font-noto-sans-cjk
```




