all: build build/main.pdf

build:
	mkdir build

build/main.pdf: main.tex
	pdflatex --output-directory build $<
	pdflatex --output-directory build $<
