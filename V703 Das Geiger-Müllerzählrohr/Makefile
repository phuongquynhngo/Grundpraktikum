all: build/main.pdf

# hier Python-Skripte:
build/Charakteristik.pdf: Charakteristik.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python Charakteristik.py
build/Zaehlrohrstroms.pdf: Zaehlrohrstroms.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python Zaehlrohrstroms.py

# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/main.pdf: build/Charakteristik.pdf
build/main.pdf: build/Zaehlrohrstroms.pdf


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
