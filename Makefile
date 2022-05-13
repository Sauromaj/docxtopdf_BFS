cdocxtopdf: 
	python3 cdocxtopdf.py
cleandocx:
	rm *.docx
cleanpdfs:
	rm -rf Allpdfs
clean: cleandocx cleanpdfs
	
