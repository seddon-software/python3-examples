my ($oldText, $newText);
my %days = ( 'mon' => 'Monday', 
             'tue' => 'Tuesday',
             'wed' => 'Wednesday', 
             'thu' => 'Thursday', 
             'fri' => 'Friday' );
my $pattern = join ('|', keys %days);
print "pattern: $pattern \n";

$oldText = "Today is wed, but tomorrow is thu - END";
print "Original text:   $oldText \n";

while ($oldText =~ /$pattern/) 
{
	$newText .= $`;
	$newText .= $days{$&};
	$oldText = $';
}

$newText .= $oldText;
print "Translated text: $newText \n";

1
