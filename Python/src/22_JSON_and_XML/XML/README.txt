lxml dependencies were not installed properly.  
The following commands resolved the problem:

brew install libxml2
brew install libxslt
brew link libxml2 --force
brew link libxslt --force