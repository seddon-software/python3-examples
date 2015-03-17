##########################################################
#
#	stat()
#
##########################################################


@FileDetails = stat("C:/autoexec.bat");
print "@FileDetails \n";

($dev, $ino, $mode, $nlink, $uid, $gid, $rdev, $size,
 $atime, $mtime, $ctime, $blksize, $blocks) = @FileDetails;

print "ctime: $ctime \n";
print "user:  $uid \n";

1