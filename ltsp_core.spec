#
# TODO:
# desc, cleanups
#
Summary:	Linux Terminal Server Project - Core
Summary(pl):	Baza Linux Terminal Server Project
Name:		ltsp_core
Version:	3.0.7
Release:	0.1
License:	GPL
Group:		Applications/Network
Source0:	http://cesnet.dl.sourceforge.net/sourceforge/ltsp/%{name}-%{version}-i386.tgz
URL:		http://www.ltsp.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
%define		_ltspdir	/home/services/ltsp
%define no_install_post_strip	1
%define	_noautoprovfiles	%{_ltspdir}/lib/* %{_ltspdir}/usr/lib/*
%define _noautoreq		"/bin/bash /bin/sh ld-linux.so.2 ld-linux.so.2 ld-linux.so.2 ld-linux.so.2 ld-linux.so.2 libcom_err.so.2 libc.so.6 libc.so.6 libc.so.6 libc.so.6 libc.so.6 libc.so.6 libdl.so.2 libdl.so.2 libdl.so.2 libe2p.so.2 libext2fs.so.2 libnsl.so.1 libnsl.so.1 libpthread.so.0 libpthread.so.0 libpthread.so.0 libtermcap.so.2 libuuid.so.1 e2fsprogs glibc"

%description
Q: How do you reduce costs AND save the planet?
A: Convert those old PCs into X terminals with LTSP

%description -l pl


%prep
%setup -q -n %{name}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_ltspdir},%{_sysconfdir}}
cd i386
cp -r {bin,dev,etc,lib,oldroot,opt,proc,root,sbin,tmp,usr} $RPM_BUILD_ROOT%{_ltspdir}/
ln -sf /tmp/var $RPM_BUILD_ROOT%{_ltspdir}/var
ln -sf /tmp/mnt $RPM_BUILD_ROOT%{_ltspdir}/mnt 
ln -sf %{_ltspdir}/etc/lts.conf $RPM_BUILD_ROOT%{_sysconfdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(700,root,root,700)
%doc README
%{_sysconfdir}/lts.conf
%{_ltspdir}/bin/
%{_ltspdir}/dev/
%attr(600,root,root)%{_ltspdir}/etc/
%{_ltspdir}/lib/
%{_ltspdir}/mnt
%{_ltspdir}/oldroot/
%{_ltspdir}/opt/
%{_ltspdir}/proc/
%{_ltspdir}/root/
%{_ltspdir}/sbin/
%{_ltspdir}/tmp/
%{_ltspdir}/usr/bin/
%{_ltspdir}/usr/lib/
%{_ltspdir}/usr/sbin/
%{_ltspdir}/usr/share/

%{_ltspdir}/var
