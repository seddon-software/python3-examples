##########################################################
#
#	translate characters
#
##########################################################

print "Enter name: ";
chomp($OriginalName = <STDIN>);

$EncryptedName = $OriginalName;
$EncryptedName =~ tr /A-Za-z/B-ZAb-za/;

$DecryptedName = $EncryptedName;
$DecryptedName =~ tr /B-ZAb-za/A-Za-z/;

print "Original:  $OriginalName \n";
print "Encrypted: $EncryptedName \n";
print "Decrypted: $DecryptedName \n";

