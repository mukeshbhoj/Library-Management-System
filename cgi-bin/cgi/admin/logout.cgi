#!/usr/bin/perl -w

use warnings;

use HTML::Template;
use CGI;
use CGI::Session;
use CGI::Cookie;

my $cgi = CGI->new();
my $session = CGI::Session->new();
$session->delete();
$session->flush();
print $cgi->redirect(-url=>'/cgi-bin/library.cgi');
