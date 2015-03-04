############################################################
#
#        void, scalar and list context
#
############################################################

GetData();      print "---\n";  # void context
$x = GetData(); print "$x \n";  # scalar context
@a = GetData(); print "@a \n";  # list context


sub GetData {
    if(wantarray()) {
        print "list context: ";
        return (25 .. 40);
    }

    if(defined wantarray()) {
        print "scalar context: ";
        return 999;
    }

    if (not defined wantarray()) {
        print "void context: ";
        return;
    }
}
