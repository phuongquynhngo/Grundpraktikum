all: build/main.pdf

# hier Python-Skripte:
#build/plot.pdf: plot.py matplotlibrc header-matplotlib.tex | build
	#TEXINPUTS=$$(pwd): python plot.py
build/rot.pdf: rot.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python rot.py
build/gelb.pdf: gelb.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python gelb.py
build/grün.pdf: grün.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python grün.py
build/blaugrün.pdf: blaugrün.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python blaugrün.py
build/violet.pdf: violet.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python violet.py		
build/gegenspannung.pdf: gegenspannung.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python gegenspannung.py		
build/deutung.pdf: deutung.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python deutung.py

# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
#build/main.pdf: build/plot.pdf
build/main.pdf: build/rot.pdf
build/main.pdf: build/gelb.pdf
build/main.pdf: build/grün.pdf
build/main.pdf: build/blaugrün.pdf
build/main.pdf: build/violet.pdf
build/main.pdf: build/deutung.pdf
build/main.pdf: build/gegenspannung.pdf

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
