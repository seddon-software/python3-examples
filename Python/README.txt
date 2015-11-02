Last updated 26 October 2015

To clone the repo use:
	git clone git://git.assembla.com/python-examples.git




To push changes to the repo:
	cd <to-the-directory-containing-this-README>
	git add .
	git commit -m "some comment"
	git push origin master


The repo on assembla can be visited at:
	https://www.assembla.com/code/python-examples/git/nodes/master

To find the largest 10 files in these examples:
	find . -type f -ls | sort -k7nr | head -10