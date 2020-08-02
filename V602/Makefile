all: build/main.pdf

# hier Python-Skripte:
build/Bragg.pdf: Bragg.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python Bragg.py
build/EmissionCu.pdf: EmissionCu.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python EmissionCu.py
build/Zink.pdf: Zink.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python Zink.py
build/Gallium.pdf: Gallium.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python Gallium.py
build/Brom.pdf: Brom.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python Brom.py
build/Rubidium.pdf: Rubidium.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python Rubidium.py
build/Strontium.pdf: Strontium.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python Strontium.py
build/Zirkonium.pdf: Zirkonium.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python Zirkonium.py
build/Rydberg.pdf: Rydberg.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python Rydberg.py
# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/main.pdf: build/Bragg.pdf
build/main.pdf: build/EmissionCu.pdf
build/main.pdf: build/Zink.pdf
build/main.pdf: build/Gallium.pdf
build/main.pdf: build/Brom.pdf
build/main.pdf: build/Rubidium.pdf
build/main.pdf: build/Strontium.pdf
build/main.pdf: build/Zirkonium.pdf
build/main.pdf: build/Rydberg.pdf

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
