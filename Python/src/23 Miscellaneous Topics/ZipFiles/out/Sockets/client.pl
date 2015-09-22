#!/bin/perl
##########################################################
#
#	Client
#
##########################################################

use IO::Socket;

$connection=new IO::Socket::INET(PeerAddr => 'localhost',
                                 PeerPort => 1200,
                                 Proto    => 'tcp');
                                 
die "Socket could not be created.Reason: $!" unless $connection;

foreach (1..10)
{
  print $connection "Msg $_: How are you?\n";
  $connection->flush();
}

close($connection);
