
.PHONY: py.pdf
py.pdf: py.tex active_chars.tex tokeniser.tex clean_macros.tex stack.tex parser.tex queue.tex
	rm py.pdf -f
	xetex py.tex

.PHONY: v
v: py.pdf
	google-chrome-stable py.pdf

active_chars.tex: gen_active.py
	python3 gen_active.py

tokeniser.tex: gen_token.py
	python3 gen_token.py

#clean_macros.tex: scan.py active_chars.tex tokeniser.tex py.tex
#	python3 scan.py

.PHONY: clean
clean:
	rm *.log *.pdf -f
	rm out.* -f
	rm -rf __pycache__
	
