############################################################
#
#        void, scalar and list context
#
############################################################

use Contextual::Return;
use Carp;

sub foo {
	return SCALAR   { 'thirty-twelve' }
           BOOL     { 0 }
           NUM      { 7 * 6 }
           STR      { 'forty-two' }
           LIST     { 1, 2, 3, 6, 4 }
           HASHREF  { { name => 'foo', value => 99 } } 
           ARRAYREF { [ 6, 3, 2, 1 ] }
           GLOBREF  { \*STDOUT } 
           CODEREF  { sub { print "this is an anonomous sub \n"} };
}

# scalar context
my $foo = foo();
print ("string:    " . $foo              , "\n");   # note the dot operator
print ("bool:      " , foo() ? "T" : "F" , "\n");
print ("number:    " , $foo + 1          , "\n");
print ("array ref: " , @{$foo}           , "\n");
print ("hash ref:  " , %{$foo}           , "\n");

# list context
my @foo = foo();
print ("list: "      , @foo              , "\n");

# file handle
print {$foo} "file handle: this is some text\n";

# function pointer
&{$foo}();

1;

