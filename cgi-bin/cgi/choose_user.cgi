#!/usr/bin/perl -w
use strict;
use DBI;
use CGI;
use HTML::Template;
use Data::Dumper;
use CGI::Session;

my %fields;
my $i=0;
	
my $session = CGI::Session->new();
my $cgi = CGI->new();

my $query = CGI->new();
my $username = $query->param('username');
my $password = $query->param('password');

$username =~ s/'/\\'/g;
$password =~ s/'/\\'/g;

my $conn = DBI->connect( 'dbi:Pg:dbname=postgres;host=127.0.0.1','postgres','mangeskaray',{AutoCommit=>1,RaiseError=>1,PrintError=>0});
my $query1 = $conn->prepare("select m_type from member m, users u where m.m_id = u.m_id and username = '$username' and password = '$password'");
$query1->execute();
my $template1 = HTML::Template->new(filename => '/var/www/project/html/header.tmpl'); 
while(my @op = $query1->fetchrow_array()){
		
		if($op[0] eq 'admin'){
			$session->param('ADMIN',$username);
			my $cookie = $cgi->cookie(CGISESSID => $session->id);
			print $query->redirect(-url=>'/cgi-bin/admin/admin_home.cgi',-cookie => $cookie);
		}

		elsif($op[0] eq 'librarian'){
			$session->param('LIBRARIAN',$username);
			my $cookie = $cgi->cookie(CGISESSID => $session->id);
			print $query->redirect(-url=>'/cgi-bin/su/su_home.cgi',-cookie => $cookie);
		}

		elsif($op[0] eq 'user'){
			$session->param('USERNAME',$username);
			my $cookie = $cgi->cookie(CGISESSID => $session->id);
			print $query->redirect(-url=>'/cgi-bin/user/user_home.cgi',-cookie => $cookie);
		}
}


my $template2 = HTML::Template->new(filename => '/var/www/project/html/login.tmpl'); 
my $template3 = HTML::Template->new(filename => '/var/www/project/html/footer.tmpl'); 

if($i == 0){
	$template2->param(wrong => "Username or password is incorrect.");
}

print $query->header(), $template1->output,$template2->output,$template3->output;


undef($query);
$conn->disconnect();
$conn = undef;