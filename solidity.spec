# Git hash of a tagged commit
%global git_hash 4fc1097e8df32897ccee8985019610fa5a869212
%undefine _package_note_file

Summary:	Object-oriented, high-level language for implementing smart contracts
Name:		solidity
Version:	0.8.22
Release:	%autorelease
URL:		https://docs.soliditylang.org/
Source0:	https://github.com/ethereum/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
License:	GPLv3
# Fedora-specific
Patch1:		solidity-0001-Use-system-wide-libs.patch
Patch2:		solidity-0002-Stop-checking-for-jsoncpp-version.patch
Patch3:		solidity-0003-Continue-on-big-endians.patch
Patch4:		solidity-0004-Use-static-linking-for-internal-libs.patch
Patch5:		solidity-0005-SMTChecker-Update-CVC4-to-cvc5.patch
Patch6:		solidity-0006-SMTChecker-Rename-CVC-interface-files.patch
Patch7:		solidity-0007-Intentionally-failing-test.patch


%ifarch s390x
#FIXME see patch no. 3
%endif


BuildRequires:	boost-devel
BuildRequires:	cmake >= 3.0
%if 0%{?fedora} >= 39
BuildRequires:	cvc5-devel
%else
BuildRequires:	cvc4-devel
%endif
BuildRequires:	fmt-devel
BuildRequires:	gcc-c++
# Should be dependency of cvc4. See https://bugzilla.redhat.com/2203174
BuildRequires:	gmp-devel
# Should be dependency of cvc4. See https://bugzilla.redhat.com/2203174
BuildRequires:	symfpu-devel
BuildRequires:	jsoncpp-devel
BuildRequires:	range-v3-devel
BuildRequires:	z3-devel


%description
Solidity is an object-oriented, high-level language for implementing smart
contracts. Smart contracts are programs which govern the behaviour of accounts
within the Ethereum state.


%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%if 0%{?fedora} >= 39
%patch5 -p1
%patch6 -p1
%patch7 -p1
%endif
echo %{git_hash} > commit_hash.txt


%build
#-DUSE_LD_GOLD:BOOL=OFF
%{cmake} \
	-DBoost_USE_STATIC_LIBS:BOOL=OFF \
	-DSTRICT_Z3_VERSION:BOOL=OFF \
	-DTESTS:BOOL=OFF
%cmake_build


%install
%cmake_install

%check
# TODO

%files
%{_bindir}/solc
%{_bindir}/yul-phaser
%doc README.md
%doc SECURITY.md
%license LICENSE.txt


%changelog
%autochangelog
