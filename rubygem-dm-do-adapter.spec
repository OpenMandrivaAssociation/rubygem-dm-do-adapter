# Generated from dm-do-adapter-1.2.0.gem by gem2rpm5 0.6.5 -*- rpm-spec -*-
%define	rbname	dm-do-adapter

Summary:	DataObjects Adapter for DataMapper
Name:		rubygem-%{rbname}

Version:	1.2.0
Release:	1
Group:		Development/Ruby
License:	GPLv2+ or Ruby
URL:		http://github.com/datamapper/dm-do-adapter
Source0:	http://gems.rubyforge.org/gems/%{rbname}-%{version}.gem
BuildRequires:	rubygems 
BuildArch:	noarch

%description
DataObjects Adapter for DataMapper

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}

%description	doc
Documents, RDoc & RI documentation for %{name}.

%prep
%setup -q

%build
%gem_build

%install
%gem_install

%files
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/dm-do-adapter
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/dm-do-adapter/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/dm-do-adapter/spec
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/dm-do-adapter/spec/*.rb
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec

%files doc
%{ruby_gemdir}/doc/%{rbname}-%{version}
%{ruby_gemdir}/gems/%{rbname}-%{version}/*.rdoc
%{ruby_gemdir}/gems/%{rbname}-%{version}/LICENSE
