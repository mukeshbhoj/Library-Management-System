#!/usr/bin/perl -w
use strict;
use DBI;
use CGI;
use HTML::Template;
use Data::Dumper;
my %fields;
my $i=0;
	


my $query = CGI->new();
my $username = $query->param('username');
my $password = $query->param('password');

my $conn = DBI->connect( 'dbi:Pg:dbname=postgres;host=127.0.0.1','postgres','mangeskaray',{AutoCommit=>1,RaiseError=>1,PrintError=>0});
my $query1 = $conn->prepare("SELECT * FROM employee");
$query1->execute();
my $template1 = HTML::Template->new(filename => '/var/www/project/html/header.tmpl'); 
while(my @op = $query1->fetchrow_array())
{
	my ($id,$name,$dept,$sal,$pass) = @op;
	if($username eq $name && $password eq $pass){
		$template1->param(USERNAME => "Welcome $name");
		$i++;
	}	
}
if($i == 0){
	$template1->param(USERNAME => "oops.....Username or password is incorrect.");
}
  
my $template2 = HTML::Template->new(filename => '/var/www/project/html/home.tmpl'); 
my $template3 = HTML::Template->new(filename => '/var/www/project/html/footer.tmpl'); 

undef($query);
$conn->disconnect();
$conn = undef;

print $query->header(), $template1->output,$template2->output,$template3->output;

