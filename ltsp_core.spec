#
# TODO:
# real descriptions
# dev permissions
#
Summary:	Linux Terminal Server Project - Core system for terminals
Summary(pl):	Podstawowy system dla terminali z Linux Terminal Server Project
Name:		ltsp_core
Version:	3.0.9
Release:	0.1
License:	GPL
Group:		Applications/Network
# Source0-md5:	4838e28c19a475e8cdd8d0b731b22264
Source0:	http://dl.sourceforge.net/ltsp/%{name}-%{version}-i386.tgz
URL:		http://www.ltsp.org/
AutoProv:	0
AutoReq:	0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_ltspdir	/home/services/ltsp
%define		no_install_post_strip	1

%description
Q: How do you reduce costs AND save the planet?
A: Convert those old PCs into X terminals with LTSP.

This package contains core system for LTSP terminals.

%description -l pl
- Jak obni¿yæ koszty I ocaliæ planetê?
- Przekszta³ciæ te stare pecety na X-terminale z u¿yciem LTSP.

Ten pakiet zawiera podstawowy system dla terminali LTSP.

%prep
%setup -q -n %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_ltspdir},%{_sysconfdir}}

cd i386
cp -r {bin,dev,etc,lib,oldroot,opt,proc,root,sbin,tmp,usr} $RPM_BUILD_ROOT%{_ltspdir}
ln -sf /tmp/var $RPM_BUILD_ROOT%{_ltspdir}/var
ln -sf /tmp/mnt $RPM_BUILD_ROOT%{_ltspdir}/mnt 
ln -sf %{_ltspdir}/etc/lts.conf $RPM_BUILD_ROOT%{_sysconfdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{_sysconfdir}/lts.conf
%dir %{_ltspdir}
%attr(755,root,root) %{_ltspdir}/bin
# XXX: fix perms inside!!!
%dir %{_ltspdir}/dev
#%{_ltspdir}/dev/*
%dir %{_ltspdir}/etc
%{_ltspdir}/etc/*.conf
%attr(755,root,root) %{_ltspdir}/etc/rc*
%attr(755,root,root) %{_ltspdir}/etc/dhclient-script
%{_ltspdir}/etc/bashrc
%{_ltspdir}/etc/fstab
%{_ltspdir}/etc/group
%{_ltspdir}/etc/inittab
%{_ltspdir}/etc/ld.so.cache
%{_ltspdir}/etc/lts.orig
%{_ltspdir}/etc/lts.conf.readme
%{_ltspdir}/etc/ltsp_functions
%{_ltspdir}/etc/modules.devfs
%{_ltspdir}/etc/passwd
%{_ltspdir}/etc/protocols
%{_ltspdir}/etc/rpc
%{_ltspdir}/etc/services
%{_ltspdir}/etc/version
%attr(755,root,root) %{_ltspdir}/lib
%{_ltspdir}/mnt
%{_ltspdir}/oldroot
%{_ltspdir}/opt
%{_ltspdir}/proc
%{_ltspdir}/root
%attr(755,root,root) %{_ltspdir}/sbin
%{_ltspdir}/tmp
%dir %{_ltspdir}/usr
%attr(755,root,root) %{_ltspdir}/usr/bin
%attr(755,root,root) %{_ltspdir}/usr/lib
%attr(755,root,root) %{_ltspdir}/usr/sbin
%{_ltspdir}/usr/share
%{_ltspdir}/var
