############################################################
#
#        Function Prototypes
#
############################################################

my @array = qw(monday tuesday wednesday thursday friday);

MySub(@array);           # array gets cast to $$@


sub MySub($$@) {
    my ($a, $b, @array) = @_;

    print("$a \n");
    print("$b \n");
    print("@array \n");
}