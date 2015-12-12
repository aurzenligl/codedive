all: build build/main.pdf

build:
	mkdir build

jpgs := $(wildcard *.jpg)

build/main.pdf: main.tex $(jpgs)
	latexmk -pdf -output-directory=build $<
