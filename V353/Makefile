all: build/main.pdf

# hier Python-Skripte:
build/plot.pdf: plot.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python plot.py

build/Polarplot2.pdf: Polarplot2.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python Polarplot2.py
build/Regression-arctan.pdf: Regression-arctan.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python Regression-arctan.py
build/Regression-exp.pdf: Regression-exp.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python Regression-exp.py
build/Regression-gerade.pdf: Regression-gerade.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python Regression-gerade.py


# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/main.pdf: build/plot.pdf

build/main.pdf: build/Polarplot2.pdf
build/main.pdf: build/Regression-arctan.pdf
build/main.pdf: build/Regression-exp.pdf
build/main.pdf: build/Regression-gerade.pdf


build/main.pdf: FORCE | build
	  TEXINPUTS=build: \
	  BIBINPUTS=build: \
	  max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	main.tex

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean
