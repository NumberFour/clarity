%define version %(ruby -I./lib/ -rrubygems -rclarity -e 'puts Clarity::VERSION')
%define rbname numberfour-clarity
%define release 1
%define gemdir /usr/lib/ruby/gems/1.8
%define gembuilddir %{buildroot}%{gemdir}
Summary: Web interface for grep and tail -f
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://github.com/tobi/clarity
Source0: %{rbname}-%{version}.gem
Source1: rubygem-%{rbname}.spec.in
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby
Requires: rubygems >= 1.3.7
Requires: rubygem-eventmachine >= 0.12.10
Requires: rubygem-eventmachine_httpserver >= 0.2.0
Requires: rubygem-json >= 1.0.0
Requires: rubygem-log4r >= 1.1.19
Requires: rubygem-hoe => 2.12
Requires: rubygem-hoe < 3
Requires: /usr/sbin/start-stop-daemon
BuildRequires: ruby
BuildRequires: rubygems >= 1.3.7
BuildArch: noarch
Provides: ruby(Numberfour-clarity) = %{version}


%description
Clarity - a log search tool
By John Tajima & Tobi Lütke & Jens Bräuer
Clarity is a Splunk like web interface for your server log files. It supports
searching (using grep) as well as trailing log files in realtime. It has been
written
using the event based architecture based on EventMachine and so allows
real-time search
of very large log files. If you hit the browser Stop button it will also kill
the grep / tail utility.
We wrote Clarity to allow our support staff to use a simple interface to look
through the various log files in our server farm. The application was such a
big success internally that we decided to release it as open source.

%prep
%setup -T -c

%build

%install
%{__rm} -rf %{buildroot}
mkdir -p %{gembuilddir}
gem install --local --install-dir %{gembuilddir} --force %{SOURCE0}
mkdir -p %{buildroot}/%{_bindir}
mv %{gembuilddir}/bin/* %{buildroot}/%{_bindir}
rmdir %{gembuilddir}/bin

mkdir -p %{buildroot}/etc/rc.d/init.d/
mv %{gembuilddir}/gems/%{rbname}-%{version}/script/clarity.init %{buildroot}/etc/rc.d/init.d/clarity

mkdir -p %{buildroot}/etc/
cp %{gembuilddir}/gems/%{rbname}-%{version}/config/config.yml.sample %{buildroot}/etc/clarity.conf

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root)
%{_bindir}/clarity
%doc %{gemdir}/gems/%{rbname}-%{version}/History.txt
%doc %{gemdir}/gems/%{rbname}-%{version}/Manifest.txt
%doc %{gemdir}/gems/%{rbname}-%{version}/PostInstall.txt
%{gemdir}/gems/%{rbname}-%{version}/README.rdoc
%{gemdir}/gems/%{rbname}-%{version}/Rakefile
%{gemdir}/gems/%{rbname}-%{version}/bin
%{gemdir}/gems/%{rbname}-%{version}/config
%{gemdir}/gems/%{rbname}-%{version}/lib
%{gemdir}/gems/%{rbname}-%{version}/public
%{gemdir}/gems/%{rbname}-%{version}/script
%{gemdir}/gems/%{rbname}-%{version}/test
%{gemdir}/gems/%{rbname}-%{version}/views
%{gemdir}/gems/%{rbname}-%{version}/.gemtest
%{gemdir}/gems/%{rbname}-%{version}/.yardoc
%{gemdir}/specifications/
%{gemdir}/cache/

%doc %{gemdir}/doc/%{rbname}-%{version}

/etc/

%changelog
