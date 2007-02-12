# TODO: missing dirs and duplicated files
%define		_arch	i386
%define		_pver	4.1

Summary:	Linux Terminal Server Project - Core system for terminals
Summary(pl.UTF-8):   Podstawowy system dla terminali z Linux Terminal Server Project
Name:		ltsp_core
Version:	4.0.1
Release:	0.1
License:	GPL
Group:		Applications/Networking
Source0:	http://www.ltsp.org/ltsp-utils-0.11.tgz
# Source0-md5:	b17b350b18b04d769fcadcd12885a573
Source1:	http://ltsp.mirrors.tds.net/pub/ltsp/ltsp-%{_pver}/ltsp-audiofile-1.1-0-%{_arch}.tgz
# Source1-md5:	1931c46b3648e01cfe92c8dcec40b41c
Source2:	http://ltsp.mirrors.tds.net/pub/ltsp/ltsp-%{_pver}/ltsp-aumix-1.1-0-%{_arch}.tgz
# Source2-md5:	d6991522dba8d22e1802f7e8bb4c26a8
Source3:	http://ltsp.mirrors.tds.net/pub/ltsp/ltsp-%{_pver}/ltsp-bash-1.1-0-%{_arch}.tgz
# Source3-md5:	02f706c9a124e16f1e221fa6589f17c1
Source4:	http://ltsp.mirrors.tds.net/pub/ltsp/ltsp-%{_pver}/ltsp-busybox-1.1-0-%{_arch}.tgz
# Source4-md5:	69c1dea563735c32d032d4373fcdd433
Source5:	http://ltsp.mirrors.tds.net/pub/ltsp/ltsp-%{_pver}/ltsp-devfsd-1.1-0-%{_arch}.tgz
# Source5-md5:	e12493167f7a8eb8f629a09a55c85446
Source6:	http://ltsp.mirrors.tds.net/pub/ltsp/ltsp-%{_pver}/ltsp-e2fsprogs-1.2-0-%{_arch}.tgz
# Source6-md5:	73a56cd926f8445b68d029a34bca6ee5
Source7:	http://ltsp.mirrors.tds.net/pub/ltsp/ltsp-%{_pver}/ltsp-esd-1.1-0-%{_arch}.tgz
# Source7-md5:	1b478ec6f52f3f8d570bd31cc07e3d45
Source8:	http://ltsp.mirrors.tds.net/pub/ltsp/ltsp-%{_pver}/ltsp-getltscfg-1.3-0-%{_arch}.tgz
# Source8-md5:	4e51f3971cd7747d59f39f06f51e9406
Source9:	http://ltsp.mirrors.tds.net/pub/ltsp/ltsp-%{_pver}/ltsp-glibc-1.0-1-%{_arch}.tgz
# Source9-md5:	c64b6b1f2dc2422efa6eaf86f920c823
Source10:	http://ltsp.mirrors.tds.net/pub/ltsp/ltsp-%{_pver}/ltsp-haltsys-1.1-0-%{_arch}.tgz
# Source10-md5:	e2d33e544b8c410646e7eaa032b59b6d
Source11:	http://ltsp.mirrors.tds.net/pub/ltsp/ltsp-%{_pver}/ltsp-libgcc_s-1.0-1-%{_arch}.tgz
# Source11-md5:	2fe39512f324c0ecb23a28c1418f07b6
Source12:	http://ltsp.mirrors.tds.net/pub/ltsp/ltsp-%{_pver}/ltsp-libpng-1.1-0-%{_arch}.tgz
# Source12-md5:	a350f3143067ec2e8d8f7300b85d3848
Source13:	http://ltsp.mirrors.tds.net/pub/ltsp/ltsp-%{_pver}/ltsp-libvncserver-1.1-0-%{_arch}.tgz
# Source13-md5:	178055da7b5d6c05e7fee9f0d4e9c0ac
Source14:	http://ltsp.mirrors.tds.net/pub/ltsp/ltsp-%{_pver}/ltsp-lp_server-1.2-0-%{_arch}.tgz
# Source14-md5:	1ed89a3455f2c8306f33660be1ff463a
Source15:	http://ltsp.mirrors.tds.net/pub/ltsp/ltsp-%{_pver}/ltsp-ltspinfod-1.2-0-%{_arch}.tgz
# Source15-md5:	36af95dcc5fb227451c09bbb9ce734e2
Source16:	http://ltsp.mirrors.tds.net/pub/ltsp/ltsp-%{_pver}/ltsp-ltsptree-1.11-0-%{_arch}.tgz
# Source16-md5:	cb9191ab0272f20ae8d82d1471e77951
Source17:	http://ltsp.mirrors.tds.net/pub/ltsp/ltsp-%{_pver}/ltsp-module-init-tools-3.2-0-%{_arch}.tgz
# Source17-md5:	cc61b437488b7ed41cd582f41ea3d55e
Source18:	http://ltsp.mirrors.tds.net/pub/ltsp/ltsp-%{_pver}/ltsp-modutils-1.1-1-%{_arch}.tgz
# Source18-md5:	cd77dcc51748cce946e19b255f99c868
Source19:	http://ltsp.mirrors.tds.net/pub/ltsp/ltsp-%{_pver}/ltsp_nasd-1.2-0-%{_arch}.tgz
# Source19-md5:	3ff2de57b820b9195800f30c8df8db75
Source20:	http://ltsp.mirrors.tds.net/pub/ltsp/ltsp-%{_pver}/ltsp-ncurses-1.1-0-%{_arch}.tgz
# Source20-md5:	e8df9ff62ee53285ac7eb29220880626
Source21:	http://ltsp.mirrors.tds.net/pub/ltsp/ltsp-%{_pver}/ltsp-net-tools-1.1-0-%{_arch}.tgz
# Source21-md5:	2d141a616494240a6a3fd81301689ac8
Source22:	http://ltsp.mirrors.tds.net/pub/ltsp/ltsp-%{_pver}/ltsp-nfs-utils-1.1-0-%{_arch}.tgz
# Source22-md5:	ad6207bf370a7f65afaf834e982eb9d1
Source23:	http://ltsp.mirrors.tds.net/pub/ltsp/ltsp-%{_pver}/ltsp-open-1.2-0-%{_arch}.tgz
# Source23-md5:	87732c7732cfe7685c08ac2a1cf7c0e3
Source24:	http://ltsp.mirrors.tds.net/pub/ltsp/ltsp-%{_pver}/ltsp-openssl-1.1-0-%{_arch}.tgz
# Source24-md5:	cead9e1fc52a03b585c980cad9d8d3d3
Source25:	http://ltsp.mirrors.tds.net/pub/ltsp/ltsp-%{_pver}/ltsp-pam-1.1-0-%{_arch}.tgz
# Source25-md5:	2bc81710a53a72cf89458114d22fe50d
Source26:	http://ltsp.mirrors.tds.net/pub/ltsp/ltsp-%{_pver}/ltsp-pci_scan-1.1-0-%{_arch}.tgz
# Source26-md5:	f64b1d660ddb74f51dead0f1e58def58
Source27:	http://ltsp.mirrors.tds.net/pub/ltsp/ltsp-%{_pver}/ltsp-popt-1.2-0-%{_arch}.tgz
# Source27-md5:	43474536769b486c4976944eddfd833e
Source28:	http://ltsp.mirrors.tds.net/pub/ltsp/ltsp-%{_pver}/ltsp-portmap-1.1-0-%{_arch}.tgz
# Source28-md5:	cfeb3528ccea17c8f03215124c5fbc74
Source29:	http://ltsp.mirrors.tds.net/pub/ltsp/ltsp-%{_pver}/ltsp-prep_swap-1.1-0-%{_arch}.tgz
# Source29-md5:	4b18ada2d15a12137aa2302f4180fef2
Source30:	http://ltsp.mirrors.tds.net/pub/ltsp/ltsp-%{_pver}/ltsp-snmpd-1.1-0-%{_arch}.tgz
# Source30-md5:	ce594c778c4b7ae7fb5fe33db9dfe085
Source31:	http://ltsp.mirrors.tds.net/pub/ltsp/ltsp-%{_pver}/ltsp-ssh-1.1-0-%{_arch}.tgz
# Source31-md5:	07984a336ad7f1ba99a98679b87af877
Source32:	http://ltsp.mirrors.tds.net/pub/ltsp/ltsp-%{_pver}/ltsp-startsess-1.2-0-%{_arch}.tgz
# Source32-md5:	a2e0ddb443e4dc7c7cab37e3bbecd23d
Source33:	http://ltsp.mirrors.tds.net/pub/ltsp/ltsp-%{_pver}/ltsp-sysvinit-1.1-0-%{_arch}.tgz
# Source33-md5:	a3113d9a7e5a9a6b89d684b17d265047
Source34:	http://ltsp.mirrors.tds.net/pub/ltsp/ltsp-%{_pver}/ltsp-tcp_wrappers-1.1-0-%{_arch}.tgz
# Source34-md5:	403a41a82fa5b44c827d35b0c3c0621e
Source35:	http://ltsp.mirrors.tds.net/pub/ltsp/ltsp-%{_pver}/ltsp-util-linux-1.1-0-%{_arch}.tgz
# Source35-md5:	6495745339de4a58f38e1a48e0d81fb6
Source36:	http://ltsp.mirrors.tds.net/pub/ltsp/ltsp-%{_pver}/ltsp-vidlist-1.4-0-%{_arch}.tgz
# Source36-md5:	c5a01f30f5917d833a64a74a105f4291
Source37:	http://ltsp.mirrors.tds.net/pub/ltsp/ltsp-%{_pver}/ltsp-xinetd-1.1-0-%{_arch}.tgz
# Source37-md5:	4886457b3308705bf6e9afede00a771c
Source38:	http://ltsp.mirrors.tds.net/pub/ltsp/ltsp-%{_pver}/ltsp-ypbind-1.1-0-%{_arch}.tgz
# Source38-md5:	48a4cde35d6ab984677d6ad208200817
Source39:	http://ltsp.mirrors.tds.net/pub/ltsp/ltsp-%{_pver}/ltsp-zlib-1.0-1-%{_arch}.tgz
# Source39-md5:	abc1d2e4457df325c0b3ba231526d738
Source40:	http://www.ltsp.org/documentation/ltsp-4.1/ltsp-4.1.3-en.pdf
# Source40-md5:	49007e389b74e35ac0735128a1901f02
URL:		http://www.ltsp.org/
BuildRequires:	perl-Digest-SHA1
BuildRequires:	perl-URI
BuildRequires:	perl-libwww
AutoProv:	0
AutoReq:	0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_ltspdir	/home/services/ltsp

%description
LTSP is an add-on package for Linux that allows you to connect lots of
low-powered thin client terminals to a Linux server. Applications
typically run on the server and accept input and display their output
on the thin client display. LTSP is available as a set of packages that
can be installed on any Linux system.

This package contains core system for LTSP terminals.

%description -l pl.UTF-8
LTSP to dodatkowy pakiet dla Linuksa pozwalający na podłączenie wielu
cienkich klientów jako terminali do serwera linuksowego. Aplikacje
zwykle działają na serwerze i przyjmują wejście oraz wyświetlają
wyjście na wyświetlaczach cienkich klientów. LTSP jest dostępny jako
zestaw pakietów, które można zainstalować na dowolnym systemie
linuksowym.

Ten pakiet zawiera podstawowy system dla terminali LTSP.

%package doc
Summary:	Documentation for LTSP
Summary(pl.UTF-8):   Dokumentacja dla LTSP
Group:		Documentation

%description doc
Documentation for LTSP (PDF file).

%description doc -l pl.UTF-8
Dokumentacja dla LTSP (plik PDF).

%prep
%setup -q -n ltsp-utils

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_ltspdir},%{_sysconfdir},/bin}

tar zxf %{SOURCE1}
tar zxf %{SOURCE2}
tar zxf %{SOURCE3}
tar zxf %{SOURCE4}
tar zxf %{SOURCE5}
tar zxf %{SOURCE6}
tar zxf %{SOURCE7}
tar zxf %{SOURCE8}
tar zxf %{SOURCE9}
tar zxf %{SOURCE10}
tar zxf %{SOURCE11}
tar zxf %{SOURCE12}
tar zxf %{SOURCE13}
tar zxf %{SOURCE14}
tar zxf %{SOURCE15}
tar zxf %{SOURCE16}
tar zxf %{SOURCE17}
tar zxf %{SOURCE18}
tar zxf %{SOURCE19}
tar zxf %{SOURCE20}
tar zxf %{SOURCE21}
tar zxf %{SOURCE22}
tar zxf %{SOURCE23}
tar zxf %{SOURCE24}
tar zxf %{SOURCE25}
tar zxf %{SOURCE26}
tar zxf %{SOURCE27}
tar zxf %{SOURCE28}
tar zxf %{SOURCE29}
tar zxf %{SOURCE30}
tar zxf %{SOURCE31}
tar zxf %{SOURCE32}
tar zxf %{SOURCE33}
tar zxf %{SOURCE34}
tar zxf %{SOURCE35}
tar zxf %{SOURCE36}
tar zxf %{SOURCE37}
tar zxf %{SOURCE38}
tar zxf %{SOURCE39}

install ltspadmin ltspcfg ltspinfo $RPM_BUILD_ROOT/bin
cd i386
cp -r {bin,dev,etc,home,include,lib,libexec,oldroot,proc,root,sbin,share,tmp,usr} $RPM_BUILD_ROOT%{_ltspdir}
install etc/lts.conf.readme $RPM_BUILD_ROOT%{_sysconfdir}/lts.conf
install man/man1/* $RPM_BUILD_ROOT%{_ltspdir}/usr/man/man1
install %{SOURCE40} ../
#ln -sf /tmp/var $RPM_BUILD_ROOT%{_ltspdir}/var
#ln -sf /tmp/mnt $RPM_BUILD_ROOT%{_ltspdir}/mnt
#ln -sf %{_ltspdir}/etc/lts.conf $RPM_BUILD_ROOT%{_sysconfdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING
%config(noreplace) %{_sysconfdir}/lts.conf
%dir /bin
%attr(755,root,root) /bin/*
%dir %{_ltspdir}
%attr(755,root,root) %{_ltspdir}/bin
%dir %{_ltspdir}/dev
%dir %{_ltspdir}/etc
%config(noreplace) %{_ltspdir}/etc/*.conf
%config(noreplace) %{_ltspdir}/etc/security/*.conf
%config(noreplace) %{_ltspdir}/etc/ssh/sshd_config
%attr(755,root,root) %{_ltspdir}/etc/rc.d/*
%attr(755,root,root) %{_ltspdir}/etc/rc*
%attr(755,root,root) %{_ltspdir}/etc/screen.d/*
%attr(755,root,root) %{_ltspdir}/etc/run_ltspinfod
%attr(755,root,root) %{_ltspdir}/etc/screen_session
%attr(755,root,root) %{_ltspdir}/etc/build_x*_cfg
%{_ltspdir}/etc
%dir %{_ltspdir}/home
%{_ltspdir}/include
%dir %{_ltspdir}/lib
%attr(755,root,root) %{_ltspdir}/lib/evms
%attr(755,root,root) %{_ltspdir}/lib/security
%{_ltspdir}/lib/pkgconfig
%{_ltspdir}/lib/*
%dir %{_ltspdir}/libexec
%attr(755,root,root) %{_ltspdir}/libexec
#%{_ltspdir}/mnt
%{_ltspdir}/oldroot
%{_ltspdir}/proc
%{_ltspdir}/root
%attr(755,root,root) %{_ltspdir}/sbin
%{_ltspdir}/share
%{_ltspdir}/tmp
%dir %{_ltspdir}/usr
%attr(755,root,root) %{_ltspdir}/usr/X11R6/bin
%attr(755,root,root) %{_ltspdir}/usr/X11R6/lib/libaudio.so.2.3
%{_ltspdir}/usr/X11R6/lib/*
%attr(755,root,root) %{_ltspdir}/usr/bin
%{_ltspdir}/usr/include
%attr(755,root,root) %{_ltspdir}/usr/lib/gconv
%{_ltspdir}/usr/lib/pkgconfig
%{_ltspdir}/usr/lib/terminfo
%{_ltspdir}/usr/lib/l*
%{_ltspdir}/usr/libexec
%{_ltspdir}/usr/man
%attr(755,root,root) %{_ltspdir}/usr/sbin
%{_ltspdir}/usr/share
%{_ltspdir}/usr/ssl

%files doc
%defattr(644,root,root,755)
%doc ltsp-4.1.3-en.pdf
