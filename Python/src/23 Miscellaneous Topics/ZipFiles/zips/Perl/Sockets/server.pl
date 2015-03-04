#!/bin/perl
##########################################################
#
#	Server
#
##########################################################

use IO::Socket;


$connection = new IO::Socket::INET(LocalHost => 'localhost',
                                   LocalPort => 1200,
                                   Proto     => 'tcp',
                                   Listen    => 5,
                                   Reuse     => 1);


die "Socket could not be created.Reason: $!" unless $connection;

while($new_connection = $connection->accept())
{
  while(defined($buffer = <$new_connection>))
  {
    print $buffer;
  }
}
