# Git hash of a tagged commit
%global git_hash 8a97fa7a1db1ec509221ead6fea6802c684ee887
%undefine _package_note_file

Summary:	Object-oriented, high-level language for implementing smart contracts
Name:		solidity
Version:	0.8.26
Release:	%autorelease
URL:		https://docs.soliditylang.org/
Source0:	https://github.com/ethereum/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
License:	GPL-3.0-only
# Fedora-specific
Patch1:		solidity-0001-Use-system-wide-libs.patch
Patch2:		solidity-0002-Continue-on-big-endians.patch
Patch3:		solidity-0003-Use-static-linking-for-internal-libs.patch


%ifarch s390x
#FIXME see patch no. 3
%endif


BuildRequires:	boost-devel
BuildRequires:	cmake >= 3.0
%if 0%{?fedora} < 39
BuildRequires:	cvc4-devel
# Should be dependency of cvc4. See https://bugzilla.redhat.com/2203174
BuildRequires:	gmp-devel
# Should be dependency of cvc4. See https://bugzilla.redhat.com/2203174
BuildRequires:	symfpu-devel
%endif
BuildRequires:	cmake(fmt)
BuildRequires:	cmake(nlohmann_json)
BuildRequires:	cmake(range-v3)
BuildRequires:	cmake(z3)
BuildRequires:	gcc-c++


%description
Solidity is an object-oriented, high-level language for implementing smart
contracts. Smart contracts are programs which govern the behaviour of accounts
within the Ethereum state.


%prep
%autosetup -p1
echo %{git_hash} > commit_hash.txt


%build
%{cmake} \
	-DUSE_SYSTEM_LIBRARIES:BOOL=ON \
	-DBoost_USE_STATIC_LIBS:BOOL=OFF \
	-DSTRICT_Z3_VERSION:BOOL=OFF \
	-DSTRICT_NLOHMANN_JSON_VERSION:BOOL=OFF \
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
