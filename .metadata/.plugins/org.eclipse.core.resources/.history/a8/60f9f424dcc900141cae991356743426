##########################################################
#
#	Working with flat files
#
##########################################################

use strict;
use warnings;

my ($FileHandle, $fileName, $workingDirectory);
$fileName = "hosts.real";
$workingDirectory = "../Data Files";

# open file containing hosts and IPs
chdir($workingDirectory);
open($FileHandle, "<", $fileName) || die "can't open $fileName";
my @data = <$FileHandle>;
my @strippedData;

foreach my $line (@data)
{
	chomp($line);

	# remove comments
	$line =~ m{([^#]*)#?};
	my $text = $1;
	
	# remove MAC addresses
	$text =~ m{
		((?:(?!e:).)*)	# ip and hostnames before MAC address
		(e[:][^ \t]*)?	# MAC address
		\s*(.*)			# any other hostnames
	}x;
	my $text1 = $1;
	my $text2 = $2;
	my $text3 = $3;
	
	push(@strippedData, $text1 . " " . $text3) if($text1);
	1
} 

foreach my $line (@strippedData)
{
	print "$line \n";	
}

1
