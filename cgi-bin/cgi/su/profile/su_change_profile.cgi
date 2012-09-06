#!/usr/bin/perl -w
use strict;
use DBI;
use CGI;
use HTML::Template;
use CGI::Session;
use Check_add_mem;

my $flag = 0;
my $query = CGI->new();
my $session = CGI::Session->new();																		##	and call
if($session->param('LIBRARIAN'))
{
	my $username1 = $session->param('LIBRARIAN');
	my $id = $query->param("txtid");
	my $name = $query->param("txtname");
	my $birthdate = $query->param("txtbirthdate");
	my $address = $query->param("txtaddress");
	my $city = $query->param("txtcity");
	my $state = $query->param("txtstate");
	my $sex = $query->param("txtsex");
	my $phno = $query->param("txtphno");
	my $joindate = $query->param("txtjoindate");
	my $usertype = $query->param("txtusertype");
	my $username = $query->param("txtusername");

	my $template1 = HTML::Template->new(filename => '/var/www/project/html/su/su_header.tmpl');   	##	su_pageheader.tmpl
	my $template2 = HTML::Template->new(filename => '/var/www/project/html/su/su_pageheader.tmpl');	##	su_footer.tmpl
	my $template4 = HTML::Template->new(filename => '/var/www/project/html/su/su_footer.tmpl'); 		##
	$template2->param(username=>$username1);

	my $template5 = HTML::Template->new(filename => '/var/www/project/html/su/profile/su_change_profile.tmpl'); 

	if(!($name))
	{$template5->param('varname'=>"Name is required");$flag = 1;}
	if(!($birthdate))
	{$template5->param('varbirthdate'=>"BirthDate is required");$flag = 1;}
	if(!($address))
	{$template5->param('varaddress'=>"Address is required");$flag = 1;}
	if(!($city))
	{$template5->param('varcity'=>"City is required");$flag = 1;}
	if(!($state))
	{$template5->param('varstate'=>"State and Country are required");$flag = 1;}
	if(!($sex))
	{$template5->param('varsex'=>"Sex is required");$flag = 1;}
	if(!($phno))
	{$template5->param('varphno'=>"Mobile Number is required");$flag = 1;}
	if(!($joindate))
	{$template5->param('varjoindate'=>"JoinDate is required");$flag = 1;}
	if(!($usertype))
	{$template5->param('varusertype'=>"Usertype is required");$flag = 1;}
	if(!($username))
	{$template5->param('varusername'=>"Username is required");$flag = 1;}



	if(!($name =~ m/^([a-zA-Z]+\s*)+$/))
	{
		$template5->param('varname'=>'Please use proper characters in name.');
		$flag = 1;
	}

	if(!($city =~ m/^[a-zA-Z]+$/))
	{
		$template5->param('varcity'=>'Please use proper characters in city.');
		$flag = 1;
	}

	if(!($state =~ m/^([a-zA-Z]+\s*)+,([a-zA-Z]+\s*)+$/))
	{
		$template5->param('varstate'=>'Please insert in this formate (statename,countryname).');
		$flag = 1;
	}

	if(!($phno =~ m/^\d{10}$/))
	{
		$template5->param('varphno'=>'Wrong mobile number.');
		$flag = 1;
	}

	$username =~ s/'/\\'/g;
	if(Check_add_mem::check_username_id($username,$id))
	{
		if(Check_add_mem::check_username($username))
		{
		$template5->param('varusername'=>'this username is already used.');
		$flag = 1;
		}
	}

	if ($flag == 1)
	{
		$username =~ s/\\'/'/g;		
					
		$template5->param(txtid=>$id);
		$template5->param(txtname=>$name);
		$template5->param(txtbirthdate=>$birthdate);
		$template5->param(txtaddress=>$address);
		$template5->param(txtcity=>$city);
		$template5->param(txtstate=>$state);
		$template5->param($sex=>'selected');
		$template5->param(txtphno=>$phno);
		$template5->param(txtjoindate=>$joindate);
		$template5->param(txttype=>$usertype);
		$template5->param(txtusername=>$username);

		print $query->header();
		print $template1->output,$template2->output,$template5->output,$template4->output;
	}

	else
	{

		$address =~ s/'/\\'/g;

		my $conn = DBI->connect( 'dbi:Pg:dbname=postgres;host=127.0.0.1','postgres','mangeskaray',{AutoCommit=>1,RaiseError=>1,PrintError=>0});
		my $query1 = $conn->prepare(" update member set m_name='$name' , m_birthdate='$birthdate' , m_address='$address' , m_city='$city' , m_state='$state' , m_sex='$sex' , m_phno='$phno' where m_id='$id'");
		my $query2 = $conn->prepare(" update users set username='$username' where m_id = '$id'");
		$query1->execute();
		$query2->execute();
		$session->param('profile'=>'Profile is changed successfully.');
		print $query->redirect(-url=>"/cgi-bin/su/profile/su_profile.cgi");
	}
}

else
{
	print $query->redirect(-url=>'/cgi-bin/library.cgi');
}
