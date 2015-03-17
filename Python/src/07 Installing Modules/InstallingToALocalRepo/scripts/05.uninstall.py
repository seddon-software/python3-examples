import pip

cmd = "uninstall -y mymodule-1.0-py2.7"
pip.main(cmd.split())
cmd = "uninstall -y mymodule-1.0"
pip.main(cmd.split())
cmd = "uninstall -y mymodule"
pip.main(cmd.split())
cmd = "show mymodule"
pip.main(cmd.split())
