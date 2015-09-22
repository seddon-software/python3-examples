##########################################################
#
#	Extracting Hosts and IP addresses
#
##########################################################

use strict;

# patterns
my $spaces = "\\s*";
my $dot = "\\.";
my $digits = "\\d+";
my $hostPattern = "$digits$dot$digits$dot$digits$dot$digits";
my $hostName = "\\w+";
my $macPattern = "e:[0-9A-Fa-f:.]+";


# read in data from file
my ($IN);
chdir("../Data Files");
my $fileName = "hosts.real";
open($IN,  "<", $fileName) || die "Can't open $fileName";
my @allLines = <$IN>;
close($IN);



# strip out comments and mac addresses
my @strippedLines;
foreach my $line (@allLines)
{
	chomp($line);
	$line =~ m{  ^([^#]*)         # text before comment
	             [#]*.*$          # comment to end of line
              }x;
    my $text1 = $1 if($1);		  
    # comments now stripped
	
	$text1 =~ m{  ^(.*?)e:        # text before mac address
              }x;
    my $text2 = $1 if($1);;		
    # comments and mac addresses now stripped
    
    # debug information
#	print "$text1\n";
#	print "$text2\n";
	
	# add entries to array    
    push(@strippedLines, $text2) if($text2 =~ /[.]/);
}

# add IP addresses to hash
my % ipAddresses;

foreach my $line (@strippedLines)
{
	$line =~ m{  ^
		         \s*
		         ($hostPattern)
		         $spaces
		         ((?:$hostName$spaces)+)	# don't capture - can be multiple hostNames
              }x;
	my $ip = $1;
	my $hostNames = $2;
	
	# add to hash
	$ipAddresses{$ip} = $hostNames;
	1
}

# print out hash
my ($key, $value);
while (($key, $value) = each(%ipAddresses)) 
{
	print "$key $value \n";
}
