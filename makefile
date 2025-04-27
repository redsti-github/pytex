PARSER_TARGETS := arithmetic.tex  bitwise.tex  comparison.tex  compound_stmt.tex  expression.tex  primary.tex  simple_stmt.tex
PARSER_TARGETS := $(addprefix parser/, $(PARSER_TARGETS))

RUNTIME_TARGETS := bool.tex  int.tex
RUNTIME_TARGETS := $(addprefix runtime/, $(RUNTIME_TARGETS))

TARGETS :=  active_chars.tex stack.tex list.tex localvar.tex tokeniser.tex parser.tex $(PARSER_TARGETS) runtime.tex $(RUNTIME_TARGETS)
TARGETS := $(addprefix build/, $(TARGETS))


.PHONY: main.pdf
main.pdf: main.tex py.tex
	xetex main.tex

.PHONY: v
v: main.pdf
	xdg-open main.pdf


py.tex: $(TARGETS)
	cp src/py.tex build/py.tex
	python3 src/expand.py build/py.tex
	cp build/py.tex py.tex

build/active_chars.tex: src/gen_active.py
	python3 src/gen_active.py

build/tokeniser.tex: src/gen_token.py src/tokeniser.tex
	python3 src/gen_token.py

build/%.tex: src/%.tex
	@mkdir -p $(@D)
	@cp $^ $@




.PHONY: clean
clean:
	rm *.log *.pdf -f
	rm out.* -f
	rm -rf build/
	rm -rf __pycache__/
	
