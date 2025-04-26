PARSER_TARGETS := arithmetic.tex  bitwise.tex  comparison.tex  compound_stmt.tex  expression.tex  primary.tex  simple_stmt.tex
PARSER_TARGETS := $(addprefix parser/, $(PARSER_TARGETS))

RUNTIME_TARGETS := bool.tex  int.tex
RUNTIME_TARGETS := $(addprefix runtime/, $(RUNTIME_TARGETS))

TARGETS := py.tex active_chars.tex stack.tex queue.tex localvar.tex tokeniser.tex parser.tex $(PARSER_TARGETS) runtime.tex $(RUNTIME_TARGETS)
TARGETS := $(addprefix build/, $(TARGETS))

.PHONY: build/py.pdf
build/py.pdf: $(TARGETS)
	rm build/py.pdf -f
	cd build && xetex py.tex

.PHONY: v
v: build/py.pdf
	xdg-open build/py.pdf

build/active_chars.tex: gen_active.py
	python3 gen_active.py

build/tokeniser.tex: gen_token.py
	python3 gen_token.py

build/%.tex: %.tex
	@mkdir -p $(@D)
	@cp $^ $@

.PHONY: clean
clean:
	rm *.log *.pdf -f
	rm out.* -f
	rm -rf build/
	rm -rf __pycache__/
	
