all: build/main.pdf

# hier Python-Skripte:
build/Vanadium.pdf: Vanadium.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python Vanadium.py
build/Vanadiumausgleichung.pdf: Vanadiumausgleichung.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python Vanadiumausgleichung.py
build/Rhodium.pdf: Rhodium.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python Rhodium.py
build/Rhodiumausgleichung.pdf: Rhodiumausgleichung.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python Rhodiumausgleichung.py
# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/main.pdf: build/Vanadium.pdf
build/main.pdf: build/Vanadiumausgleichung.pdf
build/main.pdf: build/Rhodium.pdf
build/main.pdf: build/Rhodiumausgleichung.pdf

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
