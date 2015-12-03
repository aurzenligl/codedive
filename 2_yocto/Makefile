all: build build/main.pdf

build:
	mkdir build

jpgs := $(wildcard *.jpg)

build/main.pdf: main.tex $(jpgs)
	pdflatex --output-directory build $<
	#pdflatex --output-directory build $<
