build_mail:
	tail -n +5 Obsidian/Obsidian/list,\ verbal-language.md > voc.txt
	random_voc=$$(cat voc.txt | shuf -n 1) && \
	python3 create_mail.py "$$random_voc"


update: # update obsidian to have latest notes
	git submodule update --remote # Git knows what to update thanks to the .gitmodules file
	git add .
	git commit -m "Automatically update submodule to latest versions"
	git push

.PHONY: update build_mail
