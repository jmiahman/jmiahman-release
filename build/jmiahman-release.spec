Name:       jmiahman-release
Version:    1.0
Release:    1%{?dist}
Summary:    JMiahMan Test repository configuration

Group:      System Environment/Base
License:    BSD
URL:        http://jmiahman.wordpress.com
Source0:    %{name}-%{version}.tar.gz
BuildRoot:  %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildArch: noarch

%description
JMiahMan repository configuration.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d -m 755 $RPM_BUILD_ROOT/etc/yum.repos.d
install -m 644 jmiahman.repo $RPM_BUILD_ROOT/etc/yum.repos.d/

#install -d -m 755 $RPM_BUILD_ROOT/etc/pki/rpm-gpg
#install -m 644 RPM-GPG-KEY-google-talkplugin $RPM_BUILD_ROOT/etc/pki/rpm-gpg/

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc
#/etc/pki/rpm-gpg/RPM-GPG-KEY-google-talkplugin
%config(noreplace) /etc/yum.repos.d/jmiahman.repo

%changelog
* Thu Oct 10 2013 JMiahMan <JMiahMan@gmail.com> - 1.0-1
- Initial Release
- Not signing rpms.. leave code commented out
