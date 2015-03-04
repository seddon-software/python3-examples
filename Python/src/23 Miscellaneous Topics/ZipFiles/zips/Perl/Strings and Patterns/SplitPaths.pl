##########################################################
#
#	Using $1, $2 in patterns
#
##########################################################



$path1 = "/usr/bin/ls";
$path2 = "/homedir/user407/.cshrc";
$path3 = "../../../awkscript";
$path4 = "./phone.list";

PrintHeadings();

foreach $path ($path1, $path2, $path3, $path4)
{
  PrintNames($path);
}

############################################################

sub PrintNames
{
  my $name   = $_[0];
  $dir       = ".*";
  $separator = "/";
  $file      = ".*";
  $name =~ /($dir)$separator($file)/;
  printf("%-20s%-20s\n", $1, $2);
}

sub PrintHeadings
{
  printf("%-20s%-20s\n", "Directory", "File");
  printf("%-20s%-20s\n", "=========", "====");
}