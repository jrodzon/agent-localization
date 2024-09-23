all: main.pdf

# apt-get install texlive-full

define Show =
	-killall evince
	evince main.pdf 2>/dev/null &
endef

main.pdf: main.tex tex/[1-6]-*.tex *.bib
	rm -f main.aux
	pdflatex --shell-escape main
	biber main
	makeindex main.nlo -s nomencl.ist -o main.nls
	pdflatex --shell-escape main
	pdflatex --shell-escape main
	-grep --color=auto Warn main.log
	rm -f *.aux
	$(Show)

.PHONY: archive clean show

archive:
	git archive --prefix=main-h-adapt/ --output=../main-h-adapt.zip HEAD

clean:
	git clean -n -X | grep -v swp | sed 's/Would remove //' | xargs rm -f

show:
	$(Show)

